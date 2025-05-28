#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint
from .session_auth import bp


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

User.load_from_file()

def init_app(app):
    app.register_blueprint(bp)
