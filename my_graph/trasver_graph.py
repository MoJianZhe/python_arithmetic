# 下面的算法代码可以遍历图的所有路径，寻找从 src 到 dest 的所有路径

# onPath 和 path 记录当前递归路径上的节点
# on_path 表示是以 src 为起点访问过。
on_path = [False] * len(graph)
path = []

def traverse(graph, src, dest):
    # base case
    if src < 0 or src >= len(graph):
        return
    if on_path[src]:
        # 防止死循环（成环）
        return
    if src == dest:
        # 找到目标节点
        print(f"find path: {'->'.join(map(str, path))}->{dest}")
        return

    # 前序位置
    on_path[src] = True
    path.append(src)
    for e in graph.neighbors(src):
        traverse(graph, e.to, dest)
    # 后序位置
    path.pop()
    on_path[src] = False