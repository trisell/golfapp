from app import app, db, lm
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    isAdmin = db.Column(db.Boolean, default=True) 
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
       return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id) 
    def __repr__(self):
        return '<Admin %r>' % (self.username)
    
class Team(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    isactive = db.Column(db.String(80))
    members = db.relationship('TeamMembers', backref='members', lazy='dynamic')
    score = db.relationship('TeamScore', backref='score', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
       return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)
    
    def __repr__(self):
        return '<Team %r>' % (self.teamname)

class TeamMembers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member1 = db.Column(db.String(80))
    member2 = db.Column(db.String(80))
    member3 = db.Column(db.String(80))
    member4 = db.Column(db.String(80))
    teamid = db.Column(db.Integer, db.ForeignKey('team.id'))  

class TeamScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hole1 = db.Column(db.Integer, default=0)
    hole2 = db.Column(db.Integer, default=0)
    hole3 = db.Column(db.Integer, default=0)
    hole4 = db.Column(db.Integer, default=0)
    hole5 = db.Column(db.Integer, default=0)
    hole6 = db.Column(db.Integer, default=0)
    hole7 = db.Column(db.Integer, default=0)
    hole8 = db.Column(db.Integer, default=0)
    hole9 = db.Column(db.Integer, default=0)
    hole10 = db.Column(db.Integer, default=0)
    hole11 = db.Column(db.Integer, default=0)
    hole12 = db.Column(db.Integer, default=0)
    hole13 = db.Column(db.Integer, default=0)
    hole14 = db.Column(db.Integer, default=0)
    hole15 = db.Column(db.Integer, default=0)
    hole16 = db.Column(db.Integer, default=0)
    hole17 = db.Column(db.Integer, default=0)
    hole18 = db.Column(db.Integer, default=0)
    teamid = db.Column(db.Integer, db.ForeignKey('team.id'))  
