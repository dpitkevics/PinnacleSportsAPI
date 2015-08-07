from urllib.parse import urlencode

from PinnacleSportsAPI.auth import Auth
from PinnacleSportsAPI.request import Request


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

        self.request.do_request(request_url)

    def get_sports(self):
        response = self.__execute('sports')

