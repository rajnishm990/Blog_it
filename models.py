from app import db
from datetime import datetime
from time import time
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern , '-', s)

class Blog(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String , unique = True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default = datetime.now)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.generate_slug()
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = slugify(str(int(time)))
    def __repr__(self):
        return f'<Blog id: {self.id},title: {self.title}>'