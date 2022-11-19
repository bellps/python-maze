from graphviz import Digraph

class Labirinto:
  def __init__(self, grafo):
    self.grafo = grafo
    self.pre = [-1 for _ in range(len(grafo))]
    self.contador = 0

  def labirinto_com_saida(self, entrada, saida):
    self.__labirinto_com_saidaR(entrada, saida)

    return self.pre[saida] != -1

  def visualizar_labirinto(self):
    G = Digraph()

    for i, item in enumerate(self.grafo):
      G.node(str(i))

      for e in item:
        G.edge(str(i), str(e))

    print(G)
    with open('./labirinto.dot', 'w+') as write_file:
      write_file.write(str(G))

    return

  def __labirinto_com_saidaR(self, vertice, saida_grafo):
    self.pre[vertice] = self.contador
    self.contador += 1

    for adjacente in self.grafo[vertice]:
      if self.pre[saida_grafo] != -1:
        return

      if self.pre[adjacente] == -1:
        self.__labirinto_com_saidaR(adjacente, saida_grafo)

    return
