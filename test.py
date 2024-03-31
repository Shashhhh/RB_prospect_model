from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = ''
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
year = 2022 # int | Year filter
team = 'team_example' # str | Team filter (optional)
conference = 'conference_example' # str | Conference abbreviation filter (optional)
start_week = 56 # int | Start week filter (optional)
end_week = 56 # int | Start week filter (optional)
season_type = 'regular' # str | Season type filter (regular, postseason, or both) (optional)
category = 'passing' # str | Stat category filter (e.g. passing) (optional)

try:
    # Player stats by season
    api_response = api_instance.get_player_season_stats(year,team='Michigan', category='rushing')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_season_stats: %s\n" % e)