from urllib.parse import urlencode

from PinnacleSportsAPI.auth import Auth
from PinnacleSportsAPI.request import Request

from PinnacleSportsAPI.responses.sports import SportsResponse
from PinnacleSportsAPI.responses.leagues import LeaguesResponse


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
        request_query = urlencode(parameters)

        request_url += '?%s' % request_query

        return self.request.do_request(request_url)

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
