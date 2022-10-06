from api.handlers import Handlers


def test_get_cat_name():
    handlers = Handlers()
    expected = {"misty": "maine coon"}
    actual = handlers.get_cat_name()
    assert expected == actual


def test_get_dog_name():
    handlers = Handlers()
    expected = {"sherlock": "boston terrier"}
    actual = handlers.get_dog_name()
    assert expected == actual
