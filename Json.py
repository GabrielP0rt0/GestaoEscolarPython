import json
import os
from SystemMessages import SystemMessages

class JsonMethodes():
    """Classe responsável por operações de leitura e escrita em Json
    """    
    def operation(self, option, nameDB, registros = []):
        """Faz o Gerenciamento de qual função relacionada aos arquivos Json chamar

        Args:
            option (string): save para salvar ou criar um novo arquivo, read para ler um arquivo ja existente
            nameDB (string): Nome do arquivo a ser acessado ou criardo
            registros (list, optional): Registros a serem salvos no arquivo Json. Defaults to [].

        Returns:
            list: Para o caso de leitura a função retorna uma lista direto do arquivo json selecionado
        """        
        if option == "save":
            self.__save_json(nameDB,registros )
        elif option == "read":
            return self.__read_json(nameDB)
        else:
            print(SystemMessages.invalidOption)

    def __save_json(self, name, registros):
        """Salva o arquivo Json Correspondente

        Args:
            registros (list<dict>): Objeto a ser salvo no arquivo json correspondente
            name (string): Nome do arquivo json que sera o Banco de dados
        """        
        with open(name + ".json", "w") as dataBaseJson:
            json.dump(registros, dataBaseJson)
            dataBaseJson.close

    def __read_json(self, name):
        """Abre e faz a leitura do arquivo json

        Args:
            name (string): Nome do arquivo json que sera o banco de dados

        Returns:
            list<dict>: Conteúdo do arquivo json lido
        """        
        
        if os.path.exists(name + ".json") and os.stat(name + ".json").st_size > 0:
            with open(name + ".json", "r", encoding='utf-8') as dataBaseJson:
                data = json.load(dataBaseJson)
                return data
        else:
            return []