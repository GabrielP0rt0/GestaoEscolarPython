from Json import JsonMethodes
from SystemMessages import SystemMessages

class Matriculas():
    """Classe responsável pelas funções referentes a matrículas
    """    
    def matricular(self):
        """Função responsável por criar o registro de matrícula do aluno
        """        
        self.__bancoDeDados = JsonMethodes()
        self.__matriculas = self.__bancoDeDados.operation("read", "Matriculas")
        while True:
            print('-' * 50)
            print("Matriculas")
            print("[0] Encerrar Aplicação")

            try:
                self.__codigoMatricula = int(input("Insira o código da matricula: "))
            except:
                print(SystemMessages.invalidOption)
                continue

            validateMatricula = self.__checkIdMatricula()
            if validateMatricula == False:
                print(SystemMessages.matriculaFound)
                continue

            try:
                self.__codigoAluno = int(input("Insira o código do aluno: "))
            except:
                print(SystemMessages.invalidOption)
                continue

            validateAluno = self.__checkAluno()
            if validateAluno == False:
                print(SystemMessages.notStudent)
                continue
            
            try:
                self.__codigoTurma = int(input("Insira o código da turma: "))
            except:
                print(SystemMessages.invalidOption)
                continue

            validateTurma = self.__checkTurma()
            if validateTurma == False:
                print(SystemMessages.unregisteredClass)
                continue
            
            self.__matriculas.append({'codigo': self.__codigoMatricula, 'codigoAluno': self.__codigoAluno, 'codigoTurma': self.__codigoTurma})
            self.__bancoDeDados.operation("save", "Matriculas", self.__matriculas)
            break
    
    def listarMatriculas(self):
        """Função responsável por listar todos os registros de matrículas
        """        
        self.__bancoDeDados = JsonMethodes()
        self.__matriculas = self.__bancoDeDados.operation("read", "Matriculas")
        if len(self.__matriculas) == 0:
            print("Não há registros de matrículas!")
            return
        for matricula in self.__matriculas:
            print(matricula)

    def excluirMatriculas(self):
        """Exclui o registro de matrícula do usuário
        """        
        self.__bancoDeDados = JsonMethodes()
        self.__matriculas = self.__bancoDeDados.operation("read", "Matriculas")
        while True:
            print('-' * 50)
            print(f'{"Exclusão de Matrícula":^50}')
            print('-' * 50)
            if len(self.__matriculas) == 0:
                print(SystemMessages.emptyRegisters)
                break
                
            print("Opções:")
            print("[0] Para retornar ao Menu operações")
            try:
                codigo = int((input("Digite o Código da matrícula para exclusão: ")))  
            except:
                print(SystemMessages.invalidOption)
                continue

            if codigo == 0:
                return
            
            for i, matricula in enumerate(self.__matriculas):
                if codigo == matricula.get('codigo'):
                    print("Tem certeza que deseja excluir a Matricula:")
                    print(matricula)
                    print("\n[1] para confirmar\n[2] para cancelar")
                    try:
                        codigoAcao = int(input("Opção: "))
                    except:
                        print(SystemMessages.invalidOption)
                        continue
                    if codigoAcao == 2:
                        continue
                    elif codigoAcao == 1:
                        self.__matriculas.pop(i)
                        print("Matricula apagado com sucesso")
                        self.__bancoDeDados.operation("save", "Matriculas", self.__matriculas)
                        return
                    else:
                        print(SystemMessages.invalidOption)
                        continue
                
    def __checkIdMatricula(self):
        """Checa se existe registro de matrícula com o mesmo código

        Returns:
            boolean: Falso para registro existe e true para sem registros compativeis
        """        
        for matricula in self.__matriculas:
            if self.__codigoMatricula == matricula.get('codigo'):
                return False
        return True
    
    def __checkTurma(self):
        """Checa se Existem Turmas com o código de cadastro informado

        Returns:
            boolean: True para turmas existentes e Falso para não existencia de turmas com o mesmo código
        """        
        self.__turmas = self.__bancoDeDados.operation("read", "Turmas")
        for turma in self.__turmas:
            if self.__codigoTurma == turma.get("codigo"):
                return True
        return False
    
    def __checkAluno(self):
        """Checa se existe registro de usuário estudante com o mesmo código

        Returns:
            boolean: True para registro localizado, False para nenhum registro correspondente
        """        
        self.__users = self.__bancoDeDados.operation("read", "User")
        for user in self.__users:
            if self.__codigoAluno == user.get("codigo") and user.get("type") == "Estudantes":
                return True
        return False