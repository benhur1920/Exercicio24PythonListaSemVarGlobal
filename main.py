import random

def carregandoCemJogadas(n):
  jogadas = []
  for i in range(n):
    jogadas.append(random.randint(1,6))
  #atribuindo zero a todos os elementos do vetor estatistica
  estatistica = [0,0,0,0,0,0]
  estatistica = carregarVetorEstatistica(jogadas, estatistica)
  exibirResultados(jogadas, estatistica)

def carregarVetorEstatistica(jogadas, estatistica):
  for i in range(len(jogadas)):
    for j in range(len(estatistica)):
      if jogadas[i] == j + 1:
          estatistica[j] +=  + 1
          break
  return estatistica
  
def exibirResultados(jogadas, estatistica):
  print('\nOs 100 lances foram: ')
  print(jogadas)
  print('\nEstatistica dos lances')
  print('\n------------------------------------')
  for i in range(len(estatistica)):
    print(f'\nNúmero: {i + 1}    Qtd Lance: {estatistica[i]}')
  

#programa principa
carregandoCemJogadas(100)