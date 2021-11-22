class B:
    def b(self)-> None:
        print('b')


class C:
    def c(self)-> None:
        print('c')


class D(B, C):
    def d(self)-> None:
        print(f'{self.b()}{self.c()}')


d = D()
d.d()