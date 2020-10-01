def matrix_multiply(a, b):
    c = [[] for _ in range(len(a))]
    for i in range(len(a)):        
        for j in range(len(a)):
            sum = 0
            for k in range(len(a)):
                sum += a[i][k] * b[k][j]
            c[i].append(sum)
    return c