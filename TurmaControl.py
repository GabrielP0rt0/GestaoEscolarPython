from Json import JsonMethodes
from SystemMessages import SystemMessages

class TurmaControl():
    """Classe responsável por funções envolvendo turmas
    """    
    def criar(self):
        """Função responsável pela criação de turmas
        """        
        self.__init()
        while True:
            print('-' * 50)
            print("Criar Turma")
            
            self.__codigo = int(input("[0] Para cancelar a operação qualquer momento\nDigite o código da Turma, sendo este um número maior que 0: "))
            if self.__codigo == 0:
                return
            
            verify = self.__verifyId()
            if verify == False:
                print(SystemMessages.classFound)
                continue
                
            self.__codigoProfessor = input("Digite o código do professor: ")
            if self.__codigoProfessor == 0:
                return
            
            verifyProfessor = self.__existeProfessor()
            if verifyProfessor == False:
                print(SystemMessages.notFoundProfessor)
                continue

            self.__codigoDisciplina = int(input("Digite o código da disciplina: "))
            if self.__codigoDisciplina == 0:
                return
            
            verifyDisciplina = self.__existeDisciplinas()
            if verifyDisciplina == False:
                print(SystemMessages.notFoundSubjects)
                continue
            
                    
            registro = {"codigo": self.__codigo, "codigoProfessor": self.__codigoProfessor, "codigoDisciplina": self.__codigoDisciplina}
            self.__turmas.append(registro)
            self.__bancoDeDados.operation("save", "Turmas", self.__turmas)
            print("Turma criada com sucesso!")
            return
    
    def editar(self):
        """Edita e atualiza os registros de turmas previamente cadastrados
        """        
        self.__init()
        while True:
            print('-' * 50)
            print(f'{"Edição de Turmas":^50}')
            print('-' * 50)
            if len(self.__turmas) == 0:
                print(SystemMessages.emptyRegisters)

            print("[0] para retornar a próxima página\nInsira o código da turma que deseja atualizar")
            codigoOperacao = int(input("Código: "))
            if codigoOperacao == 0:
                return
            for turma in self.__turmas:
                if codigoOperacao == turma.get('codigo'):
                    print(f"codigo do professor: {turma['codigoProfessor']}")
                    self.__codigoProfessor = input("novo codigo: ")
                    verifyProfessor = self.__existeProfessor()
                    if verifyProfessor == False:
                        print(SystemMessages.notFoundProfessor)
                        continue
                    
                    turma['codigoProfessor'] = self.__codigoProfessor

                    print(f"codigo da disciplina: {turma['codigoDisciplina']}")
                    self.__codigoDisciplina = int(input("novo codigo: "))
                    verifyDisciplina = self.__existeDisciplinas()
                    if verifyDisciplina == False:
                        print(SystemMessages.notFoundSubjects)
                        continue 
                    
                    turma['codigoDisciplina'] = self.__codigoDisciplina

                    print("\nTurma atualizada com sucesso!")
                    self.__bancoDeDados.operation("save", "Turmas", self.__turmas)
                    return
    
    def listar(self):
        """Lista todas as turmas existentes
        """        
        self.__init()
        if len(self.__turmas) == 0:
            print(SystemMessages.emptyRegisters)
            return
        
        print(self.__turmas)
    
    def excluir(self):
        """Exclui registros de turmas
        """        
        self.__init()
        while True:
            print('-' * 50)
            print(f'{"Exclusão de Turmas":^50}')
            print('-' * 50)
            if len(self.__turmas) == 0:
                print(SystemMessages.emptyRegisters)
                break
                
            print("Opções:")
            print("[0] Para retornar ao Menu operações")
            codigo = int((input("Digite o Código da Turma para exclusão: ")))  
            if codigo == 0:
                return
            
            for i, turma in enumerate(self.__turmas):
                if codigo == turma.get('codigo'):
                    print("Tem certeza que deseja excluir a turma:")
                    print(turma)
                    print("\n[1] para confirmar\n[2] para cancelar")
                    codigoAcao = int(input("Opção: "))
                    if codigoAcao == 2:
                        continue
                    elif codigoAcao == 1:
                        self.__turmas.pop(i)
                        print("Turma apagado com sucesso")
                        break
                    else:
                        print(SystemMessages.invalidOption)
                        continue
                
            self.__bancoDeDados.operation("save", "Turmas", self.__turmas)
            return
    
    def __verifyId(self):
        """Verifica se o Id de turma ja existe

        Returns:
            boolean: False para turma existe, True turma disponivel 
        """        
        for turma in self.__turmas:
            if self.__codigo == turma.get('codigo'):
                return False
        return True
    
    def __existeDisciplinas(self):
        """Verifica se a disciplina selecionada existe

        Returns:
            boolean: True para disciplina válida, False para disciplina inválida
        """        
        for disciplina in self.__disciplinas:
            if self.__codigoDisciplina in disciplina.values():
                return True
        return False
    
    def __existeProfessor(self):
        """Verifica a existencia do professor escolhido

        Returns:
            boolean: True para professor válido, False para professor não válido
        """        
        for professor in self.__professores:
            if self.__codigoProfessor in professor.values():
                return True
        return False
    
    def __init(self):
        """Inicializa os parametros de banco de dados utilizados nas funções principais desta classe
        """        
        self.__bancoDeDados = JsonMethodes()
        self.__turmas = self.__bancoDeDados.operation("read", "Turmas")
        self.__disciplinas = []
        disciplinas = self.__bancoDeDados.operation("read", "Disciplinas")
        for disciplina in disciplinas:
            self.__disciplinas.append(disciplina)
        self.__professores = []
        users = self.__bancoDeDados.operation("read", "User")
        for user in users:
            if "Professores" in user.values():
                self.__professores.append(user)
        
        
