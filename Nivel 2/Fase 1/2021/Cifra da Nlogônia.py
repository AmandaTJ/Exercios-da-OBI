p = str(input()) #palavra

def alfabeto(p):#define o alfabeto utilizado
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    vogais = "aeiou"#define as vogais
    resposta = ""#define a resposta como uma string vazia

    for letra in p:

        if letra in vogais:# Se for vogal, não altera

            resposta += letra

        else: # Se for consoante, ai fode com o codigo inteiro
            resposta += letra

            vmais = "a"#pega a vogal mais próxima da consoante

            for vogal in vogais:
                if abs(ord(letra) - ord(vogal)) < abs(ord(letra) - ord(vmais)):
                    vmais = vogal

            resposta += vmais # adiciona na resposta a vogal mais próxima

            proxima = letra # encontra a próxima consoante
            for l in alfabeto:
                if ord(l) > ord(letra) and l not in vogais:
                    proxima = l
                    break
            resposta += proxima
    return resposta
print(alfabeto(p))