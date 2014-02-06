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

    def _manual_to_dict(self):
        return dict(id=self.id, name=self.name)

class NestedClass(Dictable):
    def __init__(self, id, status, simple_class):
        Dictable.__init__(self)
        self.id = id
        self.status = status
        self.simple_class = simple_class

    def _bar(self):
        pass

    def _manual_to_dict(self):
        simple_class_dict = self.simple_class._manual_to_dict()
        return dict(id=self.id, status=self.status, simple_class=simple_class_dict)


class TwiceNestedClass(Dictable):
    def __init__(self, param1, nested_class):
        Dictable.__init__(self)
        self.param1 = param1
        self.nested_class = nested_class

    def _bar(self):
        pass

    def _manual_to_dict(self):
        nested_class_dict = dict(id=self.nested_class.id, status=self.nested_class.status)
        return dict(param1=self.param1, nested_class=nested_class_dict)


class TwoDirectionConnectionClass1(Dictable):
    def __init__(self, param1, ref_class=None):
        self.param1 = param1
        self.ref_class = ref_class

    def _manual_to_dict(self):
        ref_class_dict = dict(param1=self.ref_class.param1)
        return dict(param1=self.param1, ref_class=ref_class_dict)


class TwoDirectionConnectionClass2(Dictable):
    def __init__(self, param1, ref_class=None):
        self.param1 = param1
        self.ref_class = ref_class


def test_simple_class():
    """
    Check that simple class (all members are basic python types) is properly converted to dictionary.
    """
    simple_class = SimpleClass(id=1, name="foo")
    assert simple_class.to_dict() == simple_class._manual_to_dict()


def test_nested_class():
    """
    Check that nested class (some members are not basic python objects) is properly converted to dictionary.
    """
    simple_class = SimpleClass(id=1, name="foo")
    nested_class = NestedClass(id=2, status="active", simple_class=simple_class)
    assert nested_class.to_dict() == nested_class._manual_to_dict()


def test_twice_nested_class():
    """
    Check that when classes reference one another to_dict only goes through one stage of dependency.
    """
    simple_class = SimpleClass(id=1, name="foo")
    nested_class = NestedClass(id=2, status="active", simple_class=simple_class)
    twice_nested_class = TwiceNestedClass(param1="param1", nested_class=nested_class)
    assert twice_nested_class.to_dict() == twice_nested_class._manual_to_dict()

def test_circle_nested_class():
    class1 = TwoDirectionConnectionClass1("foo")
    class2 = TwoDirectionConnectionClass2("bar", class1)
    class1.ref_class = class2
    assert class1.to_dict() == class1._manual_to_dict()