from flask import Flask, jsonify
from flask.ext.login import LoginManager, login_user, current_user, make_secure_token, logout_user

from pantesting.db.orm import Host, User
from pantesting.db_access import db_access

login_manager = LoginManager()
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?NT'
login_manager.init_app(app)
app.register_blueprint(db_access)

@app.route('/')
def index():
    return app.send_static_file('html/index.html')


@app.route('/login')
def login():
    # Checks password with the DB.
    login_user(User(name='newt', company_name='mycomp'), remember=True)
    return 'OK'

@app.route('/logout')
def logout():
    logout_user()
    return 'OK'

@app.route('/get_user')
def get_current_user():
    if current_user and hasattr(current_user, 'company_name'):
        return jsonify(current_user.to_dict())
    return ''

@login_manager.user_loader
def load_user(userid):
    # Should fetch from the DB
    return User(name='newt', company_name='PayPal Inc.')

if __name__ == '__main__':
    app.run(debug=True)