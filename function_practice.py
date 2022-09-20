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

triangle = [[1],[1,1]]
def pascal(n):
    if n < 1:
        print('invalid')
    elif n is 1:
        print(triangle[0])
    else:
        row = 2
        while len(triangle) < n:
            n_row = []
            p_row = triangle[row -1]
            length = len(p_row) + 1
            for i in range(length):
                if i is 0:
                    n_row.append(1)
                elif i > 0 and i < length - 1:
                    n_row.append(triangle[row-1][i-1] + triangle[row-1][i])
                else:
                    n_row.append(1)
            triangle.append(n_row)
            row += 1

    for row in triangle:
        print(row)

pascal(2)
print()
pascal(7)