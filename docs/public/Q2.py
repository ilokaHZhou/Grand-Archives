def clockwiseTurnMatrix(nested_array):
    if nested_array and nested_array [0]:
        m = len(nested_array)
        n = len(nested_array[0])

        result = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = nested_array[i][j]
        
        print(result)


a = [[1, 2, 3], [4, 5, 6]]
clockwiseTurnMatrix(a)

b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
clockwiseTurnMatrix(b)

c = []
clockwiseTurnMatrix(c)

d = [[1, 0]]
clockwiseTurnMatrix(d)


e = [[1], [2]]
clockwiseTurnMatrix(e)