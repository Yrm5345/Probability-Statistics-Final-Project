from flask import render_template
from . import plants_blueprint


# @plants_blueprint.route('/')
# def HOME():
    
#     # logic to fetch and display plant information
    
#     return "<P>hEKKO</P>"
@plants_blueprint.route('/plants')
def view_plants():
    
    # logic to fetch and display plant information
    
    return render_template('plants/view_plants.html', plants=plants)

@plants_blueprint.route('/plants/<int:plant_id>')
def view_plant(plant_id):

    # Your logic to fetch and display details of a specific plant
    
    return render_template('plants/view_plant.html', plant=plant)
