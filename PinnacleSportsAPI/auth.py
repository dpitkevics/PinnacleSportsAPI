import base64


class Auth (object):
    def __init__(self,
                 username,
                 password):
        self.username = username
        self.password = password

    def get_formatted(self):
        return '%s:%s' % (self.username, self.password)

    def get_encoded(self):
        return base64.b64encode(self.get_formatted().encode('utf-8')).decode('ascii')
