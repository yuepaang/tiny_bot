import pytest
from tiny_bot import *


def test_basic_action():
    def func(bot, tracker, msg):
        return Response("world")

    class MyAction(Action):
        def run(self, bot, tracker, msg):
            return Response("hello")

    class MyActionHub(ActionHub):
        f = func
        g = MyAction()
        h = "hello world!,{{name}}"

    hub = MyActionHub()
    assert isinstance(hub['f'], Action)
    assert isinstance(hub['g'], Action)
    assert isinstance(hub['h'], Action)

    class FakeBot(object):
        def __init__(self):
            self._before_action = []
            self._after_action = []

    bot = FakeBot()

    class FakeTracker(dict):
        def _as_dict(self):
            return self

    assert hub['f'](bot, FakeTracker(), {}).body == "world"
    assert hub['g'](bot, FakeTracker(), {}).body == "hello"
    assert hub['h'](bot, FakeTracker(name="ioriiod0"), {}
                    ).body == "hello world!,ioriiod0"
