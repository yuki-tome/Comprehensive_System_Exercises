def func(t):
    result = 0
    for i in t:
        result = result + int(i)
    return result

filename = '/home/pi/ex2/id.txt'
f = open(filename, 'r')
result = func(f.readlines()) 
f.close()

filename = '/home/pi/ex2/result.txt'
f = open(filename, 'w')
f.write(str(result))
f.close()
