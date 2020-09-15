from flask import Blueprint

bp = Blueprint('main', __name__)

from app.resources import notification