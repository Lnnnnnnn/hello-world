### update time 20211104


import collections

# def BFS(matrix):
#     m, n = len(matrix), len(matrix[0])
#     dist = [[0] * n for _ in range(m)]
#     zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
#     # 将所有的 0 添加进初始队列中
#     q = collections.deque(zeroes_pos)
#     seen = set(zeroes_pos)
#
#     ## 广度优先搜索
#     while q:
#         i, j = q.popleft()
#         for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
#             if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
#                 dist[ni][nj] = dist[i][j] + 1
#                 q.append((ni, nj))
#                 seen.add((ni, nj))
#
#     return seen, dist



def func(mat):

    mat_y = len(mat)
    mat_x = len(mat[0])

    res_mat = [[0] * mat_x for _ in range(mat_y)]

    zero_pos = [(i, j) for i in range(mat_y) for j in range(mat_x) if mat[i][j] == 0]

    que = collections.deque(zero_pos)

    seen = set(zero_pos)

    while que:
        i, j = que.popleft()
        for ni, nj in [[i+0,j+1],[i+0,j-1],[i+1,j+0],[i-1,j+0]]:
            if 0 <= ni < mat_y and 0 <= nj < mat_x and (ni, nj) not in seen:
                que.append([ni,nj])
                seen.add((ni,nj))
                res_mat[ni][nj] = res_mat[i][j] + 1


    return res_mat




#
# def BFS(mat):
#
#     directions = [[0,1],[0,-1],[1,0],[1,-1]]
#
#     for map_y in range(len(mat)):
#         for map_x in range(len(mat[0])):
#
#             if mat[map_y][map_x] != 0:
#
#
#                 min_distance = len(mat) + len(mat[0])
#                 que = collections.deque([(map_y, map_x)])
#                 count = 0
#
#                 while que:
#
#                     point = que.pop()
#                     count = count + 1
#                     for move in directions:
#                         new_y = move[0] + point[0]
#                         new_x = move[1] + point[1]
#
#                         if 0 <= new_y < len(mat) and 0 <= new_x< len(mat[0]) and mat[new_y][new_x] == 0:
#
#                             if count <= min_distance:
#                                 min_distance = count
#                             mat[map_y][map_x] = min_distance
#                             break
#
#                         elif 0 <= new_y < len(mat) and 0 <= new_x< len(mat[0]) and mat[new_y][new_x] == 1:
#
#                             que.append([new_y,new_x])
#
#                 mat[map_y][map_x] = min_distance
#
#
#     return mat



if __name__ == "__main__":
    res1= func( [[0,0,0],[0,1,0],[1,1,1]])
    print(res1)




