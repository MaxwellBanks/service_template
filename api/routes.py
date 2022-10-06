from flask import Blueprint, Response
import json

from api.handlers import Handlers

api_bp = Blueprint('api', __name__)


@api_bp.route('/pets/cats', methods=['GET'])
def handle_cats() -> Response:
    handlers = Handlers()
    status = 404
    response_data = handlers.get_cat_name()
    if response_data:
        status = 200
    return Response(
        json.dumps(response_data),
        status=status,
        mimetype='application/json'
    )


@api_bp.route('/pets/dogs', methods=['GET'])
def handle_dogs() -> Response:
    handlers = Handlers()
    status = 404
    response_data = handlers.get_dog_name()
    if response_data:
        status = 200
    return Response(
        json.dumps(response_data),
        status=status,
        mimetype='application/json'
    )
