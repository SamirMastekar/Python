class SAM:

    def argument(self, *args):
        for arg in args:
            print(arg)

    def kwargs_example(self, **kwargs):
        for name, value in kwargs.items():
            print('{0} = {1}'.format(name, value))

myObject = SAM()

myObject.argument('sam', 1, 4.5, "samir Mastekar")
myObject.kwargs_example(band = 'samir Mastekar', origin = 'India')