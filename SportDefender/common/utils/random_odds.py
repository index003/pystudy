from random import uniform


def new_odds(odds):
    odds = round(odds * uniform(0.95, 1.05), 4)
    return 1.001 if odds < 1.001 else odds
