from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Resource is the Class to be instantiated as object

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item                     # flask_restful does the JSONify for us
        return {'item': None}, 404              # not found

    # def get(self):
    #     return items

    def post(self, name):
        data = request.get_json()           # if request has JSON payload, if not or wrong content-type error
        # request.get_json(force=True, silent=True)     # not good
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201                        # 201 Created


class ItemList(Resource):
    def get(self):
        return {'items': items}


# this is equivalent to app.route() decorator
api.add_resource(Item, '/item/<string:name>')     # http://localhost:5000/item/noodles
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)              # debug=True gives a nice HTML page on error
