def twice(f):
    return lambda x:f(f(f(x)))
def thrice(f):
    return lambda x:f(f(x))

print((twice)(thrice)(lambda x:x+3)(2))


def once(f):
    return lambda x: f(f(f(x)))
def something(f):
    return lambda x: f(f(x))

print((once)(something)(lambda x:x+3)(2))