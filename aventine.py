import t_av
from f_av import rot, vida_atua, tripulação, pessoal, vida
import sys
import time

## Intro ##
titleStrings = r"""
                     Star Trek: Aventine
        """
print(titleStrings)
rot(t_av.prim)
time.sleep(0.5)
nome = input("Qual seu nome Primeiro Oficial? ")
nome_rank = f"Comandante {nome}"
time.sleep(0.5)
inic_jog = (f"Você começa com 100% de escudo da nave, {nome_rank}!\n")
rot(inic_jog)

## ínicio do jogo ##
time.sleep(0.5)
quer_jogar = input("Você quer continuar a jogar?(S/N) ").lower()
while quer_jogar not in ['s', 'n']:
    v_inv = "Escolha uma opção válida!\n"
    rot(v_inv)
    quer_jogar = input("Você quer continuar a jogar?(S/N) ").lower()
if quer_jogar == "s":
    ## primeira fase ##
    rot(t_av.pri1)
    text_1 = f'Capitã Dax: "Data estelar - 2381.78, diário da Capitã. Passaram-se dois meses desde da transfêrencia do Primeiro Oficial Bowers para a USS Quito. A Federação encaminhou um novo oficial, {nome_rank}, que serviu por 6 anos na nave Bozeman como chefe de segurança, por dois anos fez parte de equipes de resgaste em campos de concentração Cardassiano e na Academia foi um cadete graduado com honras. A transfêrencia, no entanto, veio sob protesto, temos oficiais que conhecem melhor a nave, as necessidades de sua tripulação e a chegada do novo Número Um vem acompanhada de tempos que não permitem termos o luxo de alguém na tripulação ainda se adaptando a um novo comando.\nNessa semana, recebi uma mensagem Prioridade Um da presidente Nanietta Bacco ordenando que a Aventine terminasse as investigações sobre a NX-02 Columbia que desapareceu durante a guerra Federação-Romulana na data estelar 2156.45 e foi encontrada recentemente pela USS Defiant nas fronteiras com a fenda espacial bajoriana, no Quadrante Gamma. Logo chegaremos a localização da nave e temos um curto prazo para resolvermos esse mistério. Será uma oportunidade para avaliar as habilidades do novo Imediato e espero que não tenhamos que pagar caro pela sua inexperiência!"\n'
    rot(text_1)
    rot(t_av.pri2)
    rot(t_av.pri3)
    text_2 = f"Dax: {nome}, inicie as varreduras no planeta, verifique se tem alguma nave próximo a nossa localização. Já estou a caminho da Ponte!\n"
    rot(text_2)

    ans = input(
        "Comandante Gruhn: Senhor, devemos acionar os sensores de curto alcance para localizar possíveis naves ou fazer uma varredura por sinais de vida no planeta (1/2)? ")
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(
            "Comandante Gruhn: Senhor, devemos acionar os sensores de curto alcance para localizar possíveis naves ou fazer uma varredura por sinais de vida no planeta (1/2)? ")
    print("🖖")
    if ans == "1":
        text_3 = f"{nome_rank}: Gaff, temos algum resultado dos sensores?\n"
        rot(text_3)
        rot(t_av.pri4)
        rot(t_av.pri5)
        rot(t_av.pri6)

    elif ans == "2":
        text_4 = f"{nome_rank}: Gaff, inicie varreduras no planeta! Gruhn, verifique se temos qualquer sinalização de atividades na região com a Federação.\n"
        rot(text_4)
        rot(t_av.pri7)
        text_5 = f"{nome_rank}: Entendido... E recebemos alguma resposta da Federação?\n"
        rot(text_5)
        rot(t_av.pri8)
        rot(t_av.pri9)

    ans = input(
        "Tenente Tharp: Devo iniciar protocolo de interceptação a nave klingon ou autorizar o lançamento da nave auxiliar USS Coqueiros ao planeta (1/2)? \n").lower()
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(
            "Tenente Tharp: Devo iniciar protocolo de interceptação a nave klingon ou autorizar o lançamento da nave auxiliar USS Coqueiros ao planeta (1/2)? ").lower()
    print("🖖")
    if ans == "1":
        text_6 = f"{nome_rank}: Vamos interceptar essa nave! Ponte para Enfermaria - Prepare a enfermaria para possíveis baixas, estamos iniciando uma operação de resgate a uma nave klingon! - Tharp, inicie protocolo Beta 5, mantenha a nave a 1 km de distância do alcance de armas deles.\n"
        rot(text_6)
        rot(t_av.pri10)
        rot(t_av.pri11)
        rot(t_av.pri12)
        text_7 = f"{nome_rank}: Localizamos uma nave klingon a 150 km de distância de nós! Ainda não conseguimos comunicação e também não temos nenhum relatório apontando missões registradas pela aliança nessa região! A nave apresenta bastante avaria, inclusive nos propulsores... Não conseguimos nenhuma informação da tripulação ou se a nave ainda tem energia para os suportes de vida, então estamos em processo de interceptação para oferecer ajuda!\n"
        rot(text_7)
        rot(t_av.pri13)

    elif ans == "2":
        text_8 = f"{nome_rank}: -Ponte para Convés 3- Estamos autorizando a missão de reconhecimento ao planeta... Cadete Erin ficará responsável por levar a nave em segurança e aguardar a equipe retornar. Aguarde a confirmação da ponte para iniciar o desembarque da USS Coqueiros!\n"
        rot(text_8)
        rot(t_av.pri11)
        text_9 = f"Dax: {nome} qual relatório da missão até agora?\n{nome_rank}: Recebemos informações que o planeta tem altos níveis de contaminação por radiação, impedindo qualquer varredura ou teletransporte. Também localizamos uma nave klingon a 150 km de distância de nós, não conseguimos comunicação e também não temos nenhum relatório apontando missões registradas pela aliança nessa região! A nave apresenta bastante avaria, por isso enviamos os dados da nave ao Império para que mandem alguém para realizar o resgate.\n"
        rot(text_9)
        rot(t_av.pri14)
        rot(t_av.pri15)
        print("🖖")
## segunda fase ##
    ans = input(
        f"Dax: Meu deus, os motores deles estão completamente destruidos. Como essa nave não explodiu ainda?! {nome_rank}, devemos verificar se temos sinais de vida a bordo ou nos aproximar para teletransportar uma equipe de resgate (1/2)?  ")
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(
            f"Dax: Meu deus, os motores deles estão completamente destruidos. Como essa nave não explodiu ainda?! {nome_rank}, você acha que devemos verificar primeiro se temos sinais de vida a bordo ou aproximar a nave para que seja possível teletransportar uma equipe de resgate (1/2)? ")
    if ans == "1":
        an1 = f"{nome_rank}: Oliana, verifique se existe algum sinal de vida ou baixas na nave!\n"
        rot(an1)
        rot(t_av.seg1)
        rot(t_av.seg2)
        rot(t_av.seg3)

    elif ans == "2":
        rot(t_av.seg4)
        rot(t_av.seg5)
        rot(t_av.seg6)
        tripulação(5)
        rot(t_av.seg7)
## terceira fase ##
    ans = input(f"Tenente Lonnoc: Eles ativaram os escudos, senhor! Provavelmente para evitar nossas varreduras... Devemos levantar escudos ou esperar eles acionarem as armas primeiro (1/2)?")
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(f"Tenente Lonnoc: Eles ativaram os escudos, senhor! Provavelmente para evitar nossas varreduras... Devemos levantar escudos ou esperar eles acionarem as armas primeiro (1/2)?")
    print("🖖")
    if ans == "1":
        text_10 = f"{nome_rank}: Levante escudos... Alerta amarelo! Todos para suas estações de batalhas! Tenente Gaff tente novamente contato... Lonnoc me informe caso eles decidam tomar qualquer ação hostil!\n"
        rot(text_10)
        rot(t_av.ter1)
        rot(t_av.ter2)
        rot(t_av.ter3)
        vida['escudo'] = vida['escudo'] - 2
        vida_atua()

    elif ans == "2":
        rot(t_av.ter4)
        vida['escudo'] = vida['escudo'] - 15
        vida_atua()
## quarta fase ##
    text_11 = "Dax: Alerta vermelho! Gruhn procure se existe alguma nebulosa perto que possamos nos esconder... Tenente Lucy, eu preciso que você verifique por quais motivos eles estão nessa região e emita um sinal de ajuda a todas as naves aliadas que estejam perto da nossa localização!\n"
    rot(text_11)
    ans = input(
        f"{nome_rank} - Você decide atirar com fóton torpedos ou pedir para a engenharia recuperar seu escudo em 40% (1/2)? ")
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(
            f"{nome_rank} - Você decide atirar com fóton torpedos ou pedir para a engenharia recuperar seu escudo (1/2)? ")
    print("🖖")
    if ans == "1":
        rot(t_av.quar1)
        vida['escudo'] = vida['escudo'] - 30
        vida_atua()
        rot(t_av.quar2)
    elif ans == "2":
        rot(t_av.quar3)
        rot(t_av.quar4)
        vida['escudo'] = vida['escudo'] - 15
        vida_atua()
## Quinta fase ##
    an2 = f"{nome_rank}: Gruhn temos algum lugar para nos esconder? Descobrimos algo sobre o por quê deles estarem aqui?\n"
    rot(an2)
    rot(t_av.qui1)
    ans = input(f"Dax: O que você acha, número um? Devemos nos esconder e esperar ou voltar e atacar a nave klingon para força-los a responder nossos chamados (1/2)? ")
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(f"Dax: O que você acha, número um? Devemos nos esconder e esperar ou voltar e atacar a nave klingon para força-los a responder nossos chamados (1/2)? ")
    print("🖖")
    if ans == "1":
        rot(t_av.qui2)
        vida['escudo'] = vida['escudo'] - 15
        vida_atua()

    elif ans == "2":
        an3 = f"{nome_rank}: Lonnoc atire continuamente com os canhões de phaser! Tharp retorne a localização anterior e nos ponha atrás da nave.\n"
        rot(an3)
        rot(t_av.qui3)
        vida['escudo'] = vida['escudo'] - 20
        vida_atua()
## Sexta fase ##
    rot(t_av.sext1)
    rot(t_av.sext12)
    ans = input(f"Dax: Gaff interrompa a transmissão... Número Um, o que você acha das intenções deles? Devemos atender ao pedido e receber os romulanos ou negar e pedir para que possamos sair em segurança desse planeta (1/2)? ")
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(f"Dax: Gaff interrompa a transmissão... Número Um, o que você acha das intenções deles? Devemos atender ao pedido e receber os romulanos ou negar e pedir para que possamos sair em segurança desse planeta (1/2)? ")
    print("🖖")
    if ans == "1":
        rot(t_av.sext2)
        s1 = f"{nome_rank}: Lonnoc, abaixe os escudos e avise ao Chief O'Brien para teletransportar os convidados romulanos!\n"
        rot(s1)
        rot(t_av.sext3)
        vida['escudo'] = vida['escudo'] - 100
        vida_atua()
    elif ans == "2":
        rot(t_av.sext4)
        s2 = f"{nome_rank}: Capitã, a nave romulana está acionando armas!\n"
        rot(s2)
        rot(t_av.sext5)
        vida['escudo'] = vida['escudo'] - 15
        vida_atua()
## sétima fase ##
    ss1 = f"Lonnoc: Comandante... Perdemos energia auxiliar e já estamos quase perdendo o suporte de vida!\n"
    rot(ss1)
    ss2 = f"{nome_rank}: Lucy quais são os dados táticos da nave Klingon?\n"
    rot(ss2)
    rot(t_av.set1)
    ans = input(
        f"Capitã Dax: {nome}, deveriamos nos retirar e esperar a Defiant ou atacar e desabilitar a nave Klingon (1/2)? ")
    while ans not in ['1', '2']:
        v_inv = "Escolha uma opção válida!\n"
        rot(v_inv)
        ans = input(
            f"Capitã Dax: {nome}, deveriamos nos retirar e esperar a Defiant ou atacar e desabilitar a nave Klingon (1/2)? ")
    print("🖖")
    if ans == "1":
        sett1 = f"{nome_rank}: Não temos por quê arriscar a vida de nossos oficias em uma luta sem causa! Capitão Bashir deve já chegar a nossa localização. Vamos tentar sobreviver.\n"
        rot(sett1)
        rot(t_av.set2)
        sett2 = f"{nome_rank}: Tharp nos retire da zona de contato das duas naves inimigas! Se prepare para entrar em orbita paralela com o planeta...\n"
        rot(sett2)
        rot(t_av.set3)
        vida['escudo'] = vida['escudo'] - 20
        vida_atua()
        rot(t_av.set4)
    elif ans == "2":
        rot(t_av.set5)
## Oitava e última fase ##
    rot(t_av.final)
elif quer_jogar == "n":
    print("Até a próxima então!")
