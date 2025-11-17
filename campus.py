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
        
            

            
        