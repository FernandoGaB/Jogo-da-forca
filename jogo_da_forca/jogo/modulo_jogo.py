from random import choice

def obtem_palavra(palavra_ja_foi):
    palavras = open('palavras.txt', 'r')
    while True:
        palavra_escolhida = choice(palavras.readlines())
        palavra_escolhida = palavra_escolhida.rstrip()
        palavra_escolhida = palavra_escolhida.upper()
        if len(palavra_ja_foi) == 99:
            palavra_ja_foi.clear()
        if palavra_escolhida in palavra_ja_foi:
            continue
        else:
            break
    palavra_ja_foi.append(palavra_escolhida)
    palavras.close()
    return palavra_escolhida

def soma_pontos(jogador):
    jogador['pontos'] = jogador['pontos'] + 1

def letras_palavra(palavra_certa, letras_acertou, letras_da_palavra):
    letras_da_palavra = []
    for letra in palavra_certa:
        if letra in letras_acertou:
            letras_da_palavra.append(letra)
    return letras_da_palavra