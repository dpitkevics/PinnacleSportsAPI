

class BaseModel (object):
    pass


class BaseSet (object):
    set = []

    def __iter__(self):
        for sports in self.set:
            yield sports

    def add(self, instance):
        self.set.append(instance)


class BaseResponse (object):
    def __init__(self, content):
        self.content = content
