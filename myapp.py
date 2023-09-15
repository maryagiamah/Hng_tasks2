from flask import Flask, jsonify, request
from models import db, Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()

    return jsonify({'id': new_person.id, 'name': new_person.name}), 201

@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if person is not None:
        return jsonify({'id': person.id, 'name': person.name})
    else:
        return jsonify({'message': 'Person not found'}), 404

@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = Person.query.get(person_id)
    if person is not None:
        data = request.get_json()
        new_name = data.get('name')
        person.name = new_name
        db.session.commit()
        return jsonify({'message': 'Person updated'}), 200
    else:
        return jsonify({'message': 'Person not found'}), 404

@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted'}), 200
    else:
        return jsonify({'message': 'Person not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
