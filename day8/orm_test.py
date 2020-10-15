from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
api = Api(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "email": self.email}


class Operations(Resource):

    def get(self):
        users = User.query.all()
        result = []
        for user in users:
            result.append(user.serialize())
        return result

    def post(self):

        # parser
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        parser.add_argument("username", type=str)
        parser.add_argument("email", type=str)

        args = parser.parse_args()

        username = args['username']
        id = args['id']
        email = args['email']
        output = User(id=id, username=username, email=email)
        db.session.add(output)
        db.session.commit()
        return {"Id": output.id, "username": output.username, "email": output.email}

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        parser.add_argument("username", type=str)
        parser.add_argument("email", type=str)
        args = parser.parse_args()
        username = args['username']
        id = args['id']
        email = args['email']
        user = User.query.filter_by(id=id).first()
        if user is None:
            return "Not found", 404
        user.email = email
        user.username = username
        db.session.commit()
        return user.serialize()


api.add_resource(Operations, "/users/")

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True, port=8080)
