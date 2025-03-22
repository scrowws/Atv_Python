import sys

print("----- MENU PRINCIPAL ----- \n (1)Gerenciar estudantes \n (2) Gerenciar professores \n (3) Gerenciar disciplinas \n (4) Gerenciar turmas \n (5) Gerenciar matriculas \n (9) Sair \n")
gerenciamento = int(input("Informe a opcao desejada: "))
gerenciamento_selec = 0
opcao_selec = 0

if gerenciamento == 1:
    gerenciamento_selec = "[ESTUDANTES]"
elif gerenciamento == 2:
    gerenciamento_selec = "[PROFESSORES]"
elif gerenciamento == 3:
    gerenciamento_selec = "[DISCIPLINAS]"
elif gerenciamento == 4:
    gerenciamento_selec = "[TURMAS]"
elif gerenciamento == 5:
    gerenciamento_selec = "[MATRICULAS]"
elif gerenciamento == 9:
    gerenciamento_selec = "[SAIR]"
    print("Sistema encerrado")
    sys.exit()
else:
    print("Entrada invalida")
    sys.exit()

print(f"***** {gerenciamento_selec} MENU DE OPERACOES ***** \n (1) Incluir \n (2) Listar \n (3) Atualizar \n (4) Excluir \n (9) Voltar ao menu principal \n")
opcao = int(input("Informe a opcao desejada"))

if opcao == 1:
    opcao_selec = "INCLUIR"
elif opcao == 2:
    opcao_selec = "LISTAR"
elif opcao == 3:
    opcao_selec = "ATUALIZAR"
elif opcao == 4:
    opcao_selec = "EXCLUIR"
elif opcao == 4:
    opcao_selec = "[VOLTAR]"
else:
    opcao_selec = "[ENTRADA INVALIDA]"

print(f"===== {opcao_selec} =====")
print("Finalizando aplicacao")