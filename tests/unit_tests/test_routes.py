from flask import Response
import json

from api.routes import specific_call, specific_call_2


def test_mock_specific_call_200(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_answer_one',
        return_value={"key_one": "value_one"}
    )
    expected = Response(
        json.dumps({"key_one": "value_one"}),
        status=200,
        mimetype='application/json'
    )
    actual = specific_call()
    assert expected == actual


def test_mock_specific_call_404(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_answer_one',
        return_value=''
    )
    expected = Response(
        json.dumps(''),
        status=404,
        mimetype='application/json'
    )
    actual = specific_call()
    assert expected == actual


def test_mock_specific_call_2_200(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_answer_two',
        return_value={"key_two": "value_two"}
    )
    expected = Response(
        json.dumps({"key_two": "value_two"}),
        status=200,
        mimetype='application/json'
    )
    actual = specific_call_2()
    assert expected == actual


def test_mock_specific_call_2_404(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_answer_two',
        return_value=''
    )
    expected_content = ''
    expected_status_code = 404
    actual = specific_call_2()
    assert actual.status_code == expected_status_code
    assert actual.get_data() == expected_content
