from PinnacleSportsAPI.responses.base import BaseResponse, BaseModel, BaseSet


class League (BaseModel):
    id = None
    feed_contents = None
    home_team_type = None
    allow_round_robins = None
    name = None


class LeagueSet (BaseSet):
    pass


class LeaguesResponse (BaseResponse):

    def get_parsed_response(self):
        league_set = LeagueSet()

        for node in self.content.getElementsByTagName('league'):
            league = League()
            league.id = node.getAttribute('id')
            league.feed_contents = node.getAttribute('feedContents')
            league.home_team_type = node.getAttribute('homeTeamType')
            league.allow_round_robins = node.getAttribute('allowRoundRobins')
            league.name = node.firstChild.nodeValue

            league_set.add(league)

        return league_set
