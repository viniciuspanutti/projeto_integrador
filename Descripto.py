def descriptografar(texto_cifrado):
    # Alfabeto
    T = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    texto_cifrado = texto_cifrado.upper().replace(" ", "")
    n = len(texto_cifrado)
    
    # Vetor de índices (1-based)
    I = [T.index(letra) + 1 for letra in texto_cifrado]
    
    # Criando pares de sílabas
    P = []
    for i in range(n // 2):
        k = 2 * i
        P.append([I[k], I[k + 1]])
    
    # Matriz inversa da chave
    A_inv = [[2, 25], [23, 2]]
    
    # Decifrar a matriz
    D = []
    for par in P:
        d1 = (A_inv[0][0] * par[0] + A_inv[0][1] * par[1]) % 26
        d2 = (A_inv[1][0] * par[0] + A_inv[1][1] * par[1]) % 26
        d1 = 26 if d1 == 0 else d1
        d2 = 26 if d2 == 0 else d2
        D.append([d1, d2])
    
    # Texto decifrado
    TD = []
    for par in D:
        TD.append(par[0])
        TD.append(par[1])
    
    # Converter para letras
    texto_decifrado = ''.join([T[idx - 1] for idx in TD])
    
    # Remove 'X' extra se necessário
    if len(texto_decifrado) % 2 == 0 and texto_decifrado[-1] == 'X':
        texto_decifrado = texto_decifrado[:-1]
    
    print("Texto decifrado:", texto_decifrado)
    return texto_decifrado

# Parte principal simplificada
texto = input("Entre com o texto a ser descriptografado: ")
descriptografar(texto)