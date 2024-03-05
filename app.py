from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Hardcoded username and password (replace with your own logic for a real application)
    correct_username = "user123"
    correct_password = "password123"

    # Get user input from the HTML form
    username_input = request.form['username']
    password_input = request.form['password']

    # Check if the entered credentials are correct
    if username_input == correct_username and password_input == correct_password:
        return render_template('success.html', username=username_input)
    else:
        return render_template('failure.html')

if __name__ == '__main__':
    app.run(debug=True)
