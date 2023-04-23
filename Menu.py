from SystemMessages import SystemMessages
from UserControl import UserControl
from DisciplinaControl import DisciplinasControl
from TurmaControl import TurmaControl
from Matriculas import Matriculas

class GestaoEscola():
    """Classe responsável por gerar o menu principal do código
    """    
    def __init__(self):
        """função de inicialização com o menu Principal
        """        
        while True:
            print('-' * 50)
            print(f'{"Menu":^50}')
            print('-' * 50)
            print("Opções:")
            print("[0] Para encerrar a aplicação")
            print("[1] Menu de estudantes")
            print("[2] Matricular")
            print("[3] Professores")
            print("[4] Turmas")
            print("[5] Disciplinas")
            print('-' * 50)
            try:
                opcao = int(input("Sua Opção: "))
            except:
                print(SystemMessages.invalidOption)
                continue
            if opcao == 1:
                self.__optionsMenu("Estudantes")
            elif opcao == 2:
                self.__matriculasMenu()
            elif opcao == 3:
                self.__optionsMenu("Professores")
            elif opcao == 4:
                self.__optionsMenu("Turmas")
            elif opcao == 5:
                self.__optionsMenu("Disciplinas")
            elif opcao == 0:
                break
            else:
                print(SystemMessages.invalidOption)
            continue
        

    def __optionsMenu(self, type):
        """Submenu responsável pelas funções referentes a professores, alunos, turmas e disciplinas

        Args:
            type (string): referente ao tipo de menu acessado["Professores","Estudantes","Turmas","Disciplinas"]
        """        
        userService = UserControl()
        disciplinaService = DisciplinasControl()
        turmaService = TurmaControl()
        while True:
            print(f'{type:^50}')
            print('-' * 50)
            print("Opções:")
            print("[0] Retornar ao menu principal")
            print("[1] Criar")
            print("[2] Editar")
            print("[3] Listar")
            print("[4] Excluir")
            print('-' * 50)
            try:
                opcao = int(input("Sua Opção: "))
            except:
                print(SystemMessages.invalidOption)
                continue
            if opcao == 1:
                if(type == "Professores" or type == "Estudantes"):
                    userService.criarUser(type)
                elif(type == "Turmas"):
                    turmaService.criar()
                elif(type == "Disciplinas"):
                    disciplinaService.criar()
                else:
                    print(SystemMessages.anErrorAsOccurred)
                continue
            elif opcao == 2:
                if(type == "Professores" or type == "Estudantes"):
                    userService.atualizarUser(type)
                elif(type == "Turmas"):
                    turmaService.editar()
                elif(type == "Disciplinas"):
                    disciplinaService.editar()
                else:
                    print(SystemMessages.anErrorAsOccurred)
                continue
            elif opcao == 3:
                if(type == "Professores" or type == "Estudantes"):
                    userService.ler(type)
                elif(type == "Turmas"):
                    turmaService.listar()
                elif(type == "Disciplinas"):
                    disciplinaService.listar()
                else:
                    print(SystemMessages.anErrorAsOccurred)
                continue
            elif opcao == 4:
                if(type == "Professores" or type == "Estudantes"):
                    userService.excluir(type)
                elif(type == "Turmas"):
                    turmaService.excluir()
                elif(type == "Disciplinas"):
                    disciplinaService.excluir()
                else:
                    print(SystemMessages.anErrorAsOccurred)
                continue
            elif opcao == 0:
                break
            else:
                print(SystemMessages.invalidOption)
        
   
    def __matriculasMenu(self):
        """Submenu Responsável pelas funções de matrícula
        """        
        matriculasService = Matriculas()
        while True: 
            print(f'{"Matriculas":^50}')
            print('-' * 50)
            print("Matriculas:")
            print("[0] Retornar ao menu principal")
            print("[1] Criar")
            print("[2] Listar")
            print("[3] Excluir")
            print('-' * 50)
            try:
                opcao = int(input("Opção: "))
            except:
                print(SystemMessages.invalidOption)
            if opcao == 1:
                matriculasService.matricular()
                continue
            if opcao == 2:
                matriculasService.listarMatriculas()
                continue
            if opcao == 3:
                matriculasService.excluirMatriculas()
                continue
            if opcao == 0:
                break
            print(SystemMessages.invalidOption)

   