# app.py
import os, flask, flask_sqlalchemy, dotenv
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']


app = flask.Flask(__name__)

# we are going to move this later, but for now make sure you run this
# every time you install on your environment. Update your username and 
# password in a new file called sql.env
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://{}:{}@localhost/postgres'.format(sql_user, sql_pwd)
db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, world!'

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
