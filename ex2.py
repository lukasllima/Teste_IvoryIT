""" IVORYIT - TESTE
Deswevileutssen: REMÉDIO / Quanto vai gastar?
Scweisen: PARASITA/ANIMAL (MATAR)
Cada remédio mata um parasita (1 P/ 1)
CONAN (Pode mandar 2 mensagens)
    #A - Achei (N<=10) de Scweisen em (X, Y)
    #P - Quanto vou gastar para matar todas Scweisen na aárea (X, Y)

Variáveis
X: Largura do campo
Y: Cumprimento do campo
P: Preço
Q: Quantidade de mensagens
N: Número de Scweisen

Restrições
X <= 1000
Y <= 1000
P <= 10
Q <= 1000
N <= 10
"""

from time import sleep
soma = 0
opc = 0
contA = 0
contQ = 0
p = 0

while opc != 6:
    print('''
==================   MENU   ==================
    [ 1 ] - Inserir tamanho total campo
    [ 2 ] - Cadastrar Scweisen - Mensagem A
    [ 3 ] - Custo de Deswevileutssen - Mensagem P \033[31m#Não funciona\033[m
    [ 4 ] - Total de mensagens - Mensagem Q
    [ 5 ] - Exibir matriz do campo
    [ 6 ] - Sair''')

    opc = int(input('\t>>>>> - Qual sua opção? '))
    print('\n\n')
    if opc < 1 or opc > 6:
        print('\033[31mOpção inválida! Tente novamente\033[m')
    else:
        if opc == 1:
            x = int(input('Digite a largura do campo: '))
            y = int(input('Digite o cumprimento do campo: '))
            p = int(input('Qual o preço do produto/remédio: '))
            #Validação
            if x < 0 or x > 1000:
                print('Largura inválido. Tente novamente!')
                x = int(input('Digite a largura do campo: '))
            if y < 0 or y > 1000:
                print('Cumprimento inválido. Tente novamente!')
                y = int(input('Digite o cumprimento do campo: '))
            if p < 0 or p > 10:
                print('Preço inválido. Tente novamente!')
                p = int(input('Qual o preço do produto/remédio: '))
            x+=1
            y+=1
            #Gerar matriz nula
            matriz = []
            for zerar in range(x):
                matriz.append([0] * y)
        elif opc == 2:
            print('\t\tCadastro de Scweisen')
            qtde = int(input('Digite a quanidade de Scweisen que foi encontrada: '))
            aux_x = int(input('Digite a largura do campo: '))
            aux_y = int(input('Digite o Comprimento do campo: '))
            matriz[aux_x][aux_y] = qtde
            contA +=1
        elif opc == 3:#Não esta funcionando!
            #x1 = X / x2 = Y / y1 = W / Y2 = Z
            print('\t\tCálculo de custo da área')
            print('PONTO A: ')
            x1 = int(input('Largura: '))
            y1 = int(input('Comprimento: '))
            print('\nPONTO B: ')
            x2 = int(input('Largura: '))
            y2 = int(input('Comprimento: '))
            if x1 <= x2 and y1 <= y2:
                for i in range(x1, x2):
                    for j in range(y1, y2):
                        if matriz[i][j] != 0:
                            aux = matriz[i][j]
                            soma = soma + aux
                total = soma * p
                contQ += 1
                print('Foram encontrados {} Scweisen. O preço de cada Deswevileutssen é de R${}.\n Custo total: R$ {:.2f}'
                      .format(soma, p, total))
            else:
                print('\033[31mValores inválidas! Tente novamente\033[m')
        elif opc == 4:
            print('Mensagem A: {}vezes\nMensagem Q: {}vezes'.format(contA, contQ))
            print()
        elif opc == 5:
            #Exibir matriz
            for i in range(x):
                for j in range(y):
                    print(f'[{matriz[i][j]:^5}]', end='')
                print()

        else:
            print('\033[31m\t\tFinalizando...\033[m')
            sleep(2)
    print('\n\n\n\n\n')
    print('-=-' * 10)
print('Fim do programa. Volte sempre!')
