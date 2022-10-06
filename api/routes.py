from flask import Blueprint, Response
import json

from api.handlers import Handlers

api_bp = Blueprint('api', __name__)


@api_bp.route('/example_service/specific_call', methods=['GET'])
def specific_call() -> Response:
    handlers = Handlers()
    status = 404
    response_data = handlers.get_answer_one()
    if response_data:
        status = 200
    return Response(
        json.dumps(response_data),
        status=status,
        mimetype='application/json'
    )


@api_bp.route('/example_service/specific_call_2', methods=['GET'])
def specific_call_2() -> Response:
    handlers = Handlers()
    status = 404
    response_data = handlers.get_answer_two()
    if response_data:
        status = 200
    return Response(
        json.dumps(response_data),
        status=status,
        mimetype='application/json'
    )
