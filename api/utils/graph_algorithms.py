def warshall_algorithm(A):
    n = len(A)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = A[i][j] or (A[i][k] and A[k][j])
    return A


def print_matrix(matrix):
    # 获取矩阵的行数和列数
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # 打印矩阵内容
    for row in matrix:
        print("[ " + " , ".join(str(elem) for elem in row) + " ]")


def main():
    # 定义一个简单的邻接矩阵表示图
    # 矩阵中的值表示顶点之间是否存在直接连接：
    # 1 表示存在连接，0 表示不存在连接
    adjacency_matrix = [
        [1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1]
    ]

    print("原始系统可达矩阵:")
    print_matrix(adjacency_matrix)

    # 使用Warshall算法计算传递闭包
    transitive_closure = warshall_algorithm(adjacency_matrix)

    print("\n传递闭包后的邻接矩阵:")
    print_matrix(transitive_closure)


if __name__ == "__main__":
    main()
