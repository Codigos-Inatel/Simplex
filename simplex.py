import math 
import numpy as np

# Função que calcula o método SIMPLEX 
def simplex(table, lines, columns, decisions_variables, constraints):
  columns = columns-1
  pivotColumnIndex = lowerValueCalculate(table, columns) # Variável que armazena o index da coluna pivo 
  variables = np.zeros(lines) # Vetor de zeros, para armazena as variáveis 
  print("\n"+ str(table))
  while pivotColumnIndex != -1:
    pivotRowIndex = rowPivotCalculate(table, lines, columns, pivotColumnIndex) # Variável que armazena o index da linha pivo
    variables[pivotRowIndex] = pivotColumnIndex # Armazena na posição da  linha pivo, o index da coluna pivo 
    table = createNewTable(table, lines, columns, pivotRowIndex, pivotColumnIndex) # Chama funçãopara criar a nova tabela 
    print("\n"+ str(table))
    pivotColumnIndex = lowerValueCalculate(table, columns) # Variável que armazena o index da coluna pivo 
  #Mostrando os resultados calculados ao fim do Simplex 
  print("\nSolução Ótima: ")
  for i in range(1, lines):
    print("X"+ str(int(variables[i]+1)) + " = " + str(table[i][columns]))
  greatProfit = table[0][columns]
  print("\nLucro Ótimo: " + str(greatProfit))

  print("\nPreço Sombra:")
  for i in range(0, constraints):
    print("X" + str(i+1) + " = " + str(table[0][i+decisions_variables]))

# Função que retorna o index da coluna pivo, ou seja, o index do menor valor negativo da função objetivo
def lowerValueCalculate(table, columns):
  pivotColumn = -1
  lowerValue = 0
   
  for i in range(0, columns):
    if table[0][i] < lowerValue:
      lowerValue = table[0][i]
      pivotColumn = i

  return pivotColumn
# Função que retorna o index da linha pivo, ou seja, o index do menor valor negativo da função objetivo
def rowPivotCalculate(table, lines, columns, pivotColumnIndex):
  lowerValue = math.inf # Maior valor recebe infinito 
  lowerValueIndex = -1

  for i in range(0, lines):
    if table[i][pivotColumnIndex] != 0:
      division = table[i][columns]/table[i][pivotColumnIndex] # ivisão entre o numero da ultima coluna pelo numero da coluna pivo na linha i 
    else:
      division = math.inf # Retorna infinita caso a divisão seja por 0 
    # Pega o menor valor não nulo do resultado das divisões anteriores. 
    if(division > 0 and division < lowerValue):
      lowerValue = division
      lowerValueIndex = i

  return lowerValueIndex
# Função que cria e retorna a nova tabela. 
def createNewTable(table, lines, columns, pivotRowIndex, pivotColumnIndex):
  pivot = table[pivotRowIndex][pivotColumnIndex] # Pivo da tabela anterior 
  newTable = np.zeros((lines, columns+1)) # Matriz de zeros 

  for i in range(0, columns+1):
    newTable[pivotRowIndex][i] = np.around(table[pivotRowIndex][i]/pivot, 2) # Calcula a linha de referencia 
  # Calcula e preenche o restante da tabela 
  for i in range(0, lines):
    for j in range(0, columns+1):
      if i != pivotRowIndex:
        parameter = table[i][pivotColumnIndex]*-1
        newTable[i][j] = np.around(table[i][j]+(parameter*newTable[pivotRowIndex][j]), 2)

  return newTable
