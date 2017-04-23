DEFAULT_VALUE = object()

class Settings(dict):
    def __init__(self, d=None, **opt):
        if not d is None:
            self.update(d)
        for key in opt:
            self[key] = opt[key]

    def set(self, key, value):
        self[key] = value
        return value

    def get(self, key, default_value=DEFAULT_VALUE):
        if key in self:
            return self[key]
        elif default_value is DEFAULT_VALUE:
            raise Exception("Key Error: %s" % (key,))
        else:
            self.set(key, default_value)
            return default_value

    def remove(self, key):
        if key in self:
            return self.pop(key)
        else:
            return None

#------------------------------------------------------------

def test1():
    opt = Settings(aa=11, bb=22, cc='cotton')
    opt.set('foo', 999)
    opt.update(bb=22.22, bar='33.33', poo=4.44, zoo=5.55)
    opt.remove('aa')
    for key in sorted(opt):
        print("%s = %s" % (key,opt[key]))

def test2():
    d = dict(aa=11, bb=22, cc='cotton')
    opt = Settings(d)
    opt.set('foo', 999)
    for key in sorted(opt):
        print("%s = %s" % (key,opt[key]))

def test3():
    d = dict(aa=11, bb=22, cc='cotton')
    opt = Settings(d, dd='dothan', ee=55)
    for key in sorted(opt):
        print("%s = %s" % (key,opt[key]))

def test4():
    def print_opt(**opt):
        for key in sorted(opt):
            print("%s = %s" % (key,opt[key]))

    opt = Settings(aa=11, bb=22, cc='cotton')
    print_opt(**opt)

if __name__ == '__main__':
    test3()

