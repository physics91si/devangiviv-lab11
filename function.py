from functools import reduce
def squares(): return [n**2 for n in range(10)]
def squares2(): return list(map(lambda n: n ** 2, range(10)))
def sum_1_to_5(): return reduce(lambda x, y : x * y, range(1,6))
def no_py_extension(s): return [file[:len(file)-3] for file in s.split()]
def dictionary(sentence): return set(sentence.split())
