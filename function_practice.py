def max_num(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
def mult_list(li):
    prod = 1
    if len(li) > 1:
        for x in li:
            prod = prod * x
    else:
        return 
    
    return prod

def rev_string(str):
    return str[::-1]

def num_within(n, br, er):
    return n > br and n <= er

def pascal(n):
    triangle = [[1],[[1],[1]]]
    if(n < 1):
        print('invalid')
    elif(n == 1):
        print([1])