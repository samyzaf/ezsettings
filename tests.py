from ezsettings import Settings

def test1():
    opt = Settings(aa=11, bb=22, cc='cotton')
    opt.set('foo', 999)
    opt.update(bb=22.35, bar='33.45', poo=4.56, zoo=5.67)
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
    def print_opt(**opt):
        for key in sorted(opt):
            print("%s = %s" % (key,opt[key]))

    opt = Settings(aa=11, bb=22, cc='cotton')
    print_opt(**opt)

if __name__ == '__main__':
    test1()
