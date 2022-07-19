from flask import Blueprint, request, jsonify
from tank_inventory.helpers import token_required
from tank_inventory.models import db, User, Tank, tank_schema, tanks_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return{'some':'value'}

#CREATE HERO ENDPOINT
@api.route('/tanks', methods = ['POST'])
@token_required
def create_tank(current_user_token):
    name = request.json['name']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    date_created = request.json['date_created']
    owner = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")

    tank = Tank(name, description, comics_appeared_in, super_power, date_created, user_token = owner)

    db.session.add(tank)
    db.session.commit()

    response = tank_schema.dump(tank)

    return jsonify(response)

# Retrieve all Tank Endpoints
@api.route('/tanks', methods = ['GET'])
@token_required
def get_tanks(current_user_token):
    owner = current_user_token.token
    tanks = Tank.query.filter_by(user_token = owner).all()
    response = tanks_schema.dump(tanks)
    return jsonify(response)


# Retrieve ONE Tank Endpoint
@api.route('/tanks/<id>', methods = ['GET'])
@token_required
def get_tank(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        tank = Tank.query.get(id)
        response = tank_schema.dump(tank)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401

#udpate tank
@api.route('/tanks/<id>', methods = ['POST', 'PUT'])
@token_required
def update_tank(current_user_token, id):
    tank = Tank.query.get(id)

    tank.name = request.json['name']
    tank.description = request.json['description']
    tank.comics_appeared_in = request.json['comics_appeared_in']
    tank.super_power = request.json['super_power']
    tank.date_created = request.json['date_created']
    tank.owner = current_user_token.token

    db.session.commit()
    response = tank_schema.dump(tank)
    return jsonify(response)


#delete tank
@api.route('/tanks/<id>', methods=['DELETE'])
@token_required
def delete_tank(current_user_token, id):
    tank = Tank.query.get(id)
    db.session.delete(tank)
    db.session.commit()
    response = tank_schema.dump(tank)
    return jsonify(response)