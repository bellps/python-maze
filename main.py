from grafos import g1_1, g2_1, g3_1, g1_2, g2_2, g3_2
from labirinto_estrategia_1 import LabirintoEstrategia1
from labirinto_estrategia_2 import LabirintoEstrategia2

print("\n ===== Estratégia 1 =====")
print("Labirinto 1: " + str(LabirintoEstrategia1(g1_1).labirinto_com_saida()))
print("Labirinto 2: " + str(LabirintoEstrategia1(g2_1).labirinto_com_saida()))
print("Labirinto 3: " + str(LabirintoEstrategia1(g3_1).labirinto_com_saida()))

print("\n ===== Estratégia 2 =====")
print("Labirinto 1: " + str(LabirintoEstrategia2(g1_2).labirinto_com_saida()))
print("Labirinto 2: " + str(LabirintoEstrategia2(g2_2).labirinto_com_saida()))
print("Labirinto 3: " + str(LabirintoEstrategia2(g3_2).labirinto_com_saida()))