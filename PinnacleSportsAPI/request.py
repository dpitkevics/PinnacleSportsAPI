from urllib import request as urlrequest

from PinnacleSportsAPI.response import Response


class Request(object):
    def __init__(self, auth_string):
        self.auth_string = auth_string

    def do_request(self, url):
        headers = {'Content-length': '0',
                   'Content-type': 'application/xml',
                   'Authorization': 'Basic %s' % self.auth_string}

        req = urlrequest.Request(url, headers=headers)

        resp = urlrequest.urlopen(req)
        content = resp.read()

        response = Response(content)

        return response
