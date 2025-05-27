# Define o alfabeto com letras de A a Z, associando A=1, B=2, ..., Z=26
T = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Solicita ao usuário que insira a palavra a ser criptografada
NOME = input("Entre com a palavra a ser criptografada: ").upper()

# Remove qualquer caractere fora do alfabeto e transforma em maiúsculas
NOME = ''.join([c for c in NOME if c in T])

# Se o número de letras for ímpar, adiciona um 'X' no final para completar o par
if len(NOME) % 2 != 0:
    NOME += 'X'

# Converte cada letra da palavra em seu respectivo número (A=1, ..., Z=26)
I = [T.index(c) + 1 for c in NOME]

# Cria pares de números, um par para cada duas letras
P = []
for i in range(0, len(I), 2):
    P.append([I[i], I[i+1]])  # Exemplo: 'VI' → [22, 9]

# Define a matriz chave usada para a criptografia (deve ser invertível módulo 26)
A = [[2, 1],
     [3, 2]]

# Inicializa a lista onde os pares criptografados serão armazenados
C = []

# Para cada par de letras (em número), aplica a multiplicação da matriz chave
for par in P:
    # Calcula o valor da nova primeira letra (linha 1 da matriz A)
    c1 = (A[0][0]*par[0] + A[0][1]*par[1]) % 26
    # Calcula o valor da nova segunda letra (linha 2 da matriz A)
    c2 = (A[1][0]*par[0] + A[1][1]*par[1]) % 26

    # Se algum valor deu 0, corrige para 26 (já que não existe letra com índice 0)
    c1 = 26 if c1 == 0 else c1
    c2 = 26 if c2 == 0 else c2

    # Armazena o par criptografado
    C.append([c1, c2])

# Inicializa a lista final com os caracteres criptografados
TC = []

# Converte os números de volta para letras do alfabeto
for par in C:
    TC.append(T[par[0]-1])  # -1 pois listas começam do zero em Python
    TC.append(T[par[1]-1])

# Exibe a mensagem final criptografada
print("Mensagem cifrada:")
print(''.join(TC))