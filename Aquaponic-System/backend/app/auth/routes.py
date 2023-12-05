from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from . import auth_blueprint


@auth_blueprint.route('/profile')
@login_required
def view_profile():
    #  logic to fetch and display the user's profile
    return render_template('auth/profile.html', user=current_user)

@auth_blueprint.route('/logout')
@login_required
def logout():
    try: 
        #  logic to log the user out
        logout_user()
        flash("Logout successful")
        return redirect(url_for('main.index'))
    except Exception as e:
        flash(f'Error: {str(e)}')
        return redirect(url_for('main.index'))
    