from fast_depends import Depends, inject

from emp_agents.implicits import ImplicitManager
from emp_agents.utils import get_function_schema


class MyObject:
    def __init__(self, value: int):
        self.value = value


def old_load_object() -> MyObject:
    return MyObject(value=1)


def new_load_object() -> MyObject:
    return MyObject(value=100)


@inject
def do_thing_with_object(
    obj: MyObject = Depends(ImplicitManager.lazy_implicit("load_object")),
):
    assert isinstance(obj, MyObject)
    return obj


def test_implicit_manager():
    ImplicitManager.add_implicit("load_object", old_load_object)
    obj = do_thing_with_object()
    assert obj.value == 1

    schema = get_function_schema(do_thing_with_object)
    assert schema == {
        "name": "do_thing_with_object",
        "description": None,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    }

    ImplicitManager.add_implicit("load_object", new_load_object)
    obj = do_thing_with_object()
    assert obj.value == 100
