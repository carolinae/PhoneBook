import uuid


class Contact:
    def __init__(self, first, last, number, id=None):
        self.first = first.title()
        self.last = last.title()
        if '-' in number:
            self.number = number
        else:
            self.number = number[:3] + '-' + number[3:]
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id