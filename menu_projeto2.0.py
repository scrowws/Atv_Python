import sys

# Funcao para exibir o menu principal e garantir que a entrada seja valida, importante lembrar, return encera o while


def menu_principal():
    while True:
        print("----- MENU PRINCIPAL ----- \n (1)Gerenciar estudantes \n (2) Gerenciar professores \n (3) Gerenciar disciplinas \n (4) Gerenciar turmas \n (5) Gerenciar matriculas \n (9) Sair \n")
        opcao = int(input("Informe a opcao desejada: "))
        if opcao in menu_principal_opcoes:
            return opcao
        else:
            print("Entrada inválida! Tente novamente.")

# Funcaoo para exibir o menu secundário e garantir que a entrada seja valida


def menu_secundario(gerenciamento_selec):
    while True:
        print(f"***** {gerenciamento_selec} MENU DE OPERACOES ***** \n (1) Incluir \n (2) Listar \n (3) Atualizar \n (4) Excluir \n (9) Voltar ao menu principal \n")
        opcao = int(input("Informe a opcao desejada: "))
        if opcao in menu_secundario_opcoes:
            return opcao
        else:
            print("Entrada inválida! Tente novamente.")


# Mapeamento das opcoes do menu principal em lista para reduzir o uso de if e elif
menu_principal_opcoes = {
    1: "[ESTUDANTES]",
    2: "[PROFESSORES]",
    3: "[DISCIPLINAS]",
    4: "[TURMAS]",
    5: "[MATRICULAS]",
    9: "SAIR"
}

# Mapeamento das opcoes do menu secundario
menu_secundario_opcoes = {
    1: "INCLUIR",
    2: "LISTAR",
    3: "ATUALIZAR",
    4: "EXCLUIR",
    9: "VOLTAR"
}

# Loop principal do programa, ele chama as defs para serem executadas
while True:
    # Exibe o menu principal e le a opcao, chamando a def de menu_principal
    gerenciamento = menu_principal()

    # Verifica a opcao do menu principal(Pega o return da DEF e verificar se esta dentro da lista, caso o return seja 9 ele encerra)
    gerenciamento_selec = menu_principal_opcoes[gerenciamento]
    if gerenciamento == 9:
        print("Sistema encerrado")
        sys.exit()

    # Loop do menu secundário
    while True:
        # Exibe o menu secundário e lê a opção
        opcao = menu_secundario(gerenciamento_selec)

        # Verifica a opção do menu secundário
        opcao_selec = menu_secundario_opcoes[opcao]
        if opcao == 9:
            print("Voltando ao menu principal...\n")
            break  # Sai do menu secundário e volta ao menu principal

        # Exibe a opção selecionada no menu secundário
        print(f"===== {opcao_selec} =====")
        
