from Json import JsonMethodes
from SystemMessages import SystemMessages

class DisciplinasControl():
    """Classe responsável pelas funções envolvendo disciplinas
    """    
    def criar(self):
        """Criar Registro das disciplinas
        """        
        bancoDeDados = JsonMethodes()
        self.__disciplinas = bancoDeDados.operation("read", "Disciplinas")
        print('-' * 50)
        print("Criar Disciplinas")
        
        self.__codigo = int(input("[0] Para cancelar a operaçãoa qualquer momento\nDigite o código da disciplina, sendo este um número maior que 0: "))
        if self.__codigo == 0:
            return
        
        self.__nomeDisciplina = input("Digite o nome da disciplina: ")
        if self.__nomeDisciplina == "0":
            return
            
        verify = self.__verifyId()
        if verify == False:
            print(SystemMessages.nameOrDisciplineFound)
            return
                
        registro = {"codigo": self.__codigo, "nomeDisciplina": self.__nomeDisciplina}
        self.__disciplinas.append(registro)
        bancoDeDados.operation("save", "Disciplinas", self.__disciplinas)

    def editar(self):
        """Edita os registros das disciplinas cadastradas
        """        
        bancoDeDados = JsonMethodes()
        self.__disciplinas = bancoDeDados.operation("read", "Disciplinas")
        print('-' * 50)
        print(f'{"Edição de Disciplinas":^50}')
        print('-' * 50)
        if len(self.__disciplinas) == 0:
            print(SystemMessages.emptyRegisters)

        print("[0] para retornar a próxima página\nInsira o código da disciplina que deseja atualizar")
        codigoOperacao = int(input("Código: "))
        if codigoOperacao == 0:
            return
        for disciplina in self.__disciplinas:
            if codigoOperacao in disciplina.values():
                print(f"nome atual: {disciplina['nomeDisciplina']}")
                disciplina['nomeDisciplina'] = input("novo nome: ")
                print("\nDisciplina atualizado com sucesso!")
                bancoDeDados.operation("save", "Disciplinas", self.__disciplinas)
                return
    
    def listar(self):
        """Lista todas as disciplinas cadastradas
        """        
        bancoDeDados = JsonMethodes()
        self.__disciplinas = bancoDeDados.operation("read", "Disciplinas")  
        if len(self.__disciplinas) == 0:
            print(SystemMessages.emptyRegisters)
            return
        
        for disciplina in self.__disciplinas:
            print(disciplina)
    
    def excluir(self):
        """Possibilita a exclusão de disciplinas previamente cadastradas
        """        
        bancoDeDados = JsonMethodes()
        self.__disciplinas = bancoDeDados.operation("read", "Disciplinas")
        while True:
            print('-' * 50)
            print(f'{"Exclusão de Disciplina":^50}')
            print('-' * 50)
            if len(self.__disciplinas) == 0:
                print(SystemMessages.emptyRegisters)
                break
                
            print("Opções:")
            print("[0] Para retornar ao Menu operações")
            codigo = int((input("Digite o Código da disciplina para exclusão: ")))  
            if codigo == 0:
                return
            
            for i, disciplina in enumerate(self.__disciplinas):
                if codigo in disciplina.values():
                    print("Tem certeza que deseja excluir a disciplina:")
                    print(disciplina)
                    print("\n[1] para confirmar\n[2] para cancelar")
                    codigoAcao = int(input("Opção: "))
                    if codigoAcao == 2:
                        continue
                    elif codigoAcao == 1:
                        self.__disciplinas.pop(i)
                        print("Disciplina apagado com sucesso")
                        break
                    else:
                        print(SystemMessages.invalidOption)
                        continue
                
            bancoDeDados.operation("save", "Disciplinas", self.__disciplinas)
            return

    def __verifyId(self): 
        """Verifica se a disciplina ja foi cadastrada

        Returns:
            boolean: Falso caso encontre uma disciplina com o mesmo código ja cadastrado
        """        
        for disciplina in self.__disciplinas:
            if self.__codigo == disciplina.get("codigo") or self.__nomeDisciplina == disciplina.get('nomeDisciplina'):
                return False
        return True