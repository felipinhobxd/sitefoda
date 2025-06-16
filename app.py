from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

@app.route("/")
def home():
    return redirect(url_for("login"))  # ROTA CORRIGIDA AQUI

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        users = load_users()

        if email in users and users[email] == password:
            return render_template("success.html", gif="cats_dancing.gif")
        else:
            flash("Essa conta não existe ou a senha está incorreta")
            return render_template("login.html", gif="cat_sad.gif")
    return render_template("login.html", gif=None)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        users = load_users()

        if email in users:
            flash("Essa conta já existe")
            return render_template("register.html", gif="cat_sad.gif")
        else:
            users[email] = password
            save_users(users)
            return render_template("success.html", gif="cats_dancing.gif")
    return render_template("register.html", gif=None)

if __name__ == "__main__":
    app.run(debug=True)
