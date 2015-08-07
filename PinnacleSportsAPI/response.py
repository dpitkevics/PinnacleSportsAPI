from xml.dom import minidom


class Response (object):
    def __init__(self, content):
        self.content = self.__decode_content(content)
        self.content = self.__parse_content(self.content)

    @staticmethod
    def __decode_content(content):
        return content.decode('utf-8')

    @staticmethod
    def __parse_content(content):
        e = minidom.parseString(content)

        return e
