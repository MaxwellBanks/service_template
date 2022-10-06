from flask import Response
import json

from api.routes import handle_cats, handle_dogs


def test_handle_cats_200(mocker):
    expected = Response(
        json.dumps({"misty": "maine coon"}),
        status=200,
        mimetype='application/json'
    ).get_json()
    actual = handle_cats().get_json()
    assert expected == actual


def test_handle_cats_404(mocker):
    expected = Response(
        json.dumps(''),
        status=404,
        mimetype='application/json'
    ).get_json()
    actual = handle_cats().get_json()
    assert expected == actual


def test_handle_dogs_200(mocker):
    expected = Response(
        json.dumps({"sherlock": "boston terrier"}),
        status=200,
        mimetype='application/json'
    ).get_json()
    actual = handle_dogs().get_json()
    assert expected == actual


def test_handle_dogs_404(mocker):
    expected = Response(
        json.dumps(''),
        status=404,
        mimetype='application/json'
    ).get_json()
    actual = handle_dogs().get_json()
    assert expected == actual
