import uuid

class Active:

    def __init__(self,username,_id=None):
        self.username = username
        self._id = uuid.uuid4().hex

    def json(self):
        return {
            '_id':self._id,
            'username':self.username
        }
