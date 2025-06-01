# Content Hub Frontend

A static website that displays generated content from the content generator.

## Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Create required directories:
```bash
mkdir -p content static/images templates
```

3. Place your generated content:
- Put `topics.json` in the `content/` directory
- Put generated images in the `static/images/` directory

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask development server:
```bash
python app.py
```

The site will be available at http://localhost:5000

## Project Structure

```
website/
├── app.py              # Flask application
├── generate_static.py  # Static site generator
├── requirements.txt    # Python dependencies
├── content/           # Generated content
│   └── topics.json    # Topic data
├── static/            # Static files
│   ├── css/          # Stylesheets
│   └── images/       # Generated images
└── templates/         # HTML templates
    ├── index.html    # Homepage template
    └── topic.html    # Topic page template
```

## Content Generation

Content is generated using a separate Colab notebook. The generated content should be placed in the following structure:

```
content/
└── topics.json       # Contains all topic data including content and metadata
static/
└── images/          # Contains all generated images
```

## GitHub Pages Deployment

This site is automatically deployed to GitHub Pages whenever changes are pushed to the main branch. The deployment process:

1. Generates static HTML files from the templates and content
2. Deploys the static site to the main branch
3. Makes the site available at `https://yourusername.github.io/your-repo`

To enable GitHub Pages:

1. Go to your repository settings
2. Navigate to "Pages" in the sidebar
3. Under "Source", select "Deploy from a branch"
4. Select the `main` branch and `/ (root)` folder
5. Click "Save"

The site will be automatically updated whenever you push changes to the main branch.

## Local Static Site Generation

To generate the static site locally:

```bash
python generate_static.py
```

This will create a `docs` directory containing the static site files.

## Deployment

This application can be deployed to any platform that supports Python/Flask applications, such as:
- Heroku
- PythonAnywhere
- Google Cloud Run
- AWS Elastic Beanstalk

For deployment, make sure to:
1. Set up the required environment variables
2. Configure the static file serving
3. Set up a proper WSGI server (e.g., Gunicorn) 