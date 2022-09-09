class NoDucks(type):
    def __init__(cls, name, parents, props):
        if 'duck' in props:
            raise Exception("No Ducks Allowed")


try:
    class Demo(metaclass=NoDucks):
        def duck():
            print('hahha')
except:
    print('No Ducks Allowed')


class Demo(metaclass=NoDucks):
    def no_duck():
        print('hahha')
