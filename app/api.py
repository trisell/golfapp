from flask import Flask
from flask_restful import Resource, reqparse
from app import app, api, db
from .models import Team, TeamMembers, TeamScore

class CreateTeam(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('teamname', type=str, help='New team name')
            parser.add_argument('password', type=str, help="Team's login password")
            parser.add_argument('member1', type=str, help="Team's login password")
            parser.add_argument('member2', type=str, help="Team's login password")
            parser.add_argument('member3', type=str, help="Team's login password")
            parser.add_argument('member4', type=str, help="Team's login password")
 
            args = parser.parse_args()
            _teamname = args['teamname']
            _password = args['password']
            if args['teamname'] is None:
                return jsonify(msg = "Please enter a team name.", status_code = '200')
            
            elif args['password'] is None:
                return jsonify(msg = "Please enter a password.", status_code = '200')

            else:
                team = Team(teamname=_teamname, password=_password)
                db.session.add(team)
                db.session.commit
                
                t = Team.query.filter_by(teamname=_teamname).first()
                
                members = TeamMembers(member1=args['member1'], member2=args['member2'], member3=args['member3'], member4=args['member4'], members=t)

                score = TeamScore(score=t)
                db.session.add(members, score)
                db.session.commit
               
            return{'teamname': args['teamname'], 'password': args['password']}

        except Exception as e:
            return {'error': str(e)}


class GetScore(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('hole1', type=str, help='Hole 1 Score')
            parser.add_argument('hole2', type=str, help='Hole 2 Score')           
            parser.add_argument('hole3', type=str, help='Hole 3 Score')           
            parser.add_argument('hole4', type=str, help='Hole 4 Score')
            parser.add_argument('hole5', type=str, help='Hole 5 Score')
            parser.add_argument('hole6', type=str, help='Hole 6 Score')
            parser.add_argument('hole7', type=str, help='Hole 7 Score')
            parser.add_argument('hole8', type=str, help='Hole 8 Score')
            parser.add_argument('hole9', type=str, help='Hole 9 Score')
            parser.add_argument('hole10', type=str, help='Hole 10 Score')
            parser.add_argument('hole11', type=str, help='Hole 11 Score')
            parser.add_argument('hole12', type=str, help='Hole 12 Score')
            parser.add_argument('hole13', type=str, help='Hole 13 Score')
            parser.add_argument('hole14', type=str, help='Hole 14 Score')
            parser.add_argument('hole15', type=str, help='Hole 15 Score')
            parser.add_argument('hole16', type=str, help='Hole 16 Score')
            parser.add_argument('hole17', type=str, help='Hole 17 Score')
            parser.add_argument('hole18', type=str, help='Hole 18 Score')

        except Exception as e:
            return {'error': str(e)}



    def get(self):
        try:
            pass
        # gets all the hole scores from db and returns JSON.
            
        except Exception as e:
            return {'error': str(e)}











