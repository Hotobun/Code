# python 
def func():
    W = 21
    w = [0,2,3,4,5,9]
    v = [0,3,4,5,8,10]
    N = len(w)
    B = [[0 for i in range(W)] for i in range(N)]
    
    for k in range(N):
        for C in range(W):
            if w[k] > C:
                B[k][C] = B[k-1][C]
            else:
                value1 = B[k-1][C-w[k]] + v[k]
                value2 = B[k-1][C]
                B[k][C] = max(value1,value2)
    return B[-1][-1]

if __name__ == "__main__":
    result = func()
    print(result)

