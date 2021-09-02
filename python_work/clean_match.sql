delete from sport_match_info where id = {}; -- 删除比赛
delete from sport_betting_market where match_id = {}; -- 删除基本玩法
delete from sport_betting_market_option where match_id = {}; -- 删除基本选项
delete from sport_market_launch where match_id = {}; -- 删除玩法发布信息
delete from sport_market_option_launch where match_id = {}; -- 删除选项发布信息
delete from sport_betting_order where id in (select distinct order_id from sport_betting_order_option where match_id = {}); -- 删除订单信息
delete from sport_betting_order_option where match_id = {}; -- 删除订单选项(未能删除同一串关订单中的非本场比赛的订单选项)
delete from sport_third_match_score where match_id = {}; -- 删除数据方比分信息
delete from sport_third_settlement where match_id = {}; -- 删除数据方选项结算信息
delete from sport_match_score where match_id = {}; -- 删除正式比分信息
delete from sport_match_score_check where match_id = {}; -- 删除比分检验信息
delete from sport_match_option_award where match_id = {}; -- 删除选项正式开奖结果信息
delete from sport_match_option_award_check where match_id = {}; -- 删除选项开奖校验信息
delete from sport_match_hot_config where match_id = {}; -- 删除热门配置信息
delete from sport_match_operation_time where match_id = {}; -- 删除赛事操作日志表
delete from sport_permissions_info where type = 3 and permission_id  =  {}; -- 删除赛事分配信息
delete from sport_market_change_info where match_id = {};
delete from sport_match_result_check where match_id = {};