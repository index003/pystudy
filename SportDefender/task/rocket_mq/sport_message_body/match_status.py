import json
import time
from common.data import sport_data_interface


def match_status_msg(match_id, status=2):
    source_category_id = sport_data_interface.get_category_info_by_id(match_id, 'source_category_id')
    source_league_id = sport_data_interface.get_league_source_id_by_id(match_id)
    fixture_id = sport_data_interface.get_match_info_by_id(match_id, 'fixture_id')
    source_team_ids = sport_data_interface.get_team_info_by_id(match_id, 'source_team_id')
    start_date = sport_data_interface.get_match_info_by_id(match_id, 'match_time')
    home_team_id = source_team_ids[0]
    away_team_id = source_team_ids[1]
    current_millis = int(time.time() * 1000)

    match_fields = {
        "source": 'LSPORTS',
        "locationId": 0,
        "sportId": source_category_id,
        "leagueId": source_league_id,
        "fixtureId": fixture_id,
        "homeTeamId": home_team_id,
        "awayTeamId": away_team_id,
        "status": status,
        "startDate": start_date,
        "lastUpdate": current_millis
    }
    message_body = json.dumps(match_fields)
    return message_body


'''
{
  "source":"LSPORTS",
  "sportId": 6046,
  "leagueId": 3502,
  "locationId": 0,
  "fixtureId": 7398699,
  "homeTeamId": 56,
  "awayTeamId": 1134,
  "status":2,
  "startDate": 1631259925392,
  "lastUpdate": 1631259925392
}

topic:match_metadata_update

status:

NOT_STARTED_YET(1,"Not started yet","The event has not started yet"),未开赛
IN_PROGRESS(2,"In progress","The event is live"),进行中
FINISHED(3,"Finished","The event is finished"),已完赛
CANCELLED(4,"Cancelled"    ,"The event has been cancelled"),已取消
POSTPONED(5,"Postponed"    ,"The event has been postponed"),已延期
INTERRUPTED(6,"Interrupted"    ,"The event has been interrupted"),已中断
ABANDONED(7,"Abandoned"    ,"The event has been abandoned"),
COVERAGE_LOST(8,"Coverage lost","The coverage for this event has been lost"),
ABOUT_TO_START(9,"About to start","The event has not started but is about to. ")
'''
