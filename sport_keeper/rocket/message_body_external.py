import json
import random
import sys
from data import mq_basic
from config import env_config

env_config.env = "fat2"


def create_message_body_request(match_id):
    match_time = str(mq_basic.get_match_time(match_id))
    team_en_name = mq_basic.get_team_en_name(match_id)
    message_body = {
        "match_id": match_id,
        "categoryCode": "BASKETBALL",
        "leagueName": "NBA",
        "match_time": match_time,
        "homeName": team_en_name[0],
        "awayName": team_en_name[1]
    }

    return json.dumps(message_body)


def create_message_body_score_list(add_score=0):

    score_type_score_draw = [
        [1, 20, 17],
        [2, 23, 14],
        [3, 23, 18],
        [4, 14, 31],
        [100, 80, 80]]

    score_type_score_not_draw = [
        [1, 31, 31],
        [2, 30, 33],
        [3, 32, 27],
        [4, 18, 29],
        [100, 111, 120]]

    if add_score == 0:
        type_score_list = score_type_score_not_draw
    elif add_score == 1:
        type_score_list = score_type_score_draw
        type_score_list.insert(4, [11, 0, 6])
    elif add_score == 2:
        type_score_list = score_type_score_draw
        type_score_list.insert(4, [11, 4, 4])
        type_score_list.insert(5, [12, 6, 9])
    elif add_score == 3:
        type_score_list = score_type_score_draw
        type_score_list.insert(4, [11, 4, 4])
        type_score_list.insert(5, [12, 6, 6])
        type_score_list.insert(6, [13, 4, 12])
    else:
        print("the max add phase is 3,please check the addtion time")
        sys.exit()
    score_info_message = []
    for type_score in type_score_list:
        message_body = {
            "type": type_score[0],
            "home": type_score[1],
            "away": type_score[2]
        }
        score_info_message.append(message_body)

    return json.dumps(score_info_message)


def create_message_body_player_list(match_id):
    player_list = mq_basic.get_match_basketball_player_name(match_id)
    player_list_message = []
    for player in player_list:
        stats_body_list = []
        for player_type in range(1, 9):
            stats_body = {
                "type": player_type,
                "value": random.randint(5, 15)
            }
            stats_body_list.append(stats_body)
        message_body = {
            "playerName": player,
            "teamType": random.randint(1, 2),
            "stats": stats_body_list
        }
        player_list_message.append(message_body)

    return json.dumps(player_list_message)


def create_message_body_results(match_id, source_id, add_score=0):
    message_main_info = json.loads(create_message_body_request(match_id))
    message_score_info = json.loads(create_message_body_score_list(add_score))
    message_player_info = json.loads(create_message_body_player_list(match_id))

    if source_id == 1:
        source_info = ["espn", "ESPN"]
    elif source_id == 2:
        source_info = ["hupu", "HUPU"]
    elif source_id == 3:
        source_info = ["skysports", "SKYSPORTS"]
    else:
        print("the source is not exist!")

    message_main_info["sourceName"] = source_info[0]
    message_main_info["sourceType"] = source_info[1]
    message_main_info["scoreInfoList"] = message_score_info
    message_main_info["playerStatInfoList"] = message_player_info
    return json.dumps(message_main_info)
