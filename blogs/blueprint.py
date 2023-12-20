from flask import Blueprint
from flask import render_template
from models import Blog

blogs = Blueprint('blogs' , __name__ , template_folder='templates')

@blogs.route('/')
def blog_list():
    blogs= Blog.query.all()
    return render_template('blogs/blogs.html' , blogs = blogs)

@blogs.route('/<slug>')
def blog_page(slug):
    blog =Blog.query.filter(Blog.slug==slug).first()
    return render_template('blogs/blog_page.html',blog =blog) 