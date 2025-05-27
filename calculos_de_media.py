import mysql.connector
import os

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root', 
    password='1234',
    database='Projeto_sustentabilidade'
)
cursor = conexao.cursor()

# Tela de boas-vindas
print('\n\n\t=-=-=-=-= BEM VINDO(A) AO SISTEMA PARA CÁLCULO DE MÉDIAS =-=-=-=-=\n\n')
print('O sistema calculará as informações presentes no banco de dados e te retornará\n')
input('\n\t<< Tecle Enter para continuar >>')

os.system('cls' if os.name == 'nt' else 'clear')

# Exibição dos registros atuais
cursor.execute("SELECT ID, DataEntrada, LitrosConsumidos, KWHConsumido, KgNaoReciclaveis, PorcentagemResiduos, MeioDeTransporte FROM ProjetoDeSustentabilidade")
resultado = cursor.fetchall()

print('\n=-=-=-=-= Exibição dos dados de inserção: =-=-=-=-=\n')
print('| ID | Data de registro | Consumo de água | Consumo de energia | Lixo não reciclável | % de resíduos recicláveis | Transportes utilizados\t\t |')
for linha in resultado:
    print(f'{linha[0]:<4}\t{linha[1]}\t   {linha[2]} L\t\t{linha[3]} kWh\t\t\t{linha[4]} Kg\t\t\t{linha[5]}%\t\t\t\t{linha[6]}')
    print('-'*162)

print('\n=-=-=-=-= Processamento dos dados presentes no banco =-=-=-=-=\n')
print('='*50)
print('Média dos dados coletados')
print('='*50)

# Média Água
cursor.execute("SELECT AVG(LitrosConsumidos) FROM ProjetoDeSustentabilidade")
media_agua = cursor.fetchone()[0]
if media_agua is not None:
    print(f'\nMédia do consumo de água: {media_agua:.2f} L')
    if media_agua >= 150:
        if media_agua > 200:
            print("Classificação do consumo de água: Baixa sustentabilidade\n")
        else:
            print("Classificação do consumo de água: Moderada sustentabilidade\n")
    else:
        print("Classificação do consumo de água: Alta sustentabilidade\n")
else:
    print("Não há registros suficientes para calcular a média de consumo de água.\n")

# Média Energia
cursor.execute("SELECT AVG(KWHConsumido) FROM ProjetoDeSustentabilidade")
media_energia = cursor.fetchone()[0]
if media_energia is not None:
    print(f'Média do consumo de energia: {media_energia:.2f} kWh')
    if media_energia >= 300:
        print("Classificação do consumo de energia: Baixa sustentabilidade\n")
    elif media_energia >= 100:
        print("Classificação do consumo de energia: Moderada sustentabilidade\n")
    else:
        print("Classificação do consumo de energia: Alta sustentabilidade\n")
else:
    print("Não há registros suficientes para calcular a média de consumo de energia.\n")

# Média Resíduos
cursor.execute("SELECT AVG(PorcentagemResiduos) FROM ProjetoDeSustentabilidade")
media_residuos = cursor.fetchone()[0]
if media_residuos is not None:
    print(f'Média da porcentagem de resíduos recicláveis: {media_residuos:.2f}%')
    if media_residuos <= 20:
        print("Classificação dos resíduos recicláveis: Baixa sustentabilidade\n")
    elif media_residuos <= 50:
        print("Classificação dos resíduos recicláveis: Moderada sustentabilidade\n")
    else:
        print("Classificação dos resíduos recicláveis: Alta sustentabilidade\n")
else:
    print("Não há registros suficientes para calcular a média de resíduos recicláveis.\n")

# Análise dos meios de transporte
cursor.execute("SELECT MeioDeTransporte FROM ProjetoDeSustentabilidade")
dados_transporte = cursor.fetchall()

class_transporte = []
for linha in dados_transporte:
    transporte = linha[0].lower() if linha[0] else ""
    usa_publico = 'público' in transporte
    usa_bicicleta = 'bicicleta' in transporte
    usa_caminhada = 'caminhada' in transporte
    usa_eletrico = 'elétrico' in transporte
    usa_combustivel = 'combustível' in transporte
    usa_carro = 'carro' in transporte and 'elétrico' not in transporte and 'carona' not in transporte

    if (usa_publico or usa_bicicleta or usa_caminhada or usa_eletrico) and (usa_combustivel or usa_carro):
        class_transporte.append(2)  # Moderada
    elif usa_publico or usa_bicicleta or usa_caminhada or usa_eletrico:
        class_transporte.append(1)  # Alta
    else:
        class_transporte.append(3)  # Baixa

print('Média da classificação de transportes: ', end='')
if not class_transporte:
    print('Sem dados suficientes\n')
elif all(c == 1 for c in class_transporte):
    print('Alta sustentabilidade\n')
elif all(c == 3 for c in class_transporte):
    print('Baixa sustentabilidade\n')
else:
    print('Moderada sustentabilidade\n')
cursor.close()
conexao.close()