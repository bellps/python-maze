from labirinto import Labirinto

class LabirintoEstrategia2(Labirinto):
  def labirinto_com_saida(self):
    entrada = self.__achar_fonte(self.grafo)
    saida = self.__achar_sorvedouro(self.grafo)

    return super().labirinto_com_saida(entrada, saida)

  def __achar_fonte(self, grafo):
    fonte = None
    grafo_flat = set([adjacente for vertice in grafo for adjacente in vertice])

    for i in range(len(grafo)):
      if i not in grafo_flat:
        fonte = i
        break

    if fonte == None:
      raise Exception('Labirinto não possui entrada válida!')
    else:
      return fonte

  def __achar_sorvedouro(self, grafo):
    sorvedouro = None

    for i, vertice in enumerate(grafo):
      if vertice == []:
        sorvedouro = i
        break

    if sorvedouro == None:
      raise Exception('Labirinto não possui saída válida!')
    else:
      return sorvedouro
