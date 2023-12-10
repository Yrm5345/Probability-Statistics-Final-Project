
from flask import request, jsonify
from flask_login import login_required, logout_user, current_user, login_user
from . import auth_blueprint
from .user import User


@auth_blueprint.route('/profile', methods=['GET'])
@login_required
def view_profile():
    user_data = {
        "username": current_user.username,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email
    }
    return jsonify(user_data)

@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        logout_user()
        response_data = {"message": "Logout successful"}
        return jsonify(response_data), 200
    except Exception as e:
        response_data = {"error": str(e)}
        return jsonify(response_data), 500

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            user_data = {
                "username": user.username,
                "name": user.name,
                "email": user.email
            }
            return jsonify(user_data), 200
        else:
            response_data = {"error": "Invalid credentials"}
            return jsonify(response_data), 401

    except Exception as e:
        response_data = {"error": str(e)}
        return jsonify(response_data), 500

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        # username = data.get("username")
        # password = data.get("password")
        # first_name = data.get("first_name")
        # last_name = data.get("last_name")
        # email = data.get("email")

        username = "Yusuu"
        password = "hjsjss"
        first_name = "sddds"
        last_name = "dddd"
        email = data.get("email")

        new_user = User(username=username, password=password, first_name=first_name, last_name=last_name ,  email=email)
        db.session.add(new_user)
        db.session.commit()

        user_data = {
            "username": new_user.username,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email
        }
        return jsonify(user_data), 201

    except Exception as e:
        response_data = {"error": str(e)}
        return jsonify(response_data), 500
