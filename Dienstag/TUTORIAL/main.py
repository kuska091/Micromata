from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy #ORM
import os
import secrets





app = Flask(__name__)



API_KEY = os.environ.get("API_KEY")

@app.before_request
def check_api_key():
    key = request.headers.get("X-API-Key")
    if not key:
        return jsonify({"error": "API key fehlt"}), 401
    if not API_KEY or not secrets.compare_digest(key, API_KEY):
        return jsonify({"error": "API key ungültig"}), 403                              #export API_KEY="your_api_key"  # Setze deinen API-Schlüssel
                                                                                        #python -c "import secrets; print(secrets.token_urlsafe(32))"
                                                                                        


#Create Database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating
        }


with app.app_context():
    db.create_all()

#Create Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Travel Destinations API!"})


@app.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([destination.to_dict() for destination in destinations])

@app.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error": "Destination not found"}), 404


@app.route('/destinations', methods=['POST'])
def add_destination():
    data = request.get_json()
    new_destination = Destination(
        destination=data['destination'],
        country=data['country'],
        rating=data['rating']
    )
    db.session.add(new_destination)
    db.session.commit()
    return jsonify(new_destination.to_dict()), 201


#PUT -> Update a destination
@app.route('/destinations/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    data = request.get_json()
    destination = Destination.query.get(destination_id)
    if destination:
        destination.destination = data.get('destination', destination.destination)
        destination.country = data.get('country', destination.country)
        destination.rating = data.get('rating', destination.rating)
        db.session.commit()
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error": "Destination not found"}), 404




#DELETE -> Delete a destination
@app.route('/destinations/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id): 
    destination = Destination.query.get(destination_id)
    if destination:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({"message": "Destination deleted successfully"})
    else:
        return jsonify({"error": "Destination not found"}), 404 

 




if __name__ == '__main__':
    app.run(debug=True)