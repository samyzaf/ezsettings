from ezsettings import Settings

def test1():
    # Initializing Settings object opt with 5 parameters:
    #    a - integer
    #    b - integer
    #    c - string
    #    d - list
    #    e - set
    opt = Settings(a=1, b=2, c='casandra', d=list([1,2,3]), e=set(['king', 2.3, 'queen']))

    # Adding a function object to opt
    opt.f = lambda x: x**2 - 7*x + 12

    # Adding 3 more integer parameters
    opt.update(x=10, y=20, z=30)

    # Adding a nested Settings object to opt:
    opt.foo = Settings(a=0.1, b=0.2, c=0.3)

    # You can access these paramaters by:
    print(f"opt.foo.a = {opt.foo.a}")
    print(f"opt.foo.b = {opt.foo.b}")
    print(f"opt.foo.c = {opt.foo.c}")

    # Updating opt.foo with new parameters
    opt.foo.date = 'May 01, 2017'
    opt.foo.email = 'opt@settings.com'

    print(f"opt.foo.date = {opt.foo.date}")
    print(f"opt.foo.email = {opt.foo.email}")
    print(f"opt.foo =\n{opt.foo}")

    # Adding nested Settings objects to opt (recursive settings)
    opt.bar = Settings(weight=80, height=1.75, age=45)
    opt.bar.edu = Settings(elem='oakelm', high='oakhigh', college='oakcoll')

    print(opt)
    return opt

# Result of test1() should be:
#    a = 1
#    b = 2
#    bar = Settings(age=45, edu=Settings(college='oakcoll', elem='oakelm', high='oakhigh'), height=1.75, weight=80)
#    c = 'casandra'
#    d = [1, 2, 3]
#    e = {2.3, 'queen', 'king'}
#    f = <function test1.<locals>.<lambda> at 0x00000277CBFF6598>
#    foo = Settings(a=0.1, b=0.2, c=0.3, date='May 01, 2017', email='opt@settings.com')
#    x = 10
#    y = 20
#    z = 30

def test2():
    # d is a standard Python dictionary
    d = dict(weight=50, age=20, name='casandra')

    # It can be used to initialize a Settings object
    opt = Settings(d)

    # Later we can add new items to opt
    opt.address = "13 Oak street, Flintstone 520092, Nebraska, USA"

    # Settings object supports set/get methods
    for key in ['x', 'y', 'z']:
        opt.set(key, 0.0)
    for key in ['weight', 'age', 'name']:
        print(f"opt.{key} = {opt.get(key)}")
    
    # Settings object supports bracket subscripting: opt[key]
    for key in sorted(opt):
        print(f"Value of {key} is: {opt[key]}")

    print(opt)
    return opt

def test3():
    opt = Settings(a=1, b=2, c='casandra', d=list([1,2,3]), e=set(['king', 2.3, 'queen']))
    opt.foo = Settings(a=0.1, b=0.2, c=0.3)

    try:
        opt.__dict__= "This should not work! You may not use basic attributes as keys!"
    except Exception as e:
        print(f"Exception occured when trying to use '__dict__' as a key: {e}")

    try:
        opt.set = "This should not work! You may not use basic attributes as keys!"
    except Exception as e:
        print(f"Exception occured when trying to use 'set' as a key: {e}")

    try:
        opt.set("update", "This should not work! You may not use basic attributes as keys! 2")
    except Exception as e:
        print(f"Exception occured when trying to use 'update' as a key: {e}")

    print("Lets print opt and see if anything changed?")
    print(opt)
    return opt

if __name__ == '__main__':
    #test1()
    #test2()
    test3()
