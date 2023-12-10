from flask import render_template
from . import plants_blueprint


# @plants_blueprint.route('/')
# def HOME():
    
#     # logic to fetch and display plant information
    
#     return "<P>hEKKO</P>"
@plants_blueprint.route('/plants')
def view_plants():
    
    # logic to fetch and display plant information
    plants = [
        {
            'id': 0,
            'name': 'plant a',
            'info': 'text 1'
        },
        {
            'id': 1,
            'name': 'plant b',
            'info': 'text 2'
        },
        {
            'id': 2,
            'name': 'plant c',
            'info': 'text 3'
        }
    ]
    return render_template('plants/view_plants.html', plants=plants)

@plants_blueprint.route('/plants/<int:plant_id>')
def view_plant(plant_id):

    # Your logic to fetch and display details of a specific plant
    if plant_id == 0:
        plant = ['info 1', 'text a']
    elif plant_id == 1:
        plant = ['info 2', 'text b']
    elif plant_id == 2:
        plant = ['info 3', 'text c']
    return render_template('plants/view_plant.html', plant=plant)
