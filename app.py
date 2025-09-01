from flask import Flask, render_template, request
import config

app = Flask(__name__)

# Sample blog data
blogs = [
    {
        "id": 1,
        "title": "The Rise of AI in 2025",
        "category": "AI",
        "excerpt": "Artificial Intelligence is reshaping industries like never before...",
        "content": "Artificial Intelligence in 2025 has moved beyond research labs and into everyday life...",
        "image": "images/ai.jpg"
    },
    {
        "id": 2,
        "title": "Web3: Hype or the Future?",
        "category": "Blockchain",
        "excerpt": "Web3 promises decentralization, but does it live up to expectations?",
        "content": "Web3 continues to divide opinions across the tech landscape...",
        "image": "images/web3.jpg"
    },
    {
        "id": 3,
        "title": "Top 10 Python Libraries for Developers",
        "category": "Programming",
        "excerpt": "Here’s a curated list of Python libraries that will boost your productivity.",
        "content": "Python has become the go-to language for developers, and in 2025 these libraries are must-haves...",
        "image": "images/python.jpg"
    }
]

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = next((b for b in blogs if b["id"] == blog_id), None)
    return render_template("blog_detail.html", blog=blog)

@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    filtered = [b for b in blogs if query in b["title"].lower() or query in b["content"].lower()]
    return render_template("index.html", blogs=filtered, search_query=query)

@app.route('/category/<category>')
def category(category):
    filtered = [b for b in blogs if b["category"].lower() == category.lower()]
    return render_template("index.html", blogs=filtered, category=category)

if __name__ == "__main__":
    app.run(debug=True)
