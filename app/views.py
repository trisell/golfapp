from app import app, db, lm, api
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_restful import Api
from .models import Admin, Team
from .api import CreateTeam
from .forms import TeamLoginForm
@lm.user_loader
def load_Team(id):
    return Team.query.get(int(id))
@app.route('/')
def index():
        return "Hello World"
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = TeamLoginForm()
    return render_template('login.html', title='Sign In', form=form)
"""            
@app.route('/sponsors')



@app.route('/rules')
"""
api.add_resource(CreateTeam, '/CreateTeam')
