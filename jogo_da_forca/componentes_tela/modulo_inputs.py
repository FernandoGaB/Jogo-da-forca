def cria_jogador():
    usuario = {}
    usuario['nome'] = input('Informe seu nome: ')
    usuario['pontos'] = 0
    return usuario

def valida_chute():
    while True:
        chute = input('Deseja chutar a palavra? (S ou N)')
        if chute in 'Ss':
            chutar = True
            break
        elif chute in 'Nn':
            chutar = False
            break
        else:
            print('Apenas S e N são valodos! ')
    return chutar

def mostrar_menu(opçao, jogador):
    while True:
        print('-=' * 20)
        print(f'''{'-=' * 9}MENU{'-=' * 9}''')
        print('-=' * 20)
        print('1- Jogar; ')
        print('2- Ler forma de jogar; ' )
        print('3- Sair. ')
        opçao = int(input(f'{jogador.get("nome")} informe qual das ações deseja realizar! '))
        if opçao == 1 or opçao == 2 or opçao == 3:
            break
        else:
            print('Resposta invalida. ')
            print('Informe um dos numeros do menu! ') 
    return opçao

def continuar_jogando(jogo_acabou, opçao):
    while True:
        continuar = input('Você deseja jogar novamente (S ou N)? ')
        if continuar in 'Ss':
            jogo_acabou = False
            break
        elif continuar in 'Nn':
            jogo_acabou = True
            break
        else:
            print('Apenas S e N são validos! ')
        opçao = 3
    return jogo_acabou