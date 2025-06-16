from flask import Flask, render_template, request, redirect, url_for

# explicita onde está a pasta static e qual URL usar
app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/static'
)

# SECRET_KEY forte (32 bytes hex)
app.config['SECRET_KEY'] = '4e48b6706919f99898d34f21dea65f6e4663f2afa2011fad3d9b38c435b2d10f'

# In‑memory store de usuários: {email: senha}
users = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    gif = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email not in users or users[email] != password:
            message = 'Essa conta não existe ou a senha está incorreta'
            gif = url_for('static', filename='images/cat_sad.gif')
        else:
            message = 'Login bem‑sucedido!'
            gif = url_for('static', filename='images/cats_dancing.gif')
    return render_template('login.html', message=message, gif=gif)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    gif = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            message = 'Essa conta já existe'
            gif = url_for('static', filename='images/cat_sad.gif')
        else:
            users[email] = password
            message = 'Cadastro realizado com sucesso!'
            gif = url_for('static', filename='images/cats_dancing.gif')
    return render_template('register.html', message=message, gif=gif)

if __name__ == '__main__':
    app.run(debug=True)
