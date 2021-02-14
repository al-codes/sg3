from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
 
    return render_template('homepage.html')


@app.route('/form')
def show_form():
    """Displays form."""
    
    return render_template('form.html')

@app.route('/results')
def show_results():
    """Gets user input and returns a message."""
    
    message_type = request.args.getlist("message")

    return render_template('results.html', message_type=message_type, name=session['name'])

@app.route('/save-name')
def save_name():
    """Saves name to session."""

    name = request.args.get('name')
    session['name'] = name

    return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
