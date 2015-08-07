

class BaseModel (object):
    pass


class BaseSet (object):
    set = []

    def __iter__(self):
        for sports in self.set:
            yield sports

    def __getitem__(self, index):
        return self.set[index]

    def __setitem__(self, index, value):
        self.set[index] = value

    def __delitem__(self, index):
        del self.set[index]

    def add(self, instance):
        self.set.append(instance)


class BaseResponse (object):
    def __init__(self, content):
        self.content = content

    def get_parsed_response(self):
        raise NotImplementedError('Method "get_parsed_response" must be implemented in child class.')
