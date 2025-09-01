from flask import Flask, render_template
from config import BLOG_POSTS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=BLOG_POSTS)

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=BLOG_POSTS)

@app.route("/blog/<int:post_id>")
def blog_detail(post_id):
    post = next((p for p in BLOG_POSTS if p["id"] == post_id), None)
    return render_template("blog_detail.html", post=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
