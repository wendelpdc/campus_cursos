class CursosCampus:
    def __init__(self, id_curso, nome_curso):
        self.id_curso = id_curso
        self.nome_curso = nome_curso

    def add_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            print(f"O curso '{curso}' foi adicionado ao campus {self.nome}.")
        else:
            print(f"O curso {curso} já existe no campus {self.nome}.")
        
    def listar_cursos(self):
        if self.cursos:
            print(f"Cursos presentes no campus {self.nome}, até o devido momento: ")
            for curso in self.cursos:
                print(f"{curso}")
        else:
            print("Não há curso cadastrado no campus {self.nome}.")