from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

from resources.notification import notifications
from database import notification_model

app.register_blueprint(notifications)

if __name__ == '__main__':
    app.run()    