# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `__future__` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a future.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `annotations` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a annotations.
from __future__ import annotations

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `modelos` = atributo, método ou recurso acessado com o nome `modelos`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `CampoBanco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a CampoBanco.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `Tela` = classe que representa uma tela do projeto visual.
from .modelos import CampoBanco, Tela

# Armazena ou associa em `TIPOS_DE_CAMPO` o valor ou resultado definido nesta linha.
TIPOS_DE_CAMPO = {

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Entry` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Entry",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Text` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Text",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Combobox` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Combobox",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Checkbutton` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Checkbutton",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Radiobutton` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Radiobutton",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Spinbox` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Spinbox",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Scale` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Scale",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `PasswordEntry` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "PasswordEntry",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `EmailEntry` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "EmailEntry",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `DateEntry` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "DateEntry",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `TimeEntry` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "TimeEntry",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `ScrolledText` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "ScrolledText",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Menubutton` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "Menubutton",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `ToggleButton` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "ToggleButton",

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
}

# Define a rotina `_tipo_sql_do_componente`, responsável por executar a lógica relacionada a tipo sql do componente.
# `def` = define uma nova função ou um novo método.
# `_tipo_sql_do_componente` = função, método ou classe chamada para executar a operação relacionada a tipo sql do componente.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _tipo_sql_do_componente(componente) -> str:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Retorna o tipo SQLite mais adequado para o componente informado.` = texto literal utilizado nesta instrução.
    """Retorna o tipo SQLite mais adequado para o componente informado."""

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `Checkbutton` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `ToggleButton` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if componente.tipo in {"Checkbutton", "ToggleButton"}:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `INTEGER` = texto literal utilizado nesta instrução.
        return "INTEGER"

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Scale` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if componente.tipo == "Scale":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `REAL` = texto literal utilizado nesta instrução.
        return "REAL"

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Spinbox` = texto literal utilizado nesta instrução.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `validacao` = atributo, método ou recurso acessado com o nome `validacao`.
    # `Inteiro` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if componente.tipo == "Spinbox" or componente.validacao == "Inteiro":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `INTEGER` = texto literal utilizado nesta instrução.
        return "INTEGER"

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `validacao` = atributo, método ou recurso acessado com o nome `validacao`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Decimal` = texto literal utilizado nesta instrução.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `mascara` = atributo, método ou recurso acessado com o nome `mascara`.
    # `Moeda` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if componente.validacao == "Decimal" or componente.mascara == "Moeda":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `REAL` = texto literal utilizado nesta instrução.
        return "REAL"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `TEXT` = texto literal utilizado nesta instrução.
    return "TEXT"

# Define a rotina `sincronizar_campos_banco`, responsável por executar a lógica relacionada a sincronizar campos banco.
# `def` = define uma nova função ou um novo método.
# `sincronizar_campos_banco` = função, método ou classe chamada para executar a operação relacionada a sincronizar campos banco.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `Tela` = classe que representa uma tela do projeto visual.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `None` = representa ausência de valor.
def sincronizar_campos_banco(tela: Tela) -> None:

    # Inicia ou fornece um texto de múltiplas linhas utilizado por esta instrução.
    # string de múltiplas linhas = mantém um conteúdo textual contínuo que deve permanecer intacto para o funcionamento desta instrução.
    """Mantém as colunas do SQLite iguais aos campos existentes no Designer.

    A lista não funciona como um cadastro separado de colunas. Ela é reconstruída
    a partir dos componentes de entrada existentes naquele momento. Dessa forma,
    adicionar, renomear, copiar ou excluir um campo altera imediatamente a
    estrutura usada pelo código gerado e pelas Treeviews.
    """

    # Armazena ou associa em `anteriores` o valor ou resultado definido nesta linha.
    anteriores = {

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        campo.nome: campo

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
        for campo in tela.campos_banco

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `chave_primaria` = atributo, método ou recurso acessado com o nome `chave_primaria`.
        if campo.nome and not campo.chave_primaria

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    }

    # Armazena ou associa em `componentes_de_dados` o valor ou resultado definido nesta linha.
    componentes_de_dados = [

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        componente

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
        for componente in tela.componentes

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `TIPOS_DE_CAMPO` = constante utilizada para armazenar o valor relacionado a tipos de campo.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        if componente.tipo in TIPOS_DE_CAMPO and componente.nome.strip()

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `componentes_de_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes de dados.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not componentes_de_dados:

        # Armazena ou associa em `tela.campos_banco` o valor ou resultado definido nesta linha.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        tela.campos_banco = []

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Armazena ou associa em `novos_campos` o valor ou resultado definido nesta linha.
    # `novos_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a novos campos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `id` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `INTEGER` = texto literal utilizado nesta instrução.
    # `False` = representa o valor lógico falso.
    # `True` = representa o valor lógico verdadeiro.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    novos_campos = [CampoBanco("id", "INTEGER", False, True)]

    # Armazena ou associa em `nomes_utilizados` o valor ou resultado definido nesta linha.
    # `nomes_utilizados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes utilizados.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `id` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    nomes_utilizados = {"id"}

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `componentes_de_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes de dados.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for componente in componentes_de_dados:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_banco` = atributo, método ou recurso acessado com o nome `campo_banco`.
        # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not componente.campo_banco.strip():

            # Armazena ou associa em `componente.campo_banco` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `campo_banco` = atributo, método ou recurso acessado com o nome `campo_banco`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `nome` = atributo, método ou recurso acessado com o nome `nome`.
            # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            componente.campo_banco = componente.nome.strip()

        # Armazena ou associa em `nome_campo` o valor ou resultado definido nesta linha.
        # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_banco` = atributo, método ou recurso acessado com o nome `campo_banco`.
        # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        nome_campo = componente.campo_banco.strip()

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `nomes_utilizados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes utilizados.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not nome_campo or nome_campo in nomes_utilizados:

            # Encerra a iteração atual e continua o laço a partir da próxima repetição.
            # `continue` = interrompe a iteração atual e avança para a próxima repetição.
            continue

        # Armazena ou associa em `anterior` o valor ou resultado definido nesta linha.
        # `anterior` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a anterior.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `anteriores` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a anteriores.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        anterior = anteriores.get(nome_campo)

        # Armazena ou associa em `tipo` o valor ou resultado definido nesta linha.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `anterior` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a anterior.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `_tipo_sql_do_componente` = função, método ou classe chamada para executar a operação relacionada a tipo sql do componente.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        tipo = anterior.tipo if anterior else _tipo_sql_do_componente(componente)

        # Executa `novos_campos.append` com os argumentos informados para realizar a operação correspondente.
        novos_campos.append(

            # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
            CampoBanco(

                # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                nome=nome_campo,

                # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
                # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                tipo=tipo,

                # Define o argumento nomeado `obrigatorio` da chamada iniciada nas linhas anteriores.
                # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `obrigatorio` = atributo, método ou recurso acessado com o nome `obrigatorio`.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                obrigatorio=bool(componente.obrigatorio),

                # Define o argumento nomeado `chave_primaria` da chamada iniciada nas linhas anteriores.
                # `chave_primaria` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave primaria.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `False` = representa o valor lógico falso.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                chave_primaria=False,

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            )

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Executa `nomes_utilizados.add` com os argumentos informados para realizar a operação correspondente.
        # `nomes_utilizados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes utilizados.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `add` = função, método ou classe chamada para executar a operação relacionada a add.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        nomes_utilizados.add(nome_campo)

    # Armazena ou associa em `tela.campos_banco` o valor ou resultado definido nesta linha.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `novos_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a novos campos.
    tela.campos_banco = novos_campos
