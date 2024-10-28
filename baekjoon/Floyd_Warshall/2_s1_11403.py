# 경로 찾기

import sys
input = sys.stdin.readline

# 문제 입력값을 받는다
n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 최단 거리가 아닌 경로 존재의 유무만 판별하면 된다.
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            # i->k, k->j 경로가 존재한다면, i->j 경로도 존재한다.
            if graph[i][k] and graph[k][j] :
                graph[i][j] = 1

for row in graph :
    print(' '.join(map(str, row)))


# https://blog.naver.com/ndb796/221234427842