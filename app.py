from flask import Flask, render_template
from scraper import scrape_github_projects

app = Flask(__name__)

@app.route('/')
def home():
    projects = scrape_github_projects()
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
