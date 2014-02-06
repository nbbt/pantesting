from pantesting.db.orm import Dictable

__author__ = 'Anya'


class SimpleClass(Dictable):
    def __init__(self, id, name):
        Dictable.__init__(self)
        self.id = id
        self.name = name
        self._bar = "bar"

    def _foo(self):
        pass


class NestedClass(Dictable):
    def __init__(self, id, status, simple_class):
        Dictable.__init__(self)
        self.id = id
        self.status = status
        self.simple_class = simple_class

    def _bar(self):
        pass

def test_simple_class():
    """
    Check that simple class (all members are basic python types) is properly converted to dictionary.
    """
    class_details = {"id": 1, "name": "foo"}
    simple_class = SimpleClass(**class_details)

    assert simple_class.to_dict() == class_details


def test_nested_class():
    """
    Check that nested class (some members are not basic python objects) is properly converted to dictionary.
    """
    simple_class_details = {"id": 1, "name": "foo"}
    simple_class = SimpleClass(**simple_class_details)

    nested_class_details = {"id": 2, "status": "active", "simple_class": simple_class}
    nested_class = NestedClass(**nested_class_details)

    expected_dict = nested_class_details
    expected_dict["simple_class"] = simple_class_details
    assert nested_class.to_dict() == expected_dict
