import time
from collections import namedtuple
from db_operation import db_crud


def match_status_msg(match_id, status=2):
    match_fields = [
        "source", "locationId", "sportId", "leagueId", "fixtureId",
        "homeTeamId", "awayTeamId", "status", "startDate", "lastUpdate"
    ]
    MatchMsg = namedtuple('MatchMsg', match_fields)

    msg_query = ("select c.source_category_id,a.league_id,a.source_match_id as fixtureID,"
                 "a.home_team_id,a.away_team_id from sport_match_info a "
                 "LEFT JOIN sport_league_info b ON a.league_id=b.id "
                 "LEFT JOIN sport_category_info c on a.category_id = c.id where a.id= %s")

    query_result = db_crud.LOTTERY.query_execute(msg_query, match_id)
    current_millis = int(time.time() * 1000)
    match_msg = MatchMsg('LSPORTS', 0, *query_result[0], status, current_millis, current_millis)
    message_body = str(match_msg._asdict()).replace("'", '"')
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
