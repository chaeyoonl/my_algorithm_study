
data = [1, 2, 3]
N = len(data)

dp = [[0 for _ in range(N+1)] for _ in range(1<<N)]

for i in data:
    tmpList = [[i]]
    dp[1<<(i-1)][i] = tmpList

for mask in range(1<<N):
    for last in range(1, N+1):
        if not dp[mask][last]:
            continue
        for nxt in data:
            if mask & (1 << (nxt - 1)) == 0:
                if dp[(1<<(nxt-1))+mask][nxt] == 0:
                    dp[(1 << (nxt - 1)) + mask][nxt] = []

                for perm in dp[mask][last]:
                    dp[(1<<(nxt-1))+mask][nxt].append(perm+[nxt])

print(dp)
