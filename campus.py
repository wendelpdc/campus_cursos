class Campus:
    def __init__(self, codigo, nome, endereco):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cursos = []
        
    def add_curso(self, curso):
        if curso not in self.cursos:
            codigo_curso = int(input("Código do curso: "))
            nome_curso = input("Nome do curso: ")
            self.cursos.append(codigo_curso, nome_curso)
            print(f"O curso {curso} foi adicionado ao campus {self.nome} com sucesso!")
        else:
            print(f"O curso {curso} já existe no campus {self.nome}.")
        
    def listar_cursos(self):
        if self.cursos:
            print(f"Cursos presentes no campus {self.nome}: ")
            for curso in self.cursos:
                print(f"{curso}")
        else:
            print("Não há curso cadastrado no campus {self.nome}.")
            
def menu_interativo():
    print("***************")
    print("* MENU CAMPUS *")
    print("***************")

    print("1 - Criar campus")
    print("2 - Adicionar curso")
    print("3 - Listar cursos")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

if __name__ == "__main__":
    menu_interativo()

            
        