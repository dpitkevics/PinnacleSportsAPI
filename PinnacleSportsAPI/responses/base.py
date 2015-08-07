

class BaseModel (object):
    pass


class BaseSet (object):

    def __init__(self):
        self.set = []

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

    def _get_element_tag(self, node, tag_name):
        try:
            return node.getElementsByTagName(tag_name)[0]
        except IndexError:
            return None

    def _get_element_tag_value(self, node, tag_name):
        try:
            return self._get_element_tag(node, tag_name).firstChild.nodeValue
        except IndexError:
            return None
        except AttributeError:
            return None

    def get_parsed_response(self):
        raise NotImplementedError('Method "get_parsed_response" must be implemented in child class.')
