
from flask import Flask, redirect, url_for, render_template, request
import flask_sqlalchemy
import psycopg2
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from flask_caching import Cache
from celery import Celery

app = Flask(__name__)
app.config.from_object('project.config.Config')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
cache = Cache(app)

#Connection to postgres db is not working