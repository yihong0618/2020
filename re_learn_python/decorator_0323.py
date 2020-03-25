### 2020.3.23
### 精进装饰器

#### 类装饰器

class D:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        self.func()


class LZ:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val


@D
def a():
    print("in function")


class B:
    a = 3
    
    @LZ
    def t(self):
        print("in")
        return "haha"



if __name__ == "__main__":
    a()
    b = B()
    print(b.t)
    print(b.t)
