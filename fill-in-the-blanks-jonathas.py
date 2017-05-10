#encoding: UTF-8

niveis = ['A ___1___ invencao do ___2___ nao e a minha tecnologia! E a morte! pois atraves dela, o ___3___ sempre dara lugar para o ___4___ - Steve Jobs', \
'Nascemos, vivemos por um ___1___ breve e morremos. Tem sido assim ha ___2___ tempo. A ___3___ nao esta ___4___ este cenario - Steve Jobs', \
'A ___1___ regra de qualquer ___2___ utilizada nos negocios e que a automacao aplicada a uma operacao eficiente ___3___ a eficiencia. A ___4___ e que a automacao aplicada a uma operacao ineficiente ___3___ a ineficiencia - Bill Gates']
# Esta lista armazena as frases de acordo com o nivel selecionado pelo usuario.

respostas = [['maior', 'mundo', 'velho', 'novo'], \
['momento', 'muito', 'tecnologia', 'mudando'], \
['primeira','tecnologia','aumentara','segunda']]
# Esta lista armazena as respostas para serem substituidas na lista niveis.

incognitas = ['___1___', '___2___', '___3___', '___4___']
# Essa lista armazena as incognitas a serem procuradas nas frases da lista niveis.

def game_engine():
    """
        Essa função é responsável por imprimir o menu do jogo e chamar
        a função auxiliar "jogo" que faz todo o mecanismo do jogo rodar.
        Ela recebe o input "nivel" que é solicitado ao usuário para verificar
        o nível de jogo que ele deseja jogar.
    """
    index = 0
    print "#" * 45
    print "Bem vindo ao meu Quiz Challenge \nCriado por: Jonathas Tavares \nOs possíveis níveis são: \nFácil \nMédio \nDifícil\n"
    nivel = raw_input("Por favor, digite o nível desejado: \n")
    nivel = nivel.lower()
    if nivel == "facil":
        index = 0
    if nivel == "medio":
        index = 1
    if nivel == "dificil":
        index = 2
    tentativas = game_level()
    print "#" * 45 + "\n" * 2
    jogo(tentativas, index, nivel)

def jogo(tentativas, index, nivel):
    """
        Recebe os inputs de tentativas e nivel selecionados pelo usuário.
        Ela chama outras funções auxiliares que verificam se o chute do
        usuario esta correto ou não, e se o usuário quer jogar novamente ou não.
    """
    tentativas_min = 0
    tentativas_max = tentativas
    palavra_max = 4
    frase = niveis[int(index)]
    palavra = 1
    frase_nova = niveis[int(index)].split()
    print "A frase do nível " + str(nivel) + " é: \n"
    result = verifica_chute(index, palavra, frase_nova, tentativas, tentativas_max, tentativas_min, palavra_max)
    frase_nova = " ".join(frase_nova)
    print frase_nova + ". \n"
    frase_nova = frase_nova.split()
    restart = resultado(result, tentativas)
    game_restart(restart, result, tentativas)
    return tentativas

def game_level():
    """
        Essa função é chamada no início do jogo para verificar quantas tentativas
        o usuário deseja ter para acertar cada palavra, então armazena esse valor
        na variável "tentativas".
        A variável "tentativas_max" foi criada para impedir que o usuário digite
        um número maior que 10 e então tenha mais tentativas do que deveria ter.
    """
    print "#" * 45
    tentativas = raw_input("Quantas tentativas você quer ter para adivinhar cada palavra? <1 - 10> \n")
    tentativas_max = 10
    while int(tentativas) > tentativas_max:
        tentativas = raw_input("Muitas tentativas, por favor digite um número entre 1 e 10: \n")
    print "Voce tem " + tentativas + " chances por palavra. Boa sorte!"
    return tentativas

def verifica_chute(nivel, palavra, frase_nova, tentativas, tentativas_max, tentativas_min, palavra_max):
    """
        Recebe os inputs "nivel", "palavra", "frase_nova", e "tentativas", para verificar se
        o usuário acertou ou não a palavra que completa a frase.
        Utiliza os loops "FOR" e "IF" para verificar cada palavra da lista "frase_nova" e
        compará-las com as incognitas da lista "incognitas".
        Se o chute do usuário estiver correto, substitui a incógnita na lista "frase_nova"
        pelo chute do usuário, e passa para a próxima incognita.
    """
    while tentativas > tentativas_min and palavra <= palavra_max:
        chute = imprimir_frase(frase_nova, tentativas, palavra)
        acertou_errou(chute, palavra, nivel)
        if chute == respostas[int(nivel)][palavra - 1]:
            index = 0
            for pos in frase_nova:
                if pos in incognitas[palavra - 1]:
                    while index < len(frase_nova):
                        if frase_nova[index] == pos:
                            frase_nova[index] = chute
                        else:
                            index = index + 1
            palavra = int(palavra) + 1
            tentativas = tentativas_max
        else:
            tentativas = int(tentativas) - 1
    return tentativas

def imprimir_frase(frase_nova, tentativas, palavra):
    """
        Recebe os inputs "frase_nova", "tentativas", e "palavra" para controlar
        o fluxo de impressão da frase de acordo com o acerto do usuário.
        Também recebe o input "chute" solicitado ao usuário e o retorna para a
        função "verifica_chute", para que seja verificado se o usuário acertou ou não a palavra.
    """
    frase_nova = " ".join(frase_nova)
    print frase_nova + ". \n"
    frase_nova = frase_nova.split()
    print "Você tem " +str(tentativas) + " tentativas para adivinhar a palavra de número " + str(palavra) + ", boa sorte! \n\nQual palavra você acha que completa a posição de número " + str(palavra)
    chute = raw_input()
    print
    return chute

def acertou_errou(chute, palavra, nivel):
    """
        Recebe os inputs "chute", "palavra", e "nivel" para verificar se o usuário
        acertou ou errou a resposta, e imprimi as frases de acerto ou erro de acordo
        com a resposta do usuário.
    """
    if chute == respostas[int(nivel)][palavra - 1]:
        print "Parabéns, você acertou! \nA palavra da posição " + str(palavra) + " era: " + chute +". \n"
    else:
        print "Não foi dessa vez! \nA palavra que você digitou estava errada, por favor, tente novamente. \n"

def resultado(tentativas, tentativas_max):
    """
        Recebe o input do numero de tentativas restantes após o término da função "jogo",
        e também o input do número de tentativas que o usuário escolheu ter para cada palavra.
        Se ambos forem iguais, significa que o usuário venceu o jogo, descobrindo a última
        incógnita e completando a frase.
        Essa função funciona pois no fim da função "jogo", o número de tentativas é preenchido
        de acordo com o acerto ou erro do usuário.
        É solicitado ao usuário o input da variável "jogar", e a retorna para que seja
        utilizado na função "game_restart".
    """
    if tentativas == tentativas_max:
        jogar = raw_input("Parabéns, você venceu! \nVocê quer jogar novamente? \n0 - Sim \n1 - Não \n")
    else:
        jogar = raw_input("Infelizmente suas tentativas acabaram... \nDesejo mais sorte da próxima vez. \nVocê quer jogar novamente? \nSim \nNão \n")
    if jogar == "Sim" or jogar == "sim":
        jogar = True
        return jogar
    if jogar == "Nao" or jogar == "nao":
        jogar = False
        return jogar

def game_restart(jogar, result, tentativas):
    """
        Recebe o input do usuario que decide se ele quer ou não jogar novamente.
        Chama novamente a função principal baseado na decisão do usuário.
    """
    if jogar == True:
        print "\n" * 100
        print game_engine()
    if jogar == False:
        return jogar

print game_engine()
