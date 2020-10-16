from flask import Flask, abort
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)


# parser
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("username", type=str)
parser.add_argument("email", type=str)


# abort if not a valid user id
def abort_if_invalid_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        abort("Not a valid id", 404)


class User(db.Model):

    """ Model class for ORM 

        attributes:
            id : int
            username : str
            email : str
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "email": self.email}


class UsersList(Resource):
    """ For /users endpoint 

        methods: 
            get - accepts nothing, returns all users
            post - accepts user data, stores to db, returns accepted user

    """

    def get(self):
        users = User.query.all()
        result = []
        for user in users:
            result.append(user.serialize())
        return "No users", 404 if len(result) == 0 else result

    def post(self):
        args = parser.parse_args()
        username = args['username']
        id = args['id']
        email = args['email']
        output = User(id=id, username=username, email=email)
        db.session.add(output)
        db.session.commit()
        return {"Id": output.id, "username": output.username, "email": output.email}


class IndividualUser(Resource):

    """ For /users/<int:id> end point

        methods:
            get - accepts user id, returns user for that id
            put - accepts user id, updates user if valid id, returns updated user
            delete - accepts user id, deletes user if valid id, returns nothing
    """

    def get(self, id: int):
        abort_if_invalid_user(id)
        user = User.query.filter_by(id=id).first()
        return user.serialize()

    def put(self, id: int):

        args = parser.parse_args()
        username = args['username']
        email = args['email']
        abort_if_invalid_user(id)
        user = User.query.filter_by(id=id).first()
        user.email = email
        user.username = username
        db.session.commit()
        return user.serialize()

    def delete(self, id: int):
        abort_if_invalid_user(id)
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return "", 204


api.add_resource(UsersList, "/users/")
api.add_resource(IndividualUser, "/users/<int:id>/")

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True, port=8080)
