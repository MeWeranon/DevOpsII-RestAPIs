from flask import Flask, request, jsonify, json

app = Flask(__name__)

Apple = [
    {"name": "Iphone", "category": 1, "price": 999, "instock": 10},
    {"name": "Ipad", "category": 2, "price": 9999, "instock": 20},
    {"name": "Macbook", "category": 3, "price": 99999, "instock": 50},

]
def _find_next_name(name):
    data = [x for x in Apple if x['name'] == name]
    return data

print(_find_next_name("Iphone"))

@app.route('/Apple/<name>', methods=["DELETE"])
def delete_Apple(name: str):

    data = _find_next_name(name)
    if not data:
        return {"error": "Apple not found"}, 404
    else:
        Apple.remove(data[0])
        return "Apple deleted successfully", 200

#REST API
@app.route('/Apple', methods=["GET"])
def get_Apple():
    return jsonify(Apple)

# GET -by name
@app.route('/Apple/<name>', methods=["GET"])
def get_Apple_name(name):
    data = _find_next_name(name)
    return jsonify(data)

@app.route('/Apple', methods=["POST"])
def post_Apple():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock":instock,
        
    }

    if (_find_next_name(name) == name):
        return {"error": "Bad Request"}, name
    else:
        Apple.append(new_data)
        return jsonify(Apple)

@app.route('/put_Apple/<name>', methods=["PUT"])
def update_Apple(name):
    
    global Apple
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')



    for Apple in Apple:
        if  name == Apple["name"]:
            Apple["category"] = int(category)
            Apple["price"] = int(price)
            Apple["instock"] = int(instock)
            return jsonify(Apple)

    else:
        return "Error", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
