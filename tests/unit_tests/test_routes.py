from flask import Response
import json

from api.routes import handle_cats, handle_dogs


def test_mock_handle_cats_200(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_cat_name',
        return_value={"misty": "maine coon"}
    )
    expected = Response(
        json.dumps({"misty": "maine coon"}),
        status=200,
        mimetype='application/json'
    ).get_json()
    actual = handle_cats().get_json()
    assert expected == actual


def test_mock_handle_cats_404(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_cat_name',
        return_value=''
    )
    expected = Response(
        json.dumps(''),
        status=404,
        mimetype='application/json'
    ).get_json()
    actual = handle_cats().get_json()
    assert expected == actual


def test_mock_handle_dogs_200(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_dog_name',
        return_value={"sherlock": "boston terrier"}
    )
    expected = Response(
        json.dumps({"sherlock": "boston terrier"}),
        status=200,
        mimetype='application/json'
    ).get_json()
    actual = handle_dogs().get_json()
    assert expected == actual


def test_mock_handle_dogs_404(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_dog_name',
        return_value=''
    )
    expected = Response(
        json.dumps(''),
        status=404,
        mimetype='application/json'
    ).get_json()
    actual = handle_dogs().get_json()
    assert expected == actual
