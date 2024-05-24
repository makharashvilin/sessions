from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'badri'
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('profile'))
    return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
def profile():
    if 'username' in session:
        user = session['user']
        return render_template('home.html', user=user)
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['username'] = username
            session.permanent = True
            return redirect(url_for('home'))
        return render_template('home.html', username = username)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)





