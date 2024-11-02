import copy

import matplotlib.pyplot as plt
import networkx as nx


def create_directed_graph_from_adjacency_matrix(adjacency_matrix):
    """
    根据邻接矩阵创建有向图，忽略自环。
    """
    G = nx.DiGraph()
    num_nodes = len(adjacency_matrix)
    G.add_nodes_from(range(num_nodes))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i][j] == 1 and i != j:
                G.add_edge(i, j)
    return G


def draw_directed_graph(G):
    """
    绘制有向图。
    """
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.6, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue',
            font_size=10, font_weight='bold', arrows=True, edge_color='gray')
    plt.title("Directed Graph from Adjacency Matrix (Without Self-loops)")
    plt.show()


def get_layers_without_self_loops(G):
    """
    获取无自环节点的层次结构。
    """
    layers = []
    while G.number_of_nodes() > 0:
        zero_in_degree_nodes = [node for node in G.nodes if G.in_degree(node) == 0]
        if not zero_in_degree_nodes:
            layers.append(list(G.nodes))  # 停止条件，剩余节点构成循环依赖
            break
        layers.append(zero_in_degree_nodes)
        G.remove_nodes_from(zero_in_degree_nodes)
    return layers


def main():
    # 输入的邻接矩阵
    adjacency_matrix = [
        [1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1]
    ]

    # 创建有向图
    G = create_directed_graph_from_adjacency_matrix(adjacency_matrix)

    # 绘制有向图
    draw_directed_graph(G)

    # 分析层次结构
    graph_no_self_loops = copy.deepcopy(G)
    layers = get_layers_without_self_loops(graph_no_self_loops)

    # 打印层次结果
    print("\n使用有向图进行逐层分层结果:")
    for i, layer in enumerate(layers):
        print(f"Layer {i + 1}: Nodes {layer}")


if __name__ == "__main__":
    main()
