Arthur Kassick Ferreira 00288545  Turma B
Cássio Entrudo 00252847 Turma B
Leonardo Luis Carlos 00243909 Turma B

# Bibliotecas utilizadas
```
import random
from typing import Tuple
from math import sqrt,log
from time import sleep,time
````

# Estratégia
Foi utilizado uma estratégia de MCTS (Mount Carlo Tree search) para criar uma árvore com as diferentes possibilidades de jogo a fim de buscar as jogadas com as maiores chances de vitória. Cada exploração da árvore consiste em simular um conjunto de possívieis movimentos do tabuleiro que levem, a partir do estado inicial dado, a um estado final do jogo no qual um dos jogadores vença ou que ocorra o empate. Como critério para escolha dos nodos ao se aprofundar na árvore, o MCTS usa o critério UBC - Upper Confidence Bound - o qual leva em consideração tanto a taxa de vitórias encontradas nos nodos visitados, quanto a taxa (ou coeficiente) de exploração escolhida para o problema.

No que diz respeito a implementação do código para o MCTS, escolheu-se uma abordagem recursiva para a descida na árvore pela facilidade que ela fornece de fazer o movimento reverso de subida, isto é, de atualizar os nodos visitados no caminho ao nodo folha encontrado e do resultado do jogo (vitória das peças brancas, pretas ou do empate).

 ```
 UCB = (self.vitorias/self.visitas + (self.C - self.custo/60) * sqrt(log(self.pai.visitas)/self.visitas ))
 ```
 
## Condição de parada:
   
   Foi utilizado o tempo limite de 5 segundos para a exploração da árvore de Monte Carlo. Com uma margem de 100ms, enquanto houver tempo disponível o código continua a simular possíveis conjuntos de jogadas dado um estado inicial. Considera-se uma iteração na exploração da árvore o caminho percorrido do estado inicial dado a um estado terminal (isto é, em que haja vitória de um jogador ou de empate).
    
# Eventuais melhorias

Uma pequena melhoria implementada é o do ajuste do coeficiente de exploração conforme o código se aprofunda na árvore: quanto mais profunda a busca se encontra, maior a incerteza das simulações e com isso o desejo de garantir que as possibilidades encontradas se aproximem do resultado real.

# Dificuldades encontradas

Durante os testes, descobriu-se por meio do python profile que o maior gargalo do programa está nas funções de manipulação do tabuleiro. Muito provavelmente ao uso de matrizes de string , as quais tem grande penalidade de desempenho no python, para a representação do tabuleiro. Abaixo um excerto de um desses relatórios:

```
  4138620 function calls (4129606 primitive calls) in 17.648 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1576680    3.973    0.000    3.973    0.000 board.py:184(find_where_to_play_from_owned)
    17636    3.347    0.000    7.841    0.000 board.py:322(find_legal_moves_sparse)
  1023945    2.441    0.000    2.441    0.000 board.py:153(find_bracket)
   408397    1.262    0.000    2.161    0.000 board.py:353(<lambda>)
     9363    1.144    0.000    2.706    0.000 board.py:304(find_legal_moves_dense)
    55144    0.716    0.000    2.877    0.000 {built-in method builtins.any}
   268326    0.458    0.000    0.458    0.000 {method 'add' of 'set' objects}
```
Visto a ineficiência dessas funções, a solução encontrada para minimizar ao máximo o impacto no desempenho do código foi de somente manipular o tabuleiro quando estritamente necessário, isto é, ao de fato visitar um nodo o qual deseja simular sua respectiva jogada.

# Bibliografia

https://en.wikipedia.org/wiki/Monte_Carlo_tree_search

https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/

https://towardsdatascience.com/monte-carlo-tree-search-158a917a8baa

https://www.cs.swarthmore.edu/~mitchell/classes/cs63/f20/reading/mcts.html

https://www.programiz.com/python-programming/time

https://docs.python.org/3/library/profile.html
