from common_files import clean_match
from function_files import award_pending
from common_files import db_util

db_util.env = 3

# matchIds = award_pending.matchIds
# clean_match.clean_match_list(matchIds)
clean_match.clean_match(306)
