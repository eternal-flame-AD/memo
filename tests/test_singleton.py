import os,sys  
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir)

from singleton import MyClass, MySingletonClass, MyNonSingletonClass


def test_singleton():
    a = MyClass()
    b = MyClass()
    assert a != b
    a = MySingletonClass()
    b = MySingletonClass()
    assert a == b
    a = MyNonSingletonClass()
    b = MyNonSingletonClass()
    assert a != b