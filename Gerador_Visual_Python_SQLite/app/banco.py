# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
import json

# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `sqlite3` = módulo da biblioteca padrão utilizado para trabalhar com bancos de dados SQLite.
import sqlite3

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `pathlib` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a pathlib.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `Path` = classe de pathlib utilizada para representar caminhos de arquivos e pastas.
from pathlib import Path

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `typing` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a typing.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `Optional` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Optional.
# `Tuple` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Tuple.
from typing import List, Optional, Tuple

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `modelos` = atributo, método ou recurso acessado com o nome `modelos`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
from .modelos import Projeto

# Define a classe `BancoProjetos`, responsável por agrupar dados e comportamentos relacionados a BancoProjetos.
# `class` = define uma nova classe.
# `BancoProjetos` = classe responsável pelo armazenamento dos projetos no banco SQLite.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
class BancoProjetos:

    # Define o método construtor responsável por inicializar os atributos, estados e recursos necessários do objeto.
    # `def` = define uma nova função ou um novo método.
    # `__init__` = método construtor executado automaticamente ao criar uma nova instância da classe.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `caminho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a caminho.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `|` = combina alternativas, inclusive tipos aceitos em uma anotação.
    # `None` = representa ausência de valor.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    def __init__(self, caminho: str | None = None):

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `caminho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a caminho.
        # `is` = compara a identidade entre objetos.
        # `None` = representa ausência de valor.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if caminho is None:

            # Armazena ou associa em `pasta` o valor ou resultado definido nesta linha.
            # `pasta` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a pasta.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Path` = classe de pathlib utilizada para representar caminhos de arquivos e pastas.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `home` = função, método ou classe chamada para executar a operação relacionada a home.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `/` = operador utilizado para realizar divisão.
            # `.gerador_visual_tkinter` = texto literal utilizado nesta instrução.
            pasta = Path.home() / ".gerador_visual_tkinter"

            # Executa `pasta.mkdir` com os argumentos informados para realizar a operação correspondente.
            # `pasta` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a pasta.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `mkdir` = função, método ou classe chamada para executar a operação relacionada a mkdir.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `parents` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a parents.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `True` = representa o valor lógico verdadeiro.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `exist_ok` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exist ok.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            pasta.mkdir(parents=True, exist_ok=True)

            # Armazena ou associa em `caminho` o valor ou resultado definido nesta linha.
            # `caminho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a caminho.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `str` = função ou tipo utilizado para representar e converter valores para texto.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `pasta` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a pasta.
            # `/` = operador utilizado para realizar divisão.
            # `projetos.db` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            caminho = str(pasta / "projetos.db")

        # Armazena ou associa em `self.caminho` o valor ou resultado definido nesta linha.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `caminho` = atributo, método ou recurso acessado com o nome `caminho`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `caminho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a caminho.
        self.caminho = caminho

        # Executa `self._criar_estrutura` com os argumentos informados para realizar a operação correspondente.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `_criar_estrutura` = função, método ou classe chamada para executar a operação relacionada a criar estrutura.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        self._criar_estrutura()

    # Define a rotina `conectar`, responsável por executar a lógica relacionada a conectar.
    # `def` = define uma nova função ou um novo método.
    # `conectar` = função, método ou classe chamada para executar a operação relacionada a conectar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def conectar(self):

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `sqlite3` = módulo da biblioteca padrão utilizado para trabalhar com bancos de dados SQLite.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `connect` = função, método ou classe chamada para executar a operação relacionada a connect.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `caminho` = atributo, método ou recurso acessado com o nome `caminho`.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return sqlite3.connect(self.caminho)

    # Define a rotina `_criar_estrutura`, responsável por executar a lógica relacionada a criar estrutura.
    # `def` = define uma nova função ou um novo método.
    # `_criar_estrutura` = função, método ou classe chamada para executar a operação relacionada a criar estrutura.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def _criar_estrutura(self):

        # Abre um contexto controlado para utilizar o recurso indicado e finalizar seu gerenciamento automaticamente ao sair do bloco.
        # `with` = inicia um gerenciador de contexto para controlar automaticamente o recurso utilizado no bloco.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `conectar` = função, método ou classe chamada para executar a operação relacionada a conectar.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
        # `conexao` = representa a conexão ativa com o banco de dados SQLite.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        with self.conectar() as conexao:

            # Executa `conexao.execute` com os argumentos informados para realizar a operação correspondente.
            conexao.execute(

                # Inicia ou fornece um texto de múltiplas linhas utilizado por esta instrução.
                # string de múltiplas linhas = mantém um conteúdo textual contínuo que deve permanecer intacto para o funcionamento desta instrução.
                """
                CREATE TABLE IF NOT EXISTS projetos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    conteudo_json TEXT NOT NULL,
                    atualizado_em TEXT DEFAULT CURRENT_TIMESTAMP
                )
                """

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            )

            # Executa `conexao.commit` com os argumentos informados para realizar a operação correspondente.
            # `conexao` = representa a conexão ativa com o banco de dados SQLite.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `commit` = função, método ou classe chamada para executar a operação relacionada a commit.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            conexao.commit()

    # Define a rotina `salvar`, responsável por executar a lógica relacionada a salvar.
    # `def` = define uma nova função ou um novo método.
    # `salvar` = função, método ou classe chamada para executar a operação relacionada a salvar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    def salvar(self, projeto: Projeto) -> int:

        # Armazena ou associa em `conteudo` o valor ou resultado definido nesta linha.
        # `conteudo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conteudo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `dumps` = função, método ou classe chamada para executar a operação relacionada a dumps.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `ensure_ascii` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ensure ascii.
        # `False` = representa o valor lógico falso.
        # `indent` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indent.
        # `2` = valor numérico associado a `indent` nesta instrução.
        conteudo = json.dumps(projeto.para_dict(), ensure_ascii=False, indent=2)

        # Abre um contexto controlado para utilizar o recurso indicado e finalizar seu gerenciamento automaticamente ao sair do bloco.
        # `with` = inicia um gerenciador de contexto para controlar automaticamente o recurso utilizado no bloco.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `conectar` = função, método ou classe chamada para executar a operação relacionada a conectar.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
        # `conexao` = representa a conexão ativa com o banco de dados SQLite.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        with self.conectar() as conexao:

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `projeto_id` = atributo, método ou recurso acessado com o nome `projeto_id`.
            # `is` = compara a identidade entre objetos.
            # `None` = representa ausência de valor.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if projeto.projeto_id is None:

                # Armazena ou associa em `cursor` o valor ou resultado definido nesta linha.
                cursor = conexao.execute(

                    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                    # `INSERT INTO projetos (nome, conteudo_json) VALUES (?, ?)` = texto literal utilizado nesta instrução.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    "INSERT INTO projetos (nome, conteudo_json) VALUES (?, ?)",

                    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    # `conteudo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conteudo.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    (projeto.nome, conteudo),

                # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                )

                # Armazena ou associa em `projeto.projeto_id` o valor ou resultado definido nesta linha.
                # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `projeto_id` = atributo, método ou recurso acessado com o nome `projeto_id`.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `cursor` = representa o cursor utilizado para executar comandos e acessar resultados do banco de dados.
                # `lastrowid` = atributo, método ou recurso acessado com o nome `lastrowid`.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                projeto.projeto_id = int(cursor.lastrowid)

            # Inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            else:

                # Executa `conexao.execute` com os argumentos informados para realizar a operação correspondente.
                conexao.execute(

                    # Inicia ou fornece um texto de múltiplas linhas utilizado por esta instrução.
                    # string de múltiplas linhas = mantém um conteúdo textual contínuo que deve permanecer intacto para o funcionamento desta instrução.
                    """
                    UPDATE projetos
                    SET nome = ?, conteudo_json = ?, atualizado_em = CURRENT_TIMESTAMP
                    WHERE id = ?
                    """,

                    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    # `conteudo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conteudo.
                    # `projeto_id` = atributo, método ou recurso acessado com o nome `projeto_id`.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    (projeto.nome, conteudo, projeto.projeto_id),

                # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                )

            # Executa `conexao.commit` com os argumentos informados para realizar a operação correspondente.
            # `conexao` = representa a conexão ativa com o banco de dados SQLite.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `commit` = função, método ou classe chamada para executar a operação relacionada a commit.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            conexao.commit()

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `projeto_id` = atributo, método ou recurso acessado com o nome `projeto_id`.
        return projeto.projeto_id

    # Define a rotina `salvar_como_novo`, responsável por executar a lógica relacionada a salvar como novo.
    # `def` = define uma nova função ou um novo método.
    # `salvar_como_novo` = função, método ou classe chamada para executar a operação relacionada a salvar como novo.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    def salvar_como_novo(self, projeto: Projeto) -> int:

        # Armazena ou associa em `projeto.projeto_id` o valor ou resultado definido nesta linha.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `projeto_id` = atributo, método ou recurso acessado com o nome `projeto_id`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `None` = representa ausência de valor.
        projeto.projeto_id = None

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `salvar` = função, método ou classe chamada para executar a operação relacionada a salvar.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return self.salvar(projeto)

    # Define a rotina `listar`, responsável por executar a lógica relacionada a listar.
    # `def` = define uma nova função ou um novo método.
    # `listar` = função, método ou classe chamada para executar a operação relacionada a listar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `Tuple` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Tuple.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def listar(self) -> List[Tuple[int, str, str]]:

        # Abre um contexto controlado para utilizar o recurso indicado e finalizar seu gerenciamento automaticamente ao sair do bloco.
        # `with` = inicia um gerenciador de contexto para controlar automaticamente o recurso utilizado no bloco.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `conectar` = função, método ou classe chamada para executar a operação relacionada a conectar.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
        # `conexao` = representa a conexão ativa com o banco de dados SQLite.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        with self.conectar() as conexao:

            # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
            return conexao.execute(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # texto literal = fornece o conteúdo textual utilizado por esta instrução.
                "SELECT id, nome, atualizado_em FROM projetos ORDER BY atualizado_em DESC, id DESC"

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `fetchall` = função, método ou classe chamada para executar a operação relacionada a fetchall.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            ).fetchall()

    # Define a rotina `carregar`, responsável por executar a lógica relacionada a carregar.
    # `def` = define uma nova função ou um novo método.
    # `carregar` = função, método ou classe chamada para executar a operação relacionada a carregar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Optional` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Optional.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    def carregar(self, projeto_id: int) -> Optional[Projeto]:

        # Abre um contexto controlado para utilizar o recurso indicado e finalizar seu gerenciamento automaticamente ao sair do bloco.
        # `with` = inicia um gerenciador de contexto para controlar automaticamente o recurso utilizado no bloco.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `conectar` = função, método ou classe chamada para executar a operação relacionada a conectar.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
        # `conexao` = representa a conexão ativa com o banco de dados SQLite.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        with self.conectar() as conexao:

            # Armazena ou associa em `linha` o valor ou resultado definido nesta linha.
            linha = conexao.execute(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `SELECT conteudo_json FROM projetos WHERE id = ?` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "SELECT conteudo_json FROM projetos WHERE id = ?",

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                (projeto_id,),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `fetchone` = função, método ou classe chamada para executar a operação relacionada a fetchone.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            ).fetchone()

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not linha:

            # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
            # `return` = encerra a rotina atual e devolve o valor especificado.
            # `None` = representa ausência de valor.
            return None

        # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Projeto` = classe que representa um projeto criado no Gerador Visual.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
        # `loads` = função, método ou classe chamada para executar a operação relacionada a loads.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        projeto = Projeto.de_dict(json.loads(linha[0]))

        # Armazena ou associa em `projeto.projeto_id` o valor ou resultado definido nesta linha.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `projeto_id` = atributo, método ou recurso acessado com o nome `projeto_id`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
        projeto.projeto_id = projeto_id

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        return projeto

    # Define a rotina `excluir`, responsável por executar a lógica relacionada a excluir.
    # `def` = define uma nova função ou um novo método.
    # `excluir` = função, método ou classe chamada para executar a operação relacionada a excluir.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `None` = representa ausência de valor.
    def excluir(self, projeto_id: int) -> None:

        # Abre um contexto controlado para utilizar o recurso indicado e finalizar seu gerenciamento automaticamente ao sair do bloco.
        # `with` = inicia um gerenciador de contexto para controlar automaticamente o recurso utilizado no bloco.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `conectar` = função, método ou classe chamada para executar a operação relacionada a conectar.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
        # `conexao` = representa a conexão ativa com o banco de dados SQLite.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        with self.conectar() as conexao:

            # Executa `conexao.execute` com os argumentos informados para realizar a operação correspondente.
            # `conexao` = representa a conexão ativa com o banco de dados SQLite.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `execute` = função, método ou classe chamada para executar a operação relacionada a execute.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `DELETE FROM projetos WHERE id = ?` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            conexao.execute("DELETE FROM projetos WHERE id = ?", (projeto_id,))

            # Executa `conexao.commit` com os argumentos informados para realizar a operação correspondente.
            # `conexao` = representa a conexão ativa com o banco de dados SQLite.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `commit` = função, método ou classe chamada para executar a operação relacionada a commit.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            conexao.commit()
