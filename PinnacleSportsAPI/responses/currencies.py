from PinnacleSportsAPI.responses.base import BaseResponse, BaseModel, BaseSet


class Currency (BaseModel):
    code = None
    name = None


class CurrencySet (BaseSet):
    pass


class CurrenciesResponse (BaseResponse):

    def get_parsed_response(self):
        currency_set = CurrencySet()

        for node in self.content.getElementsByTagName('currency'):
            currency = Currency()
            currency.code = node.getAttribute('code')
            currency.name = node.firstChild.nodeValue

            currency_set.add(currency)

        return currency_set
