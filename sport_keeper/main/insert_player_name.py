import sys
import xlrd
from data import db_score
from config import env_config

env_config.env = 'fat2'


def get_source_name(source_id):
    book = xlrd.open_workbook('name_data.xls')
    sheet1 = book.sheets()[0]
    std_name_list = sheet1.col_values(0)
    sky_name_list = sheet1.col_values(1)
    hupu_name_list = sheet1.col_values(2)
    espn_name_list = sheet1.col_values(3)
    if source_id == 1:
        source_info = ['ESPN', std_name_list, espn_name_list]
    elif source_id == 2:
        source_info = ['HUPU', std_name_list, hupu_name_list]
    elif source_id == 3:
        source_info = ['SKYSPORTS', std_name_list, sky_name_list]
    else:
        print("the source is not exist, please check it!")
        sys.exit()
    return source_info


def update_mapping(source_id):
    source_info = get_source_name(source_id)
    source = source_info[0]
    std_name_list = source_info[1]
    origin_name_list = source_info[2]
    for i in range(1, len(std_name_list)):
        std_name = std_name_list[i]
        origin_name = origin_name_list[i]
        db_score.update_score_db_name_mapping(origin_name, std_name, source)


# source_id: 1 espn 2 hupu 3 skysports
update_mapping(4)
