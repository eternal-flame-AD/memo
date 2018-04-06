from singleton import MyClass,MySingletonClass,MyNonSingletonClass
def test_singleton():
    a=MyClass()
    b=MyClass()
    assert a!=b
    a=MySingletonClass()
    b=MySingletonClass()
    assert a==b
    a=MyNonSingletonClass()
    b=MyNonSingletonClass()
    assert a!=b