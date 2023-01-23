BLACK = 'B'
WHITE = 'W'
VAZIO = '.'
PX = 0
PY = 1
peca_jogador = ('B','W')
peca_outro_jogador = {'B':'W','W':'B'}
IND_MAX = 7


TABULEIRO_INICIAL = [
"........", 
"........",
"........",
"...WB...",
"...BW...",
"........",
"........",
"........",
]

'''
TABULEIRO_INICIAL = [
"........", 
"........",
"........",
"...WB...",
"...BWB..",
".....W..",
"........",
"........",
]'''


class Nodo():
  def __init__(self):
    self.visitas = 0
    self.vitorias = 0
    self.jogador = 0


def jogada(tabuleiro,jogador):
  return

def get_posicoes_pecas(tabuleiro):
  posicoes = {BLACK : [],WHITE: [],VAZIO : []}

  for y,linha in enumerate(tabuleiro):
      for x,peca in enumerate(linha):
        posicoes[peca].append((x,y))

          
  return posicoes


#gera posições vizinhas válidas para as coordenadas dadas
def posicoes_vizinhas_disponiveis(posicao,posicoes,tabuleiro):
  x,y = posicao
  peca_adversaria = tabuleiro[y][x]
  peca = peca_outro_jogador[peca_adversaria]
  posicoes_jogador = posicoes[peca] 
  posicoes_adversaria = posicoes[peca_adversaria]

  posicoes_candidatas = [(x1,y1) for x1,y1 in [(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)] 
          if (x1 >= 0 and x1 <= IND_MAX) and (y1 >= 0 and y1 <= IND_MAX) and ((x1,y1) in posicoes[VAZIO])]

  pos = []
  print(posicoes_candidatas)
  posicoes_capturadas = {}

  #Procura entre as posições livres no tabuleiro as que resultam em captura de peças adversárias, assim como quais peças serão capturadas.
  for posicao_livre in posicoes_candidatas:
    #print(f"{posicao_livre=}")
    x,y = posicao_livre
    captura = False
    posicoes_capturadas[(x,y)] = []

    #busca horizontal ->
    for cx in range(x+1,IND_MAX):

      if(tabuleiro[y][cx] == peca_adversaria):
        posicoes_capturadas[(x,y)].append((cx,y))

        if(tabuleiro[y][cx+1] == peca):
          captura = True

      elif(tabuleiro[y][cx] == peca):
        break

    #busca horizontal <-
    for cx in range(x,0,-1):
      if(tabuleiro[y][cx] == peca_adversaria): 
        posicoes_capturadas[(x,y)].append((cx,y))

        if (tabuleiro[y][cx-1] == peca):
     #   print(f"B={cx=}||{y=}|{tabuleiro[y][cx]}||{tabuleiro[y][cx-1]}")
          captura = True

      elif(tabuleiro[y][cx] == peca):
        break

    #busca vertical
    for cy in range(y+1,IND_MAX):
      if(tabuleiro[cy][x] == peca_adversaria and tabuleiro[cy+1][x] == peca):
      #  print(f"C={cx=}||{y=}|{tabuleiro[cy][x]}||{tabuleiro[cy+1][x]}")
        captura = True

      elif(tabuleiro[cy][x] == peca):
        break

    #busca vertical
    for cy in range(y,0,-1):
      if(tabuleiro[cy][x] == peca_adversaria and tabuleiro[cy-1][x] == peca):
     #   print(f"d={cx=}||{y=}|{tabuleiro[cy][x]}||{tabuleiro[cy-1][x]}")
        captura = True
      elif(tabuleiro[cy][x] == peca):
        break

    #busca diagonal
    for cx,cy in zip(range(x+1,IND_MAX),range(y+1,IND_MAX)):
      if(tabuleiro[cy][cx] == peca_adversaria and tabuleiro[cy+1][cx+1] == peca):
       # print(f"A={cx=}||{cy=}|{tabuleiro[cy][cx]}||{tabuleiro[cy+1][cx+1]}")
        captura = True

      elif(tabuleiro[cy][cx] == peca):
        break

    #busca diagonal
    for cx,cy in zip(range(x,0,-1),range(y,0,-1)):
      if(tabuleiro[cy][cx] == peca_adversaria and tabuleiro[cy-1][cx-1] == peca):
        captura = True

      elif(tabuleiro[cy][cx] == peca):
        break


    if(captura):
      pos.append(posicao_livre)
    
    

  print(posicoes_capturadas)
  return pos


def pecas_vizinhas(posicao,tabuleiro):
  x,y = posicao
  return [(x1,y1,tabuleiro[y1][x1]) for x1,y1 in [(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)] 
          if (x1 >= 0 and x1 <= IND_MAX) and (y1 >= 0 and y1 <= IND_MAX)]




#verifica se tem uma linha horizontal ou vertical entre duas posições
def checar_linha(posicao1,posicao2):
  return  (posicao1[PX] == posicao2[PX] or posicao1[PY] == posicao2[PY] or (abs(posicao1[PX]-posicao2[PX]) == abs(posicao1[PY]-posicao2[PY])))

def checar_linha_captura(posicao1,posicao2,posicao3):
  return  ( (posicao1[PX] == posicao2[PX] and posicao1[PX] == posicao3[PX]) or 
           (posicao1[PY] == posicao2[PY and posicao1[PY] == posicao3[PY]]) or 
           (abs(posicao1[PX]-posicao2[PX]) == abs(posicao1[PY]-posicao2[PY])) and abs(posicao1[PX]-posicao3[PX]) == abs(posicao1[PY]-posicao3[PY]))
  

def alterar_tabuleiro():
  return


def gerar_jogada(posicoes,jogador):
  jogador_adversario = jogador ^ 1
  peca_adversario = peca_jogador[jogador_adversario]
  posicoes_adversario = posicoes[peca_adversario]




def jogar_peca(posicoes,jogador,posicao):
  peca_jogar = peca_jogador[jogador]
  jogador_adversario = jogador ^ 1
  peca_adversario = peca_jogador[jogador_adversario]
  x,y = posicao

  if(posicao in posicoes[VAZIO]):
      for posicao_peca_adversario in posicoes[peca_adversario]:
        if(posicao_peca_adversario in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]):
          print(posicao_peca_adversario)
          print("ok")

  return

def print_tabuleiro(tabuleiro):
  for line in tabuleiro:
    print(line)
  



posicoes = get_posicoes_pecas(TABULEIRO_INICIAL)
print(posicoes)
jogadas = posicoes_vizinhas_disponiveis((4,4),posicoes,TABULEIRO_INICIAL)

print(jogadas)
print("\n")
jogadas = posicoes_vizinhas_disponiveis((3,3),posicoes,TABULEIRO_INICIAL)
print(jogadas)


