from app import models
from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, IntegerField
from wtforms.validators import Required, EqualTo



class AdminLoginForm(Form):
    username = TextField('adminUnLogin', [Required()])
    password = PasswordField('adminPwLogin', [Required()]) 

class AdminCreationForm(Form):
    username = TextField('adminUnCreate', [Required()])
    password = PasswordField('adminPwCreate', [Required(), EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Repeat Password')

class TeamCreateForm(Form):
    teamname = TextField('teamNameCreate', [Required()])
    teamPassword = PasswordField('adminPwCreate', [Required(), EqualTo('teamConfirm', message='Passwords do not match')])
    teamConfim = PasswordField('Repeat Password')
    
class TeamLoginForm(Form):
    username = TextField('teamUnLogin', [Required()])
    password = PasswordField('teamPwLogin', [Required()]) 

class TeamMemebersForm(Form):
    team_member1 = TextField('teamMem1')
    team_member2 = TextField('teamMem2')
    team_member3 = TextField('teamMem3')
    team_member4 = TextField('teamMem4')

class TeamScoreForm(Form):
    hole1 = IntegerField('hole1')
    hole2 = IntegerField('hole2')
    hole3 = IntegerField('hole3')
    hole4 = IntegerField('hole4')
    hole5 = IntegerField('hole5')
    hole6 = IntegerField('hole6')
    hole7 = IntegerField('hole7')
    hole8 = IntegerField('hole8')
    hole9 = IntegerField('hole9')
    hole10 = IntegerField('hole10')
    hole11 = IntegerField('hole11')
    hole12 = IntegerField('hole12')
    hole13 = IntegerField('hole13')
    hole14 = IntegerField('hole14')
    hole15 = IntegerField('hole15')
    hole16 = IntegerField('hole16')
    hole17 = IntegerField('hole17')
    hole18 = IntegerField('hole18')








