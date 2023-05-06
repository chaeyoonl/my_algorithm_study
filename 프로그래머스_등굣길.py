def solution(m, n, puddles):
    dpTable = [[0] * (m+1) for _ in range(n+1)]
    dpTable[1][1] = 1
    for i, j in puddles:
        dpTable[j][i] = -1
        
    print(dpTable)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if dpTable[i][j] == -1:
                dpTable[i][j] = 0
                continue
            dpTable[i][j] += (dpTable[i-1][j] + dpTable[i][j-1])
            
    print(dpTable)

    return dpTable[n][m] % 1000000007
