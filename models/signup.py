import uuid
import datetime

class Signup:

    def __init__(self,username,email,password,_id=None,date=None):
        self.username = username
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex
        self.date = datetime.datetime.utcnow()

    def json(self):
        return {
            "_id":self._id,
            "username":self.username,
            "email":self.email,
            "password":self.password,
            "date":self.date
        }
