from labirinto import Labirinto

class LabirintoEstrategia1(Labirinto):
  def labirinto_com_saida(self):
    entrada = 0
    saida = len(self.grafo) - 1

    return super().labirinto_com_saida(entrada, saida)
