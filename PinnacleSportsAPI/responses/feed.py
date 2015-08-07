from PinnacleSportsAPI.responses.base import BaseResponse, BaseModel, BaseSet


class FeedMaxBetType(BaseModel):
    spread = None
    total_points = None
    money_line = None
    team_totals = None


class FeedTeamTotalPointsContainerType(BaseModel):
    home_team_total = None
    away_team_total = None


class FeedMoneyLineType(BaseModel):
    away_price = None
    home_price = None
    draw_price = None


class FeedTotalPointsType(BaseModel):
    alt_line_id = None
    points = None
    over_price = None
    under_price = None


class FeedSpreadType(BaseModel):
    alt_line_id = None
    away_spread = None
    away_price = None
    home_spread = None
    home_price = None


class FeedPeriodType(BaseModel):
    line_id = None
    number = None
    description = None
    cutoff_date_time = None
    spread_set = None
    total_set = None
    money_line = None
    team_totals = None
    max_bet_amount = None


class FeedTeamType(BaseModel):
    type = None
    name = None
    rotation_number = None
    pitcher = None
    score = None
    red_cards = None


class FeedEventType(BaseModel):
    id = None
    start_date_time = None
    is_live = None
    live_status = None
    status = None
    draw_rotation_number = None
    away_team = None
    home_team = None
    period_set = None


class FeedLeagueType(BaseModel):
    id = None
    event_set = None


class FeedSportType(BaseModel):
    id = None
    league_set = None


class FeedType(BaseModel):
    feed_time = None
    feed_sport_set = None


class FeedTotalSet(BaseSet):
    pass


class FeedSpreadSet(BaseSet):
    pass


class FeedPeriodSet(BaseSet):
    pass


class FeedEventSet(BaseSet):
    pass


class FeedLeagueSet(BaseSet):
    pass


class FeedSportSet(BaseSet):
    pass


class Feed(BaseModel):
    ODDS_FORMATS = {
        'ODDS_FORMAT_AMERICAN': 'AMERICAN',
        'ODDS_FORMAT_DECIMAL': 'DECIMAL',
        'ODDS_FORMAT_HONGKONG': 'HONGKONG',
        'ODDS_FORMAT_INDONESIAN': 'INDONESIAN',
        'ODDS_FORMAT_MALAY': 'MALAY',
    }

    feed_type = None


class FeedResponse(BaseResponse):
    def get_parsed_response(self):
        feed = Feed()
        feed.feed_type = FeedType()

        feed_node = self._get_element_tag(self.content, 'fdTime')
        feed.feed_type.feed_time = feed_node.firstChild.nodeValue

        feed.feed_type.feed_sport_set = FeedSportSet()
        for feed_sport_node in self.content.getElementsByTagName('sport'):
            feed_sport_type = FeedSportType()
            feed_sport_type.id = self._get_element_tag_value(feed_sport_node, 'id')

            feed_sport_type.league_set = FeedLeagueSet()
            for feed_league_node in feed_sport_node.getElementsByTagName('league'):
                feed_league_type = FeedLeagueType()
                feed_league_type.id = self._get_element_tag_value(feed_league_node, 'id')

                feed_league_type.event_set = FeedEventSet()
                for feed_event_node in feed_league_node.getElementsByTagName('event'):
                    feed_event_type = FeedEventType()
                    feed_event_type.id = self._get_element_tag_value(feed_event_node, 'id')
                    feed_event_type.start_date_time = self._get_element_tag_value(feed_event_node, 'startDateTime')
                    feed_event_type.is_live = self._get_element_tag_value(feed_event_node, 'IsLive')
                    feed_event_type.live_status = self._get_element_tag_value(feed_event_node, 'lStatus')
                    feed_event_type.status = self._get_element_tag_value(feed_event_node, 'status')
                    feed_event_type.draw_rotation_number = self._get_element_tag_value(feed_event_node, 'drawRotNum')

                    home_team_node = self._get_element_tag(feed_event_node, 'homeTeam')
                    home_team_type = FeedTeamType()
                    home_team_type.type = home_team_node.getAttribute('type')
                    home_team_type.name = self._get_element_tag_value(home_team_node, 'name')
                    home_team_type.rotation_number = self._get_element_tag_value(home_team_node, 'rotNum')
                    home_team_type.pitcher = self._get_element_tag_value(home_team_node, 'pitcher')
                    home_team_type.score = self._get_element_tag_value(home_team_node, 'score')
                    home_team_type.red_cards = self._get_element_tag_value(home_team_node, 'redCards')

                    feed_event_type.home_team = home_team_type

                    away_team_node = self._get_element_tag(feed_event_node, 'awayTeam')
                    away_team_type = FeedTeamType()
                    away_team_type.type = away_team_node.getAttribute('type')
                    away_team_type.name = self._get_element_tag_value(away_team_node, 'name')
                    away_team_type.rotation_number = self._get_element_tag_value(away_team_node, 'rotNum')
                    away_team_type.pitcher = self._get_element_tag_value(away_team_node, 'pitcher')
                    away_team_type.score = self._get_element_tag_value(away_team_node, 'score')
                    away_team_type.red_cards = self._get_element_tag_value(away_team_node, 'redCards')

                    feed_event_type.away_team = away_team_type

                    feed_event_type.period_set = FeedPeriodSet()
                    for feed_period_node in feed_event_node.getElementsByTagName('period'):
                        feed_period_type = FeedPeriodType()
                        feed_period_type.line_id = feed_period_node.getAttribute('lineId')
                        feed_period_type.number = self._get_element_tag_value(feed_period_node, 'number')
                        feed_period_type.description = self._get_element_tag_value(feed_period_node, 'description')
                        feed_period_type.cutoff_date_time = self._get_element_tag_value(feed_period_node, 'cutoffDateTime')

                        feed_period_type.spread_set = FeedSpreadSet()
                        for feed_spread_node in feed_period_node.getElementsByTagName('spread'):
                            feed_spread_type = FeedSpreadType()
                            feed_spread_type.alt_line_id = feed_spread_node.getAttribute('altLineId')
                            feed_spread_type.away_spread = self._get_element_tag_value(feed_spread_node, 'awaySpread')
                            feed_spread_type.away_price = self._get_element_tag_value(feed_spread_node, 'awayPrice')
                            feed_spread_type.home_spread = self._get_element_tag_value(feed_spread_node, 'homeSpread')
                            feed_spread_type.home_price = self._get_element_tag_value(feed_spread_node, 'homePrice')

                            feed_period_type.spread_set.add(feed_spread_type)

                        feed_period_type.total_set = FeedTotalSet()
                        for feed_total_node in feed_period_node.getElementsByTagName('total'):
                            feed_total_type = FeedTotalPointsType()
                            feed_total_type.alt_line_id = feed_total_node.getAttribute('altLineId')
                            feed_total_type.points = self._get_element_tag_value(feed_total_node, 'points')
                            feed_total_type.over_price = self._get_element_tag_value(feed_total_node, 'overPrice')
                            feed_total_type.under_price = self._get_element_tag_value(feed_total_node, 'underPrice')

                            feed_period_type.total_set.add(feed_total_type)

                        feed_money_line_node = self._get_element_tag(feed_period_node, 'moneyLine')
                        feed_money_line_type = FeedMoneyLineType()
                        feed_money_line_type.away_price = self._get_element_tag_value(feed_money_line_node, 'awayPrice')
                        feed_money_line_type.home_price = self._get_element_tag_value(feed_money_line_node, 'homePrice')
                        feed_money_line_type.draw_price = self._get_element_tag_value(feed_money_line_node, 'drawPrice')

                        feed_period_type.money_line = feed_money_line_type

                        feed_max_bet_amount_node = feed_period_node.getElementsByTagName('maxBetAmount')
                        feed_max_bet_amount_type = FeedMaxBetType()
                        feed_max_bet_amount_type.spread = self._get_element_tag_value(feed_max_bet_amount_node, 'spread')
                        feed_max_bet_amount_type.total_points = self._get_element_tag_value(feed_max_bet_amount_node, 'totalPoints')
                        feed_max_bet_amount_type.money_line = self._get_element_tag_value(feed_max_bet_amount_node, 'moneyLine')

                        feed_event_type.period_set.add(feed_period_type)

                    feed_league_type.event_set.add(feed_event_type)

                feed_sport_type.league_set.add(feed_league_type)

            feed.feed_type.feed_sport_set.add(feed_sport_type)

        return feed
