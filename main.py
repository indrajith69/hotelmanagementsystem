from flask import Flask, render_template, redirect, url_for, request
import functions


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('login-email')
    password = request.form.get('login-password')
    role = request.form.get('login-role')

    print(role)
    print(email)
    print(password)

    return "loged in"


@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('register-email')
    password = request.form.get('register-password')
    firstname = request.form.get('register-firstname')
    lastname = request.form.get('register-lastname')
    phoneno = request.form.get('register-phon')

    print(firstname)
    print(lastname)
    print(email)
    print(phoneno)
    print(password)

    return "loged in"

if __name__ == '__main__':
    functions.test()
    app.run(host='192.168.1.62', port=5000, debug=True)