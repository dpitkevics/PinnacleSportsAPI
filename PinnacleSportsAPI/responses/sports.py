from PinnacleSportsAPI.responses.base import BaseResponse, BaseModel, BaseSet


class Sports (BaseModel):
    id = None
    feed_contents = None
    name = None


class SportsSet (BaseSet):
    pass


class SportsResponse (BaseResponse):

    def get_parsed_response(self):
        sports_set = SportsSet()

        for node in self.content.getElementsByTagName('sport'):
            sports = Sports()
            sports.id = node.getAttribute('id')
            sports.feed_contents = node.getAttribute('feedContents')
            sports.name = node.firstChild.nodeValue

            sports_set.add(sports)

        return sports_set
