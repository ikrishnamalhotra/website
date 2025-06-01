from flask import Flask, render_template_string, abort
import json
import os

app = Flask(__name__)

# Load the generated content
def load_content():
    content_dir = "content"
    if not os.path.exists(content_dir):
        os.makedirs(content_dir)
    
    # Load topics from the JSON file
    topics_file = os.path.join(content_dir, "topics.json")
    if os.path.exists(topics_file):
        with open(topics_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Load the HTML templates
with open("templates/index.html", "r", encoding="utf-8") as f:
    INDEX_TEMPLATE = f.read()

with open("templates/topic.html", "r", encoding="utf-8") as f:
    TOPIC_TEMPLATE = f.read()

@app.route("/")
def index():
    topics = load_content()
    return render_template_string(INDEX_TEMPLATE, topics=topics)

@app.route("/topic/<slug>")
def topic_detail(slug):
    topics = load_content()
    topic = next((t for t in topics if t["slug"] == slug), None)
    if topic is None:
        abort(404)
    
    return render_template_string(
        TOPIC_TEMPLATE,
        generated_title_html=topic["title"],
        generated_title_plain=topic["title"],
        generated_audience=topic["target_audience"],
        generated_tone=topic["tone"],
        image_url=f"/static/images/{topic['image_filename']}",
        content_html=topic["content_html"]
    )

if __name__ == "__main__":
    app.run(debug=True) 