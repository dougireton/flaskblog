from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Anthony Roberson',
        'title': 'Connecting to an RDS Database with Lambda',
        'content': 'This article will detail deploying a Lambda function written in .NET Core C# that connects to an RDS database, selects some data, and returns the output in JSON format.',
        'date_posted': 'February 6th, 2019'
    },
    {
        'author': 'Andrew Clark',
        'title': 'Global Accelerator',
        'content': 'Among the many announcements at this year AWS re:Invent conference was a new service: Global Accelerator.',
        'date_posted': 'December 12th, 2018'
    },
    {
        'author': 'Jameson Ricks',
        'title': 'Creating Dynamic Scripts using EC2 Metadata',
        'content': 'CloudFormation templates, when written with portability in mind, allow you to write one template and deploy it multiple times in many different environments.',
        'date_posted': 'December 11th, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')