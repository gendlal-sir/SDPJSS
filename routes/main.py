from flask import Blueprint, render_template, request, jsonify
from db import collection

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.json.get('name')
        if not name:
            raise ValueError("Name is required")
        collection.insert_one({'name': name})
        return jsonify({'status': 'success', 'message': f'Hello, {name}!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@main.route('/dashboard')
def dashboard():
    users = list(collection.find({}, {'_id': 0}))
    return render_template('dashboard.html', users=users)
@main.route('/check-name')
def check_name():
    name = request.args.get('name', '').strip()
    exists = collection.find_one({'name': name}) is not None
    return jsonify({'exists': exists})
