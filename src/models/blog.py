import datetime
import uuid

from src.common.database import Database
from src.models.post import Post


class Blof(object):
    def __init__(self, author, title, decription, _id=None):
        self.author = author
        self.title = title
        self.decription = decription
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self,title,content,
                 date = datetime.datetime.utcnow()):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post data,or leave blank for today")



        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author':self.author,
            'title':self.title,
            'description':self.decription,
            '_id':self._id
        }

    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.find_one(colllection='blogs',
                                      query={'_id':id})
        return cls(**blog_data)
        # return cls(author=blog_data['author'],
        #            title=blog_data['title'],
        #            decription=blog_data['description'],
        #            _id = blog_data['_id'])
