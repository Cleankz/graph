class Vertex:

    def __init__(self, val):
        self.Value = val

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size# максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)] # матрица смежности  0 отсутствие ребра 1 наличие
        self.vertex = [None] * size # хранит вершины

    def AddVertex(self, v): # сперва преобразуем в класс вертекс
        if not None in self.vertex:
            return False
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        return


    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v): # получает на вход индекс
        self.vertex[v] = None  # ваш код удаления вершины со всеми её рёбрами
        for i in range(len(self.m_adjacency[v])):
            if self.m_adjacency[v][i] != 0:
                self.m_adjacency[v][i] = 0
        for j in range(len(self.m_adjacency)):
            if self.m_adjacency[j][v] == 1:
                self.m_adjacency[j][v] = 0
        # ваш код удаления вершины со всеми её рёбрами
        return


    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        # True если есть ребро между вершинами v1 и v2
        return False

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2
        return

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        # удаление ребра между вершинами v1 и v2
        return
