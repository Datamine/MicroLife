class Foo(object):
    def __init__(self, x, parent):
        self.x = x
        self.parent = parent

    def foomethod(self):
        print "call"

    def barmethod(self):
        print self.y

class Bar(object):
    def __init__(self, y):
        self.y = y

    def barf(self):
        self.f = Foo(5, self)

    def zelf(self):
        self.f.foomethod()


