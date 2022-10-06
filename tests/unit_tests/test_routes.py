from api.routes import specific_call, specific_call_2


def test_mock_specific_call(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_answer_one',
        return_value={"key_one": "value_one"}
    )
    expected = {"key_one": "value_one"}
    actual = specific_call()
    assert expected == actual


def test_mock_specific_call_2(mocker):
    mocker.patch(
        'api.handlers.Handlers.get_answer_two',
        return_value={"key_two": "value_two"}
    )
    expected = {"key_two": "value_two"}
    actual = specific_call_2()
    assert expected == actual
