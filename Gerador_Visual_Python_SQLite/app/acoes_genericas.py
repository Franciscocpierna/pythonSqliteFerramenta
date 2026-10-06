# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `__future__` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a future.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `annotations` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a annotations.
from __future__ import annotations

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `typing` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a typing.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `Iterable` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Iterable.
from typing import Iterable

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `modelos` = atributo, método ou recurso acessado com o nome `modelos`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `CampoBanco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a CampoBanco.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `Componente` = classe que representa um componente inserido no Designer Visual.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `Tela` = classe que representa uma tela do projeto visual.
from .modelos import CampoBanco, Componente, Projeto, Tela

# Armazena ou associa em `TIPOS_ENTRADA` o valor ou resultado definido nesta linha.
TIPOS_ENTRADA = {

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Entry` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Text` = texto literal utilizado nesta instrução.
    # `Combobox` = texto literal utilizado nesta instrução.
    # `Checkbutton` = texto literal utilizado nesta instrução.
    "Entry", "Text", "Combobox", "Checkbutton",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Radiobutton` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Spinbox` = texto literal utilizado nesta instrução.
    # `Scale` = texto literal utilizado nesta instrução.
    "Radiobutton", "Spinbox", "Scale"

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
}

# Define a rotina `nomes_componentes_entrada`, responsável por executar a lógica relacionada a nomes componentes entrada.
# `def` = define uma nova função ou um novo método.
# `nomes_componentes_entrada` = identificador relacionado a um campo de entrada de dados, associado a nomes componentes entrada.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `Tela` = classe que representa uma tela do projeto visual.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `list` = função ou tipo utilizado para criar ou representar uma lista.
# `[` = abre uma lista, índice, acesso a elemento ou compreensão.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `]` = fecha a lista, índice, acesso a elemento ou compreensão.
def nomes_componentes_entrada(tela: Tela) -> list[str]:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
    # `TIPOS_ENTRADA` = identificador relacionado a um campo de entrada de dados, associado a TIPOS ENTRADA.
    # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return [c.nome for c in tela.componentes if c.tipo in TIPOS_ENTRADA and c.nome]

# Define a rotina `_tem_nome`, responsável por executar a lógica relacionada a tem nome.
# `def` = define uma nova função ou um novo método.
# `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `Tela` = classe que representa uma tela do projeto visual.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `bool` = tipo lógico que representa os valores verdadeiro ou falso.
def _tem_nome(tela: Tela, nome: str) -> bool:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `any` = função, método ou classe chamada para executar a operação relacionada a any.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return any(c.nome == nome for c in tela.componentes)

# Define a rotina `_tipo_sql_componente`, responsável por executar a lógica relacionada a tipo sql componente.
# `def` = define uma nova função ou um novo método.
# `_tipo_sql_componente` = função, método ou classe chamada para executar a operação relacionada a tipo sql componente.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `Componente` = classe que representa um componente inserido no Designer Visual.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
def _tipo_sql_componente(comp: Componente) -> str:

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Checkbutton` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if comp.tipo == "Checkbutton":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `INTEGER` = texto literal utilizado nesta instrução.
        return "INTEGER"

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Scale` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if comp.tipo == "Scale":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `REAL` = texto literal utilizado nesta instrução.
        return "REAL"

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Spinbox` = texto literal utilizado nesta instrução.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `validacao` = atributo, método ou recurso acessado com o nome `validacao`.
    # `Inteiro` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if comp.tipo == "Spinbox" or comp.validacao == "Inteiro":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `INTEGER` = texto literal utilizado nesta instrução.
        return "INTEGER"

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `validacao` = atributo, método ou recurso acessado com o nome `validacao`.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Decimal` = texto literal utilizado nesta instrução.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `mascara` = atributo, método ou recurso acessado com o nome `mascara`.
    # `Moeda` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if comp.validacao == "Decimal" or comp.mascara == "Moeda":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `REAL` = texto literal utilizado nesta instrução.
        return "REAL"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `TEXT` = texto literal utilizado nesta instrução.
    return "TEXT"

# Define a rotina `garantir_campos_banco_automaticos`, responsável por executar a lógica relacionada a garantir campos banco automaticos.
# `def` = define uma nova função ou um novo método.
# `garantir_campos_banco_automaticos` = função, método ou classe chamada para executar a operação relacionada a garantir campos banco automaticos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `Tela` = classe que representa uma tela do projeto visual.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `None` = representa ausência de valor.
def garantir_campos_banco_automaticos(tela: Tela) -> None:

    # Inicia ou fornece um texto de múltiplas linhas utilizado por esta instrução.
    # string de múltiplas linhas = mantém um conteúdo textual contínuo que deve permanecer intacto para o funcionamento desta instrução.
    """Cria colunas SQLite a partir dos componentes de entrada.

    O usuário ainda pode alterar o "Campo do banco" manualmente. Quando ele
    não informa um campo, o nome do próprio componente é usado como coluna.
    """

    # Armazena ou associa em `tem_campos_definidos` o valor ou resultado definido nesta linha.
    # `tem_campos_definidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tem campos definidos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `any` = função, método ou classe chamada para executar a operação relacionada a any.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
    tem_campos_definidos = any(c.nome.strip() for c in tela.campos_banco)

    # Armazena ou associa em `tem_componentes_de_entrada` o valor ou resultado definido nesta linha.
    tem_componentes_de_entrada = any(

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `TIPOS_ENTRADA` = identificador relacionado a um campo de entrada de dados, associado a TIPOS ENTRADA.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        comp.tipo in TIPOS_ENTRADA and bool(comp.nome.strip())

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
        for comp in tela.componentes

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `tem_campos_definidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tem campos definidos.
    # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
    # `tem_componentes_de_entrada` = identificador relacionado a um campo de entrada de dados, associado a tem componentes de entrada.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not tem_campos_definidos and not tem_componentes_de_entrada:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Armazena ou associa em `existentes` o valor ou resultado definido nesta linha.
    # `existentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a existentes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    existentes = {c.nome for c in tela.campos_banco if c.nome}

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `any` = função, método ou classe chamada para executar a operação relacionada a any.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `chave_primaria` = atributo, método ou recurso acessado com o nome `chave_primaria`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not any(c.chave_primaria for c in tela.campos_banco):

        # Executa `tela.campos_banco.insert` com os argumentos informados para realizar a operação correspondente.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
        # `insert` = função, método ou classe chamada para executar a operação relacionada a insert.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `id` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `False` = representa o valor lógico falso.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        tela.campos_banco.insert(0, CampoBanco("id", "INTEGER", False, True))

        # Executa `existentes.add` com os argumentos informados para realizar a operação correspondente.
        # `existentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a existentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `add` = função, método ou classe chamada para executar a operação relacionada a add.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `id` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        existentes.add("id")

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for comp in tela.componentes:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `TIPOS_ENTRADA` = identificador relacionado a um campo de entrada de dados, associado a TIPOS ENTRADA.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if comp.tipo not in TIPOS_ENTRADA or not comp.nome:

            # Encerra a iteração atual e continua o laço a partir da próxima repetição.
            # `continue` = interrompe a iteração atual e avança para a próxima repetição.
            continue

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_banco` = atributo, método ou recurso acessado com o nome `campo_banco`.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not comp.campo_banco:

            # Armazena ou associa em `comp.campo_banco` o valor ou resultado definido nesta linha.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `campo_banco` = atributo, método ou recurso acessado com o nome `campo_banco`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `nome` = atributo, método ou recurso acessado com o nome `nome`.
            comp.campo_banco = comp.nome

        # Armazena ou associa em `nome_campo` o valor ou resultado definido nesta linha.
        # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_banco` = atributo, método ou recurso acessado com o nome `campo_banco`.
        # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        nome_campo = comp.campo_banco.strip()

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `existentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a existentes.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if nome_campo and nome_campo not in existentes:

            # Executa `tela.campos_banco.append` com os argumentos informados para realizar a operação correspondente.
            tela.campos_banco.append(

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
                    # `_tipo_sql_componente` = função, método ou classe chamada para executar a operação relacionada a tipo sql componente.
                    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    tipo=_tipo_sql_componente(comp),

                    # Define o argumento nomeado `obrigatorio` da chamada iniciada nas linhas anteriores.
                    # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
                    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `obrigatorio` = atributo, método ou recurso acessado com o nome `obrigatorio`.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    obrigatorio=bool(comp.obrigatorio),

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

            # Executa `existentes.add` com os argumentos informados para realizar a operação correspondente.
            # `existentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a existentes.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `add` = função, método ou classe chamada para executar a operação relacionada a add.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `nome_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome campo.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            existentes.add(nome_campo)

# Define a rotina `_configurar_calculo`, responsável por executar a lógica relacionada a configurar calculo.
def _configurar_calculo(

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Componente` = classe que representa um componente inserido no Designer Visual.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    comp: Componente,

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Iterable` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Iterable.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    campos: Iterable[str],

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    resultado: str,

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    operador: str,

    # Declara `expressao` com anotação de tipo e armazena o valor definido nesta linha.
    # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    expressao: str = "",

    # Declara `formato` com anotação de tipo e armazena o valor definido nesta linha.
    # `formato` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    formato: str = "",

    # Declara `resultado_2` com anotação de tipo e armazena o valor definido nesta linha.
    # `resultado_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado 2.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    resultado_2: str = "",

    # Declara `expressao_2` com anotação de tipo e armazena o valor definido nesta linha.
    # `expressao_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao 2.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    expressao_2: str = "",

# Executa a instrução desta linha como parte da lógica atual do programa.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `None` = representa ausência de valor.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
) -> None:

    # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `acao` = atributo, método ou recurso acessado com o nome `acao`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Calcular com campos` = texto literal utilizado nesta instrução.
    comp.acao = "Calcular com campos"

    # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    comp.campos_acao = [x for x in campos if x]

    # Armazena ou associa em `comp.campo_resultado` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `campo_resultado` = atributo, método ou recurso acessado com o nome `campo_resultado`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado.
    comp.campo_resultado = resultado

    # Armazena ou associa em `comp.operador` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `operador` = atributo, método ou recurso acessado com o nome `operador`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
    comp.operador = operador

    # Armazena ou associa em `comp.expressao` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `expressao` = atributo, método ou recurso acessado com o nome `expressao`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
    comp.expressao = expressao

    # Armazena ou associa em `comp.formato_resultado` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `formato_resultado` = atributo, método ou recurso acessado com o nome `formato_resultado`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `formato` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato.
    comp.formato_resultado = formato

    # Armazena ou associa em `comp.campo_resultado_2` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `campo_resultado_2` = atributo, método ou recurso acessado com o nome `campo_resultado_2`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `resultado_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado 2.
    comp.campo_resultado_2 = resultado_2

    # Armazena ou associa em `comp.expressao_2` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `expressao_2` = atributo, método ou recurso acessado com o nome `expressao_2`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `expressao_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao 2.
    comp.expressao_2 = expressao_2

# Define a rotina `migrar_acao_legada`, responsável por executar a lógica relacionada a migrar acao legada.
# `def` = define uma nova função ou um novo método.
# `migrar_acao_legada` = função, método ou classe chamada para executar a operação relacionada a migrar acao legada.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `Componente` = classe que representa um componente inserido no Designer Visual.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
# `Tela` = classe que representa uma tela do projeto visual.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `None` = representa ausência de valor.
def migrar_acao_legada(comp: Componente, tela: Tela) -> None:

    # Inicia ou fornece um texto de múltiplas linhas utilizado por esta instrução.
    # string de múltiplas linhas = mantém um conteúdo textual contínuo que deve permanecer intacto para o funcionamento desta instrução.
    """Transforma os exemplos antigos em configurações genéricas.

    Depois da migração não há ações como "Calcular IMC" ou
    "Calcular desconto". Todos usam os mesmos blocos reutilizáveis.
    """

    # Armazena ou associa em `acao` o valor ou resultado definido nesta linha.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `acao` = atributo, método ou recurso acessado com o nome `acao`.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `Nenhuma` = texto literal utilizado nesta instrução.
    acao = comp.acao or "Nenhuma"

    # Armazena ou associa em `entradas` o valor ou resultado definido nesta linha.
    # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `nomes_componentes_entrada` = identificador relacionado a um campo de entrada de dados, associado a nomes componentes entrada.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    entradas = nomes_componentes_entrada(tela)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Salvar registro` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Salvar registro":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        comp.acao = "Cadastrar no SQLite"

        # Armazena ou associa em `comp.texto` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `texto` = atributo, método ou recurso acessado com o nome `texto`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        comp.texto = "Cadastrar no SQLite"

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `list` = função ou tipo utilizado para criar ou representar uma lista.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        comp.campos_acao = list(entradas)

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Atualizar registro` = texto literal utilizado nesta instrução.
    # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Atualizar registro" and not comp.campos_acao:

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `list` = função ou tipo utilizado para criar ou representar uma lista.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        comp.campos_acao = list(entradas)

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Limpar formulário` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Limpar formulário":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
        comp.acao = "Limpar campos selecionados"

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `list` = função ou tipo utilizado para criar ou representar uma lista.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        comp.campos_acao = list(entradas)

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calculadora: inserir tecla` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calculadora: inserir tecla":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Inserir valor em campo` = texto literal utilizado nesta instrução.
        comp.acao = "Inserir valor em campo"

        # Armazena ou associa em `comp.campo_resultado` o valor ou resultado definido nesta linha.
        comp.campo_resultado = (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `visor` = texto literal utilizado nesta instrução.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            "visor" if _tem_nome(tela, "visor")

            # Executa `else` com os argumentos informados para realizar a operação correspondente.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # texto vazio = representa uma string sem caracteres.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            else (entradas[0] if entradas else "")

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Armazena ou associa em `comp.valor_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `valor_acao` = atributo, método ou recurso acessado com o nome `valor_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # texto vazio = representa uma string sem caracteres.
        comp.valor_acao = ""

        # Armazena ou associa em `comp.modo_insercao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `modo_insercao` = atributo, método ou recurso acessado com o nome `modo_insercao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Adicionar` = texto literal utilizado nesta instrução.
        comp.modo_insercao = "Adicionar"

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calculadora: limpar` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calculadora: limpar":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
        comp.acao = "Limpar campos selecionados"

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        comp.campos_acao = (

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `visor` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `list` = função ou tipo utilizado para criar ou representar uma lista.
            # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
            ["visor"] if _tem_nome(tela, "visor") else list(entradas)

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calculadora: calcular` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calculadora: calcular":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular expressão de um campo` = texto literal utilizado nesta instrução.
        comp.acao = "Calcular expressão de um campo"

        # Armazena ou associa em `alvo` o valor ou resultado definido nesta linha.
        alvo = (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `visor` = texto literal utilizado nesta instrução.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            "visor" if _tem_nome(tela, "visor")

            # Executa `else` com os argumentos informados para realizar a operação correspondente.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # texto vazio = representa uma string sem caracteres.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            else (entradas[0] if entradas else "")

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `alvo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        comp.campos_acao = [alvo] if alvo else []

        # Armazena ou associa em `comp.campo_resultado` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_resultado` = atributo, método ou recurso acessado com o nome `campo_resultado`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `alvo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo.
        comp.campo_resultado = alvo

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `historico` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if _tem_nome(tela, "historico"):

            # Armazena ou associa em `comp.alvo_auxiliar` o valor ou resultado definido nesta linha.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `alvo_auxiliar` = atributo, método ou recurso acessado com o nome `alvo_auxiliar`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `historico` = texto literal utilizado nesta instrução.
            comp.alvo_auxiliar = "historico"

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            comp,

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `numero_1` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `numero_2` = texto literal utilizado nesta instrução.
            # `operacao` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            ["numero_1", "numero_2", "operacao"],

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `resultado` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Operação definida no Campo 3` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Operação definida no Campo 3",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular média escolar` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular média escolar":

        # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
        campos = [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nota_1` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `nota_2` = texto literal utilizado nesta instrução.
            # `nota_3` = texto literal utilizado nesta instrução.
            # `nota_4` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            x for x in ["nota_1", "nota_2", "nota_3", "nota_4"]

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            if _tem_nome(tela, x)

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        ]

        # Armazena ou associa em `destino` o valor ou resultado definido nesta linha.
        # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `media` = texto literal utilizado nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `resultado` = texto literal utilizado nesta instrução.
        destino = "media" if _tem_nome(tela, "media") else "resultado"

        # Armazena ou associa em `destino_2` o valor ou resultado definido nesta linha.
        # `destino_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino 2.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `situacao` = texto literal utilizado nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `_tem_nome` = função, método ou classe chamada para executar a operação relacionada a tem nome.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # texto vazio = representa uma string sem caracteres.
        destino_2 = "situacao" if _tem_nome(tela, "situacao") else ""

        # Armazena ou associa em `expr_2` o valor ou resultado definido nesta linha.
        expr_2 = (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `'Aprovado' if R >= 7 else ` = texto literal utilizado nesta instrução.
            "'Aprovado' if R >= 7 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('Recuperação' if R >= 5 else 'Reprovado')` = texto literal utilizado nesta instrução.
            "('Recuperação' if R >= 5 else 'Reprovado')"

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `destino_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino 2.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # texto vazio = representa uma string sem caracteres.
        ) if destino_2 else ""

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
            # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
            # `Média` = texto literal utilizado nesta instrução.
            comp, campos, destino, "Média",

            # Armazena ou associa em `resultado_2` o valor ou resultado definido nesta linha.
            # `resultado_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado 2.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `destino_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino 2.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `expressao_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao 2.
            # `expr_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expr 2.
            resultado_2=destino_2, expressao_2=expr_2,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular IMC` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular IMC":

        # Armazena ou associa em `expr` o valor ou resultado definido nesta linha.
        expr = (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `str(round(A / (B * B), 2)) + ' - ' + ` = texto literal utilizado nesta instrução.
            "str(round(A / (B * B), 2)) + ' - ' + "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('Baixo peso' if (A / (B * B)) < 18.5 else ` = texto literal utilizado nesta instrução.
            "('Baixo peso' if (A / (B * B)) < 18.5 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('Peso adequado' if (A / (B * B)) < 25 else ` = texto literal utilizado nesta instrução.
            "('Peso adequado' if (A / (B * B)) < 25 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('Sobrepeso' if (A / (B * B)) < 30 else 'Obesidade')))` = texto literal utilizado nesta instrução.
            "('Sobrepeso' if (A / (B * B)) < 30 else 'Obesidade')))"

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `peso` = texto literal utilizado nesta instrução.
            # `altura` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["peso", "altura"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `expr` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expr.
            "Expressão personalizada", expr,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular desconto` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular desconto":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `preco` = texto literal utilizado nesta instrução.
            # `percentual` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["preco", "percentual"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Expressão personalizada",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `round(A * (1 - B / 100), 2)` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "round(A * (1 - B / 100), 2)",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular comissão` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular comissão":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `vendas` = texto literal utilizado nesta instrução.
            # `percentual` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["vendas", "percentual"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `round(A * B / 100, 2)` = texto literal utilizado nesta instrução.
            "Expressão personalizada", "round(A * B / 100, 2)",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Converter temperatura` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Converter temperatura":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `celsius` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["celsius"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `round(A * 9 / 5 + 32, 2)` = texto literal utilizado nesta instrução.
            "Expressão personalizada", "round(A * 9 / 5 + 32, 2)",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Converter quilômetros para milhas` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Converter quilômetros para milhas":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `quilometros` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["quilometros"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `round(A * 0.621371, 3)` = texto literal utilizado nesta instrução.
            "Expressão personalizada", "round(A * 0.621371, 3)",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Gerar tabuada` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Gerar tabuada":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Gerar lista por repetição` = texto literal utilizado nesta instrução.
        comp.acao = "Gerar lista por repetição"

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `numero` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        comp.campos_acao = ["numero"]

        # Armazena ou associa em `comp.campo_resultado` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_resultado` = atributo, método ou recurso acessado com o nome `campo_resultado`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `resultado` = texto literal utilizado nesta instrução.
        comp.campo_resultado = "resultado"

        # Armazena ou associa em `comp.operador` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `operador` = atributo, método ou recurso acessado com o nome `operador`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Multiplicar` = texto literal utilizado nesta instrução.
        comp.operador = "Multiplicar"

        # Armazena ou associa em `comp.repeticao_inicio` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `repeticao_inicio` = atributo, método ou recurso acessado com o nome `repeticao_inicio`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `1` = texto literal utilizado nesta instrução.
        comp.repeticao_inicio = "1"

        # Armazena ou associa em `comp.repeticao_fim` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `repeticao_fim` = atributo, método ou recurso acessado com o nome `repeticao_fim`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `10` = texto literal utilizado nesta instrução.
        comp.repeticao_fim = "10"

        # Armazena ou associa em `comp.expressao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `expressao` = atributo, método ou recurso acessado com o nome `expressao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `{A} x {N} = {resultado}` = texto literal utilizado nesta instrução.
        comp.expressao = "{A} x {N} = {resultado}"

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Verificar par ou ímpar` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Verificar par ou ímpar":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `numero` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["numero"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Expressão personalizada",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `'Par' if int(A) % 2 == 0 else 'Ímpar'` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "'Par' if int(A) % 2 == 0 else 'Ímpar'",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Verificar maioridade` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Verificar maioridade":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Aplicar condição` = texto literal utilizado nesta instrução.
        comp.acao = "Aplicar condição"

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `idade` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        comp.campos_acao = ["idade"]

        # Armazena ou associa em `comp.campo_resultado` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_resultado` = atributo, método ou recurso acessado com o nome `campo_resultado`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `resultado` = texto literal utilizado nesta instrução.
        comp.campo_resultado = "resultado"

        # Armazena ou associa em `comp.comparador` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `comparador` = atributo, método ou recurso acessado com o nome `comparador`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `>=` = texto literal utilizado nesta instrução.
        comp.comparador = ">="

        # Armazena ou associa em `comp.valor_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `valor_acao` = atributo, método ou recurso acessado com o nome `valor_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `18` = texto literal utilizado nesta instrução.
        comp.valor_acao = "18"

        # Armazena ou associa em `comp.resultado_verdadeiro` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `resultado_verdadeiro` = atributo, método ou recurso acessado com o nome `resultado_verdadeiro`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Maior de idade` = texto literal utilizado nesta instrução.
        comp.resultado_verdadeiro = "Maior de idade"

        # Armazena ou associa em `comp.resultado_falso` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `resultado_falso` = atributo, método ou recurso acessado com o nome `resultado_falso`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Menor de idade` = texto literal utilizado nesta instrução.
        comp.resultado_falso = "Menor de idade"

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Classificar nota` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Classificar nota":

        # Armazena ou associa em `expr` o valor ou resultado definido nesta linha.
        expr = (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `'A' if A >= 9 else ` = texto literal utilizado nesta instrução.
            "'A' if A >= 9 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('B' if A >= 7 else ` = texto literal utilizado nesta instrução.
            "('B' if A >= 7 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('C' if A >= 5 else ` = texto literal utilizado nesta instrução.
            "('C' if A >= 5 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('D' if A >= 3 else 'E')))` = texto literal utilizado nesta instrução.
            "('D' if A >= 3 else 'E')))"

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nota` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["nota"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `expr` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expr.
            "Expressão personalizada", expr,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Conceito {resultado}` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Conceito {resultado}",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular salário líquido` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular salário líquido":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `salario_bruto` = texto literal utilizado nesta instrução.
            # `desconto_percentual` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["salario_bruto", "desconto_percentual"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Expressão personalizada",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `round(A * (1 - B / 100), 2)` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "round(A * (1 - B / 100), 2)",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular pagamento por horas` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular pagamento por horas":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `horas` = texto literal utilizado nesta instrução.
            # `valor_hora` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            # `Multiplicar` = texto literal utilizado nesta instrução.
            comp, ["horas", "valor_hora"], "resultado", "Multiplicar"

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular consumo de combustível` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular consumo de combustível":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `distancia` = texto literal utilizado nesta instrução.
            # `litros` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            # `Dividir` = texto literal utilizado nesta instrução.
            comp, ["distancia", "litros"], "resultado", "Dividir"

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular troco` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular troco":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `total_compra` = texto literal utilizado nesta instrução.
            # `valor_recebido` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["total_compra", "valor_recebido"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `round(B - A, 2)` = texto literal utilizado nesta instrução.
            "Expressão personalizada", "round(B - A, 2)",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular parcelamento` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular parcelamento":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `valor_total` = texto literal utilizado nesta instrução.
            # `parcelas` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            # `Dividir` = texto literal utilizado nesta instrução.
            comp, ["valor_total", "parcelas"], "resultado", "Dividir"

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Calcular orçamento` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Calcular orçamento":

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            comp,

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `quantidade` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `preco_unitario` = texto literal utilizado nesta instrução.
            # `desconto_percentual` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            ["quantidade", "preco_unitario", "desconto_percentual"],

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `resultado` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Expressão personalizada",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `round(A * B * (1 - C / 100), 2)` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "round(A * B * (1 - C / 100), 2)",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Verificar estoque mínimo` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Verificar estoque mínimo":

        # Armazena ou associa em `comp.acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Aplicar condição` = texto literal utilizado nesta instrução.
        comp.acao = "Aplicar condição"

        # Armazena ou associa em `comp.campos_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_acao` = atributo, método ou recurso acessado com o nome `campos_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `quantidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `estoque_minimo` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        comp.campos_acao = ["quantidade", "estoque_minimo"]

        # Armazena ou associa em `comp.campo_resultado` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campo_resultado` = atributo, método ou recurso acessado com o nome `campo_resultado`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `resultado` = texto literal utilizado nesta instrução.
        comp.campo_resultado = "resultado"

        # Armazena ou associa em `comp.comparador` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `comparador` = atributo, método ou recurso acessado com o nome `comparador`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `<=` = texto literal utilizado nesta instrução.
        comp.comparador = "<="

        # Armazena ou associa em `comp.valor_acao` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `valor_acao` = atributo, método ou recurso acessado com o nome `valor_acao`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # texto vazio = representa uma string sem caracteres.
        comp.valor_acao = ""

        # Armazena ou associa em `comp.resultado_verdadeiro` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `resultado_verdadeiro` = atributo, método ou recurso acessado com o nome `resultado_verdadeiro`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `REPOR ESTOQUE` = texto literal utilizado nesta instrução.
        comp.resultado_verdadeiro = "REPOR ESTOQUE"

        # Armazena ou associa em `comp.resultado_falso` o valor ou resultado definido nesta linha.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `resultado_falso` = atributo, método ou recurso acessado com o nome `resultado_falso`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Estoque suficiente` = texto literal utilizado nesta instrução.
        comp.resultado_falso = "Estoque suficiente"

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Avaliar satisfação` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Avaliar satisfação":

        # Armazena ou associa em `expr` o valor ou resultado definido nesta linha.
        expr = (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `'Excelente' if A >= 9 else ` = texto literal utilizado nesta instrução.
            "'Excelente' if A >= 9 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('Bom' if A >= 7 else ` = texto literal utilizado nesta instrução.
            "('Bom' if A >= 7 else "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `('Regular' if A >= 5 else 'Insatisfeito'))` = texto literal utilizado nesta instrução.
            "('Regular' if A >= 5 else 'Insatisfeito'))"

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nota` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `resultado` = texto literal utilizado nesta instrução.
            comp, ["nota"], "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `expr` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expr.
            "Expressão personalizada", expr,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Corrigir questionário` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if acao == "Corrigir questionário":

        # Armazena ou associa em `expr` o valor ou resultado definido nesta linha.
        expr = (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `(1 if upper(str(A)) == 'B' else 0) + ` = texto literal utilizado nesta instrução.
            "(1 if upper(str(A)) == 'B' else 0) + "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `(1 if upper(str(B)) == 'C' else 0) + ` = texto literal utilizado nesta instrução.
            "(1 if upper(str(B)) == 'C' else 0) + "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `(1 if upper(str(C)) == 'A' else 0)` = texto literal utilizado nesta instrução.
            "(1 if upper(str(C)) == 'A' else 0)"

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Executa `_configurar_calculo` com os argumentos informados para realizar a operação correspondente.
        _configurar_calculo(

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            comp,

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `resposta_1` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `resposta_2` = texto literal utilizado nesta instrução.
            # `resposta_3` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            ["resposta_1", "resposta_2", "resposta_3"],

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `resultado` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "resultado",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Expressão personalizada",

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `expr` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expr.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            expr,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `{resultado} de 3 respostas corretas` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "{resultado} de 3 respostas corretas",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

# Define a rotina `garantir_botao_cadastro`, responsável por executar a lógica relacionada a garantir botao cadastro.
# `def` = define uma nova função ou um novo método.
# `garantir_botao_cadastro` = identificador relacionado a um botão da interface, associado a garantir botao cadastro.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `Tela` = classe que representa uma tela do projeto visual.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `None` = representa ausência de valor.
def garantir_botao_cadastro(tela: Tela) -> None:

    # Armazena ou associa em `entradas` o valor ou resultado definido nesta linha.
    # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `nomes_componentes_entrada` = identificador relacionado a um campo de entrada de dados, associado a nomes componentes entrada.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    entradas = nomes_componentes_entrada(tela)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not entradas:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    if any(

        # Armazena ou associa em `c.tipo` o valor ou resultado definido nesta linha.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Button` = texto literal utilizado nesta instrução.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        c.tipo == "Button" and

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Salvar registro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        c.acao in {"Cadastrar no SQLite", "Salvar registro"}

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
        for c in tela.componentes

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    ):

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        return

    # Armazena ou associa em `max_bottom` o valor ou resultado definido nesta linha.
    # `max_bottom` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a max bottom.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `y` = atributo, método ou recurso acessado com o nome `y`.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `altura` = atributo, método ou recurso acessado com o nome `altura`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `default` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default.
    # `40` = valor numérico associado a `default` nesta instrução.
    max_bottom = max((c.y + c.altura for c in tela.componentes), default=40)

    # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `max_bottom` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a max bottom.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `18` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y = max_bottom + 18

    # Armazena ou associa em `tela.altura` o valor ou resultado definido nesta linha.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `altura` = atributo, método ou recurso acessado com o nome `altura`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `70` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    tela.altura = max(tela.altura, y + 70)

    # Executa `tela.componentes.append` com os argumentos informados para realizar a operação correspondente.
    tela.componentes.append(

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
            # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            tipo="Button",

            # Define o argumento nomeado `x` da chamada iniciada nas linhas anteriores.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `35` = coordenada numérica utilizada no eixo X nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            x=35,

            # Define o argumento nomeado `y` da chamada iniciada nas linhas anteriores.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            y=y,

            # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `210` = valor numérico utilizado para definir a largura nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            largura=210,

            # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `40` = valor numérico utilizado para definir a altura nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            altura=40,

            # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `btn_cadastrar_sqlite` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            nome="btn_cadastrar_sqlite",

            # Define o argumento nomeado `texto` da chamada iniciada nas linhas anteriores.
            # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            texto="Cadastrar no SQLite",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Cadastrar no SQLite",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `list` = função ou tipo utilizado para criar ou representar uma lista.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `entradas` = identificador relacionado a um campo de entrada de dados, associado a entradas.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campos_acao=list(entradas),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `_criar_tela_registro_sqlite`, responsável por executar a lógica relacionada a criar tela registro sqlite.
# `def` = define uma nova função ou um novo método.
# `_criar_tela_registro_sqlite` = função, método ou classe chamada para executar a operação relacionada a criar tela registro sqlite.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _criar_tela_registro_sqlite() -> Tela:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Tela mínima para projetos que originalmente só possuem navegação.` = texto literal utilizado nesta instrução.
    """Tela mínima para projetos que originalmente só possuem navegação."""

    # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
    tela = Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Registro SQLite` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Registro SQLite",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Registro SQLite` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Registro SQLite",

        # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `1000` = valor numérico utilizado para definir a largura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        largura=1000,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `650` = valor numérico utilizado para definir a altura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=650,

        # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `registros_gerais` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="registros_gerais",

        # Define o argumento nomeado `campos_banco` da chamada iniciada nas linhas anteriores.
        # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
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
        campos_banco=[CampoBanco("id", "INTEGER", False, True)],

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Armazena ou associa em `tela.componentes` o valor ou resultado definido nesta linha.
    tela.componentes = [

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Armazena ou associa em `tipo` o valor ou resultado definido nesta linha.
            # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Label` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `40` = coordenada numérica utilizada no eixo X nesta instrução.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `35` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `600` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `45` = valor numérico utilizado para definir a altura nesta instrução.
            tipo="Label", x=40, y=35, largura=600, altura=45,

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `titulo` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
            # `Registro SQLite` = texto literal utilizado nesta instrução.
            nome="titulo", texto="Registro SQLite",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Armazena ou associa em `tipo` o valor ou resultado definido nesta linha.
            # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Label` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `40` = coordenada numérica utilizada no eixo X nesta instrução.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `115` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `160` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `30` = valor numérico utilizado para definir a altura nesta instrução.
            tipo="Label", x=40, y=115, largura=160, altura=30,

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `lbl_descricao` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
            # `Descrição` = texto literal utilizado nesta instrução.
            nome="lbl_descricao", texto="Descrição",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Armazena ou associa em `tipo` o valor ou resultado definido nesta linha.
            # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Entry` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `200` = coordenada numérica utilizada no eixo X nesta instrução.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `110` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `430` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `36` = valor numérico utilizado para definir a altura nesta instrução.
            tipo="Entry", x=200, y=110, largura=430, altura=36,

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `descricao` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
            nome="descricao", campo_banco="descricao",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Armazena ou associa em `tipo` o valor ou resultado definido nesta linha.
            # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `200` = coordenada numérica utilizada no eixo X nesta instrução.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `175` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `210` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `42` = valor numérico utilizado para definir a altura nesta instrução.
            tipo="Button", x=200, y=175, largura=210, altura=42,

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `btn_cadastrar_sqlite` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            nome="btn_cadastrar_sqlite", texto="Cadastrar no SQLite",

            # Armazena ou associa em `acao` o valor ou resultado definido nesta linha.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `descricao` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            acao="Cadastrar no SQLite", campos_acao=["descricao"],

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Armazena ou associa em `tipo` o valor ou resultado definido nesta linha.
            # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `425` = coordenada numérica utilizada no eixo X nesta instrução.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `175` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `150` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `42` = valor numérico utilizado para definir a altura nesta instrução.
            tipo="Button", x=425, y=175, largura=150, altura=42,

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `btn_limpar` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
            # `Limpar` = texto literal utilizado nesta instrução.
            nome="btn_limpar", texto="Limpar",

            # Armazena ou associa em `acao` o valor ou resultado definido nesta linha.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `descricao` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            acao="Limpar campos selecionados", campos_acao=["descricao"],

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Executa `garantir_campos_banco_automaticos` com os argumentos informados para realizar a operação correspondente.
    # `garantir_campos_banco_automaticos` = função, método ou classe chamada para executar a operação relacionada a garantir campos banco automaticos.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    garantir_campos_banco_automaticos(tela)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    return tela

# Define a rotina `normalizar_projeto`, responsável por executar a lógica relacionada a normalizar projeto.
def normalizar_projeto(

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    projeto: Projeto,

    # Declara `adicionar_botao_cadastro` com anotação de tipo e armazena o valor definido nesta linha.
    # `adicionar_botao_cadastro` = identificador relacionado a um botão da interface, associado a adicionar botao cadastro.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    adicionar_botao_cadastro: bool = True,

# Executa a instrução desta linha como parte da lógica atual do programa.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
) -> Projeto:

    # Inicia ou fornece um texto de múltiplas linhas utilizado por esta instrução.
    # string de múltiplas linhas = mantém um conteúdo textual contínuo que deve permanecer intacto para o funcionamento desta instrução.
    """Compatibiliza projetos antigos com o motor genérico.

    Nos modelos e nos 30 exemplos, garante ao menos um botão que grava no
    SQLite. Em um projeto vazio criado manualmente pelo usuário, a interface
    chama esta função sem inserir componentes automaticamente.
    """

    # Executa `projeto.garantir_tela` com os argumentos informados para realizar a operação correspondente.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `garantir_tela` = função, método ou classe chamada para executar a operação relacionada a garantir tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto.garantir_tela()

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `telas` = atributo, método ou recurso acessado com o nome `telas`.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for tela in projeto.telas:

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for comp in tela.componentes:

            # Executa `migrar_acao_legada` com os argumentos informados para realizar a operação correspondente.
            # `migrar_acao_legada` = função, método ou classe chamada para executar a operação relacionada a migrar acao legada.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            migrar_acao_legada(comp, tela)

        # Executa `garantir_campos_banco_automaticos` com os argumentos informados para realizar a operação correspondente.
        # `garantir_campos_banco_automaticos` = função, método ou classe chamada para executar a operação relacionada a garantir campos banco automaticos.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        garantir_campos_banco_automaticos(tela)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `adicionar_botao_cadastro` = identificador relacionado a um botão da interface, associado a adicionar botao cadastro.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if adicionar_botao_cadastro:

        # Armazena ou associa em `ja_tem_cadastro` o valor ou resultado definido nesta linha.
        ja_tem_cadastro = any(

            # Armazena ou associa em `c.tipo` o valor ou resultado definido nesta linha.
            # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
            # `==` = operador de comparação utilizado para verificar se os valores são iguais.
            # `Button` = texto literal utilizado nesta instrução.
            # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
            # `acao` = atributo, método ou recurso acessado com o nome `acao`.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            c.tipo == "Button" and c.acao == "Cadastrar no SQLite"

            # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `telas` = atributo, método ou recurso acessado com o nome `telas`.
            for tela in projeto.telas

            # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
            for c in tela.componentes

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `ja_tem_cadastro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ja tem cadastro.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not ja_tem_cadastro:

            # Armazena ou associa em `candidatas` o valor ou resultado definido nesta linha.
            candidatas = [

                # Executa a instrução desta linha como parte da lógica atual do programa.
                # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
                # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
                # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
                # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `telas` = atributo, método ou recurso acessado com o nome `telas`.
                # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
                # `nomes_componentes_entrada` = identificador relacionado a um campo de entrada de dados, associado a nomes componentes entrada.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                t for t in projeto.telas if nomes_componentes_entrada(t)

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            ]

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `candidatas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatas.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if candidatas:

                # Executa `garantir_botao_cadastro` com os argumentos informados para realizar a operação correspondente.
                # `garantir_botao_cadastro` = identificador relacionado a um botão da interface, associado a garantir botao cadastro.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `candidatas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatas.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                garantir_botao_cadastro(candidatas[0])

            # Inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            else:

                # Armazena ou associa em `tela_registro` o valor ou resultado definido nesta linha.
                # `tela_registro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela registro.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `_criar_tela_registro_sqlite` = função, método ou classe chamada para executar a operação relacionada a criar tela registro sqlite.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                tela_registro = _criar_tela_registro_sqlite()

                # Executa `projeto.telas.append` com os argumentos informados para realizar a operação correspondente.
                # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `telas` = atributo, método ou recurso acessado com o nome `telas`.
                # `append` = função, método ou classe chamada para executar a operação relacionada a append.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `tela_registro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela registro.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                projeto.telas.append(tela_registro)

                # Armazena ou associa em `menu` o valor ou resultado definido nesta linha.
                menu = next(

                    # Executa a instrução desta linha como parte da lógica atual do programa.
                    (

                        # Executa a instrução desta linha como parte da lógica atual do programa.
                        # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
                        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
                        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
                        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                        # `telas` = atributo, método ou recurso acessado com o nome `telas`.
                        t for t in projeto.telas

                        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
                        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
                        # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
                        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
                        # `lower` = função, método ou classe chamada para executar a operação relacionada a lower.
                        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                        # `startswith` = função, método ou classe chamada para executar a operação relacionada a startswith.
                        # `menu` = texto literal utilizado nesta instrução.
                        if t.nome.lower().startswith("menu")

                    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    ),

                    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                    # `None` = representa ausência de valor.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    None,

                # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                )

                # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
                # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
                # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
                # `is` = compara a identidade entre objetos.
                # `not` = inverte o resultado lógico da expressão seguinte.
                # `None` = representa ausência de valor.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                if menu is not None:

                    # Armazena ou associa em `max_bottom` o valor ou resultado definido nesta linha.
                    max_bottom = max(

                        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
                        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                        # `y` = atributo, método ou recurso acessado com o nome `y`.
                        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
                        # `altura` = atributo, método ou recurso acessado com o nome `altura`.
                        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
                        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
                        # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
                        # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
                        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                        (c.y + c.altura for c in menu.componentes),

                        # Define o argumento nomeado `default` da chamada iniciada nas linhas anteriores.
                        # `default` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default.
                        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                        # `120` = valor numérico associado a `default` nesta instrução.
                        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                        default=120,

                    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    )

                    # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
                    y = min(

                        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                        # `max_bottom` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a max bottom.
                        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
                        # `20` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                        max_bottom + 20,

                        # Executa `max` com os argumentos informados para realizar a operação correspondente.
                        # `max` = função que retorna o maior valor entre os valores informados.
                        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                        # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                        # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
                        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                        # `altura` = atributo, método ou recurso acessado com o nome `altura`.
                        # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
                        # `75` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                        max(120, menu.altura - 75),

                    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    )

                    # Executa `menu.componentes.append` com os argumentos informados para realizar a operação correspondente.
                    menu.componentes.append(

                        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
                        Componente(

                            # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
                            # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `Button` = texto literal utilizado nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            tipo="Button",

                            # Define o argumento nomeado `x` da chamada iniciada nas linhas anteriores.
                            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `70` = coordenada numérica utilizada no eixo X nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            x=70,

                            # Define o argumento nomeado `y` da chamada iniciada nas linhas anteriores.
                            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            y=y,

                            # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
                            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `245` = valor numérico utilizado para definir a largura nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            largura=245,

                            # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
                            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `55` = valor numérico utilizado para definir a altura nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            altura=55,

                            # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
                            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `abrir_registro_sqlite` = texto literal utilizado nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            nome="abrir_registro_sqlite",

                            # Define o argumento nomeado `texto` da chamada iniciada nas linhas anteriores.
                            # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `Registro SQLite` = texto literal utilizado nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            texto="Registro SQLite",

                            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
                            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `Abrir outra tela` = texto literal utilizado nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            acao="Abrir outra tela",

                            # Define o argumento nomeado `tela_destino` da chamada iniciada nas linhas anteriores.
                            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
                            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                            # `Registro SQLite` = texto literal utilizado nesta instrução.
                            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                            tela_destino="Registro SQLite",

                        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                        )

                    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    )

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    if adicionar_botao_cadastro and any(

        # Armazena ou associa em `c.tipo` o valor ou resultado definido nesta linha.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Button` = texto literal utilizado nesta instrução.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `acao` = atributo, método ou recurso acessado com o nome `acao`.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        c.tipo == "Button" and c.acao == "Cadastrar no SQLite"

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `telas` = atributo, método ou recurso acessado com o nome `telas`.
        for tela in projeto.telas

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
        for c in tela.componentes

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    ):

        # Armazena ou associa em `projeto.exibir_aba_dados` o valor ou resultado definido nesta linha.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `exibir_aba_dados` = atributo, método ou recurso acessado com o nome `exibir_aba_dados`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        projeto.exibir_aba_dados = True

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    return projeto

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `sincronizacao_campos` = atributo, método ou recurso acessado com o nome `sincronizacao_campos`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `sincronizar_campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a sincronizar campos banco.
# `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
# `garantir_campos_banco_automaticos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a garantir campos banco automaticos.
from .sincronizacao_campos import sincronizar_campos_banco as garantir_campos_banco_automaticos
