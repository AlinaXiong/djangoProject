# 通过 warshall 计算传递闭包矩阵
def warshall_algorithm(A):
    n = len(A)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = A[i][j] or (A[i][k] and A[k][j])
    return A

# 递阶分层分析
def hierarchy_layers(reachability_matrix):
    n = len(reachability_matrix)
    remaining_nodes = set(range(n))  # 节点集合，从0到n-1
    layers = []  # 存储各层节点

    while remaining_nodes:
        current_layer = set()
        for node in remaining_nodes:
            # 检查当前节点是否依赖于其他节点
            is_dependent = any(reachability_matrix[other][node] == 1 and other in remaining_nodes for other in range(n) if other != node)
            if not is_dependent:
                current_layer.add(node)

        if not current_layer:
            # 如果存在循环依赖或孤立节点，将这些节点作为单独一层加入
            current_layer = remaining_nodes

        # 将当前层的节点加入层次列表
        layers.append(list([x + 1 for x in current_layer]))
        # 从剩余节点中移除当前层的节点
        remaining_nodes -= current_layer

    return layers

# 移除举证中指定的行列
def remove_matching_rows_and_columns(matrix, indices_to_remove):
    """
    删除矩阵中指定索引的行和对应的列，并返回修改后的矩阵。

    参数:
    matrix -- 原始二维矩阵 (list[list])
    indices_to_remove -- 要删除的行和列的索引列表 (list[int])

    返回值:
    新的二维矩阵，其中指定索引的行和对应的列已被删除。
    """
    # 确保索引列表中的值在有效范围内
    if not all(0 <= index < len(matrix) for index in indices_to_remove):
        raise IndexError("索引列表中的值超出了矩阵的行范围")

    # 根据索引列表过滤行和列
    new_matrix = [
        [element for index, element in enumerate(row)
         if index not in indices_to_remove]
        for index, row in enumerate(matrix)
        if index not in indices_to_remove
    ]

    return new_matrix

# 打印矩阵
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

    # 计算层次结构
    layers = hierarchy_layers(transitive_closure)

    indices = []
    print("\n递阶分层结果:")
    for i, layer in enumerate(layers):
        print(f"Layer {i + 1}: Nodes {layer}")
        indices.extend([x - 1 for x in layer])

        hahaha= remove_matching_rows_and_columns(transitive_closure, indices)
        print_matrix(hahaha)


if __name__ == "__main__":
    main()
