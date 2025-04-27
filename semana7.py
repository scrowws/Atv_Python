import sys
import json
import os

# Lista para armazenar estudantes
estudantes = []

# Funcao para salvar estudantes no arquivo estudantes.json
def salvar_estudantes():
    try:
        with open('estudantes.json', 'w', encoding='utf-8') as f:
            json.dump(estudantes, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar estudantes: {e}")

# Funcao para carregar estudantes do arquivo estudantes.json
def carregar_estudantes():
    global estudantes
    if os.path.exists('estudantes.json'):
        try:
            with open('estudantes.json', 'r', encoding='utf-8') as f:
                estudantes = json.load(f)
        except json.JSONDecodeError:
            print("Arquivo estudantes.json corrompido! Criando uma nova lista de estudantes.")
            estudantes = []
        except Exception as e:
            print(f"Erro ao carregar estudantes: {e}")
            estudantes = []
    else:
        print("Arquivo estudantes.json não encontrado. Iniciando com lista vazia.")
        estudantes = []# Se o arquivo nao existir comeca vazio

# Carrega estudantes logo que o programa inicia
carregar_estudantes()

# Funcao para exibir o menu principal
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

# Funcao para exibir o menu secundário
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

# Funcao para incluir um estudante
def incluir_estudante():
    codigo = input("Informe o código do estudante: ")
    nome = input("Informe o nome do estudante: ")
    cpf = input("Informe o CPF do estudante: ")
    estudante = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    }
    estudantes.append(estudante)
    salvar_estudantes()
    print(f"Estudante '{nome}' incluído com sucesso!\n")

# Funcao para listar estudantes
def listar_estudantes():
    carregar_estudantes()  # Atualiza a lista a partir do arquivo
    if estudantes:
        print("\nLista de Estudantes:")
        for estudante in estudantes:
            print(f"Código: {estudante['codigo']} | Nome: {estudante['nome']} | CPF: {estudante['cpf']}")
        print()
    else:
        print("Não há estudantes cadastrados.\n")

# Funcao para editar um estudante
def editar_estudante():
    carregar_estudantes()  # Atualiza a lista a partir do arquivo
    if not estudantes:
        print("Não há estudantes cadastrados.\n")
        return

    codigo = input("Informe o código do estudante que deseja editar: ")
    estudante_encontrado = None

    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            estudante_encontrado = estudante
            break

    if estudante_encontrado:
        print(f"Você selecionou o estudante: {estudante_encontrado['nome']}")
        novo_nome = input(f"Digite o novo nome (atual: {estudante_encontrado['nome']}): ")
        estudante_encontrado['nome'] = novo_nome

        novo_codigo = input(f"Digite o novo código (atual: {estudante_encontrado['codigo']}): ")
        estudante_encontrado['codigo'] = novo_codigo

        novo_cpf = input(f"Digite o novo CPF (atual: {estudante_encontrado['cpf']}): ")
        estudante_encontrado['cpf'] = novo_cpf

        salvar_estudantes()
        print(f"Estudante '{estudante_encontrado['nome']}' atualizado com sucesso!\n")
    else:
        print("Estudante não encontrado.\n")

# Funcao para excluir um estudante
def excluir_estudante():
    carregar_estudantes()  # Atualiza a lista a partir do arquivo
    if not estudantes:
        print("Não há estudantes cadastrados.\n")
        return

    codigo = input("Informe o código do estudante que deseja excluir: ")
    estudante_encontrado = None

    for estudante in estudantes:
        if str(estudante['codigo']) == str(codigo):
            estudante_encontrado = estudante
            break

    if estudante_encontrado:
        estudantes.remove(estudante_encontrado)
        salvar_estudantes()
        print(f"Estudante '{estudante_encontrado['nome']}' excluído com sucesso!\n")
    else:
        print("Estudante não encontrado.\n")

# Dicionario de opções do menu principal
menu_principal_opcoes = {
    1: "[ESTUDANTES]",
    2: "[PROFESSORES]",
    3: "[DISCIPLINAS]",
    4: "[TURMAS]",
    5: "[MATRICULAS]",
    9: "SAIR"
}

# Dicionario de opções do menu secundário
menu_secundario_opcoes = {
    1: "INCLUIR",
    2: "LISTAR",
    3: "ATUALIZAR",
    4: "EXCLUIR",
    9: "VOLTAR"
}

# Loop principal do programa
while True:
    gerenciamento = menu_principal()
    gerenciamento_selec = menu_principal_opcoes[gerenciamento]

    if gerenciamento == 9:
        print("Sistema encerrado")
        sys.exit()

    if gerenciamento == 1:  # Estudantes
        while True:
            opcao = menu_secundario(gerenciamento_selec)
            opcao_selec = menu_secundario_opcoes[opcao]
            if opcao == 9:
                print("Voltando ao menu principal...\n")
                break

            elif opcao == 1:  # Incluir
                incluir_estudante()
            elif opcao == 2:  # Listar
                listar_estudantes()
            elif opcao == 3:  # Atualizar
                editar_estudante()
            elif opcao == 4:  # Excluir
                excluir_estudante()
            else:
                print(f"===== {opcao_selec} =====")
    else:
        print("Em desenvolvimento...\nVoltando ao menu principal...\n")
