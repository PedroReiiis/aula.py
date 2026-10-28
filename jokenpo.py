import random


PEDRA = "✊"
PAPEL = "✋"
TESOURA = "✌️"

print("--- Start Game ---")

while True:
    print("\nEscolha sua jogada:")
    print("1 - Pedra", (PEDRA))
    print("2 - Papel", (PAPEL))
    print("3 - Tesoura", (TESOURA))
    print("0 - Sair do jogo")

    print("----Loading-----")

    escolha_usuario = input("Digite o número da sua opção: ")
    
    
    match escolha_usuario:
        case "1":
            jogada = PEDRA
        case "2":
            jogada = PAPEL
        case "3":
            jogada = TESOURA
        case "0":
            print("Obrigado por jogar! Até logo! 👋")
            break  
        case _:
            print("Opção inválida! Tente novamente.")
            continue  

    
    pc = random.choice([PEDRA, PAPEL, TESOURA])
    
    print("\nVocê: ",(jogada))
    print("Computador:", (pc))
    
    
    match (jogada, pc):
        
        case (jog1, jog2) if jog1 == jog2:
            print("Empate! 🤝")
            
        
        case ("✊", "✌️") | ("✋", "✊") | ("✌️", "✋"):
            print("Você venceu! ")
            
        
        case _:
            print("Você Perdeu")
