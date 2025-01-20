from pprint import pprint

class SampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def greet(self):
        return f"Привет! Я - {self.name}, а моё значение {self.value}."

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    module = obj.__class__.__module__


    properties = {}
    if hasattr(obj, '__dict__'):
        properties['__dict__'] = obj.__dict__
    if hasattr(obj, '__doc__'):
        properties['__doc__'] = obj.__doc__

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'properties': properties
    }

sample_object = SampleClass("Пример", 33)
info = introspection_info(sample_object)
pprint(info)
print(sample_object.greet())