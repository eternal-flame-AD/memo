def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

class MyClass():
    pass

@singleton
class MySingletonClass(MyClass):
    pass

class MyNonSingletonClass(MyClass):
    pass