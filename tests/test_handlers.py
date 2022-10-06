from api.handlers import Handlers


def test_get_answer_one():
    handlers = Handlers()
    expected = {"key_one": "value_one"}
    actual = handlers.get_answer_one()
    assert expected == actual


def test_get_answer_two():
    handlers = Handlers()
    expected = {"key_two": "value_two"}
    actual = handlers.get_answer_two()
    assert expected == actual
