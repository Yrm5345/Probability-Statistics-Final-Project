
from flask import request, jsonify
from flask_login import login_required, logout_user, current_user, login_user
from . import auth_blueprint
from .user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


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

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            user_data = {
                "username": user.username,
                "first_name": user.first_name,  
                "last_name": user.last_name,    
                "email": user.email
            }
            return jsonify(user_data), 200
        else:
            print("User not found")
            response_data = {"error": "Invalid credentials"}
            return jsonify(response_data), 401

    except Exception as e:
        response_data = {"error": str(e)}
        return jsonify(response_data), 500


@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        print("Received data:", data)

        username = data.get("username")
        password = data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")

        # Validate input
        if not (username and password and email):
            raise ValueError("Username, password, and email are required.")


        # Check for existing user with the same username or email
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            raise ValueError("Username or email is already in use.")


        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            username=username,
            password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        from .. import db
        db.session.add(new_user)
        db.session.commit()

        print("User added to the database")

        user_data = {
            "username": new_user.username,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email
        }
        return jsonify(user_data), 201

    except Exception as e:
        print("Error:", e)
        response_data = {"error": str(e)}
        return jsonify(response_data), 500
