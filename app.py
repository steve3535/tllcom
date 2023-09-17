from flask import Flask, render_template,url_for, request, redirect 
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required,login_user,logout_user,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
app.config['SECRET_KEY'] = 'your_secure_and_random_string_here'

api = Api(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)
    password = db.Column(db.String(150),nullable=False)

    @property
    def is_active(self):
    # Assuming all users are active (adjust as needed)
      return True

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

        
   
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class HelloWorld(Resource):
    def get(self):
        return 'Hello, World'

api.add_resource(HelloWorld,'/lab1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        user = User.query.filter_by(username=username).first()
        if user:
            return 'Username already exists!'

        # Encrypt the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Create a new user and save to database
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True)
