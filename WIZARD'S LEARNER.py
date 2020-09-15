# WIZARD'S LEARNER
# Turma 01H - 2019
# Ana Paula Castro - 31927017
# Beatriz Bertan - 31955312
# João Victor Gonçalves - 31913105
# Marcela Sousa - 31958443

import time
import math
import sys

zoo = []


print("WIZARD'S LEARNER \n")

print("Este jogo foi inspirado na saga ”O Hobbit” de J. R. R. Tolkien.\n")

print("-------------------------------------------------------------\n")



def nome():
    name = str(input("Digite seu nome para começar:"))
    return name



def inicio(name):
    print(".\n")
    time.sleep(0.5)
    print(".\n")
    time.sleep(0.5)
    print(".\n")
    time.sleep(0.5)
    print("Mago diz: Olá, meu jovem aprendiz! Meu nome é Jorge.\n")
    time.sleep(2)
    print("Jorge, o Mago diz: Qual é o seu nome?\n")
    time.sleep(2)
    print("Você diz: Meu nome é", name ,". \n")
    time.sleep(2)
    print("Jorge, o Mago diz: Seja bem-vindo ao jogo Wizard's Learner, eu estive esperando por você,", name, "! \n")
    time.sleep(2)
    print("Jorge, o Mago diz: Há alguns anos, o reino Mantara sofreu um terrível ataque de um dragão chamado Smaug e, desde então, nínguem foi capaz de morar lá.\n")
    time.sleep(2)
    print("Jorge, o Mago diz: Derrotando o dragão, você se torna um feiticeiro completo!\n")
    time.sleep(2)
    print("Jorge, o Mago diz: Você está disposto a me ajudar?\n")
    disp = input(str("sim/não:\n"))
    if disp == "sim":
        print("Jorge, o Mago diz: Ótimo! Sabia que podia contar com você. Agora, vou te explicar como derrotar o dragão!\n")
        time.sleep(2)
        print("Jorge, o Mago diz: Infelizmente, eu temo em te dizer que derrotá-lo não será tão fácil!\n")
        time.sleep(2)
        print("Jorge, o Mago diz: Desde que ele se apossou do reino, ele habita o castelo no topo da montanha.\n")
        time.sleep(2)
        print('''Jorge, o Mago diz: Para chegar lá, é preciso seguir o caminho pela Floresta-Sem-Fim, que leva diretamente para a Montanha Solitária.
Ao chegar lá, é necessário seguir a trilha da direita.\n''')
        time.sleep(2)
        print("Jorge, o Mago diz: Mas preste atenção! Não vá, de jeito nenhum, pela trilha da esquerda, pois ela é enfeitiçada. Caso contrário, um terrível destino cairá sobre você.\n")
        time.sleep(2)
        print('''Jorge, o Mago diz: Agora, eu não sei te explicar o motivo e nem o por quê, mas Smaug odeia matemática. Ele realmente odeia!
Ouso dizer que esse é o maior ponto fraco desse monstro.\n''')
        time.sleep(2)
        print("Jorge, o Mago diz: É por isso que você deve usar a lógica matemática, ao invés da força, se quiser derrotar esse dragão.\n\n")
        time.sleep(2)
        print("-------------------------------------------------------------\n\n")
        time.sleep(3)
        print("Aqui vão algumas regras do jogo: \n")
        time.sleep(2)
        print("Esse jogo é dividido em três níveis, cada um com 5 perguntas, todos eles contendo algum problema matemático.\n")
        time.sleep(2)
        print("Cada questão vale 2 pontos, então pense com cuidado ao responder!\n")
        time.sleep(2)
        print("A dificuldade do jogo aumenta a cada nível, mas é necessário completá-lo.\n\n")
        time.sleep(2)
        print("Ao final do jogo, receba o seu feedback!\n")
        time.sleep(2)
        print("-------------------------------------------------------------\n\n")
        
    else:
        print("Jorge, o Mago diz: Certo, quem sabe o próximo aprendiz seja menos tolo.\n")
        time.sleep(2)
        print("Você desistiu do jogo... Encerrando o jogo.")
        sys.exit()

        
def regras():
    rule = str(input("Deseja ver as regras novamente? (sim/não) \n"))
    while rule == "sim":
        print("Aqui vão algumas regras do jogo: \n")
        time.sleep(2)
        print("Esse jogo é dividido em três níveis, cada um com 5 perguntas, todos eles contendo algum problema matemático.\n")
        time.sleep(2)
        print("Cada questão vale 2 pontos, então pense com cuidado ao responder!\n")
        time.sleep(2)
        print("A dificuldade do jogo aumenta a cada nível, mas é necessário completá-lo.\n\n")
        time.sleep(2)
        print("Ao final do jogo, receba o seu feedback!\n")
        time.sleep(2)
        rule = str(input("Deseja ver as regras novamente? (sim/não) \n"))
        

 
# Fase 1
def msgFase1(name):
    time.sleep(1)
    print("-------------------------------------------------------------\n\n")
    time.sleep(2)
    print('''Após uma longa explicação daquele mago chato, você, o nosso herói, finalmente estava pronto para iniciar sua aventura. Com sua coragem e determinação,
você agarrou sua bolsa e saiu pela porta, ansioso para conquistar seu objetivo: tornar-se um mago completo.\n''')
    time.sleep(2)
    print('''Depois de andar por um bom tempo, você finalmente chegou à Floresta-Sem-Fim, e olhou, receoso, para ela. A floresta não recebeu o nome de “sem-fim” à toa,
pois suas árvores eram altas o suficiente para confundir quem se atrevesse a adentrá-la.\n ''')
    time.sleep(2)
    print("Mas você, meu jovem, é destemido: você chutou o medo para longe e entrou naquela florestinha mixuruca.\n ")
    time.sleep(2)
    print("Após enfrentar diversos vilões, se assustar com morcegos e andar por um bom tempo no escuro, você encontrou uma clareira.\n")
    time.sleep(2)
    print("No meio da clareira estava localizada uma mesa com velas, repleta de alimentos que pareciam apetitosos. Seu estômago roncou, você não comia há um bom tempo.\n")
    time.sleep(2)
    print("Quem seria idiota o suficiente de abandonar esse banquete aqui?”, você pensou.\n")
    time.sleep(2)
    print("Ora, não havia ninguém lá, então provavelmente não vai ter problemas se você parar um pouco para comer… tinha pudim! Você amava pudim!\n")
    time.sleep(2)
    print("Sem nem se importar com boas maneiras, você atacou os pratos, feliz por finalmente estar enchendo sua barriga.\n")
    time.sleep(2)
    print("Até que você escuta um grito que te faz gelar:\n")
    time.sleep(2)
    print("“O QUE VOCÊ ESTÁ FAZENDO?”\n")
    time.sleep(2)
    print("Ferrou.\n\n")
    time.sleep(2)
    print("FERROU!\n")
    time.sleep(3)
    print("Tremendo, você se vira, mas logo solta um suspiro de alívio. Era apenas um duende. Um duende muito fofo!!\n")
    time.sleep(2)
    print(name,", o Aprendiz diz: Olá meu amiguinho.\n")
    time.sleep(2)
    print("Duende diz: Qual é o seu nome? Preciso saber para marcá-lo na minha lista!\n")
    time.sleep(2)
    print(name, ", o Aprendiz diz: Meu nome é", name, "\n")
    time.sleep(2)
    print("Duende diz: Como você tem coragem de comer o jantar do grande Robertão?\n")
    time.sleep(2)
    print(name,", o Aprendiz diz: Robertão?\n")
    time.sleep(2)
    print('''Robertão, o Duende diz: SIM! Eu sou o Robertão! Ora, era só o que me faltava! Olhe para você, está me devendo minha comida!
Responda às minhas perguntas e o deixarei ir embora!\n''')
    time.sleep(2)
    print("Robertão, o Duende diz: Se você não for bem, terá consequências no futuro, então fique esperto!\n\n")
    time.sleep(4)


    
# Questão 1 
def quest1(name):
    print("Questão 1\n")
    print("Robertão, o Duende diz: Observe a lista e responda:\n")
    zoo = ["Leão", "Jacaré", "Girafa", "Elefante", "Macaco"]
    print (zoo)
    q1 = input(str("Qual animal ocupa a 3º posição?\n"))
    if q1 == "Girafa":
        print("Robertão, o Duende diz: Macacos me mordam! Você acertou a questão,", name, "!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 2
    else:
        print("Robertão, o Duende diz: Ha ha! Você errou, a resposta correta é Girafa!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 0



# Questão 2
def quest2(name):
    print("Questão 2\n")
    print("Robertão, o Duende diz: Some os números à seguir:\n")
    q2 = int(input("51 + 24 + 32 =\n"))
    if q2 == 107:
        print("Robertão, o Duende diz: Não é possível! Você acertou a questão,", name, "!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 2
    else:
        print("Robertão, o Duende diz: Ha ha! Você errou, a resposta correta é 107!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 0


    
# Questão 3   
def quest3(name):
    print("Questão 3\n")
    q3 = int(input('''Para completar uma página do álbum é preciso 15 figurinhas. Rafaela já tem 8 figurinhas, coladas na mesma página.
Quantas figurinhas ela ainda precisa para completar essa página?\n'''))
    if q3 == 7:
        print("Robertão, o Duende diz: Não é possível! Você acertou a questão,", name, "!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 2
    else:
        print("Robertão, o Duende diz: Ha ha! Você errou, a resposta correta é 7!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 0



# Questão 4
def quest4(name):
    print("Questão 4\n")
    q4 = int(input("Rafaela paga 2 real em cada pacote de figurinha. Ela comprou 12 pacotes. Quantos reais ela gastou?\n"))
    if q4 == 24:
        print("Robertão, o Duende diz: Você acertou a questão, parece até que está roubando!", name, "!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 2
    else:
        print("Robertão, o Duende diz: Ha ha! Você errou, a resposta correta é 24!\n")
        time.sleep(2)
        print("Robertão, o Duende diz: Próxima questão!\n\n")
        time.sleep(2)
        return 0



# Questão 5
def quest5(name):
    print("Questão 5 - ÚLTIMA QUESTÃO DA FASE 1\n")
    q5 = int(input('''Lorena possui 40 reais e precisa ir ao mercado comprar leite, ovos e açúcar, no caixa, o valor da compra foi de 25 reais.
Com quantos reais Lorena ficou após a compra?\n'''))
    if q5 == 15:
        print("Robertão, o Duende diz: Você acertou a questão, impossível!", name, "!\n\n")
        time.sleep(2)
        return 2
    else:
        print("Robertão, o Duende diz: Ha ha! Você errou, a resposta correta é 15!\n")
        time.sleep(3)
        return 0

    

# Fase 2
def msgFase2():
    print("Robertão, o Duende diz: Parabéns, parece que você não é tão burro quanto eu pensei. Vou deixar você ir embora, dessa vez.\n")
    time.sleep(3)
    print('''Feliz, você comemorou, mas logo lembrou-se que ainda estava perdido na floresta. Então você pede ajuda de Robertão, e este resmunga um ‘moleque folgado, não basta comer minha comida’,
porém resolve te ajudar. Que duende gentil!\n''')
    time.sleep(3)
    print("-------------------------------------------------------------\n\n")
    time.sleep(3)
    print("Finalmente, depois de andarem por um atalho, Robertão para e aponta à sua frente.\n")
    time.sleep(3)
    print("Aqui estamos, garoto. Essa é a Montanha Solitária. Imagino que você não tenha dificuldade em vê-la.\n")
    time.sleep(3)
    print("A menos que você fosse o tipo mais cego de ciclope, era impossível não enxergá-la.\n")
    print('''As terras abriam-se amplas ao seu redor, cheias da água do rio que subdividia-se em centenas de cursos tortuosos, ou parava em pântanos ou lagos pontilhados de ilhotas
por todos os lados; mas, mesmo assim, uma forte correnteza avançava pelo meio. E, na distância, a cabeça escura, enfiada numa nuvem rasgada, assomava a Montanha!\n''')
    time.sleep(3)
    print('''Não se viam seus vizinhos mais próximos ao nordeste nem o terreno acidentado que ligava a eles. Sozinha se erguia, olhando para a floresta através dos pântanos.
A montanha Solitária! Você viera de longe e enfrentara muitas aventuras para vê-la, e agora não gostava nem um pouco de sua aparência.\n''')
    time.sleep(3)
    print("Mas você não tinha tempo para ter medo, então avançou em direção à ela.\n")
    time.sleep(3)
    print("Infelizmente para você, a entrada da montanha era guardada por ogros terríveis.\n")
    time.sleep(3)
    print("Um deles chamava-se Jeniffer, a Ogra, mas ela não parecia tão má quanto o resto de seu bando.\n")
    time.sleep(3)
    print("Até que você notou no tom de voz da ogra uma gentileza fingida, e percebeu que ela era igual ou pior que os outros.\n")
    time.sleep(3)
    print("Contendo um sorriso sarcástico, ela te explica que você só poderá passar se conseguir responder cinco perguntas.\n")
    time.sleep(3)
    print("Você suspira, mas concorda.\n")
    time.sleep(3)
    print("Por que diabos aquele povo gostava tanto de perguntas??\n\n")

# Questão 6
def quest6():
    print("Questão 6\n")
    print("Utilize a LETRA da resposta correta nesta questão\n")
    q6 = str(input('''Em uma cidade, o número de carros é formado por seis milhares, mais sete centenas, mais oito dezenas e mais seis unidades que são iguais a:
a) 6786 b) 6876 c) 7686 d) 8766\n'''))
    if q6 == "a":
        print("Jeniffer, a Ogra diz: Isso não pode ter acontecido! Você acertou, vamos ver até quando você continuará assim!\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 2
    else:
        print("Jeniffer, a Ogra ri e diz: Ai! Que penaa, parece que você erro-u! A resposta correta era 'a) 6786' HiHi.\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 0

# Questão 7
def quest7():
    print("Questão 7\n")
    q7 = int(input("Qual é o valor de x na equação: x - 59 = 203\n"))
    if q7 == 262:
        print("Jeniffer, a Ogra diz: Isso não pode ter acontecido! Você acertou, vamos ver até quando você continuará assim!\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 2
    else:
        print("Jeniffer, a Ogra ri e diz: Ai! Que penaa, parece que você erro-u! A resposta correta era '262' HiHi.\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 0

# Questão 8
def quest8():
    print("Questão 8\n")
    q8 = int(input('''Uma papelaria, em janeiro, tendo em vista o início das aulas, comprou uma remessa grande de cadernos. Ao receber a encomenda,
a papelaria recebeu 2 caixas de 1000 cadernos, 3 caixas de 100 cadernos, 2 pacotes de 10 cadernos. Quantos cadernos a papelaria comprou?\n'''))
    if q8 == 2320:
        print("Jeniffer, a Ogra diz: Como??!? Você acertou, vamos ver até quando você continuará assim!\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 2
    else:
        print("Jeniffer, a Ogra ri e diz: Ai! Que penaa, parece que você erro-u! A resposta correta era '2320' HiHi.\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 0

# Questão 9
def quest9():
    print("Questão 9\n")
    q9 = int(input("A soma de dois números é igual a 5129. Se um número é 2375, qual é o outro?\n"))
    if q9 == 2754:
        print("Jeniffer, a Ogra diz: Você está fazendo um jogo comigo, garotàáh? Você acertou, vamos ver até quando você continuará assim!\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 2
    else:
        print("Jeniffer, a Ogra ri e diz: Ai! Que penaa, parece que você erro-u! A resposta correta era '2754' HiHi.\n")
        time.sleep(2)
        print("Jeniffer, a Ogra diz: Próxima questão! \n\n")
        time.sleep(2)
        return 0

# Questão 10
def quest10():
    print("Questão 10 - ÚLTIMA QUESTÃO DA FASE 2\n")
    print("Utilize a LETRA da resposta correta nesta questão\n")
    q10 = str(input('''Setecentos e cinqüenta mil computadores serão distribuídos igualmente entre as escolas do Estado do Paraná, pelo governo estadual.
Cada escola vai receber 50 computadores. Quantas escolas receberão computadores? a) 15 b) 150 c) 1500 d) 15000\n'''))
    if q10 == "d":
        print("Jeniffer, a Ogra diz: Não é possível!! Você acertou, vamos ver até quando você continuará assim!\n")
        time.sleep(2)
        return 2
    else:
        print("Jeniffer, a Ogra ri e diz: Ai! Que penaa, parece que você erro-u! A resposta correta era 'd) 15000' HiHi.\n")
        time.sleep(2)
        return 0


# Caminhos
def msgCaminhos(name):
    
    print ('Jeniffer, a Ogra diz: Você conseguiu acertar todas, parabéns...\n')
    time.sleep(2)
    print (name,", o Aprendiz diz: Seu sarcásmo é irritante.\n")
    time.sleep(2)
    print ("Jeniffer, a Ogra diz: Okay, estressadinho. Eu só ia te desejar boa sorte... você vai precisar.")
    time.sleep(2)
    print ("Dizendo isso, a ogra riu em deboche e voltou para o seus irmãos, deixando um certo jovem aprendiz muito confuso para trás.")
    time.sleep(2)
    print("-------------------------------------------------------------\n\n")
    time.sleep(2)
    print ('Você já não aguentava mais andar e responder perguntas de matemática: sua cabeça doía e seus pés estavam quase falhando.\n')
    time.sleep(2)
    print ('Você se sentou para descansar e comer um pouco do que sobrou, mas notou a presença de uma bifurcação próxima ao seu local de repouso.\n')
    time.sleep(2)
    print ('A trilha da montanha se dividia em dois caminhos, direita e esquerda, sem te dar nenhuma indicação de qual direção seguir.\n')
    time.sleep(2)
    print ('Temeroso, você sentia que se tratava de uma armadilha e, dependendo da sua escolha, um destino terrível cairia sobre você… \n')
    time.sleep(2)
    print('Um terrível destino cairia sobre você...?\n')
    time.sleep(2)
    print ('Era isso! O mago havia te alertado sobre esses caminhos!\n')
    time.sleep(2)
    print ('Mas você estava tão cansado e com tanto sono para lembrar qual era o certo … será que você conseguiria?\n')

# Escolhendo o Caminho
def escolherCaminhos():
    escolha = input ('Por qual caminho você vai seguir?\n')
    if escolha == 'direita':
        print ('Sim, era a direita! Você quase podia ouvir a voz do Mago Jorge te alertando!\n')
        time.sleep(1.5)
        return escolha
    else:
        print ('Sim, era a esquerda! Você quase podia ouvir a voz do Mago Jorge te alertando!\n')
        time.sleep(2)
        print ('Sem querer perder tempo, você se levanta preparado para continuar a aventura.\n')
        time.sleep(2)
        print ('Mesmo sem descansar, você se sentia revigorado e disposto a derrotar o dragão, mas... \n')
        time.sleep(4)
        print ('OH, NÃO!!!!!\n')
        time.sleep(3)
        print ('Você não reparou, mas a trilha para a esquerda era íngreme e extremamente escorregadia!\n')
        time.sleep(3)
        print('Sem conseguir manter o controle de seu corpo, você tropeça e começa a rolar descontroladamente!!!\n')
        time.sleep(3)
        print('Para piorar, o fim da ladeira dava de cara com um penhasco, então você não pôde evitar e acabou caindo :O \n')
        time.sleep(3)
        print('Perece que você errou o caminho :/ \n')
        time.sleep(3)
        print ('Você morreu e não foi capaz de se tornar um feiticeiro completo, mas boa sorte na próxima vez. \n')
        sys.exit(0)

# Fase 3
def msgFase3():
    print ('Vendo que nada de ruim te ocorreu durante o seu caminho pela direita, você finalmente respirou aliviado.\n')
    time.sleep(2)
    print ('O cansaço já havia abandonado seu corpo após um bom descanso, e você se sentia revigorado para continuar a sua aventura.\n')
    time.sleep(2)
    print ('''Mas já não era mais necessário ir à lugar algum, pois diante de você encontrava-se o Castelo de Thorin. Entretanto, você observou
a construção consternado: havia algo de diferente no ar.\n''')
    time.sleep(2)
    print ('O castelo, que um dia fora cheio de vida e símbolo de riqueza do reino, agora mostrava-se completamente vazio e em ruínas.\n')
    time.sleep(2)
    print ('Isso é ridículo!, você pensou. Está na hora de alguém por Smaug em seu lugar... e esse alguém sou eu.\n')
    time.sleep(2)
    print ('Uau, meu caro jogador! Você é tão corajoso e valente, até me arrepiei!\n')
    time.sleep(2)
    print ('Eu queria ser capaz de por uma música épica em sua homenagem, mas isso está fora do meu alcance :( \n')
    time.sleep(2)
    print ('Mas chega de enrolação!! Vamos voltar para a nossa história:\n')
    time.sleep(2)
    print ('Finalmente você havia achado a sua determinação para encarar aquele dragão. \n')
    time.sleep(2)
    print ('Estava na hora de se tornar um feiticeiro completo.\n')
    time.sleep(2)
    print("-------------------------------------------------------------\n\n")
    time.sleep(2)
    print ('Demorou um tempo até você conseguir achar uma entrada para o castelo, pois Smaug havia se isolado completamente dentro dele. \n')
    time.sleep(2)
    print ('Mas após uma longa procura, você foi encontrar a brecha para que pudesse entrar. \n')
    time.sleep(2)
    print ('''E então, lá estava ele, um enorme dragão vermelho-dourado, ferrado no sono, um ruído palpitante vinha de suas narinas e mandíbulas,
junto com tufos de fumaça, mas, no sono, o fogo estava arrefecido. Embaixo dele, sob os membros e a grande cauda enrolada, e em torno dele, por
todos os lados, espalhando-se pelo chão invisível, jaziam incontáveis pilhas de objetos preciosos, ouro trabalhado e ouro bruto, pedras e jóias,
e prata, que a luz rubra tingia de vermelho. \n''')
    time.sleep(4)
    print ('''Era Smaug, o terrível, as asas recolhidas como as de um morcego incomensurável, virado parcialmente para um lado, de modo que você
conseguia ver a enorme barriga cravejada em ouro.\n''')
    time.sleep(2)
    print ('Irritado, você acorda o dragão, praparado para derrotá-lo. \n')
    time.sleep(2)
    print ('Smaug estava, obviamente, enfurecido com sua intromissão, mas você não ligava mais.\n')
    time.sleep(2)
    print ('Você estava preparado para as questões de matemática que estavam por vir.\n')


# Questão 11
def quest11():
    print ('Questão 11 \n')
    print ('Smaug, o terrível diz: Observe as sequências a seguir: \n')
    a = [1,2,3,5,7,9,11,13]
    print ('a)', a)
    b = [3,5,7,9,11,13,19,21]
    print ('b)', b)
    c = [0,1,2,7,11,13,19,23]
    print ('c)', c)
    d = [3,5,7,11,13,17,19,23]
    print ('d)', d)
    q4 = input (str ('Qual das sequências é formada apenas por números primos?\n'))
    if q4 == 'd':
        print ('Smaug, o Terrível diz: Maldição, você acertou!')
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!')
        time.sleep(2)
        return 2
    else:
        print ("Smaug, o Terrível diz: HÁ HÁ HÁ, eu sabia que você ia errar! A resposta correta era 'd'\n")
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!\n')
        time.sleep(2)
        return 0

# Questão 12
def quest12():
    print("Questão 12 \n")
    q12 = str(input('''Smaug, o Terrível diz: Claudina saiu com uma amiga e resolveram comer uma pizza, que foi dividida em oito pedaços. Cada uma comeu dois pedaços.
A porcentagem de pizza comida por cada uma foi de: a) 25% b) 50% c) 60% d) 75% \n'''))
    if q12 == "b":
        print ('Smaug, o Terrível diz: Maldição, você acertou! Como isso foi possível?')
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!')
        time.sleep(2)
        return 2
    else:
        print ("Smaug, o Terrível diz: HÁ HÁ HÁ, era óbvio que você ia errar! A resposta correta era 'b' ")
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!')
        time.sleep(2)
        return 0

# Questão 13
def quest13():
    print("Questão 13 \n")
    print("Utilize sim/não para responder esta questão.\n")
    q13 = str(input('''Júlio tem R$ 2129,00, Márcia tem R$ 3175,00, André tem R$ 3279,00 e Rita tem R$ 4325,00.
Juntando os valores das meninas e juntando também os valores dos outros dois, obtém-se a mesma quantia? sim/não \n'''))
    if q13 == "não":
        print ('Smaug, o Terrível diz: Maldição, você acertou! Como isso foi possível?\n')
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!\n')
        time.sleep(2)
        return 2
    else:
        print ("Smaug, o Terrível diz: HÁ HÁ HÁ, você não garantiu seu acerto! A resposta correta era 'não'\n")
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!\n')
        time.sleep(2)
        return 0

# Questão 14
def quest14():
    print("Questão 14 \n")
    q14 = int(input('''Em uma cidade, há duzentos e sete mil, quinhentos e noventa e oito homens e cento e noventa e oito mil,
seiscentas e dezoito mulheres. Escreva o numeral que representa a quantidade total de habitantes.\n'''))
    if q14 == 406216:
        print ('Smaug, o Terrível diz: Maldição, você acertou! Você já está me irritando!\n')
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!\n')
        time.sleep(2)
        return 2
    else:
        print ("Smaug, o Terrível diz: HÁ HÁ HÁ, você não garantiu seu acerto! A resposta correta era '406216'\n")
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!\n')
        time.sleep(2)
        return 0

# Questão 15
def quest15():
    print("Questão 15 - ÚLTIMA QUESTÃO DO JOGO, PRESTE MUITA ATENÇÃO! \n")
    q15 = int(input('''A população da cidade de São Paulo é de 10 886 518 habitantes.
A população de Maceió é de 896 965 habitantes e a de Aracaju é de 520 303 habitantes.
Quantas pessoas vivem a mais em São Paulo do que nas outras duas capitais juntas?\n'''))
    if q15 == 9469250:
        print ('Smaug, o Terrível diz: Maldição, você acertou! Já chega! Perdi minha paciência com você!\n')
        time.sleep(2)
        print ('Smaug, o Terrível diz: Próxima questão!\n')
        time.sleep(2)
        return 2
    else:
        print ("Smaug, o Terrível diz: HÁ HÁ HÁ, você não garantiu seu acerto! A resposta correta era '9469250'! Perdi minha paciência com você!\n")
        time.sleep(2)
        return 0

def msgFinal():
    print('Você nunca havia visto um dragão tão furioso em sua vida inteira. Ou melhor, você nunca nem mesmo tinha visto um dragão.\n')
    time.sleep(2)
    print('E, vendo Smaug praticamente cuspir fogo pelo nariz, preferia que sua vida tivesse continuado dessa forma.\n')
    time.sleep(2)
    print('O dragão gritou outra vez, mais forte do que antes, e toda a estrutura do castelo chacoalhou. Obviamente, você já não se sentia mais tão corajoso quanto antes.\n')
    time.sleep(2)
    print('Smaug certamente havia sido derrotado, mas ele não parecia entender isso, pois já estava prestes a te atacar. E o que você poderia fazer?\n')
    time.sleep(2)
    print('Você era apenas um simples jovem aprendiz de feiticeiro, então seus poderes não eram fortes o suficiente para lidar com um monstro gigante.\n')
    time.sleep(2)
    print('Entretanto, quando já não havia mais saída e você se encontrava encurralado na parede, uma estranha luz começou a brilhar no anel em que você usava.\n')
    time.sleep(2)
    print('Mas não era qualquer anel, era o seu anel de aprendiz de feiticeiro! E o anel de um aprendiz brilhando só poderia significar uma coisa:\n')
    time.sleep(2)
    print('Você finalmente conseguiu! Você se tornou um feiticeiro completo!\n')
    time.sleep(2)
    print('Você sorriu, mesmo com Smaug bufando em seu cangote. Sua coragem fora revigorada, pois dragãozinho nenhum seria páreo para você.\n')
    time.sleep(2)
    print('Então, você conjurou um feitiço e lançou no terrível Smaug, que acabou sendo pego desprevenido e foi empurrado para o outro lado do enorme salão.\n')
    time.sleep(2)
    print('Ele tentou revidar, mas você conseguiu desviar e lançar um outro feitiço, poderoso o suficiente para expulsar Smaug do castelo.\n')
    time.sleep(2)
    print('Em fim o dragão fora derrotado e, agora, você poderia voltar para casa. Não como um jovem aprendiz, mas como um feiticeiro completo.\n')
    time.sleep(2)
    print("-------------------------------------------------------------\n\n")


def feedback(contador):
    print("Sua pontuação final foi", contador)
    if contador == 30:
        print("Incrível! Você fez a pontuação máxima! Com certeza o seu 10 está garantido na próxima prova de matemática! Parabéns!\n")
    elif contador <= 28 and contador >= 20 :
        print("Parabéns, você teve uma pontuação excelente!\n")
    elif contador >=16 and contador < 20:
        print("Parabéns, você teve uma boa pontuação!\n")
    else:
        print("Parece que alguém precisa estudar mais matemática, em! Jogue novamente para treinar um pouco mais :)")

def final():
    time.sleep(4)
    print('Jorge, o Mago diz: Parabéns, você terminou o jogo!')
    time.sleep(2)
    print('Jorge, o Mago diz: Espero que tenha gostado e melhorado seu aprendizado em matemática! Até mais, Mago dos Magos!')

def main():
    name = nome()
    inicio(name)
    regras()
    msgFase1(name)
    contador = quest1(name)
    contador = contador + quest2(name)
    contador = contador + quest3(name)
    contador = contador + quest4(name)
    contador = contador + quest5(name)
    print("Sua pontuação atual é:", contador)
    msgFase2()
    contador = contador + quest6()
    contador = contador + quest7()
    contador = contador + quest8()
    contador = contador + quest9()
    contador = contador + quest10()
    print("Sua pontuação atual é:", contador)
    msgCaminhos(name)
    escolherCaminhos()
    msgFase3()
    contador = contador + quest11()
    contador = contador + quest12()
    contador = contador + quest13()
    contador = contador + quest14()
    contador = contador + quest15()
    print("Sua pontuação atual é:", contador)
    msgFinal()
    feedback(contador)

main()
    
    
