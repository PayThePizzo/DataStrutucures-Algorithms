from structures import Graph


def main():
    g = Graph(rand=True)
    g.show()
    g1_pi = g.BFS(g.node())
    g2_pi = g.DFS()
    g1_pi.show()
    g2_pi.show()


if __name__ == '__main__':
    main()
