from flask import Blueprint, Response
import json
from werkzeug.exceptions import NotFound, InternalServerError

errors_bp = Blueprint('errors', __name__)


@errors_bp.app_errorhandler(404)
def not_found_error(error: NotFound) -> Response:
    return Response(
        json.dumps(
            "404: Requested resource not found. "
            "Make sure you re correctly spelling your path "
            "and that you are requesting valid query parameters."
            ),
        404,
        mimetype='application/json'
    )


@errors_bp.app_errorhandler(500)
def internal_error(error: InternalServerError) -> Response:
    return Response(
        json.dumps("500: Internal server error."),
        500,
        mimetype='application/json'
    )
