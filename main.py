from app import app
import views
from blogs.blueprint import blogs
from app import db

app.register_blueprint(blogs , url_prefix ='/blogs')
if __name__ == '__main__':
    db.create_all()
    app.run()