from math import sqrt,log
from typing import Tuple, Union
from advsearch.othello.gamestate import GameState
from advsearch.othello.board import Board

class Nodo():
  C = sqrt(2)
  count = 0

  def __init__(self,gamestate,custo,pai = None):
    self.gamestate = gamestate
    self.custo = custo
    self.pai = pai
    self.vitorias = 0
    self.visitas = 0
    self.filhos = []


  def verificar_vitoria(self,ganhador = None):
    if(self.gamestate.is_terminal()):
      if(self.gamestate.winner() == self.pai.gamestate.player):
        self.vitorias += 1
      return self.gamestate.winner()
    
    else:
      try:
        if(ganhador == self.pai.gamestate.player):
          self.vitorias += 1
      except AttributeError:
        pass

  def UCB(self):
    if(self.pai is None or self.visitas == 0):
      return 5


    return (self.vitorias/self.visitas + self.C * sqrt(log(self.pai.visitas)/self.visitas ))

  def gerar_filhos(self):
    if(self.gamestate.is_terminal() == False and not self.filhos):
      jogadas = self.gamestate.legal_moves()

      for jogada in jogadas:
        next_gamestate = self.gamestate.next_state(jogada)
        self.filhos.append(Nodo(next_gamestate,self.custo+1,self))

  def escolhe_melhor_filho(self):
    if(self.filhos):
      filhos = sorted(self.filhos, key = Nodo.UCB, reverse = True)
      return filhos[0]


def explorar_arvore(nodo):
  nodo.visitas += 1
  Nodo.count += 1
  nodo.gerar_filhos()
  next_nodo = nodo.escolhe_melhor_filho()

  if(next_nodo):
    ganhador = explorar_arvore(next_nodo)
    next_nodo.verificar_vitoria(ganhador)
    return ganhador

  return nodo.verificar_vitoria()

    #print(jogadas)


tabuleiro = Board()
estado = GameState(tabuleiro,'B')
arvore = Nodo(estado,0)
print(arvore.gamestate.winner())

for x in range(100):
  explorar_arvore(arvore)

print(arvore.visitas)

for filho in arvore.filhos:
  print(f"{filho.vitorias}/{filho.visitas}")
  for x in filho.filhos:
    print(f"\t {x.vitorias}/{x.visitas}")
print(Nodo.count)

