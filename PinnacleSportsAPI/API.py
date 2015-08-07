from urllib.parse import urlencode

from PinnacleSportsAPI.auth import Auth
from PinnacleSportsAPI.request import Request
from PinnacleSportsAPI.exceptions import ParameterError

from PinnacleSportsAPI.responses.sports import SportsResponse
from PinnacleSportsAPI.responses.leagues import LeaguesResponse
from PinnacleSportsAPI.responses.feed import Feed, FeedResponse


class PinnacleSportsAPI (object):
    ENDPOINT_URL = 'https://api.pinnaclesports.com/v1/'

    def __init__(self,
                 username,
                 password):
        self.auth = Auth(username, password)
        self.request = Request(self.auth.get_encoded())

    def __execute(self, method, parameters=None):
        if parameters is None:
            parameters = {}

        request_url = self.ENDPOINT_URL + method
        request_query = self.__build_query(parameters)

        request_url += '?%s' % request_query

        return self.request.do_request(request_url)

    def __build_query(self, parameters):
        query_paramters = dict()
        for key, value in parameters.items():
            if value is not None:
                query_paramters[key] = value

        return urlencode(query_paramters)

    def get_sports(self):
        response = self.__execute('sports')

        sports_response = SportsResponse(response.content)

        return sports_response.get_parsed_response()

    def get_leagues(self, sports_id):
        response = self.__execute('leagues', {
            'sportId': sports_id,
        })

        leagues_response = LeaguesResponse(response.content)

        return leagues_response.get_parsed_response()

    def get_feed(self, sports_id=None, league_id=None, odds_format=None, last=None, is_live=None, currency_code=None):
        if sports_id is None and (is_live is None or is_live != 1):
            raise ParameterError('Sports id is mandatory if is_live parameter is not set and is not equal to "1".')

        if odds_format is not None and odds_format in Feed.ODDS_FORMATS:
            raise ParameterError('Invalid odds format.')

        is_live = bool(is_live)
        if is_live:
            is_live = 1
        else:
            is_live = 0

        response = self.__execute('feed', {
            'sportId': sports_id,
            'leagueId': league_id,
            'oddsFormat': odds_format,
            'last': last,
            'islive': is_live,
            'currencyCode': currency_code,
        })

        feed_response = FeedResponse(response.content)

        return feed_response.get_parsed_response()
