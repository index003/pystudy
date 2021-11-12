import json
from rocket_mq.mq_basic_data import get_fixture_id_by_id,get_category_id_by_id

score_periods = {
    # 足球
    8: [('WHOLE', 2, 2),
        ('FIRST_HALF', 1, 1),
        ('SECOND_HALF', 1, 1)
        ],
    # 篮球
    9: [('WHOLE', 80, 80),
        ('QUARTER_1ST', 20, 17),
        ('QUARTER_2ND', 23, 14),
        ('QUARTER_3RD', 23, 18),
        ('QUARTER_4TH', 14, 31),
        ('OVER_TIME', 13, 16)
        ],
    # 网球
    10: [('WHOLE', 3, 2),
         ('SET_1ST', 4, 6),
         ('SET_2ND', 6, 3),
         ('SET_3RD', 7, 5),
         ('SET_4TH', 2, 6),
         ('SET_5TH', 7, 6)
         ],
    # 美式足球
    11: [('WHOLE', 25, 25),
         ('AM_QUARTER_1ST', 0, 7),
         ('AM_QUARTER_2ND', 3, 3),
         ('AM_QUARTER_3RD', 6, 12),
         ('AM_QUARTER_4TH', 16, 3),
         ('OVER_TIME', 6, 0)
         ],
    # 棒球
    12: [('WHOLE', 7, 7),
         ('INNING_1ST', 0, 0),
         ('INNING_2ND', 1, 0),
         ('INNING_3RD', 1, 0),
         ('INNING_4TH', 0, 1),
         ('INNING_5TH', 0, 0),
         ('INNING_6TH', 5, 0),
         ('INNING_7TH', 0, 2),
         ('INNING_8TH', 0, 2),
         ('INNING_9TH', 0, 2),
         ('OVER_TIME', 0, 1)
         ],
    # 排球
    219: [('WHOLE', 2, 3),
          ('VOLLEYBALL_1ST', 21, 25),
          ('VOLLEYBALL_2ND', 23, 25),
          ('VOLLEYBALL_3RD', 26, 24),
          ('VOLLEYBALL_4TH', 25, 20),
          ('VOLLEYBALL_5TH', 5, 15)
          ]
}


def create_score_periods_fields(category_id):
    periods_field = []
    for period_elements in score_periods[category_id]:
        period_field = {
            "type": period_elements[0],
            "homeScore": period_elements[1],
            "awayScore": period_elements[2]
        }

        periods_field.append(period_field)
    return periods_field


def create_score_message_body(match_id):
    fixtureId = get_fixture_id_by_id(match_id)
    category_id = get_category_id_by_id(match_id)
    periods_type_fields = create_score_periods_fields(category_id)
    score_message_body = {
        "source": "LSPORTS",
        "fixtureId": fixtureId,
        "periods": periods_type_fields
    }
    return json.dumps(score_message_body)


def create_live_score_message_body(match_id, home_score=0, away_score=0):
    fixtureId = get_fixture_id_by_id(match_id)
    live_score_message_body = {
        "source": "LSPORTS",
        "fixtureId": fixtureId,
        "scoreboard": {
            "status": 2,
            "homeScore": home_score,
            "awayScore": away_score
        }
    }
    return json.dumps(live_score_message_body)



