from PinnacleSportsAPI.responses.base import BaseResponse, BaseModel, BaseSet


class Line(BaseModel):
    status = None
    price = None
    line_id = None
    alt_line_id = None
    team_1_score = None
    team_2_score = None
    team_1_red_cards = None
    team_2_red_cards = None
    max_risk_stake = None
    min_risk_stake= None
    max_win_stake = None
    min_win_stake = None
    effective_as_of = None


class LineResponse(BaseResponse):

    def get_parsed_response(self):
        line = Line()
        line.status = self._get_element_tag_value(self.content, 'status')
        line.price = self._get_element_tag_value(self.content, 'price')
        line.line_id = self._get_element_tag_value(self.content, 'lineId')
        line.alt_line_id = self._get_element_tag_value(self.content, 'altLineId')
        line.team_1_score = self._get_element_tag_value(self.content, 'team1Score')
        line.team_2_score = self._get_element_tag_value(self.content, 'team2Score')
        line.team_1_red_cards = self._get_element_tag_value(self.content, 'team1RedCards')
        line.team_2_red_cards = self._get_element_tag_value(self.content, 'team2RedCards')
        line.max_risk_stake = self._get_element_tag_value(self.content, 'maxRiskStake')
        line.min_risk_stake = self._get_element_tag_value(self.content, 'minRiskStake')
        line.max_win_stake = self._get_element_tag_value(self.content, 'maxWinStake')
        line.min_win_stake = self._get_element_tag_value(self.content, 'minWinStake')
        line.effective_as_of = self._get_element_tag_value(self.content, 'effectiveAsOf')

        return line