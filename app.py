from flask import Flask, render_template, request, session, redirect, url_for, flash
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'abcd123'

# -----------------------------
# Load Battery Models
# -----------------------------
soh_model = joblib.load("soh_model.pkl")
rul_model = joblib.load("rul_model.pkl")
scaler = joblib.load("scaler.pkl")
le_battery = joblib.load("battery_le.pkl")

# -----------------------------
# User storage (temporary)
# -----------------------------
users = {}

# -----------------------------
# Home Page
# -----------------------------
@app.route('/')
def home():
    return render_template('home.html')


# -----------------------------
# User Registration
# -----------------------------
@app.route('/user_registration', methods=['GET', 'POST'])
def user_registration():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('user_registration'))

        if username not in users:
            users[username] = {'password': password}
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('user_login'))
        else:
            flash('User already exists', 'error')

    return render_template('user_registration.html')


# -----------------------------
# User Login
# -----------------------------
@app.route('/user_login', methods=['GET', 'POST'])
def user_login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:

            session['username'] = username
            flash('Login successful', 'success')
            return redirect(url_for('index'))

        else:
            flash('Invalid username or password', 'error')

    return render_template('user_login.html')


# -----------------------------
# Dashboard
# -----------------------------
@app.route('/index')
def index():

    if 'username' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('user_login'))

    return render_template('index.html')


# -----------------------------
# Battery Prediction
# -----------------------------
@app.route('/predict', methods=['GET', 'POST'])

def predict():

    if 'username' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('user_login'))

    if request.method == 'POST':

        battery_id = request.form['battery_id']
        cycle = float(request.form['cycle'])
        chI = float(request.form['chI'])
        chV = float(request.form['chV'])
        chT = float(request.form['chT'])
        disI = float(request.form['disI'])
        disV = float(request.form['disV'])
        disT = float(request.form['disT'])
        BCt = float(request.form['BCt'])

        battery_encoded = le_battery.transform([battery_id])[0]

        input_features = np.array([[battery_encoded, cycle, chI, chV, chT, disI, disV, disT, BCt]])

        input_scaled = scaler.transform(input_features)

        predicted_soh = soh_model.predict(input_scaled)[0]
        predicted_rul = rul_model.predict(input_scaled)[0]

        return render_template(
            'result.html',
            soh=round(predicted_soh, 2),
            rul=int(predicted_rul),
            battery_id=battery_id,
            cycle=int(cycle),
            chI=chI,
            chV=chV,
            chT=chT,
            disI=disI,
            disV=disV,
            disT=disT,
            BCt=BCt
        )

    return render_template('predict.html')


# -----------------------------
# Logout
# -----------------------------
@app.route('/logout')

def logout():

    session.pop('username', None)

    flash('You have been logged out', 'info')

    return redirect(url_for('home'))


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)