import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""
print(SETUP)


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *("{:.3f}".format(x) for x in res))


clock("listcomp        :", "[ord(s) for s in symbols if ord(s) > 127]")
clock("listcomp + func :", "[ord(s) for s in symbols if non_ascii(ord(s))]")
clock("filter + lambda :", "list(filter(lambda c: c > 127, map(ord, symbols)))")
clock("filter + func   :", "list(filter(non_ascii, map(ord, symbols)))")

"""
listcomp        : 0.013 0.012 0.011 0.011 0.011
listcomp + func : 0.020 0.020 0.018 0.018 0.018
filter + lambda : 0.017 0.018 0.016 0.016 0.016
filter + func   : 0.016 0.016 0.016 0.016 0.015
"""
