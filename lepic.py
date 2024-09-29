#importar a biblioteca para capturar eventos do teclado
#precisa fazer pip install da biblioteca KEYBOARD
import keyboard

#inicializar o dicionário para armazenar as pontuações dos médicos
scoreboard = {}

#função para atualizar a pontuação do médico no dicionário
def atualizar_scoreboard(nome_medico, pontuacao_medico_sum):
    scoreboard[nome_medico] = pontuacao_medico_sum

#função para exibir o dicionário de pontuações
def mostrar_scoreboard():
    print(f'Tabela atual: {scoreboard}')

#função principal que executa a simulação
def start():
    pontuacao = 0  #inicializar a pontuação do médico
    print("Digite o nome do médico")
    nome = input()  #capturar o nome do médico via input

    print("Aperte ENTER para começar!")
    keyboard.wait('enter')  #esperar o usuário apertar ENTER para iniciar a simulação
    
    #loop para capturar eventos do teclado e alterar pontuação
    while True:
        evento = keyboard.read_event()  #ler o evento de teclado
        if evento.event_type == keyboard.KEY_DOWN:  #verificar se a tecla foi pressionada
            if evento.name == 'a':  #se a tecla 'a' for pressionada
                pontuacao = pontuacao + 5  #adicionar 5 pontos à pontuação
                print(f"Acerto! Pontuação: {pontuacao}")
            elif evento.name == 'e':  #se a tecla 'e' for pressionada
                pontuacao = pontuacao - 3  #subtrair 3 pontos da pontuação
                print(f"Erro! Pontuação: {pontuacao}")
            elif evento.name == 'backspace':  #se a tecla BACKSPACE for pressionada
                print(f"Saindo da simulação... Pontuação final: {pontuacao}")
                break  #sair do loop e encerrar a simulação
    
    #atualizar a pontuação do médico no dicionário
    atualizar_scoreboard(nome, pontuacao)
    mostrar_scoreboard()  #exibir o scoreboard atualizado

#iniciar a simulação
start()
