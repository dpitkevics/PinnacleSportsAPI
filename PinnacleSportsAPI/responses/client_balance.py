from PinnacleSportsAPI.responses.base import BaseResponse, BaseModel


class ClientBalance(BaseModel):
    available_balance = None
    outstanding_transactions = None
    given_credit = None
    currency = None


class ClientBalanceResponse(BaseResponse):

    def get_parsed_response(self):
        client_balance = ClientBalance()
        client_balance.available_balance = self._get_element_tag_value(self.content, 'availableBalance')
        client_balance.outstanding_transactions = self._get_element_tag_value(self.content, 'outstandingTransactions')
        client_balance.given_credit = self._get_element_tag_value(self.content, 'givenCredit')
        client_balance.currency = self._get_element_tag_value(self.content, 'currency')

        return client_balance