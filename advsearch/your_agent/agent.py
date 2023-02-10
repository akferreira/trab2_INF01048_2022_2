import random
from typing import Tuple

from ..othello.gamestate import GameState
from math import sqrt,log
from time import sleep,time

class Nodo():
  C = 0.8

  count = 0 #variável de debug. Utilizada para saber o número total de nodos visitados durante a execução do código

  def __init__(self,gamestate,custo,jogada,pai = None):
    self.gamestate = gamestate
    self.custo = custo  #quantidade de movimentos necessários para atingir o estado
    self.pai = pai
    self.vitorias = 0
    self.visitas = 0
    self.jogada = jogada #qual a jogada é realizada no turno correspondente ao nodo.
    self.filhos = []


  #Verifica se o jogador cujo turno criou esse nodo ganhou ou não. Se o turno atual é das brancas, é porque as pretas jogaram na última jogada e 
  #culminaram no estado atual do tabuleiro. 
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
    #Para nodos sem visitas, ou a raiz da árvore. 
    if(self.pai is None or self.visitas == 0):
      return 1
    
    #self.custo/60 é um parâmetro para ligeiramente alterar o coeficiente de exploração da MCTS quando se chega nos níveis mais profundos da árvore
    return (self.vitorias/self.visitas + (self.C - self.custo/60) * sqrt(log(self.pai.visitas)/self.visitas ))

  #Para fins de otimização, o tabuleiro só é criado quando necessário a partir do gamestate
  def criar_tabuleiro(self):
    if(self.jogada is not None):
      next_gamestate = self.pai.gamestate.next_state(self.jogada)
      self.gamestate = next_gamestate
      return

  def gerar_filhos(self):
    if(self.gamestate.is_terminal() == False and not self.filhos):
      jogadas = self.gamestate.legal_moves()

      for jogada in jogadas:
        
        self.filhos.append(Nodo(None,self.custo+1,jogada,self))

    return self.vitorias/self.visitas

  def escolhe_melhor_filho(self):
    if(self.filhos):
      filhos = sorted(self.filhos, key = Nodo.UCB, reverse = True)

      return filhos[0]

  def escolhe_melhor_jogada(self):
    if(self.filhos):
      filhos = sorted(self.filhos, key = Nodo.taxa_vitoria, reverse = True)
      return filhos[0]

  #para escolher a melhor jogada desse turno. Não considera coeficiente de exploração
  def taxa_vitoria(self):
    if(self.visitas == 0):
      return 0

    else:
      return self.vitorias/self.visitas

  def visitar_nodo(self):
    self.visitas += 1
    Nodo.count += 1
    self.criar_tabuleiro()
    self.gerar_filhos()

def explorar_arvore(nodo):
  nodo.visitar_nodo()
  next_nodo = nodo.escolhe_melhor_filho()

  if(next_nodo is not None):
    ganhador = explorar_arvore(next_nodo)
    next_nodo.verificar_vitoria(ganhador)
    return ganhador

  #nodo terminal
  return nodo.verificar_vitoria()

def make_move(estado_atual):
  arvore = Nodo(estado_atual,0,None)
  start = time()
  now = time()

  while(now - start < 4.9):
    explorar_arvore(arvore)
    now = time()
    
  best = arvore.escolhe_melhor_jogada()
  return best.jogada






