from flask import render_template
from . import equaponic_blueprint

@equaponic_blueprint.route('/dashboard')
def dashboard():

    # logic for getting the data from the aurdino api and display in in the dashboard
    
    return render_template('equaponic/dashboard.html', data=data)

@equaponic_blueprint.route('/statistics')
def statistics():

    # logic to generate statistics

    return render_template('equaponic/statistics.html')
