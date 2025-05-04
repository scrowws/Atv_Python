import sys
import json
import os

# Classe de base


class ModuloBase:
    def __init__(self, nome_modulo, campos, nome_arquivo):
        self.nome_modulo = nome_modulo
        self.campos = campos
        self.nome_arquivo = nome_arquivo
        self.dados = self.carregar()

    def carregar(self):
        if os.path.exists(self.nome_arquivo):
            try:
                with open(self.nome_arquivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                print(
                    f"Erro ao carregar {self.nome_arquivo}, iniciando lista vazia.")
        return []

    def salvar(self):
        try:
            with open(self.nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump(self.dados, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar {self.nome_modulo}: {e}")

    def incluir(self):
        novo = {}
        for campo in self.campos:
            novo[campo] = input(f"{campo.capitalize()}: ")

        if any(reg.get("codigo") == novo.get("codigo") for reg in self.dados):
            print("Já existe um registro com esse código!\n")
            return

        if not self.validar_referencias(novo):
            return

        self.dados.append(novo)
        self.salvar()
        print(f"{self.nome_modulo[:-1].capitalize()} incluído com sucesso!\n")

    def listar(self):
        if self.dados:
            print(f"\nLista de {self.nome_modulo.capitalize()}:")
            for reg in self.dados:
                print(" | ".join(
                    [f"{k.capitalize()}: {v}" for k, v in reg.items()]))
            print()
        else:
            print(f"Não há {self.nome_modulo} cadastrados.\n")

    def editar(self):
        codigo = input("Código para editar: ")
        for reg in self.dados:
            if reg.get("codigo") == codigo:
                for campo in self.campos:
                    novo = input(f"{campo} atual ({reg[campo]}): ")
                    if novo:
                        reg[campo] = novo
                self.salvar()
                print(f"{self.nome_modulo[:-1].capitalize()} atualizado!\n")
                return
        print("Registro não encontrado.\n")

    def excluir(self):
        codigo = input("Código para excluir: ")
        for reg in self.dados:
            if reg.get("codigo") == codigo or reg.get("codigo_turma") == codigo:
                self.dados.remove(reg)
                self.salvar()
                print(f"{self.nome_modulo[:-1].capitalize()} excluído!\n")
                return
        print("Registro não encontrado.\n")

    def validar_referencias(self, novo):
        return True  # Padrao para modulos simples


# Subclasses com validacoes especificas
class Estudante(ModuloBase):
    def __init__(self):
        super().__init__("estudantes", [
            "codigo", "nome", "cpf"], "estudantes.json")


class Professor(ModuloBase):
    def __init__(self):
        super().__init__("professores", [
            "codigo", "nome", "cpf"], "professores.json")


class Disciplina(ModuloBase):
    def __init__(self):
        super().__init__("disciplinas", ["codigo", "nome"], "disciplinas.json")


class Turma(ModuloBase):
    def __init__(self, professores, disciplinas):
        super().__init__(
            "turmas", ["codigo", "codigo_professor", "codigo_disciplina"], "turmas.json")
        self.professores = professores
        self.disciplinas = disciplinas

    def validar_referencias(self, novo):
        if not any(p["codigo"] == novo["codigo_professor"] for p in self.professores.dados):
            print("Código de professor inválido!")
            return False
        if not any(d["codigo"] == novo["codigo_disciplina"] for d in self.disciplinas.dados):
            print("Código de disciplina inválido!")
            return False
        return True


class Matricula(ModuloBase):
    def __init__(self, turmas, estudantes):
        super().__init__("matriculas", [
            "codigo_turma", "codigo_estudante"], "matriculas.json")
        self.turmas = turmas
        self.estudantes = estudantes

    def validar_referencias(self, novo):
        if not any(t["codigo"] == novo["codigo_turma"] for t in self.turmas.dados):
            print("Código de turma inválido!")
            return False
        if not any(e["codigo"] == novo["codigo_estudante"] for e in self.estudantes.dados):
            print("Código de estudante inválido!")
            return False
        return True


# Funcoes de menu
def menu_principal():
    while True:
        print("----- MENU PRINCIPAL -----")
        print("(1) Estudantes\n(2) Professores\n(3) Disciplinas\n(4) Turmas\n(5) Matrículas\n(9) Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao in range(1, 6):
                return opcao
            elif opcao == 9:
                print("Encerrando...")
                sys.exit()
            else:
                print("Opção inválida!\n")
        except ValueError:
            print("Digite um número válido.\n")


def menu_operacoes(modulo):
    while True:
        print(f"\n--- [{modulo.nome_modulo.upper()}] ---")
        print("(1) Incluir\n(2) Listar\n(3) Atualizar\n(4) Excluir\n(9) Voltar")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                modulo.incluir()
            elif opcao == 2:
                modulo.listar()
            elif opcao == 3:
                modulo.editar()
            elif opcao == 4:
                modulo.excluir()
            elif opcao == 9:
                break
            else:
                print("Opção inválida!\n")
        except ValueError:
            print("Entrada inválida!\n")


# Inicializacao
estudantes = Estudante()
professores = Professor()
disciplinas = Disciplina()
turmas = Turma(professores, disciplinas)
matriculas = Matricula(turmas, estudantes)

modulos = [estudantes, professores, disciplinas, turmas, matriculas]

# Loop principal
while True:
    opcao = menu_principal()
    modulo_escolhido = modulos[opcao - 1]
    menu_operacoes(modulo_escolhido)
