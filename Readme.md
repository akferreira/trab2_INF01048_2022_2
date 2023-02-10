# Othello | Trabalho 2 da disciplina de Inteligência Artificial INF01048
- Arthur Kassick Ferreira | 00301388 | Turma B

- Cássio Entrudo | 00252847 | Turma B

- Leonardo Luis Carlos | 00243909 | Turma B
==============================================================================


O relatório deve conter: 

Bibliotecas que precisem ser instaladas para executar sua implementação. 
Descrição da função de avaliação, 
da estratégia de parada;
eventuais melhorias (quiescence search, singular extensions, etc para a poda alfa-beta ou qualquer melhoria para o MCTS); 
decisões de projeto e dificuldades encontradas; 
e bibliografia completa (incluindo sites).

#Bibliotecas utilizadas
import threading
import time
import random
from typing import Tuple

# Estratégia
UBC - Upper Confidence Bound foi a estratégia escolhida para abordar o problema. Foi implementado no agent.py, que faz uma exploração recursiva e ao chegar numa folha ele verifica qual valor "ganhou" e "sobe" a árvore com o valor desempilhando.

  
 return (self.vitorias/self.visitas + (self.C - self.custo/60) * sqrt(log(self.pai.visitas)/self.visitas ))
 
## Condição de parada:
    Foi utilizado o tempo limite de 5 segundos ou que atinja um estado terminal
# Eventuais melhorias
Na função UCB, foi comentada uma linha que altera o retorno que altera o coeficiente de exploração da árvore caso tenha níveis mais profundos
    (#self.custo/60 é um parâmetro para ligeiramente alterar o coeficiente de exploração da MCTS)
  ### Algumas das dificuldades encontradas: 
  - Problemas em se acertar com a biblioteca de time;
  - Problema na retira do nó com melhor escolha;
  - Problema com jogadas inválidas quando a melhor não estava disponível
