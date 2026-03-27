# algarismos da senha
senha_correta = "python123"
tentativas = "3"
conectado = False
# corpo do código 
print (" Bem vindo ao Sistema de conexão Wi-fi da Lh Technology!")
while not conectado: 
    senha = input("Digite a senha para se conectar:")
    if senha == senha_correta: 
        print("Conectado com sucesso!")
        conectado = True
    else:
        print("Senha incorreta. Tente Novamente.")
        tentativas = int(tentativas) - 1
        chance_restante = 3 - tentativas
        if tentativas > 0:
            print(f"Você usou {chance_restante} das 3 tentativas.")
        else:
            print("Número de tentativas excedido. Acesso bloqueado.")

print("obrigado por usar o sistema da Lh tecnolgy.")



