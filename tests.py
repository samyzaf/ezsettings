from ezsettings import Settings

def test1():
    opt = Settings(aa=11, bb=22, cc='casandra')
    opt.set('foo', 999)
    opt.update(bb=22.22, bar='33.33', poo=4.44, zoo=5.55)
    print("opt.aa =", opt.aa)
    print("opt.cc =", opt.cc)
    print(dir(opt))
    opt.pop('aa')
    for key in sorted(opt):
        print("Value of %s is: %s" % (key, opt.get(key)))

def test2():
    d = dict(aa=11, bb=22, cc='casandra')
    opt = Settings(d)
    opt.foo = 999
    opt.bar = 'baracuda'
    print(opt)
    for key in sorted(opt):
        print("Value of %s is: %s" % (key, opt[key]))

def test3():
    d = dict(aa=11, bb=22, cc='casandra')
    opt = Settings(d, dd='dothan', ee=55)
    for key in sorted(opt):
        print("%s = %s" % (key, opt.get(key)))

def test4():
    d = dict(aa=11, bb=22, cc='casandra')
    opt = Settings(d, dd='dothan', ee=55)
    print(opt)

if __name__ == '__main__':
    test1()

