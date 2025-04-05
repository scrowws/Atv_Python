# Estudante: Leonardo Flores dos Santos
# Curso: Raciocínio Computacional (11100010563_20251_05)

import sys  # Import realizado para poder utilizar a funcao sys.exit()


estudantes = []  # Lista para armazenar estudantes


# Funcao para exibir o menu principal e garantir que a entrada seja valida, importante lembrar, return utilizado para retornar o valor na funcao, tambem encerra o while por acabar com a Def
def menu_principal():
    while True:
        print("----- MENU PRINCIPAL -----\n(1) Gerenciar estudantes\n(2) Gerenciar professores\n(3) Gerenciar disciplinas\n(4) Gerenciar turmas\n(5) Gerenciar matriculas\n(9) Sair\n")
        try:
            opcao = int(input("Informe a opcao desejada: "))
            if opcao in menu_principal_opcoes:
                return opcao
            else:
                print("Entrada inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


#  Funcaoo para exibir o menu secundário e garantir que a entrada seja valida, passado a variavel gerenciamento_selec como parametro, pois uma funcao nao consegue acessar variaveis de fora dela
def menu_secundario(gerenciamento_selec):
    while True:
        print(f"***** {gerenciamento_selec} MENU DE OPERACOES *****\n(1) Incluir\n(2) Listar\n(3) Atualizar\n(4) Excluir\n(9) Voltar ao menu principal\n")
        try:
            opcao = int(input("Informe a opcao desejada: "))
            if opcao in menu_secundario_opcoes:
                return opcao
            else:
                print("Entrada inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


# Dicionario de mapeamento das opcoes do menu secundario, para reduzir a utilizacao de if, elif e else
menu_principal_opcoes = {
    1: "[ESTUDANTES]",
    2: "[PROFESSORES]",
    3: "[DISCIPLINAS]",
    4: "[TURMAS]",
    5: "[MATRICULAS]",
    9: "SAIR"
}


# Dicionario de mapeamento das opcoes do menu secundario
menu_secundario_opcoes = {
    1: "INCLUIR",
    2: "LISTAR",
    3: "ATUALIZAR",
    4: "EXCLUIR",
    9: "VOLTAR"
}


# Loop principal do programa, ele chama as defs para serem executadas
while True:
    # Exibe o menu principal e le a opcao, chamando a def de menu_principal gerenciamento_selec recebe a opcao escolhida com base no dicionario de menu principal, com base na variavel gerenciamento que contem a opcao selecionada pelo usuario
    gerenciamento = menu_principal()
    gerenciamento_selec = menu_principal_opcoes[gerenciamento]

    # Verifica a opcao do menu principal(Pega o return da DEF e verificar se esta dentro da lista, caso o return seja 9 ele encerra)
    if gerenciamento == 9:
        print("Sistema encerrado")
        sys.exit()

    # Caso return seja 1 ele prossegue para operacoes de estudantes, outras opcoes ele informa que esta em desenvolvimento e retorna ao menu principal
    if gerenciamento == 1:
        while True:
            opcao = menu_secundario(gerenciamento_selec)
            opcao_selec = menu_secundario_opcoes[opcao]
            if opcao == 9:
                print("Voltando ao menu principal...\n")
                break

            if opcao == 1:
                nome = input("Informe o nome do estudante: ")
                estudantes.append(nome)
                print(f"Estudante '{nome}' incluído com sucesso!\n")
            elif opcao == 2:
                if estudantes:
                    print("\nLista de Estudantes:")
                    # com base no index da lista ele cria um lopp, dessa forma
                    for idx, estudante in enumerate(estudantes, start=1):
                        # sempre que um novo estudando for adicinado o loop vai seguir
                        print(f"{idx}. {estudante}")
                    print()
                else:
                    print("Não há estudantes cadastrados.\n")
            elif opcao in [3, 4]:
                print("Em desenvolvimento...\nVoltando ao menu de operações...\n")
            else:
                print(f"===== {opcao_selec} =====")
    else:
        print("Em desenvolvimento...\nVoltando ao menu principal...\n")
