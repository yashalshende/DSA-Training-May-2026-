# def func(value, values):
#     var =1
#     values[0] =44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])

def f(i, values = []):
    values.append(i)
    return values
print(f(1))
print(f(2))
print(f(3))     