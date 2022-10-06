from flask import Response
import json

from api.routes import specific_call, specific_call_2


def test_specific_call_200(mocker):
    expected = Response(
        json.dumps({"key_one": "value_one"}),
        status=200,
        mimetype='application/json'
    ).get_json()
    actual = specific_call().get_json()
    assert expected == actual


def test_specific_call_404(mocker):
    expected = Response(
        json.dumps(''),
        status=404,
        mimetype='application/json'
    ).get_json()
    actual = specific_call().get_json()
    assert expected == actual


def test_specific_call_2_200(mocker):
    expected = Response(
        json.dumps({"key_two": "value_two"}),
        status=200,
        mimetype='application/json'
    ).get_json()
    actual = specific_call_2().get_json()
    assert expected == actual


def test_specific_call_2_404(mocker):
    expected = Response(
        json.dumps(''),
        status=404,
        mimetype='application/json'
    ).get_json()
    actual = specific_call_2().get_json()
    assert expected == actual
