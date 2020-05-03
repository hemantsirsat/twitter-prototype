import uuid
import datetime
from common.database import Database

class Post:

    def __init__(self,username,content,_id=None,date=None):
        self.username = username
        self.content = content
        self._id = uuid.uuid4().hex
        self.date = datetime.datetime.utcnow()

    def json(self):
        return{
            '_id':self._id,
            'date':self.date,
            'username':self.username,
            'content':self.content
        }


