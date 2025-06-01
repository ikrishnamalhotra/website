import os
import json
import shutil
from jinja2 import Environment, FileSystemLoader

def generate_static_site():
    # Create output directory
    output_dir = "docs"  # GitHub Pages uses 'docs' directory
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "static"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "static/images"), exist_ok=True)
    
    # Load templates
    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template('index.html')
    topic_template = env.get_template('topic.html')
    
    # Load content
    with open('content/topics.json', 'r', encoding='utf-8') as f:
        topics = json.load(f)
    
    # Generate index page
    index_html = index_template.render(topics=topics)
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    # Generate topic pages
    for topic in topics:
        topic_html = topic_template.render(
            generated_title_html=topic["title"],
            generated_title_plain=topic["title"],
            generated_audience=topic["target_audience"],
            generated_tone=topic["tone"],
            image_url=f"static/images/{topic['image_filename']}",
            content_html=topic["content_html"]
        )
        
        # Create topic page in root directory
        with open(os.path.join(output_dir, f"{topic['slug']}.html"), 'w', encoding='utf-8') as f:
            f.write(topic_html)
    
    # Create 404.html for handling client-side routing
    with open(os.path.join(output_dir, '404.html'), 'w', encoding='utf-8') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Page Not Found</title>
    <script>
        // Single Page Apps for GitHub Pages
        // MIT License
        // https://github.com/rafgraph/spa-github-pages
        var pathSegmentsToKeep = 1;
        var l = window.location;
        l.replace(
            l.protocol + '//' + l.hostname + (l.port ? ':' + l.port : '') +
            l.pathname.split('/').slice(0, 1 + pathSegmentsToKeep).join('/') + '/?/' +
            l.pathname.slice(1).split('/').slice(pathSegmentsToKeep).join('/').replace(/&/g, '~and~') +
            (l.search ? '&' + l.search.slice(1).replace(/&/g, '~and~') : '') +
            l.hash
        );
    </script>
</head>
<body>
</body>
</html>""")
    
    # Copy static files
    shutil.copytree('static', os.path.join(output_dir, 'static'), dirs_exist_ok=True)
    
    print(f"Static site generated in {output_dir}")

if __name__ == "__main__":
    generate_static_site() 