import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src import app, mongo

class TestShapesController(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        mongo.db.shapes.delete_many({})

    def test_get_shapes(self):
        # Insert multiple test shape data into the MongoDB collection
        test_shapes_data = [
            {"type": "circle", "properties": {"radius": 10}},
            {"type": "rectangle", "properties": {"width": 20, "height": 30}}
        ]
        for shape_data in test_shapes_data:
            mongo.db.shapes.insert_one(shape_data)

        response = self.app.get('/shapes')

        self.assertEqual(response.status_code, 200)

        # Verify that each shape type is present in the response data
        for shape_data in test_shapes_data:
            self.assertIn(shape_data["type"].encode(), response.data)

    def test_create_shape(self):
        new_shape_data = {"type": "rectangle", "properties": {"width": 20, "height": 30}}
        response = self.app.post('/shapes', json=new_shape_data)
        prevCount=mongo.db.shapes.count_documents({})
        self.assertEqual(response.status_code, 201)

        self.assertEqual(mongo.db.shapes.count_documents({}), 1)

    def test_update_shape(self):
        test_shape_data = {"type": "circle", "properties": {"radius": 15}}
        result = mongo.db.shapes.insert_one(test_shape_data)
        shape_id = str(result.inserted_id)

        updated_shape_data = {"type": "rectangle", "properties": {"width": 25, "height": 35}}
        response = self.app.put(f'/shapes/{shape_id}', json=updated_shape_data)

        self.assertEqual(response.status_code, 200)

        updated_shape = mongo.db.shapes.find_one({"_id": result.inserted_id})
        self.assertEqual(updated_shape['type'], 'rectangle')
        self.assertEqual(updated_shape['properties']['width'], 25)
        self.assertEqual(updated_shape['properties']['height'], 35)

    def test_delete_shape(self):
        test_shape_data = {"type": "circle", "properties": {"radius": 20}}
        result = mongo.db.shapes.insert_one(test_shape_data)
        shape_id = str(result.inserted_id)

        print("Count of documents before deletion:", mongo.db.shapes.count_documents({}))

        response = self.app.delete(f'/shapes/{shape_id}')

        self.assertEqual(response.status_code, 200)

        # Verify that the response data contains the expected message
        self.assertIn(b'Shape deleted successfully', response.data)

        # Log the count of documents after deletion
        print("Count of documents after deletion:", mongo.db.shapes.count_documents({}))

        # Verify that the count of documents in the MongoDB collection is 0
        self.assertEqual(mongo.db.shapes.count_documents({}), 0)


if __name__ == '__main__':
    unittest.main()
