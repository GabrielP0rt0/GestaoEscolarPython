from Json import JsonMethodes
from SystemMessages import SystemMessages

class UserControl:
    """Classe responsável pelas funções que dizem respeito aos usuários, Professores e Estudantes
    """    
    def criarUser(self, type):
        """Cria o registro de usuário

        Args:
            type (string): Professores para criar um registro do tipo Professores e Estudantes para criar um registro do tipo Estudantes
        """        
        dataBase = JsonMethodes()
        bancoDeDadosUser = dataBase.operation("read", "User")
        print('-' * 50)
        print("Criar Registros")
        
        self.__codigo = int(input("[0] Para cancelar a operaçãoa qualquer momento\nDigite o código do usuário, sendo este um número maior que 0: "))
        if self.__codigo == 0:
            return
        for dadosUser in bancoDeDadosUser:
            if self.__codigo in dadosUser.values():
                print(SystemMessages.userExist)
                return
            
        self.__nome = input("Digite o nome do usuário: ")
        if self.__nome == "0":
            return

        self.__cpf = input("Digite o cpf do estudante: ")
        if self.__cpf == "0":
            return
        for dadosUser in bancoDeDadosUser:
            if self.__cpf in dadosUser.values():
                print(SystemMessages.cpfExist)
                return
            
        registro = {"codigo": self.__codigo, "nome": self.__nome, "cpf": self.__cpf, "type": type}
        bancoDeDadosUser.append(registro)
        dataBase.operation("save", "User", bancoDeDadosUser)

    def ler(self, type):
        """Le os registros de usuários do tipo correspondente

        Args:
            type (string): Filtro para ler usuários do tipo Professores ou Estudantes
        """        
        dataBase = JsonMethodes()
        registrosUsers = dataBase.operation("read", "User")
        if len(registrosUsers) == 0:
            print(SystemMessages.emptyRegisters)
            return
        
        for registro in registrosUsers:
            if type == registro.get('type'):
                print(registro)

    def excluir(self, type):
        """Exclui usuários do tipo correspondente do registro

        Args:
            type (string): Filtro para excluir usuários do tipo Professores ou Estudantes
        """        
        dataBase = JsonMethodes()
        registroUsers = dataBase.operation("read", "User")
        while True:
            print('-' * 50)
            print(f'{"Exclusão de usuário":^50}')
            print('-' * 50)
            if len(registroUsers) == 0:
                print(SystemMessages.emptyRegisters)
                break
                
            print("Opções:")
            print("[0] Para retornar ao Menu operações")
            try:
                codigoExclusao = int(input("Digite o Código do usuário para exclusão: "))  
            except:
                print(SystemMessages.invalidOption)
                continue

            if codigoExclusao == "0":
                return
            
            for i, registro in enumerate(registroUsers):
                if codigoExclusao in registro.values() and type in registro.values():
                    print("Tem certeza que deseja excluir o usuários:")
                    print(registro)
                    print("\n[1] para confirmar\n[2] para cancelar")
                    codigo_acao = int(input("Opção: "))
                    if codigo_acao == 2:
                        continue
                    elif codigo_acao == 1:
                        registroUsers.pop(i)
                        print("Usuário apagado com sucesso")
                        return
                    else:
                        print(SystemMessages.invalidOption)
                        continue
                elif codigoExclusao in registro.values():
                    print(SystemMessages.userNotFound)
                    continue
                
            dataBase.operation("save", "User", registroUsers)
    
    def atualizarUser(self, type):
        """Edita usuários do tipo correspondente

        Args:
            type (string): Filtro para editar usuários do tipo Professores ou Estudantes
        """        
        dataBase = JsonMethodes()
        registroUsers = dataBase.operation("read", "User")
        while True:
            print('-' * 50)
            print(f'{"Edição de Usuário":^50}')
            print('-' * 50)
            if len(registroUsers) == 0:
                print(SystemMessages.emptyRegisters)
                break

            print("[0] para retornar a próxima página\nInsira o código do usuário que deseja atualizar")
            codigoOperacao = int(input("Código: "))
            if codigoOperacao == 0:
                break
            for registro in registroUsers:
                if codigoOperacao in registro.values() and type in registro.values():
                    print(f"nome atual: {registro['nome']}")
                    registro['nome'] = input("novo nome: ")
                    print("CPF atual: ")
                    registro['cpf'] = input("novo cpf: ")
                    print("\nUsuário atualizado com sucesso!")
                    dataBase.operation("save", "User", registroUsers)
                    break
                elif codigoOperacao in registro.values():
                    print(SystemMessages.userNotFound)
                    continue