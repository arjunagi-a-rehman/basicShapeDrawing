from src import app,mongo
from flask import request,render_template,jsonify
from bson import ObjectId

@app.route('/shapes', methods=['GET'])
def get_shapes():
    shapes = list(mongo.db.shapes.find())
    json_shaps=[]
    for shape in shapes:
        json_shaps.append({
            "id":str(shape['_id']),
            "type":shape['type'],
            "properties":shape['properties']
        })
    return jsonify({'shapes': json_shaps})

@app.route('/shapes', methods=['POST'])
def create_shape():
    data = request.json
    tempShape=mongo.db.shapes.insert_one(data)
    inserted_id = tempShape.inserted_id  # Get the inserted document's _id
    # Construct the shape dictionary with the inserted _id
    shape = {
        "id": str(inserted_id),
        "type": data['type'],
        "properties": data['properties']
    }
    return jsonify(shape), 201

@app.route('/shapes/<id>', methods=['PUT'])
def update_shape(id):
    data = request.json
    object_id = ObjectId(id)
    mongo.db.shapes.update_one({'_id': object_id}, {'$set': data})
    return jsonify({'message': 'Shape updated successfully'})

@app.route('/shapes/<id>', methods=['DELETE'])
def delete_shape(id):
    object_id = ObjectId(id)
    mongo.db.shapes.delete_one({'_id': object_id})
    return jsonify({'message': 'Shape deleted successfully'})

@app.route('/')
def renderHome():
    return render_template('index.html')


