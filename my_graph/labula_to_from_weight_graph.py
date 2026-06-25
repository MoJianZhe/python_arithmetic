# 无向加权图的通用实现
#无向加权图就等同于双向的有向加权图，所以直接复用上面用邻接表/领接矩阵实现的 WeightedDigraph 类就行了，只是在增加边的时候，要同时添加两条边：
from my_graph.labula_to_weight_graph import WeightedDigraph

class WeightedUndigraph:
    def __init__(self, n):
        self.graph = WeightedDigraph(n)

    # 增，添加一条带权重的无向边
    def addEdge(self, frm, to, weight):
        self.graph.addEdge(frm, to, weight)
        self.graph.addEdge(to, frm, weight)

    # 删，删除一条无向边
    def removeEdge(self, frm, to):
        self.graph.removeEdge(frm, to)
        self.graph.removeEdge(to, frm)

    # 查，判断两个节点是否相邻
    def hasEdge(self, frm, to):
        return self.graph.hasEdge(frm, to)

    # 查，返回一条边的权重
    def weight(self, frm, to):
        return self.graph.weight(frm, to)

    # 查，返回某个节点的所有邻居节点
    def neighbors(self, v):
        return self.graph.neighbors(v)

if __name__ == "__main__":
    graph = WeightedUndigraph(3)
    graph.addEdge(0, 1, 1)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)

    print(graph.hasEdge(0, 1))  # true
    print(graph.hasEdge(1, 0))  # true

    for edge in graph.neighbors(2):
        print(f"{2} <-> {edge.to}, weight: {edge.weight}")
    # 2 <-> 0, weight: 3
    # 2 <-> 1, weight: 4

    graph.removeEdge(0, 1)
    print(graph.hasEdge(0, 1))  # false
    print(graph.hasEdge(1, 0))  # false