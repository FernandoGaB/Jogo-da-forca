from componentes_tela.modulo_inputs import cria_jogador, valida_chute, mostrar_menu, continuar_jogando
from componentes_tela.modulo_janelas import desenha_jogo, divisoes, mostrar_regras, exibe_palavra
from jogo.modulo_jogo import obtem_palavra, soma_pontos, letras_palavra
from time import sleep

letras_acertou = []
letras_da_palavra = []
palavra_ja_foi = []
letras_ja_foi = []
erros = 0
letra = None
jogo_acabou = False
opçao = 0
chutar = None
jogador = None
palavra_chave = None

print('Bem vindo ao jogo da forca!')

jogador = cria_jogador()

while opçao != 3:
    if jogo_acabou:
        opçao = 3
    else:
        opçao = mostrar_menu(opçao, jogador)

    if opçao == 1:

        while not jogo_acabou:
            palavra_certa =  obtem_palavra(palavra_ja_foi)
            while True:
                if len(palavra_certa) == len(letras_da_palavra):
                    soma_pontos(jogador)
                    divisoes()
                    desenha_jogo(erros, jogador)
                    exibe_palavra(letra, palavra_certa, letras_acertou)
                    divisoes()
                    print(f'Parabéns {jogador.get("nome")}. ')
                    print('Você ganhou! ')
                    break
                if erros == 7:
                    print(f'A palavra certa era {palavra_certa}. ')
                    break

                divisoes()
                desenha_jogo(erros, jogador)
                exibe_palavra(letra, palavra_certa, letras_acertou)
                divisoes()

                letra = input(f'{jogador.get("nome")}, informe uma letra: ')

                if letra.isspace():
                    print('Somente letras são validas.')
                    sleep(1)
                elif letra.isalpha():
                    letra = letra.upper()
                    if letra in letras_ja_foi:
                        print('Você já usou essa letra tente outra! ')
                        sleep(1)
                    elif len(letra) == 1:
                        letras_ja_foi.append(letra)
                        if letra in palavra_certa:
                            letras_acertou.append(letra)
                            letras_da_palavra = letras_palavra(palavra_certa, letras_acertou, letras_da_palavra)
                            print('Você acertou! ')
                            sleep(1)
                        else:
                            erros = erros + 1
                            print('Infelizmente você errou! ')
                            sleep(1)
                    elif len(letra) > 1: 
                        if len(letra) == len(palavra_certa):
                            chutar = valida_chute()
                            if chutar:
                                if letra == palavra_certa:
                                    soma_pontos(jogador)
                                    print(palavra_certa)
                                    print(f'Parabéns {jogador.get("nome")}. ')
                                    print('Você ganhou! ')
                                    sleep(1)
                                    break
                                else:
                                    erros = 7
                            else:
                                continue
                        else:
                            print('Informe uma letra ou chute! ')
                            sleep(1)
                    elif len(letra) < 1:
                        print('Você deve inserir uma letra! ')
                        sleep(1)
                else:
                    print('Apenas letras são validas. ')
                    print('Tente novamente! ')
                    sleep(1)
                
            jogo_acabou = continuar_jogando(jogo_acabou, opçao)
            letras_acertou.clear()
            letras_da_palavra.clear()
            letras_ja_foi.clear()
            palavra_chave = None
            erros = 0
            palavra_certa = None

    elif opçao == 2:
        mostrar_regras()
    elif opçao == 3:
        print(f'Espero que tenha se divertido {jogador.get("nome")}! ')
        print('Até a proxima. ')
    else:
        print('Opção invalida! ')
        print('Escolha uma das opções do menu. ')
        sleep(1)