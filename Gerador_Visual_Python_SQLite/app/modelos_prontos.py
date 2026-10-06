# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `__future__` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a future.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `annotations` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a annotations.
from __future__ import annotations

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `copy` = módulo utilizado para criar cópias de objetos.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `deepcopy` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a deepcopy.
from copy import deepcopy

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

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `acoes_genericas` = atributo, método ou recurso acessado com o nome `acoes_genericas`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `normalizar_projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normalizar projeto.
from .acoes_genericas import normalizar_projeto

# Define a rotina `_campo_visual`, responsável por executar a lógica relacionada a campo visual.
# `def` = define uma nova função ou um novo método.
# `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
# `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
# `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# texto vazio = representa uma string sem caracteres.
# `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
# `None` = representa ausência de valor.
# `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
# `Nenhuma` = texto literal utilizado nesta instrução.
# `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
# `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
# `False` = representa o valor lógico falso.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _campo_visual(tipo, x, y, largura, nome, campo, texto="", opcoes=None, mascara="Nenhuma", validacao="Nenhuma", obrigatorio=False):

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Componente(

        # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tipo=tipo,

        # Define o argumento nomeado `x` da chamada iniciada nas linhas anteriores.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        x=x,

        # Define o argumento nomeado `y` da chamada iniciada nas linhas anteriores.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        y=y,

        # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        largura=largura,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `100` = valor numérico utilizado para definir a altura nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Text` = texto literal utilizado nesta instrução.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `34` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=100 if tipo == "Text" else 34,

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome=nome,

        # Define o argumento nomeado `texto` da chamada iniciada nas linhas anteriores.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        texto=texto,

        # Define o argumento nomeado `opcoes` da chamada iniciada nas linhas anteriores.
        # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        opcoes=opcoes or [],

        # Define o argumento nomeado `campo_banco` da chamada iniciada nas linhas anteriores.
        # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campo_banco=campo,

        # Define o argumento nomeado `mascara` da chamada iniciada nas linhas anteriores.
        # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        mascara=mascara,

        # Define o argumento nomeado `validacao` da chamada iniciada nas linhas anteriores.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        validacao=validacao,

        # Define o argumento nomeado `obrigatorio` da chamada iniciada nas linhas anteriores.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        obrigatorio=obrigatorio,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `criar_tela_crud`, responsável por executar a lógica relacionada a criar tela crud.
# `def` = define uma nova função ou um novo método.
# `criar_tela_crud` = função, método ou classe chamada para executar a operação relacionada a criar tela crud.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
# `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
# `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
# `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `True` = representa o valor lógico verdadeiro.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_crud(nome_tela, titulo, tabela, definicoes, incluir_menu=True):

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Cria uma tela CRUD editável com formulário, filtro e Treeview.` = texto literal utilizado nesta instrução.
    """Cria uma tela CRUD editável com formulário, filtro e Treeview."""

    # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
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
    campos = [CampoBanco("id", "INTEGER", False, True)]

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `Componente` = classe que representa um componente inserido no Designer Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Label` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `25` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `560` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `44` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `titulo` = texto literal utilizado nesta instrução.
    # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    componentes = [Componente("Label", 35, 25, 560, 44, "titulo", titulo)]

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if incluir_menu:

        # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
        componentes.extend([

            # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
            # `Componente` = classe que representa um componente inserido no Designer Visual.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `760` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `26` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `95` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `36` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `btn_menu` = texto literal utilizado nesta instrução.
            # `Menu` = texto literal utilizado nesta instrução.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Menu Principal` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            Componente("Button", 760, 26, 95, 36, "btn_menu", "Menu", acao="Abrir outra tela", tela_destino="Menu Principal"),

            # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
            # `Componente` = classe que representa um componente inserido no Designer Visual.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `865` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `26` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `95` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `36` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `btn_sair` = texto literal utilizado nesta instrução.
            # `Sair` = texto literal utilizado nesta instrução.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Sair da conta` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            Componente("Button", 865, 26, 95, 36, "btn_sair", "Sair", acao="Sair da conta"),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        ])

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `x_label_esq` = identificador relacionado a um rótulo de texto da interface.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `x_campo_esq` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x campo esq.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `35` = valor numérico associado a `x_campo_esq` nesta instrução.
    # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    x_label_esq, x_campo_esq = 35, 160

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `x_label_dir` = identificador relacionado a um rótulo de texto da interface.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `x_campo_dir` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x campo dir.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `485` = valor numérico associado a `x_campo_dir` nesta instrução.
    # `595` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    x_label_dir, x_campo_dir = 485, 595

    # Armazena ou associa em `y_atual` o valor ou resultado definido nesta linha.
    # `y_atual` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y atual.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `95` = valor numérico associado a `y_atual` nesta instrução.
    y_atual = 95

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `inicio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a inicio.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `range` = função que cria uma sequência numérica utilizada normalmente em repetições.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for inicio in range(0, len(definicoes), 2):

        # Armazena ou associa em `itens_linha` o valor ou resultado definido nesta linha.
        # `itens_linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens linha.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `inicio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a inicio.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        itens_linha = definicoes[inicio:inicio + 2]

        # Armazena ou associa em `altura_linha` o valor ou resultado definido nesta linha.
        # `altura_linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linha.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `max` = função que retorna o maior valor entre os valores informados.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `widget` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Entry` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Text` = texto literal utilizado nesta instrução.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `34` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `itens_linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens linha.
        altura_linha = max(100 if item.get("widget", "Entry") == "Text" else 34 for item in itens_linha)

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `enumerate` = função que percorre elementos fornecendo também o respectivo índice.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `itens_linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for coluna, item in enumerate(itens_linha):

            # Executa `campos.append` com os argumentos informados para realizar a operação correspondente.
            # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `tipo_sql` = texto literal utilizado nesta instrução.
            # `TEXT` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `False` = representa o valor lógico falso.
            campos.append(CampoBanco(item["nome"], item.get("tipo_sql", "TEXT"), item.get("obrigatorio", False), False))

            # Armazena ou associa em `direita` o valor ou resultado definido nesta linha.
            # `direita` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a direita.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
            # `==` = operador de comparação utilizado para verificar se os valores são iguais.
            # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
            direita = coluna == 1

            # Armazena ou associa em `xl` o valor ou resultado definido nesta linha.
            # `xl` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a xl.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `x_label_dir` = identificador relacionado a um rótulo de texto da interface.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `direita` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a direita.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `x_label_esq` = identificador relacionado a um rótulo de texto da interface.
            xl = x_label_dir if direita else x_label_esq

            # Armazena ou associa em `xc` o valor ou resultado definido nesta linha.
            # `xc` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a xc.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `x_campo_dir` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x campo dir.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `direita` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a direita.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `x_campo_esq` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x campo esq.
            xc = x_campo_dir if direita else x_campo_esq

            # Armazena ou associa em `largura` o valor ou resultado definido nesta linha.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `300` = valor numérico utilizado para definir a largura nesta instrução.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `direita` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a direita.
            # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
            # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            largura = 300 if direita else 270

            # Armazena ou associa em `widget` o valor ou resultado definido nesta linha.
            # `widget` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a widget.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `widget` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Entry` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            widget = item.get("widget", "Entry")

            # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
            # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `Componente` = classe que representa um componente inserido no Designer Visual.
            # `Label` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `xl` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a xl.
            # `y_atual` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y atual.
            # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
            # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            componentes.append(Componente("Label", xl, y_atual + 2, 115, 30, f"lbl_{item['nome']}", item["rotulo"]))

            # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
            componentes.append(_campo_visual(

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `widget` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a widget.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `xc` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a xc.
                # `y_atual` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y atual.
                # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                widget, xc, y_atual, largura, item["nome"], item["nome"],

                # Armazena ou associa em `opcoes` o valor ou resultado definido nesta linha.
                # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
                # `mascara` = texto literal utilizado nesta instrução.
                # `Nenhuma` = texto literal utilizado nesta instrução.
                opcoes=item.get("opcoes"), mascara=item.get("mascara", "Nenhuma"),

                # Armazena ou associa em `validacao` o valor ou resultado definido nesta linha.
                # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `validacao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Nenhuma` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `False` = representa o valor lógico falso.
                validacao=item.get("validacao", "Nenhuma"), obrigatorio=item.get("obrigatorio", False),

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            ))

        # Armazena ou associa em `y_atual` o valor ou resultado definido nesta linha.
        # `y_atual` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y atual.
        # `+=` = operador de atribuição composta que soma o valor da direita ao valor atual.
        # `max` = função que retorna o maior valor entre os valores informados.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `54` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `altura_linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linha.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `20` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        y_atual += max(54, altura_linha + 20)

    # Armazena ou associa em `y_botoes` o valor ou resultado definido nesta linha.
    # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `y_atual` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y atual.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `10` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_botoes = y_atual + 10

    # Armazena ou associa em `nomes_campos` o valor ou resultado definido nesta linha.
    # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
    # `nome` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
    nomes_campos = [item["nome"] for item in definicoes]

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
            # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 35, y_botoes, 190, 38,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_salvar` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            "btn_salvar", "Cadastrar no SQLite",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Cadastrar no SQLite",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campos_acao=nomes_campos,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `235` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
            # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 235, y_botoes, 130, 38,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_atualizar` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Atualizar` = texto literal utilizado nesta instrução.
            "btn_atualizar", "Atualizar",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Atualizar registro` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Atualizar registro",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campos_acao=nomes_campos,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `375` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
            # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 375, y_botoes, 120, 38,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_excluir` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Excluir` = texto literal utilizado nesta instrução.
            "btn_excluir", "Excluir",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Excluir registro` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Excluir registro",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `505` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
            # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 505, y_botoes, 120, 38,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_limpar` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Limpar` = texto literal utilizado nesta instrução.
            "btn_limpar", "Limpar",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Limpar campos selecionados",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campos_acao=nomes_campos,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `campo_filtro` o valor ou resultado definido nesta linha.
    # `campo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo filtro.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
    # `id` = texto literal utilizado nesta instrução.
    campo_filtro = definicoes[0]["nome"] if definicoes else "id"

    # Armazena ou associa em `y_filtro` o valor ou resultado definido nesta linha.
    # `y_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y filtro.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `75` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_filtro = y_botoes + 75

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y filtro.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_filtro` = texto literal utilizado nesta instrução.
        # `Pesquisar` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 35, y_filtro + 2, 110, 30, "lbl_filtro", "Pesquisar"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Filtro` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y filtro.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `34` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `filtro_principal` = texto literal utilizado nesta instrução.
        # `Digite para pesquisar` = texto literal utilizado nesta instrução.
        # `campo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo filtro.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `alvo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo filtro.
        # `tabela_dados` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Filtro", 145, y_filtro, 320, 34, "filtro_principal", "Digite para pesquisar", campo_filtro=campo_filtro, alvo_filtro="tabela_dados"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Treeview` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y filtro.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `925` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `245` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `tabela_dados` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Treeview", 35, y_filtro + 55, 925, 245, "tabela_dados"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Tela` = classe que representa uma tela do projeto visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `1000` = valor numérico utilizado para definir a largura nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `y_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y filtro.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `340` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    return Tela(nome=nome_tela, titulo=titulo, largura=1000, altura=max(650, y_filtro + 340), tabela=tabela, componentes=componentes, campos_banco=campos)

# Define a rotina `criar_tela_login`, responsável por executar a lógica relacionada a criar tela login.
# `def` = define uma nova função ou um novo método.
# `criar_tela_login` = função, método ou classe chamada para executar a operação relacionada a criar tela login.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `Menu Principal` = texto literal utilizado nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_login(destino="Menu Principal") -> Tela:

    # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
    campos = [

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `id` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `False` = representa o valor lógico falso.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("id", "INTEGER", False, True),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("usuario", "TEXT", True, False),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("senha", "TEXT", True, False),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("nome", "TEXT", False, False),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `400` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `48` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `Acesso ao Sistema` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 300, 80, 400, 48, "titulo", "Acesso ao Sistema"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `400` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `subtitulo` = texto literal utilizado nesta instrução.
        # `Entre com seu usuário e senha para continuar` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 300, 135, 400, 30, "subtitulo", "Entre com seu usuário e senha para continuar"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `185` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `440` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_login` = texto literal utilizado nesta instrução.
        # `Login` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 280, 185, 440, 285, "painel_login", "Login"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_usuario` = texto literal utilizado nesta instrução.
        # `Usuário` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 330, 230, 110, 30, "lbl_usuario", "Usuário"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `264` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `340` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `36` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Entry", 330, 264, 340, 36, "usuario", "", campo_banco="usuario", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_senha` = texto literal utilizado nesta instrução.
        # `Senha` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 330, 320, 110, 30, "lbl_senha", "Senha"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `354` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `340` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `36` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
        # `Senha` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Entry", 330, 354, 340, 36, "senha", "", campo_banco="senha", mascara="Senha", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `415` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `340` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_entrar` = texto literal utilizado nesta instrução.
        # `Entrar` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Entrar / validar login` = texto literal utilizado nesta instrução.
        # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
        # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Button", 330, 415, 340, 42, "btn_entrar", "Entrar", acao="Entrar / validar login", tela_destino=destino),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `478` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `credenciais_demo` = texto literal utilizado nesta instrução.
        # `Primeiro acesso: admin / admin` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 330, 478, 360, 28, "credenciais_demo", "Primeiro acesso: admin / admin"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Tela` = classe que representa uma tela do projeto visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Login` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `1000` = valor numérico utilizado para definir a largura nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `650` = valor numérico utilizado para definir a altura nesta instrução.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `usuarios` = texto literal utilizado nesta instrução.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return Tela(nome="Login", titulo="Login", largura=1000, altura=650, tabela="usuarios", componentes=componentes, campos_banco=campos)

# Define a rotina `criar_tela_menu`, responsável por executar a lógica relacionada a criar tela menu.
# `def` = define uma nova função ou um novo método.
# `criar_tela_menu` = função, método ou classe chamada para executar a operação relacionada a criar tela menu.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
def criar_tela_menu(nome_sistema: str, destinos) -> Tela:

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `48` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 45, 35, 650, 48, "titulo", nome_sistema),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `88` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `instrucao` = texto literal utilizado nesta instrução.
        # `Escolha uma opção para continuar` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 45, 88, 650, 30, "instrucao", "Escolha uma opção para continuar"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `colunas` o valor ou resultado definido nesta linha.
    # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `3` = valor numérico associado a `colunas` nesta instrução.
    colunas = 3

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `enumerate` = função que percorre elementos fornecendo também o respectivo índice.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for i, destino in enumerate(destinos):

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `divmod` = função, método ou classe chamada para executar a operação relacionada a divmod.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        linha, coluna = divmod(i, colunas)

        # Armazena ou associa em `x` o valor ou resultado definido nesta linha.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `70` = coordenada numérica utilizada no eixo X nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        x = 70 + coluna * 285

        # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `160` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        y = 160 + linha * 105

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        componentes.append(Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `245` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `72` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `lower` = função, método ou classe chamada para executar a operação relacionada a lower.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `replace` = função, método ou classe chamada para executar a operação relacionada a replace.
            # ` ` = texto literal utilizado nesta instrução.
            # `_` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            "Button", x, y, 245, 72, f"abrir_{destino.lower().replace(' ', '_')}", destino,

            # Armazena ou associa em `acao` o valor ou resultado definido nesta linha.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
            acao="Abrir outra tela", tela_destino=destino,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        ))

    # Armazena ou associa em `y_sair` o valor ou resultado definido nesta linha.
    # `y_sair` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y sair.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `160` = valor numérico associado a `y_sair` nesta instrução.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `//` = operador utilizado para realizar divisão inteira.
    # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
    # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `20` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_sair = 160 + ((max(0, len(destinos)-1)) // colunas + 1) * 105 + 20

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Separator` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `70` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_sair` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y sair.
        # `815` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `8` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `separador_menu` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Separator", 70, y_sair, 815, 8, "separador_menu", ""),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `700` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_sair` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y sair.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `185` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_sair` = texto literal utilizado nesta instrução.
        # `Sair da conta` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Button", 700, y_sair + 30, 185, 42, "btn_sair", "Sair da conta", acao="Sair da conta"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Tela` = classe que representa uma tela do projeto visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Menu Principal` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
    # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `1000` = valor numérico utilizado para definir a largura nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `y_sair` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y sair.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `menu` = texto literal utilizado nesta instrução.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return Tela(nome="Menu Principal", titulo=nome_sistema, largura=1000, altura=max(650, y_sair + 120), tabela="menu", componentes=componentes, campos_banco=[])

# Define a rotina `montar_projeto_com_fluxo`, responsável por executar a lógica relacionada a montar projeto com fluxo.
# `def` = define uma nova função ou um novo método.
# `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
# `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def montar_projeto_com_fluxo(nome, tema, telas_funcionais) -> Projeto:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Monta Login -> Menu Principal -> telas funcionais e inicia pelo Login.` = texto literal utilizado nesta instrução.
    """Monta Login -> Menu Principal -> telas funcionais e inicia pelo Login."""

    # Armazena ou associa em `nomes` o valor ou resultado definido nesta linha.
    # `nomes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    nomes = [t.nome for t in telas_funcionais]

    # Armazena ou associa em `login` o valor ou resultado definido nesta linha.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_login` = função, método ou classe chamada para executar a operação relacionada a criar tela login.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Menu Principal` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    login = criar_tela_login("Menu Principal")

    # Armazena ou associa em `menu` o valor ou resultado definido nesta linha.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_menu` = função, método ou classe chamada para executar a operação relacionada a criar tela menu.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `nomes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    menu = criar_tela_menu(nome, nomes)

    # Armazena ou associa em `telas` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    telas = [login, menu] + list(telas_funcionais)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return Projeto(nome, tema, telas, login.id)

# Define a rotina `_modelo_crud`, responsável por executar a lógica relacionada a modelo crud.
# `def` = define uma nova função ou um novo método.
# `_modelo_crud` = função, método ou classe chamada para executar a operação relacionada a modelo crud.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome projeto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
# `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
# `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
# `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
# `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `Azul corporativo` = texto literal utilizado nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _modelo_crud(nome_projeto, nome_tela, titulo, tabela, definicoes, tema="Azul corporativo") -> Projeto:

    # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_crud` = função, método ou classe chamada para executar a operação relacionada a criar tela crud.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    tela = criar_tela_crud(nome_tela, titulo, tabela, definicoes)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome_projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome projeto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return montar_projeto_com_fluxo(nome_projeto, tema, [tela])

# Define a rotina `modelo_clientes`, responsável por executar a lógica relacionada a modelo clientes.
# `def` = define uma nova função ou um novo método.
# `modelo_clientes` = função, método ou classe chamada para executar a operação relacionada a modelo clientes.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_clientes() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Cadastro de Clientes", "Clientes", "Cadastro de Clientes", "clientes", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Nome` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `email` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `E-mail` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `telefone` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Telefone` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone", "validacao": "Telefone"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cidade` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cidade", "rotulo": "Cidade"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cpf` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `CPF` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cpf", "rotulo": "CPF", "mascara": "CPF", "validacao": "CPF"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `estado` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Estado` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `SP` = texto literal utilizado nesta instrução.
        # `RJ` = texto literal utilizado nesta instrução.
        # `MG` = texto literal utilizado nesta instrução.
        # `PR` = texto literal utilizado nesta instrução.
        # `SC` = texto literal utilizado nesta instrução.
        # `RS` = texto literal utilizado nesta instrução.
        # `BA` = texto literal utilizado nesta instrução.
        # `GO` = texto literal utilizado nesta instrução.
        # `PE` = texto literal utilizado nesta instrução.
        # `CE` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "estado", "rotulo": "Estado", "widget": "Combobox", "opcoes": ["SP", "RJ", "MG", "PR", "SC", "RS", "BA", "GO", "PE", "CE"]},

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

# Define a rotina `modelo_produtos`, responsável por executar a lógica relacionada a modelo produtos.
# `def` = define uma nova função ou um novo método.
# `modelo_produtos` = função, método ou classe chamada para executar a operação relacionada a modelo produtos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_produtos() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Cadastro de Produtos", "Produtos", "Cadastro de Produtos", "produtos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `produto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Produto` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "produto", "rotulo": "Produto", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `codigo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Código` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "codigo", "rotulo": "Código"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `categoria` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Categoria` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Alimentos` = texto literal utilizado nesta instrução.
        # `Eletrônicos` = texto literal utilizado nesta instrução.
        # `Casa` = texto literal utilizado nesta instrução.
        # `Informática` = texto literal utilizado nesta instrução.
        # `Outros` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "categoria", "rotulo": "Categoria", "widget": "Combobox", "opcoes": ["Alimentos", "Eletrônicos", "Casa", "Informática", "Outros"]},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `preco` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Preço` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `REAL` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Moeda` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "preco", "rotulo": "Preço", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `estoque` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Estoque` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "estoque", "rotulo": "Estoque", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `fornecedor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Fornecedor` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "fornecedor", "rotulo": "Fornecedor"},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Verde` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Verde")

# Define a rotina `modelo_contatos`, responsável por executar a lógica relacionada a modelo contatos.
# `def` = define uma nova função ou um novo método.
# `modelo_contatos` = função, método ou classe chamada para executar a operação relacionada a modelo contatos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_contatos() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Agenda de Contatos", "Contatos", "Agenda de Contatos", "contatos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Nome` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `telefone` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Telefone` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone", "validacao": "Telefone"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `email` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `E-mail` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `empresa` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Empresa` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "empresa", "rotulo": "Empresa"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cidade` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cidade", "rotulo": "Cidade"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `observacoes` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Observações` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Text` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "observacoes", "rotulo": "Observações", "widget": "Text"},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Claro` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Claro")

# Define a rotina `modelo_estoque`, responsável por executar a lógica relacionada a modelo estoque.
# `def` = define uma nova função ou um novo método.
# `modelo_estoque` = função, método ou classe chamada para executar a operação relacionada a modelo estoque.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_estoque() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Controle de Estoque", "Estoque", "Controle de Estoque", "estoque", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `produto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Produto` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "produto", "rotulo": "Produto", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `codigo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Código` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "codigo", "rotulo": "Código", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `quantidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Quantidade` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "quantidade", "rotulo": "Quantidade", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `estoque_minimo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Estoque mínimo` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "estoque_minimo", "rotulo": "Estoque mínimo", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `localizacao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Localização` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "localizacao", "rotulo": "Localização"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `fornecedor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Fornecedor` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "fornecedor", "rotulo": "Fornecedor"},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Minimalista` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Minimalista")

# Define a rotina `modelo_tarefas`, responsável por executar a lógica relacionada a modelo tarefas.
# `def` = define uma nova função ou um novo método.
# `modelo_tarefas` = função, método ou classe chamada para executar a operação relacionada a modelo tarefas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_tarefas() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Gerenciador de Tarefas", "Tarefas", "Gerenciador de Tarefas", "tarefas", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `tarefa` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Tarefa` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "tarefa", "rotulo": "Tarefa", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `prioridade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Prioridade` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Baixa` = texto literal utilizado nesta instrução.
        # `Média` = texto literal utilizado nesta instrução.
        # `Alta` = texto literal utilizado nesta instrução.
        # `Urgente` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "prioridade", "rotulo": "Prioridade", "widget": "Combobox", "opcoes": ["Baixa", "Média", "Alta", "Urgente"]},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Pendente` = texto literal utilizado nesta instrução.
        # `Em andamento` = texto literal utilizado nesta instrução.
        # `Concluída` = texto literal utilizado nesta instrução.
        # `Cancelada` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Pendente", "Em andamento", "Concluída", "Cancelada"]},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `prazo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Prazo` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Data` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "prazo", "rotulo": "Prazo", "mascara": "Data", "validacao": "Data"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `responsavel` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Responsável` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "responsavel", "rotulo": "Responsável"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `categoria` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Categoria` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "categoria", "rotulo": "Categoria"},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Escuro` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Escuro")

# Define a rotina `modelo_comercial`, responsável por executar a lógica relacionada a modelo comercial.
# `def` = define uma nova função ou um novo método.
# `modelo_comercial` = função, método ou classe chamada para executar a operação relacionada a modelo comercial.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_comercial() -> Projeto:

    # Armazena ou associa em `clientes` o valor ou resultado definido nesta linha.
    clientes = criar_tela_crud("Clientes", "Cadastro de Clientes", "clientes", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Nome` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `email` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `E-mail` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `telefone` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Telefone` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cidade` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cidade", "rotulo": "Cidade"},

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `produtos` o valor ou resultado definido nesta linha.
    produtos = criar_tela_crud("Produtos", "Cadastro de Produtos", "produtos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `produto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Produto` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "produto", "rotulo": "Produto", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `preco` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Preço` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `REAL` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Moeda` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "preco", "rotulo": "Preço", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `estoque` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Estoque` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "estoque", "rotulo": "Estoque", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `categoria` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Categoria` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "categoria", "rotulo": "Categoria"},

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `vendas` o valor ou resultado definido nesta linha.
    vendas = criar_tela_crud("Vendas", "Registro de Vendas", "vendas", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cliente` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cliente` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cliente", "rotulo": "Cliente", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `produto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Produto` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "produto", "rotulo": "Produto", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `quantidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Quantidade` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "quantidade", "rotulo": "Quantidade", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `valor_total` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Valor total` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `REAL` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Moeda` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "valor_total", "rotulo": "Valor total", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `data` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Data` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "data", "rotulo": "Data", "mascara": "Data", "validacao": "Data"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Aberta` = texto literal utilizado nesta instrução.
        # `Paga` = texto literal utilizado nesta instrução.
        # `Cancelada` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Aberta", "Paga", "Cancelada"]},

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Sistema Comercial` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Azul corporativo` = texto literal utilizado nesta instrução.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `clientes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a clientes.
    # `produtos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a produtos.
    # `vendas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a vendas.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return montar_projeto_com_fluxo("Sistema Comercial", "Azul corporativo", [clientes, produtos, vendas])

# Define a rotina `modelo_calculadora`, responsável por executar a lógica relacionada a modelo calculadora.
# `def` = define uma nova função ou um novo método.
# `modelo_calculadora` = função, método ou classe chamada para executar a operação relacionada a modelo calculadora.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_calculadora() -> Projeto:

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `560` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `52` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `Calculadora` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 220, 45, 560, 52, "titulo", "Calculadora"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_numero_1` = texto literal utilizado nesta instrução.
        # `Primeiro número` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 250, 145, 180, 30, "lbl_numero_1", "Primeiro número"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `450` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `140` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `numero_1` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Entry", 450, 140, 300, 38, "numero_1", ""),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `205` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_operacao` = texto literal utilizado nesta instrução.
        # `Operação` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 250, 205, 180, 30, "lbl_operacao", "Operação"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `450` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `operacao` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Somar` = texto literal utilizado nesta instrução.
        # `Subtrair` = texto literal utilizado nesta instrução.
        # `Multiplicar` = texto literal utilizado nesta instrução.
        # `Dividir` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Combobox", 450, 200, 300, 38, "operacao", "", opcoes=["Somar", "Subtrair", "Multiplicar", "Dividir"]),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `265` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_numero_2` = texto literal utilizado nesta instrução.
        # `Segundo número` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 250, 265, 180, 30, "lbl_numero_2", "Segundo número"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `450` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `260` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `numero_2` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Entry", 450, 260, 300, 38, "numero_2", ""),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `450` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 450, 330, 145, 42,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_calcular` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Calcular` = texto literal utilizado nesta instrução.
            "btn_calcular", "Calcular",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Calcular com campos` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Calcular com campos",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `numero_1` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `numero_2` = texto literal utilizado nesta instrução.
            # `operacao` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            campos_acao=["numero_1", "numero_2", "operacao"],

            # Define o argumento nomeado `campo_resultado` da chamada iniciada nas linhas anteriores.
            # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `resultado` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campo_resultado="resultado",

            # Define o argumento nomeado `operador` da chamada iniciada nas linhas anteriores.
            # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Operação definida no Campo 3` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            operador="Operação definida no Campo 3",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `605` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 605, 330, 145, 42,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_limpar` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Limpar` = texto literal utilizado nesta instrução.
            "btn_limpar", "Limpar",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Limpar campos selecionados",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `numero_1` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `numero_2` = texto literal utilizado nesta instrução.
            # `operacao` = texto literal utilizado nesta instrução.
            # `resultado` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            campos_acao=["numero_1", "numero_2", "operacao", "resultado"],

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `415` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_resultado` = texto literal utilizado nesta instrução.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 250, 415, 180, 30, "lbl_resultado", "Resultado"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `450` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `resultado` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Entry", 450, 410, 300, 42, "resultado", ""),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `485` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `32` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `instrucao` = texto literal utilizado nesta instrução.
        # `Escolha a operação, informe os dois números e clique em Calcular.` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 250, 485, 500, 32, "instrucao", "Escolha a operação, informe os dois números e clique em Calcular."),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
    tela = Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calculadora` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Calculadora",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calculadora` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Calculadora",

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
        # `calculadora` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="calculadora",

        # Define o argumento nomeado `componentes` da chamada iniciada nas linhas anteriores.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        componentes=componentes,

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

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Azul corporativo` = texto literal utilizado nesta instrução.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return Projeto("Calculadora", "Azul corporativo", [tela], tela.id)

# Define a rotina `modelo_alunos`, responsável por executar a lógica relacionada a modelo alunos.
# `def` = define uma nova função ou um novo método.
# `modelo_alunos` = função, método ou classe chamada para executar a operação relacionada a modelo alunos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_alunos() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Cadastro de Alunos", "Alunos", "Cadastro de Alunos", "alunos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Nome` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `matricula` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Matrícula` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "matricula", "rotulo": "Matrícula", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `curso` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Curso` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "curso", "rotulo": "Curso"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `turma` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Turma` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "turma", "rotulo": "Turma"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `email` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `E-mail` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `telefone` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Telefone` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone", "validacao": "Telefone"},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Claro` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Claro")

# Define a rotina `modelo_livros`, responsável por executar a lógica relacionada a modelo livros.
# `def` = define uma nova função ou um novo método.
# `modelo_livros` = função, método ou classe chamada para executar a operação relacionada a modelo livros.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_livros() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Biblioteca de Livros", "Livros", "Biblioteca de Livros", "livros", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `titulo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Título` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "titulo", "rotulo": "Título", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `autor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Autor` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "autor", "rotulo": "Autor", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `categoria` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Categoria` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "categoria", "rotulo": "Categoria"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `isbn` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `ISBN` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "isbn", "rotulo": "ISBN"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `ano` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Ano` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "ano", "rotulo": "Ano", "tipo_sql": "INTEGER", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Disponível` = texto literal utilizado nesta instrução.
        # `Emprestado` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Disponível", "Emprestado"]},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Minimalista` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Minimalista")

# Define a rotina `modelo_financeiro`, responsável por executar a lógica relacionada a modelo financeiro.
# `def` = define uma nova função ou um novo método.
# `modelo_financeiro` = função, método ou classe chamada para executar a operação relacionada a modelo financeiro.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_financeiro() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Controle Financeiro", "Lançamentos", "Controle Financeiro", "lancamentos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `descricao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Descrição` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "descricao", "rotulo": "Descrição", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `tipo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Tipo` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Receita` = texto literal utilizado nesta instrução.
        # `Despesa` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "tipo", "rotulo": "Tipo", "widget": "Combobox", "opcoes": ["Receita", "Despesa"], "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `categoria` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Categoria` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "categoria", "rotulo": "Categoria"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `valor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Valor` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `REAL` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Moeda` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "valor", "rotulo": "Valor", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `data` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Data` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "data", "rotulo": "Data", "mascara": "Data", "validacao": "Data"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Pendente` = texto literal utilizado nesta instrução.
        # `Pago` = texto literal utilizado nesta instrução.
        # `Recebido` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Pendente", "Pago", "Recebido"]},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Verde` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Verde")

# Define a rotina `modelo_consultas`, responsável por executar a lógica relacionada a modelo consultas.
# `def` = define uma nova função ou um novo método.
# `modelo_consultas` = função, método ou classe chamada para executar a operação relacionada a modelo consultas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_consultas() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Agenda de Consultas", "Consultas", "Agenda de Consultas", "consultas", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `paciente` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Paciente` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "paciente", "rotulo": "Paciente", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `profissional` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Profissional` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "profissional", "rotulo": "Profissional", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `data` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Data` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "data", "rotulo": "Data", "mascara": "Data", "validacao": "Data"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `horario` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Horário` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "horario", "rotulo": "Horário"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `especialidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Especialidade` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "especialidade", "rotulo": "Especialidade"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Agendada` = texto literal utilizado nesta instrução.
        # `Realizada` = texto literal utilizado nesta instrução.
        # `Cancelada` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Agendada", "Realizada", "Cancelada"]},

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

# Define a rotina `modelo_ordens_servico`, responsável por executar a lógica relacionada a modelo ordens servico.
# `def` = define uma nova função ou um novo método.
# `modelo_ordens_servico` = função, método ou classe chamada para executar a operação relacionada a modelo ordens servico.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_ordens_servico() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Ordens de Serviço", "Ordens de Serviço", "Ordens de Serviço", "ordens_servico", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cliente` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cliente` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cliente", "rotulo": "Cliente", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `servico` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Serviço` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "servico", "rotulo": "Serviço", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `descricao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Descrição` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Text` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "descricao", "rotulo": "Descrição", "widget": "Text"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `valor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Valor` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `REAL` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Moeda` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "valor", "rotulo": "Valor", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `data` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Data` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "data", "rotulo": "Data", "mascara": "Data", "validacao": "Data"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Aberta` = texto literal utilizado nesta instrução.
        # `Em execução` = texto literal utilizado nesta instrução.
        # `Concluída` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Aberta", "Em execução", "Concluída"]},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Escuro` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Escuro")

# Define a rotina `modelo_veiculos`, responsável por executar a lógica relacionada a modelo veiculos.
# `def` = define uma nova função ou um novo método.
# `modelo_veiculos` = função, método ou classe chamada para executar a operação relacionada a modelo veiculos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_veiculos() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Cadastro de Veículos", "Veículos", "Cadastro de Veículos", "veiculos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `placa` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Placa` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "placa", "rotulo": "Placa", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `modelo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Modelo` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "modelo", "rotulo": "Modelo", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `marca` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Marca` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "marca", "rotulo": "Marca"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `ano` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Ano` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "ano", "rotulo": "Ano", "tipo_sql": "INTEGER", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cor` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cor", "rotulo": "Cor"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `proprietario` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Proprietário` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "proprietario", "rotulo": "Proprietário"},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Minimalista` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Minimalista")

# Define a rotina `modelo_eventos`, responsável por executar a lógica relacionada a modelo eventos.
# `def` = define uma nova função ou um novo método.
# `modelo_eventos` = função, método ou classe chamada para executar a operação relacionada a modelo eventos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_eventos() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Controle de Eventos", "Eventos", "Controle de Eventos", "eventos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `evento` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Evento` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "evento", "rotulo": "Evento", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `data` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Data` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "data", "rotulo": "Data", "mascara": "Data", "validacao": "Data"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `local` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Local` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "local", "rotulo": "Local"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `responsavel` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Responsável` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "responsavel", "rotulo": "Responsável"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `vagas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Vagas` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "vagas", "rotulo": "Vagas", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Planejado` = texto literal utilizado nesta instrução.
        # `Confirmado` = texto literal utilizado nesta instrução.
        # `Encerrado` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Planejado", "Confirmado", "Encerrado"]},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Claro` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Claro")

# Define a rotina `modelo_receitas`, responsável por executar a lógica relacionada a modelo receitas.
# `def` = define uma nova função ou um novo método.
# `modelo_receitas` = função, método ou classe chamada para executar a operação relacionada a modelo receitas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_receitas() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Gerenciador de Receitas", "Receitas", "Gerenciador de Receitas", "receitas", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Receita` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "nome", "rotulo": "Receita", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `categoria` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Categoria` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "categoria", "rotulo": "Categoria"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `tempo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Tempo (min)` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "tempo", "rotulo": "Tempo (min)", "tipo_sql": "INTEGER", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `porcoes` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Porções` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "porcoes", "rotulo": "Porções", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `ingredientes` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Ingredientes` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Text` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "ingredientes", "rotulo": "Ingredientes", "widget": "Text"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `preparo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Preparo` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Text` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "preparo", "rotulo": "Preparo", "widget": "Text"},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Verde` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Verde")

# Define a rotina `modelo_funcionarios`, responsável por executar a lógica relacionada a modelo funcionarios.
# `def` = define uma nova função ou um novo método.
# `modelo_funcionarios` = função, método ou classe chamada para executar a operação relacionada a modelo funcionarios.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_funcionarios() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Cadastro de Funcionários", "Funcionários", "Cadastro de Funcionários", "funcionarios", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Nome` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cpf` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `CPF` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cpf", "rotulo": "CPF", "mascara": "CPF", "validacao": "CPF"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cargo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cargo` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cargo", "rotulo": "Cargo"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `departamento` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Departamento` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "departamento", "rotulo": "Departamento"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `salario` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Salário` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `REAL` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Moeda` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "salario", "rotulo": "Salário", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Ativo` = texto literal utilizado nesta instrução.
        # `Afastado` = texto literal utilizado nesta instrução.
        # `Inativo` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Ativo", "Afastado", "Inativo"]},

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

# Define a rotina `modelo_pedidos`, responsável por executar a lógica relacionada a modelo pedidos.
# `def` = define uma nova função ou um novo método.
# `modelo_pedidos` = função, método ou classe chamada para executar a operação relacionada a modelo pedidos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_pedidos() -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _modelo_crud("Controle de Pedidos", "Pedidos", "Controle de Pedidos", "pedidos", [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `pedido` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Pedido` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "pedido", "rotulo": "Pedido", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `cliente` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Cliente` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "cliente", "rotulo": "Cliente", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `produto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Produto` = texto literal utilizado nesta instrução.
        # `obrigatorio` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "produto", "rotulo": "Produto", "obrigatorio": True},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `quantidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Quantidade` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "quantidade", "rotulo": "Quantidade", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `valor_total` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Valor total` = texto literal utilizado nesta instrução.
        # `tipo_sql` = texto literal utilizado nesta instrução.
        # `REAL` = texto literal utilizado nesta instrução.
        # `mascara` = texto literal utilizado nesta instrução.
        # `Moeda` = texto literal utilizado nesta instrução.
        # `validacao` = texto literal utilizado nesta instrução.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "valor_total", "rotulo": "Valor total", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `status` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `Status` = texto literal utilizado nesta instrução.
        # `widget` = texto literal utilizado nesta instrução.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Recebido` = texto literal utilizado nesta instrução.
        # `Separação` = texto literal utilizado nesta instrução.
        # `Enviado` = texto literal utilizado nesta instrução.
        # `Entregue` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Recebido", "Separação", "Enviado", "Entregue"]},

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Azul corporativo` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ], tema="Azul corporativo")

# Armazena ou associa em `_criar_tela_login_original` o valor ou resultado definido nesta linha.
# `_criar_tela_login_original` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a criar tela login original.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `criar_tela_login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a criar tela login.
_criar_tela_login_original = criar_tela_login

# Define a rotina `criar_tela_login`, responsável por executar a lógica relacionada a criar tela login.
# `def` = define uma nova função ou um novo método.
# `criar_tela_login` = função, método ou classe chamada para executar a operação relacionada a criar tela login.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `Menu Principal` = texto literal utilizado nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_login(destino="Menu Principal") -> Tela:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Cria o Login com entrada no sistema e acesso ao cadastro de usuário.` = texto literal utilizado nesta instrução.
    """Cria o Login com entrada no sistema e acesso ao cadastro de usuário."""

    # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_criar_tela_login_original` = função, método ou classe chamada para executar a operação relacionada a criar tela login original.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    tela = _criar_tela_login_original(destino)

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for componente in tela.componentes:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `painel_login` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if componente.nome == "painel_login":

            # Armazena ou associa em `componente.altura` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `altura` = atributo, método ou recurso acessado com o nome `altura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `335` = valor numérico utilizado para definir a altura nesta instrução.
            componente.altura = 335

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `btn_entrar` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif componente.nome == "btn_entrar":

            # Armazena ou associa em `componente.x` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `330` = coordenada numérica utilizada no eixo X nesta instrução.
            componente.x = 330

            # Armazena ou associa em `componente.y` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `415` = coordenada numérica utilizada no eixo Y nesta instrução.
            componente.y = 415

            # Armazena ou associa em `componente.largura` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `160` = valor numérico utilizado para definir a largura nesta instrução.
            componente.largura = 160

            # Armazena ou associa em `componente.texto` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `texto` = atributo, método ou recurso acessado com o nome `texto`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Entrar` = texto literal utilizado nesta instrução.
            componente.texto = "Entrar"

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `credenciais_demo` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif componente.nome == "credenciais_demo":

            # Armazena ou associa em `componente.y` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `478` = coordenada numérica utilizada no eixo Y nesta instrução.
            componente.y = 478

            # Armazena ou associa em `componente.largura` o valor ou resultado definido nesta linha.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `390` = valor numérico utilizado para definir a largura nesta instrução.
            componente.largura = 390

    # Executa `tela.componentes.append` com os argumentos informados para realizar a operação correspondente.
    tela.componentes.append(

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `510` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `415` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 510, 415, 160, 42,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_criar_usuario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Criar usuário` = texto literal utilizado nesta instrução.
            "btn_criar_usuario", "Criar usuário",

            # Armazena ou associa em `acao` o valor ou resultado definido nesta linha.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Cadastrar Usuário` = texto literal utilizado nesta instrução.
            acao="Abrir outra tela", tela_destino="Cadastrar Usuário",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    return tela

# Define a rotina `criar_tela_cadastro_usuario`, responsável por executar a lógica relacionada a criar tela cadastro usuario.
# `def` = define uma nova função ou um novo método.
# `criar_tela_cadastro_usuario` = função, método ou classe chamada para executar a operação relacionada a criar tela cadastro usuario.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_cadastro_usuario() -> Tela:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Cria uma tela simples para cadastrar uma nova conta antes do Login.` = texto literal utilizado nesta instrução.
    """Cria uma tela simples para cadastrar uma nova conta antes do Login."""

    # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
    campos = [

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `id` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `False` = representa o valor lógico falso.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("id", "INTEGER", False, True),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("nome", "TEXT", True, False),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("usuario", "TEXT", True, False),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("senha", "TEXT", True, False),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `48` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `Criar novo usuário` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 250, 55, 500, 48, "titulo", "Criar novo usuário"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `108` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `subtitulo` = texto literal utilizado nesta instrução.
        # `Cadastre uma conta para acessar o sistema` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 250, 108, 500, 30, "subtitulo", "Cadastre uma conta para acessar o sistema"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `245` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `155` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `510` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_cadastro` = texto literal utilizado nesta instrução.
        # `Dados do usuário` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 245, 155, 510, 330, "painel_cadastro", "Dados do usuário"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `205` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_nome` = texto literal utilizado nesta instrução.
        # `Nome` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 300, 205, 130, 30, "lbl_nome", "Nome"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `435` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `202` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `265` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `nome` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 435, 202, 265, "nome", "nome", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `265` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_usuario` = texto literal utilizado nesta instrução.
        # `Usuário` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 300, 265, 130, 30, "lbl_usuario", "Usuário"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `435` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `262` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `265` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 435, 262, 265, "usuario", "usuario", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `325` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_senha` = texto literal utilizado nesta instrução.
        # `Senha` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 300, 325, 130, 30, "lbl_senha", "Senha"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `435` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `322` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `265` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Senha` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 435, 322, 265, "senha", "senha", mascara="Senha", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `395` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 300, 395, 190, 42,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_cadastrar_usuario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Cadastrar usuário` = texto literal utilizado nesta instrução.
            "btn_cadastrar_usuario", "Cadastrar usuário",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Cadastrar no SQLite",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `usuario` = texto literal utilizado nesta instrução.
            # `senha` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            campos_acao=["nome", "usuario", "senha"],

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `510` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `395` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 510, 395, 190, 42,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_limpar_usuario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Limpar` = texto literal utilizado nesta instrução.
            "btn_limpar_usuario", "Limpar",

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Limpar campos selecionados",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `usuario` = texto literal utilizado nesta instrução.
            # `senha` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            campos_acao=["nome", "usuario", "senha"],

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `510` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `400` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Button", 300, 510, 400, 42,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_voltar_login` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Voltar para o Login` = texto literal utilizado nesta instrução.
            "btn_voltar_login", "Voltar para o Login",

            # Armazena ou associa em `acao` o valor ou resultado definido nesta linha.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Login` = texto literal utilizado nesta instrução.
            acao="Abrir outra tela", tela_destino="Login",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `565` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `400` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `info_usuario` = texto literal utilizado nesta instrução.
        # `Depois do cadastro, volte ao Login para entrar.` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 300, 565, 400, 28, "info_usuario", "Depois do cadastro, volte ao Login para entrar."),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar Usuário` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Cadastrar Usuário",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Criar usuário` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Criar usuário",

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
        # `usuarios` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="usuarios",

        # Define o argumento nomeado `componentes` da chamada iniciada nas linhas anteriores.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        componentes=componentes,

        # Define o argumento nomeado `campos_banco` da chamada iniciada nas linhas anteriores.
        # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campos_banco=campos,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `criar_tela_gerenciar_usuarios`, responsável por executar a lógica relacionada a criar tela gerenciar usuarios.
# `def` = define uma nova função ou um novo método.
# `criar_tela_gerenciar_usuarios` = função, método ou classe chamada para executar a operação relacionada a criar tela gerenciar usuarios.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_gerenciar_usuarios() -> Tela:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Cria uma tela administrativa completa para consultar e editar usuários.` = texto literal utilizado nesta instrução.
    """Cria uma tela administrativa completa para consultar e editar usuários."""

    # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
    tela = criar_tela_crud(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Usuários` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Usuários",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Gerenciamento de Usuários` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Gerenciamento de Usuários",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `usuarios` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "usuarios",

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Nome` = texto literal utilizado nesta instrução.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `True` = representa o valor lógico verdadeiro.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `usuario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Usuário` = texto literal utilizado nesta instrução.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `True` = representa o valor lógico verdadeiro.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "usuario", "rotulo": "Usuário", "obrigatorio": True},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `senha` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Nova senha` = texto literal utilizado nesta instrução.
            # `mascara` = texto literal utilizado nesta instrução.
            # `Senha` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "senha", "rotulo": "Nova senha", "mascara": "Senha"},

            # Executa a instrução desta linha como parte da lógica atual do programa.
            {

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `perfil` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Perfil` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                "nome": "perfil", "rotulo": "Perfil", "widget": "Combobox",

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Administrador` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Operador` = texto literal utilizado nesta instrução.
                # `Consulta` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                "opcoes": ["Administrador", "Operador", "Consulta"],

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            },

            # Executa a instrução desta linha como parte da lógica atual do programa.
            {

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                "nome": "status", "rotulo": "Status", "widget": "Combobox",

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Ativo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Inativo` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                "opcoes": ["Ativo", "Inativo"],

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            },

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `incluir_menu` da chamada iniciada nas linhas anteriores.
        # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        incluir_menu=True,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Executa `tela.componentes.append` com os argumentos informados para realizar a operação correspondente.
    tela.componentes.append(

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        Componente(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Label` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `355` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `590` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "Label", 35, 355, 590, 28,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `aviso_senha_usuario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "aviso_senha_usuario",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # texto literal = fornece o conteúdo textual utilizado por esta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Para manter a senha atual ao editar pela aba Dados cadastrados, deixe Nova senha vazia.",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    return tela

# Armazena ou associa em `_criar_tela_menu_original` o valor ou resultado definido nesta linha.
# `_criar_tela_menu_original` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a criar tela menu original.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `criar_tela_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a criar tela menu.
_criar_tela_menu_original = criar_tela_menu

# Define a rotina `criar_tela_menu`, responsável por executar a lógica relacionada a criar tela menu.
# `def` = define uma nova função ou um novo método.
# `criar_tela_menu` = função, método ou classe chamada para executar a operação relacionada a criar tela menu.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
def criar_tela_menu(nome_sistema: str, destinos) -> Tela:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Cria o Menu Principal incluindo o gerenciamento de usuários.` = texto literal utilizado nesta instrução.
    """Cria o Menu Principal incluindo o gerenciamento de usuários."""

    # Armazena ou associa em `destinos` o valor ou resultado definido nesta linha.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    destinos = list(destinos)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `Usuários` = texto literal utilizado nesta instrução.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if "Usuários" not in destinos:

        # Executa `destinos.append` com os argumentos informados para realizar a operação correspondente.
        # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Usuários` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        destinos.append("Usuários")

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_criar_tela_menu_original` = função, método ou classe chamada para executar a operação relacionada a criar tela menu original.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _criar_tela_menu_original(nome_sistema, destinos)

# Define a rotina `montar_projeto_com_fluxo`, responsável por executar a lógica relacionada a montar projeto com fluxo.
# `def` = define uma nova função ou um novo método.
# `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
# `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def montar_projeto_com_fluxo(nome, tema, telas_funcionais) -> Projeto:

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    """Monta um sistema completo: Login, cadastro de conta, menu, usuários e telas do sistema."""

    # Armazena ou associa em `telas_funcionais` o valor ou resultado definido nesta linha.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    telas_funcionais = list(telas_funcionais)

    # Armazena ou associa em `nomes` o valor ou resultado definido nesta linha.
    # `nomes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    nomes = [t.nome for t in telas_funcionais]

    # Armazena ou associa em `login` o valor ou resultado definido nesta linha.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_login` = função, método ou classe chamada para executar a operação relacionada a criar tela login.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Menu Principal` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    login = criar_tela_login("Menu Principal")

    # Armazena ou associa em `cadastro_usuario` o valor ou resultado definido nesta linha.
    # `cadastro_usuario` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a cadastro usuario.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_cadastro_usuario` = função, método ou classe chamada para executar a operação relacionada a criar tela cadastro usuario.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    cadastro_usuario = criar_tela_cadastro_usuario()

    # Armazena ou associa em `gerenciar_usuarios` o valor ou resultado definido nesta linha.
    # `gerenciar_usuarios` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a gerenciar usuarios.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_gerenciar_usuarios` = função, método ou classe chamada para executar a operação relacionada a criar tela gerenciar usuarios.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    gerenciar_usuarios = criar_tela_gerenciar_usuarios()

    # Armazena ou associa em `menu` o valor ou resultado definido nesta linha.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_menu` = função, método ou classe chamada para executar a operação relacionada a criar tela menu.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `nomes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    menu = criar_tela_menu(nome, nomes)

    # Armazena ou associa em `telas` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `cadastro_usuario` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a cadastro usuario.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `gerenciar_usuarios` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a gerenciar usuarios.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    telas = [login, cadastro_usuario, menu, gerenciar_usuarios] + telas_funcionais

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = Projeto(nome, tema, telas, login.id)

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

# Armazena ou associa em `_modelo_calculadora_original` o valor ou resultado definido nesta linha.
# `_modelo_calculadora_original` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo calculadora original.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `modelo_calculadora` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo calculadora.
_modelo_calculadora_original = modelo_calculadora

# Define a rotina `modelo_calculadora`, responsável por executar a lógica relacionada a modelo calculadora.
# `def` = define uma nova função ou um novo método.
# `modelo_calculadora` = função, método ou classe chamada para executar a operação relacionada a modelo calculadora.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def modelo_calculadora() -> Projeto:

    # Armazena ou associa em `base` o valor ou resultado definido nesta linha.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_modelo_calculadora_original` = função, método ou classe chamada para executar a operação relacionada a modelo calculadora original.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    base = _modelo_calculadora_original()

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tema` = atributo, método ou recurso acessado com o nome `tema`.
    # `telas` = atributo, método ou recurso acessado com o nome `telas`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return montar_projeto_com_fluxo("Calculadora", base.tema, base.telas)

# Armazena ou associa em `MODELOS` o valor ou resultado definido nesta linha.
MODELOS = [

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Cadastro de Clientes` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_clientes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo clientes.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Cadastro de Clientes", "descricao": "Sistema completo com Login, criação e gerenciamento de usuários, Menu Principal e clientes com cadastro, edição, exclusão, pesquisa e tabela.", "fabrica": modelo_clientes},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Cadastro de Produtos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_produtos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo produtos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Cadastro de Produtos", "descricao": "Sistema completo com usuários, produtos, categoria, preço, estoque, fornecedor, cadastro, edição, exclusão e pesquisa.", "fabrica": modelo_produtos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Agenda de Contatos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_contatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo contatos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Agenda de Contatos", "descricao": "Agenda completa com Login, usuários, Menu Principal, cadastro, edição, exclusão, pesquisa e gerenciamento de contatos.", "fabrica": modelo_contatos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Controle de Estoque` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_estoque` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo estoque.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Controle de Estoque", "descricao": "Controle completo de estoque com usuários, quantidades, estoque mínimo, cadastro, edição, exclusão e pesquisa.", "fabrica": modelo_estoque},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Gerenciador de Tarefas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_tarefas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo tarefas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Gerenciador de Tarefas", "descricao": "Sistema completo com usuários, tarefas, prioridade, status, prazo, responsável, cadastro, edição e pesquisa.", "fabrica": modelo_tarefas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Sistema Comercial` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_comercial` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo comercial.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Sistema Comercial", "descricao": "Sistema comercial completo com Login, usuários, Clientes, Produtos, Vendas e operações de cadastro, edição, exclusão e pesquisa.", "fabrica": modelo_comercial},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # `Calculadora funcional para somar, subtrair, multiplicar e dividir dois números.` = texto literal utilizado nesta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_calculadora` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo calculadora.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora", "descricao": "Calculadora funcional para somar, subtrair, multiplicar e dividir dois números.", "fabrica": modelo_calculadora},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Cadastro de Alunos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_alunos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo alunos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Cadastro de Alunos", "descricao": "Sistema completo de alunos com Login, usuários, matrícula, curso, turma, e-mail, telefone e CRUD.", "fabrica": modelo_alunos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Biblioteca de Livros` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # `Cadastro de livros com autor, categoria, ISBN, ano e situação do empréstimo.` = texto literal utilizado nesta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_livros` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo livros.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Biblioteca de Livros", "descricao": "Cadastro de livros com autor, categoria, ISBN, ano e situação do empréstimo.", "fabrica": modelo_livros},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Controle Financeiro` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_financeiro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo financeiro.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Controle Financeiro", "descricao": "Controle financeiro completo com Login, usuários, receitas, despesas, categoria, valor, data, status e CRUD.", "fabrica": modelo_financeiro},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Agenda de Consultas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_consultas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo consultas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Agenda de Consultas", "descricao": "Agenda completa com Login, cadastro e gerenciamento de usuários, consultas, paciente, profissional, data, horário, status e CRUD.", "fabrica": modelo_consultas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Ordens de Serviço` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_ordens_servico` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo ordens servico.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Ordens de Serviço", "descricao": "Controle completo de ordens de serviço com usuários, cliente, serviço, valor, data, andamento e CRUD.", "fabrica": modelo_ordens_servico},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Cadastro de Veículos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_veiculos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo veiculos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Cadastro de Veículos", "descricao": "Sistema completo de veículos com Login, usuários, placa, modelo, marca, ano, cor, proprietário e CRUD.", "fabrica": modelo_veiculos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Controle de Eventos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_eventos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo eventos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Controle de Eventos", "descricao": "Controle completo de eventos com Login, usuários, data, local, responsável, vagas, status e CRUD.", "fabrica": modelo_eventos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Gerenciador de Receitas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_receitas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo receitas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Gerenciador de Receitas", "descricao": "Gerenciador completo de receitas com Login, usuários, ingredientes, preparo, tempo, porções, pesquisa e CRUD.", "fabrica": modelo_receitas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Cadastro de Funcionários` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_funcionarios` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo funcionarios.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Cadastro de Funcionários", "descricao": "Sistema completo de funcionários com Login, usuários, CPF, cargo, departamento, salário, status e CRUD.", "fabrica": modelo_funcionarios},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Controle de Pedidos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # texto literal = fornece o conteúdo textual utilizado por esta instrução.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `modelo_pedidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo pedidos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Controle de Pedidos", "descricao": "Controle completo de pedidos com Login, usuários, cliente, produto, quantidade, valor, status e CRUD.", "fabrica": modelo_pedidos},

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `]` = fecha a lista, índice, acesso a elemento ou compreensão.
]

# Define a rotina `obter_modelo`, responsável por executar a lógica relacionada a obter modelo.
# `def` = define uma nova função ou um novo método.
# `obter_modelo` = função, método ou classe chamada para executar a operação relacionada a obter modelo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
def obter_modelo(indice: int) -> Projeto:

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `deepcopy` = função, método ou classe chamada para executar a operação relacionada a deepcopy.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `MODELOS` = constante utilizada para armazenar o valor relacionado a modelos.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = deepcopy(MODELOS[indice]["fabrica"]())

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `normalizar_projeto` = função, método ou classe chamada para executar a operação relacionada a normalizar projeto.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `adicionar_botao_cadastro` = identificador relacionado a um botão da interface, associado a adicionar botao cadastro.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return normalizar_projeto(projeto, adicionar_botao_cadastro=True)

# Define a rotina `_estilo_titulo`, responsável por executar a lógica relacionada a estilo titulo.
# `def` = define uma nova função ou um novo método.
# `_estilo_titulo` = função, método ou classe chamada para executar a operação relacionada a estilo titulo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _estilo_titulo(comp):

    # Armazena ou associa em `comp.fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `fonte` = atributo, método ou recurso acessado com o nome `fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Segoe UI` = texto literal utilizado nesta instrução.
    comp.fonte = "Segoe UI"

    # Armazena ou associa em `comp.tamanho_fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tamanho_fonte` = atributo, método ou recurso acessado com o nome `tamanho_fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `22` = valor numérico utilizado para definir o tamanho da fonte.
    comp.tamanho_fonte = 22

    # Armazena ou associa em `comp.negrito` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `negrito` = atributo, método ou recurso acessado com o nome `negrito`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    comp.negrito = True

    # Armazena ou associa em `comp.cor_texto` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
    # canal vermelho = 22 em uma escala de 0 a 255.
    # canal verde = 50 em uma escala de 0 a 255.
    # canal azul = 79 em uma escala de 0 a 255.
    comp.cor_texto = "#16324F"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    return comp

# Define a rotina `_estilo_subtitulo`, responsável por executar a lógica relacionada a estilo subtitulo.
# `def` = define uma nova função ou um novo método.
# `_estilo_subtitulo` = função, método ou classe chamada para executar a operação relacionada a estilo subtitulo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _estilo_subtitulo(comp):

    # Armazena ou associa em `comp.fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `fonte` = atributo, método ou recurso acessado com o nome `fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Segoe UI` = texto literal utilizado nesta instrução.
    comp.fonte = "Segoe UI"

    # Armazena ou associa em `comp.tamanho_fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tamanho_fonte` = atributo, método ou recurso acessado com o nome `tamanho_fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `10` = valor numérico utilizado para definir o tamanho da fonte.
    comp.tamanho_fonte = 10

    # Armazena ou associa em `comp.cor_texto` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#5E6B78` = código hexadecimal que representa aproximadamente a cor azul.
    # canal vermelho = 94 em uma escala de 0 a 255.
    # canal verde = 107 em uma escala de 0 a 255.
    # canal azul = 120 em uma escala de 0 a 255.
    comp.cor_texto = "#5E6B78"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    return comp

# Define a rotina `_estilo_botao_primario`, responsável por executar a lógica relacionada a estilo botao primario.
# `def` = define uma nova função ou um novo método.
# `_estilo_botao_primario` = identificador relacionado a um botão da interface, associado a estilo botao primario.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _estilo_botao_primario(comp):

    # Armazena ou associa em `comp.fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `fonte` = atributo, método ou recurso acessado com o nome `fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Segoe UI` = texto literal utilizado nesta instrução.
    comp.fonte = "Segoe UI"

    # Armazena ou associa em `comp.tamanho_fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tamanho_fonte` = atributo, método ou recurso acessado com o nome `tamanho_fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `10` = valor numérico utilizado para definir o tamanho da fonte.
    comp.tamanho_fonte = 10

    # Armazena ou associa em `comp.negrito` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `negrito` = atributo, método ou recurso acessado com o nome `negrito`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    comp.negrito = True

    # Armazena ou associa em `comp.cor_texto` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
    # canal vermelho = 255 em uma escala de 0 a 255.
    # canal verde = 255 em uma escala de 0 a 255.
    # canal azul = 255 em uma escala de 0 a 255.
    comp.cor_texto = "#FFFFFF"

    # Armazena ou associa em `comp.cor_fundo` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#2D6CDF` = código hexadecimal que representa aproximadamente a cor azul vivo.
    # canal vermelho = 45 em uma escala de 0 a 255.
    # canal verde = 108 em uma escala de 0 a 255.
    # canal azul = 223 em uma escala de 0 a 255.
    comp.cor_fundo = "#2D6CDF"

    # Armazena ou associa em `comp.alinhamento` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `alinhamento` = atributo, método ou recurso acessado com o nome `alinhamento`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Centro` = texto literal utilizado nesta instrução.
    comp.alinhamento = "Centro"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    return comp

# Define a rotina `_estilo_botao_secundario`, responsável por executar a lógica relacionada a estilo botao secundario.
# `def` = define uma nova função ou um novo método.
# `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _estilo_botao_secundario(comp):

    # Armazena ou associa em `comp.fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `fonte` = atributo, método ou recurso acessado com o nome `fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Segoe UI` = texto literal utilizado nesta instrução.
    comp.fonte = "Segoe UI"

    # Armazena ou associa em `comp.tamanho_fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tamanho_fonte` = atributo, método ou recurso acessado com o nome `tamanho_fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `10` = valor numérico utilizado para definir o tamanho da fonte.
    comp.tamanho_fonte = 10

    # Armazena ou associa em `comp.negrito` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `negrito` = atributo, método ou recurso acessado com o nome `negrito`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    comp.negrito = True

    # Armazena ou associa em `comp.cor_texto` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#243447` = código hexadecimal que representa aproximadamente a cor azul escuro.
    # canal vermelho = 36 em uma escala de 0 a 255.
    # canal verde = 52 em uma escala de 0 a 255.
    # canal azul = 71 em uma escala de 0 a 255.
    comp.cor_texto = "#243447"

    # Armazena ou associa em `comp.cor_fundo` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#E9EEF5` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
    # canal vermelho = 233 em uma escala de 0 a 255.
    # canal verde = 238 em uma escala de 0 a 255.
    # canal azul = 245 em uma escala de 0 a 255.
    comp.cor_fundo = "#E9EEF5"

    # Armazena ou associa em `comp.alinhamento` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `alinhamento` = atributo, método ou recurso acessado com o nome `alinhamento`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Centro` = texto literal utilizado nesta instrução.
    comp.alinhamento = "Centro"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    return comp

# Define a rotina `_estilo_botao_perigo`, responsável por executar a lógica relacionada a estilo botao perigo.
# `def` = define uma nova função ou um novo método.
# `_estilo_botao_perigo` = identificador relacionado a um botão da interface, associado a estilo botao perigo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _estilo_botao_perigo(comp):

    # Armazena ou associa em `comp.fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `fonte` = atributo, método ou recurso acessado com o nome `fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Segoe UI` = texto literal utilizado nesta instrução.
    comp.fonte = "Segoe UI"

    # Armazena ou associa em `comp.tamanho_fonte` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `tamanho_fonte` = atributo, método ou recurso acessado com o nome `tamanho_fonte`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `10` = valor numérico utilizado para definir o tamanho da fonte.
    comp.tamanho_fonte = 10

    # Armazena ou associa em `comp.negrito` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `negrito` = atributo, método ou recurso acessado com o nome `negrito`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    comp.negrito = True

    # Armazena ou associa em `comp.cor_texto` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
    # canal vermelho = 255 em uma escala de 0 a 255.
    # canal verde = 255 em uma escala de 0 a 255.
    # canal azul = 255 em uma escala de 0 a 255.
    comp.cor_texto = "#FFFFFF"

    # Armazena ou associa em `comp.cor_fundo` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#B53A3A` = código hexadecimal que representa aproximadamente a cor vermelho.
    # canal vermelho = 181 em uma escala de 0 a 255.
    # canal verde = 58 em uma escala de 0 a 255.
    # canal azul = 58 em uma escala de 0 a 255.
    comp.cor_fundo = "#B53A3A"

    # Armazena ou associa em `comp.alinhamento` o valor ou resultado definido nesta linha.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `alinhamento` = atributo, método ou recurso acessado com o nome `alinhamento`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Centro` = texto literal utilizado nesta instrução.
    comp.alinhamento = "Centro"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
    return comp

# Define a rotina `criar_tela_login`, responsável por executar a lógica relacionada a criar tela login.
# `def` = define uma nova função ou um novo método.
# `criar_tela_login` = função, método ou classe chamada para executar a operação relacionada a criar tela login.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `Menu Principal` = texto literal utilizado nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_login(destino="Menu Principal") -> Tela:

    # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
    campos = [

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `id` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `False` = representa o valor lógico falso.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("id", "INTEGER", False, True),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("usuario", "TEXT", True, False),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("senha", "TEXT", True, False),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `470` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `610` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_apresentacao` = texto literal utilizado nesta instrução.
        # `Bem-vindo` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 45, 45, 470, 610, "painel_apresentacao", "Bem-vindo", cor_fundo="#EAF2FF", cor_texto="#16324F"),

        # Executa `_estilo_titulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_titulo` = função, método ou classe chamada para executar a operação relacionada a estilo titulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `395` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `Sistema pronto para usar` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_titulo(Componente("Label", 80, 105, 395, 55, "titulo", "Sistema pronto para usar", cor_fundo="#EAF2FF")),

        # Executa `_estilo_subtitulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_subtitulo` = função, método ou classe chamada para executar a operação relacionada a estilo subtitulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `385` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `texto_apresentacao` = texto literal utilizado nesta instrução.
        # texto literal = fornece o conteúdo textual utilizado por esta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_subtitulo(Componente("Label", 80, 170, 385, 55, "texto_apresentacao", "Entre com sua conta para acessar os módulos, cadastros, pesquisas e gerenciamento de registros.", cor_fundo="#EAF2FF")),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `item_1` = texto literal utilizado nesta instrução.
        # `• Cadastros completos e editáveis` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#24445F` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 36 em uma escala de 0 a 255.
        # canal verde = 68 em uma escala de 0 a 255.
        # canal azul = 95 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 80, 275, 360, 30, "item_1", "• Cadastros completos e editáveis", cor_fundo="#EAF2FF", cor_texto="#24445F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `item_2` = texto literal utilizado nesta instrução.
        # `• Pesquisa, alteração e exclusão` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#24445F` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 36 em uma escala de 0 a 255.
        # canal verde = 68 em uma escala de 0 a 255.
        # canal azul = 95 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 80, 320, 360, 30, "item_2", "• Pesquisa, alteração e exclusão", cor_fundo="#EAF2FF", cor_texto="#24445F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `365` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `item_3` = texto literal utilizado nesta instrução.
        # `• Banco SQLite integrado` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#24445F` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 36 em uma escala de 0 a 255.
        # canal verde = 68 em uma escala de 0 a 255.
        # canal azul = 95 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 80, 365, 360, 30, "item_3", "• Banco SQLite integrado", cor_fundo="#EAF2FF", cor_texto="#24445F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `item_4` = texto literal utilizado nesta instrução.
        # `• Gerenciamento de usuários` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#24445F` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 36 em uma escala de 0 a 255.
        # canal verde = 68 em uma escala de 0 a 255.
        # canal azul = 95 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 80, 410, 360, 30, "item_4", "• Gerenciamento de usuários", cor_fundo="#EAF2FF", cor_texto="#24445F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `535` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `370` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `dica_login` = texto literal utilizado nesta instrução.
        # `Primeiro acesso: usuário admin e senha admin` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#4E6070` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 78 em uma escala de 0 a 255.
        # canal verde = 96 em uma escala de 0 a 255.
        # canal azul = 112 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 80, 535, 370, 55, "dica_login", "Primeiro acesso: usuário admin e senha admin", cor_fundo="#EAF2FF", cor_texto="#4E6070"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `565` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `75` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `555` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `545` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_login` = texto literal utilizado nesta instrução.
        # `Acesso ao sistema` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 565, 75, 555, 545, "painel_login", "Acesso ao sistema", cor_fundo="#FFFFFF", cor_texto="#16324F"),

        # Executa `_estilo_titulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_titulo` = função, método ou classe chamada para executar a operação relacionada a estilo titulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `125` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `455` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `48` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo_login` = texto literal utilizado nesta instrução.
        # `Entrar` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_titulo(Componente("Label", 615, 125, 455, 48, "titulo_login", "Entrar" , cor_fundo="#FFFFFF")),

        # Executa `_estilo_subtitulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_subtitulo` = função, método ou classe chamada para executar a operação relacionada a estilo subtitulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `177` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `455` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `subtitulo_login` = texto literal utilizado nesta instrução.
        # `Informe seu usuário e sua senha` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_subtitulo(Componente("Label", 615, 177, 455, 30, "subtitulo_login", "Informe seu usuário e sua senha", cor_fundo="#FFFFFF")),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `235` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_usuario` = texto literal utilizado nesta instrução.
        # `Usuário` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#334155` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 51 em uma escala de 0 a 255.
        # canal verde = 65 em uma escala de 0 a 255.
        # canal azul = 85 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 615, 235, 180, 28, "lbl_usuario", "Usuário", cor_fundo="#FFFFFF", cor_texto="#334155"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `267` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `455` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 615, 267, 455, "usuario", "usuario", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `325` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_senha` = texto literal utilizado nesta instrução.
        # `Senha` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#334155` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 51 em uma escala de 0 a 255.
        # canal verde = 65 em uma escala de 0 a 255.
        # canal azul = 85 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 615, 325, 180, 28, "lbl_senha", "Senha", cor_fundo="#FFFFFF", cor_texto="#334155"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `357` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `455` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Senha` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 615, 357, 455, "senha", "senha", mascara="Senha", obrigatorio=True),

        # Executa `_estilo_botao_primario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_primario` = identificador relacionado a um botão da interface, associado a estilo botao primario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `46` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_entrar` = texto literal utilizado nesta instrução.
        # `Entrar` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Entrar / validar login` = texto literal utilizado nesta instrução.
        # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
        # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_primario(Componente("Button", 615, 430, 215, 46, "btn_entrar", "Entrar", acao="Entrar / validar login", tela_destino=destino)),

        # Executa `_estilo_botao_secundario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `855` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `46` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_criar_usuario` = texto literal utilizado nesta instrução.
        # `Criar usuário` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Abrir outra tela` = texto literal utilizado nesta instrução.
        # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
        # `Cadastrar Usuário` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_secundario(Componente("Button", 855, 430, 215, 46, "btn_criar_usuario", "Criar usuário", acao="Abrir outra tela", tela_destino="Cadastrar Usuário")),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `615` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `510` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `455` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `seguranca` = texto literal utilizado nesta instrução.
        # `As senhas são armazenadas de forma protegida no SQLite.` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 100 em uma escala de 0 a 255.
        # canal verde = 116 em uma escala de 0 a 255.
        # canal azul = 139 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 615, 510, 455, 55, "seguranca", "As senhas são armazenadas de forma protegida no SQLite.", cor_fundo="#FFFFFF", cor_texto="#64748B"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Login` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Login",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Login` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Login",

        # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `1180` = valor numérico utilizado para definir a largura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        largura=1180,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `700` = valor numérico utilizado para definir a altura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=700,

        # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `usuarios` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="usuarios",

        # Define o argumento nomeado `componentes` da chamada iniciada nas linhas anteriores.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        componentes=componentes,

        # Define o argumento nomeado `campos_banco` da chamada iniciada nas linhas anteriores.
        # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campos_banco=campos,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `criar_tela_cadastro_usuario`, responsável por executar a lógica relacionada a criar tela cadastro usuario.
# `def` = define uma nova função ou um novo método.
# `criar_tela_cadastro_usuario` = função, método ou classe chamada para executar a operação relacionada a criar tela cadastro usuario.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_cadastro_usuario() -> Tela:

    # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
    campos = [

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `id` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `INTEGER` = texto literal utilizado nesta instrução.
        # `False` = representa o valor lógico falso.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("id", "INTEGER", False, True),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("nome", "TEXT", True, False),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("usuario", "TEXT", True, False),

        # Executa `CampoBanco` com os argumentos informados para realizar a operação correspondente.
        # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `TEXT` = texto literal utilizado nesta instrução.
        # `True` = representa o valor lógico verdadeiro.
        # `False` = representa o valor lógico falso.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        CampoBanco("senha", "TEXT", True, False),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_estilo_titulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_titulo` = função, método ou classe chamada para executar a operação relacionada a estilo titulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `600` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `48` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `Criar usuário` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_titulo(Componente("Label", 45, 35, 600, 48, "titulo", "Criar usuário")),

        # Executa `_estilo_subtitulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_subtitulo` = função, método ou classe chamada para executar a operação relacionada a estilo subtitulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `82` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `700` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `subtitulo` = texto literal utilizado nesta instrução.
        # `Cadastre uma conta para acessar o sistema.` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_subtitulo(Componente("Label", 45, 82, 700, 30, "subtitulo", "Cadastre uma conta para acessar o sistema.")),

        # Executa `_estilo_botao_secundario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `935` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_voltar_login` = texto literal utilizado nesta instrução.
        # `Voltar para o Login` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Abrir outra tela` = texto literal utilizado nesta instrução.
        # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
        # `Login` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_secundario(Componente("Button", 935, 38, 200, 40, "btn_voltar_login", "Voltar para o Login", acao="Abrir outra tela", tela_destino="Login")),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `1090` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_cadastro` = texto literal utilizado nesta instrução.
        # `Dados da conta` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 45, 135, 1090, 410, "painel_cadastro", "Dados da conta", cor_fundo="#FFFFFF", cor_texto="#16324F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `90` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `210` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_nome` = texto literal utilizado nesta instrução.
        # `Nome completo` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 90, 190, 210, 28, "lbl_nome", "Nome completo", cor_fundo="#FFFFFF"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `90` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `222` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `460` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `nome` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 90, 222, 460, "nome", "nome", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `630` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `210` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_usuario` = texto literal utilizado nesta instrução.
        # `Nome de usuário` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 630, 190, 210, 28, "lbl_usuario", "Nome de usuário", cor_fundo="#FFFFFF"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `630` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `222` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `460` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `usuario` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 630, 222, 460, "usuario", "usuario", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `90` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `210` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_senha` = texto literal utilizado nesta instrução.
        # `Senha` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 90, 300, 210, 28, "lbl_senha", "Senha", cor_fundo="#FFFFFF"),

        # Executa `_campo_visual` com os argumentos informados para realizar a operação correspondente.
        # `_campo_visual` = função, método ou classe chamada para executar a operação relacionada a campo visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Entry` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `90` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `332` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `460` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `senha` = texto literal utilizado nesta instrução.
        # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Senha` = texto literal utilizado nesta instrução.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo_visual("Entry", 90, 332, 460, "senha", "senha", mascara="Senha", obrigatorio=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `630` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `orientacao_senha` = texto literal utilizado nesta instrução.
        # `Escolha uma senha e guarde-a para fazer o próximo acesso.` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 100 em uma escala de 0 a 255.
        # canal verde = 116 em uma escala de 0 a 255.
        # canal azul = 139 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 630, 300, 430, 55, "orientacao_senha", "Escolha uma senha e guarde-a para fazer o próximo acesso.", cor_fundo="#FFFFFF", cor_texto="#64748B"),

        # Executa `_estilo_botao_primario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_primario` = identificador relacionado a um botão da interface, associado a estilo botao primario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `90` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `425` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `46` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_cadastrar_usuario` = texto literal utilizado nesta instrução.
        # `Cadastrar usuário` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `usuario` = texto literal utilizado nesta instrução.
        # `senha` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_primario(Componente("Button", 90, 425, 220, 46, "btn_cadastrar_usuario", "Cadastrar usuário", acao="Cadastrar no SQLite", campos_acao=["nome", "usuario", "senha"])),

        # Executa `_estilo_botao_secundario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `425` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `46` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_limpar_usuario` = texto literal utilizado nesta instrução.
        # `Limpar` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `usuario` = texto literal utilizado nesta instrução.
        # `senha` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_secundario(Componente("Button", 330, 425, 160, 46, "btn_limpar_usuario", "Limpar", acao="Limpar campos selecionados", campos_acao=["nome", "usuario", "senha"])),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `580` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `1090` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `info_usuario` = texto literal utilizado nesta instrução.
        # `Depois do cadastro, retorne ao Login e utilize o novo usuário para entrar.` = texto literal utilizado nesta instrução.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#5E6B78` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 94 em uma escala de 0 a 255.
        # canal verde = 107 em uma escala de 0 a 255.
        # canal azul = 120 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 45, 580, 1090, 42, "info_usuario", "Depois do cadastro, retorne ao Login e utilize o novo usuário para entrar.", cor_texto="#5E6B78"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar Usuário` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Cadastrar Usuário",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Criar usuário` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Criar usuário",

        # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `1180` = valor numérico utilizado para definir a largura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        largura=1180,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `680` = valor numérico utilizado para definir a altura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=680,

        # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `usuarios` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="usuarios",

        # Define o argumento nomeado `componentes` da chamada iniciada nas linhas anteriores.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        componentes=componentes,

        # Define o argumento nomeado `campos_banco` da chamada iniciada nas linhas anteriores.
        # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campos_banco=campos,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `criar_tela_crud`, responsável por executar a lógica relacionada a criar tela crud.
# `def` = define uma nova função ou um novo método.
# `criar_tela_crud` = função, método ou classe chamada para executar a operação relacionada a criar tela crud.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
# `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
# `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
# `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `True` = representa o valor lógico verdadeiro.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_crud(nome_tela, titulo, tabela, definicoes, incluir_menu=True):

    # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
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
    campos = [CampoBanco("id", "INTEGER", False, True)]

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_estilo_titulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_titulo` = função, método ou classe chamada para executar a operação relacionada a estilo titulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `44` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_titulo(Componente("Label", 45, 28, 650, 44, "titulo", titulo)),

        # Executa `_estilo_subtitulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_subtitulo` = função, método ou classe chamada para executar a operação relacionada a estilo subtitulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `72` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `720` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `subtitulo` = texto literal utilizado nesta instrução.
        # `Cadastre, pesquise e gerencie os registros nesta tela.` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_subtitulo(Componente("Label", 45, 72, 720, 28, "subtitulo", "Cadastre, pesquise e gerencie os registros nesta tela.")),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if incluir_menu:

        # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
        componentes.extend([

            # Executa `_estilo_botao_secundario` com os argumentos informados para realizar a operação correspondente.
            # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `Componente` = classe que representa um componente inserido no Designer Visual.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `915` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `32` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
            # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `btn_menu` = texto literal utilizado nesta instrução.
            # `Menu` = texto literal utilizado nesta instrução.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Menu Principal` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _estilo_botao_secundario(Componente("Button", 915, 32, 100, 38, "btn_menu", "Menu", acao="Abrir outra tela", tela_destino="Menu Principal")),

            # Executa `_estilo_botao_perigo` com os argumentos informados para realizar a operação correspondente.
            # `_estilo_botao_perigo` = identificador relacionado a um botão da interface, associado a estilo botao perigo.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `Componente` = classe que representa um componente inserido no Designer Visual.
            # `Button` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `1030` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `32` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `btn_sair` = texto literal utilizado nesta instrução.
            # `Sair` = texto literal utilizado nesta instrução.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Sair da conta` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _estilo_botao_perigo(Componente("Button", 1030, 32, 105, 38, "btn_sair", "Sair", acao="Sair da conta")),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        ])

    # Armazena ou associa em `colunas` o valor ou resultado definido nesta linha.
    # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `3` = valor numérico associado a `colunas` nesta instrução.
    colunas = 3

    # Armazena ou associa em `largura_form` o valor ou resultado definido nesta linha.
    # `largura_form` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura form.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `1090` = valor numérico associado a `largura_form` nesta instrução.
    largura_form = 1090

    # Armazena ou associa em `linhas` o valor ou resultado definido nesta linha.
    # `linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linhas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
    # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `//` = operador utilizado para realizar divisão inteira.
    linhas = (len(definicoes) + colunas - 1) // colunas

    # Armazena ou associa em `altura_linhas` o valor ou resultado definido nesta linha.
    # `altura_linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linhas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    altura_linhas = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `range` = função que cria uma sequência numérica utilizada normalmente em repetições.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linhas.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for linha in range(linhas):

        # Armazena ou associa em `itens` o valor ou resultado definido nesta linha.
        # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        itens = definicoes[linha * colunas:(linha + 1) * colunas]

        # Executa `altura_linhas.append` com os argumentos informados para realizar a operação correspondente.
        # `altura_linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linhas.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `max` = função que retorna o maior valor entre os valores informados.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `widget` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Entry` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Text` = texto literal utilizado nesta instrução.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `34` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `34` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        altura_linhas.append(max([100 if i.get("widget", "Entry") == "Text" else 34 for i in itens] or [34]))

    # Armazena ou associa em `altura_form` o valor ou resultado definido nesta linha.
    # `altura_form` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura form.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `115` = valor numérico associado a `altura_form` nesta instrução.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `sum` = função que soma os valores de uma sequência.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `88` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `h` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a h.
    # `54` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `altura_linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linhas.
    # `72` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    altura_form = 115 + sum(max(88, h + 54) for h in altura_linhas) + 72

    # Armazena ou associa em `altura_form` o valor ou resultado definido nesta linha.
    # `altura_form` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura form.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    altura_form = max(300, altura_form)

    # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `append` = função, método ou classe chamada para executar a operação relacionada a append.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Componente` = classe que representa um componente inserido no Designer Visual.
    # `Frame` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `largura_form` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura form.
    # `altura_form` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura form.
    # `painel_formulario` = texto literal utilizado nesta instrução.
    # `Cadastro e edição` = texto literal utilizado nesta instrução.
    # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
    # canal vermelho = 255 em uma escala de 0 a 255.
    # canal verde = 255 em uma escala de 0 a 255.
    # canal azul = 255 em uma escala de 0 a 255.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
    # canal vermelho = 22 em uma escala de 0 a 255.
    # canal verde = 50 em uma escala de 0 a 255.
    # canal azul = 79 em uma escala de 0 a 255.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    componentes.append(Componente("Frame", 45, 120, largura_form, altura_form, "painel_formulario", "Cadastro e edição", cor_fundo="#FFFFFF", cor_texto="#16324F"))

    # Armazena ou associa em `x_colunas` o valor ou resultado definido nesta linha.
    # `x_colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x colunas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `85` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `435` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `785` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    x_colunas = [85, 435, 785]

    # Armazena ou associa em `larguras` o valor ou resultado definido nesta linha.
    # `larguras` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a larguras.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    larguras = [300, 300, 300]

    # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `170` = coordenada numérica utilizada no eixo Y nesta instrução.
    y = 170

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `range` = função que cria uma sequência numérica utilizada normalmente em repetições.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linhas.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for linha in range(linhas):

        # Armazena ou associa em `itens` o valor ou resultado definido nesta linha.
        # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        itens = definicoes[linha * colunas:(linha + 1) * colunas]

        # Armazena ou associa em `altura_linha` o valor ou resultado definido nesta linha.
        # `altura_linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linha.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `altura_linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linhas.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        altura_linha = altura_linhas[linha]

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `enumerate` = função que percorre elementos fornecendo também o respectivo índice.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for coluna, item in enumerate(itens):

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            nome = item["nome"]

            # Armazena ou associa em `rotulo` o valor ou resultado definido nesta linha.
            # `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            rotulo = item["rotulo"]

            # Armazena ou associa em `widget` o valor ou resultado definido nesta linha.
            # `widget` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a widget.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `widget` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Entry` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            widget = item.get("widget", "Entry")

            # Executa `campos.append` com os argumentos informados para realizar a operação correspondente.
            # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `CampoBanco` = função, método ou classe chamada para executar a operação relacionada a CampoBanco.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `tipo_sql` = texto literal utilizado nesta instrução.
            # `TEXT` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `False` = representa o valor lógico falso.
            campos.append(CampoBanco(nome, item.get("tipo_sql", "TEXT"), item.get("obrigatorio", False), False))

            # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
            # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `Componente` = classe que representa um componente inserido no Designer Visual.
            # `Label` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `x_colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x colunas.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
            # `larguras` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a larguras.
            # `26` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            # `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
            # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
            # canal vermelho = 255 em uma escala de 0 a 255.
            # canal verde = 255 em uma escala de 0 a 255.
            # canal azul = 255 em uma escala de 0 a 255.
            # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
            # `#334155` = código hexadecimal que representa aproximadamente a cor azul escuro.
            # canal vermelho = 51 em uma escala de 0 a 255.
            # canal verde = 65 em uma escala de 0 a 255.
            # canal azul = 85 em uma escala de 0 a 255.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            componentes.append(Componente("Label", x_colunas[coluna], y, larguras[coluna], 26, f"lbl_{nome}", rotulo, cor_fundo="#FFFFFF", cor_texto="#334155"))

            # Armazena ou associa em `comp` o valor ou resultado definido nesta linha.
            comp = _campo_visual(

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `widget` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a widget.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                widget,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `x_colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x colunas.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                x_colunas[coluna],

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
                # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
                # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y + 30,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `larguras` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a larguras.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                larguras[coluna],

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                nome,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                nome,

                # Define o argumento nomeado `opcoes` da chamada iniciada nas linhas anteriores.
                # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                opcoes=item.get("opcoes"),

                # Define o argumento nomeado `mascara` da chamada iniciada nas linhas anteriores.
                # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `mascara` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Nenhuma` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                mascara=item.get("mascara", "Nenhuma"),

                # Define o argumento nomeado `validacao` da chamada iniciada nas linhas anteriores.
                # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `validacao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Nenhuma` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                validacao=item.get("validacao", "Nenhuma"),

                # Define o argumento nomeado `obrigatorio` da chamada iniciada nas linhas anteriores.
                # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `False` = representa o valor lógico falso.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                obrigatorio=item.get("obrigatorio", False),

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            )

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `widget` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a widget.
            # `==` = operador de comparação utilizado para verificar se os valores são iguais.
            # `Text` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if widget == "Text":

                # Armazena ou associa em `comp.altura` o valor ou resultado definido nesta linha.
                # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `altura` = atributo, método ou recurso acessado com o nome `altura`.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `85` = valor numérico utilizado para definir a altura nesta instrução.
                comp.altura = 85

            # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
            # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            componentes.append(comp)

        # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `+=` = operador de atribuição composta que soma o valor da direita ao valor atual.
        # `max` = função que retorna o maior valor entre os valores informados.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `88` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `altura_linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura linha.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `54` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        y += max(88, altura_linha + 54)

    # Armazena ou associa em `nomes_campos` o valor ou resultado definido nesta linha.
    # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
    # `nome` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
    nomes_campos = [item["nome"] for item in definicoes]

    # Armazena ou associa em `y_botoes` o valor ou resultado definido nesta linha.
    # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `120` = valor numérico associado a `y_botoes` nesta instrução.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `altura_form` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura form.
    # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
    # `62` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_botoes = 120 + altura_form - 62

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `_estilo_botao_primario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_primario` = identificador relacionado a um botão da interface, associado a estilo botao primario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `85` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_salvar` = texto literal utilizado nesta instrução.
        # `Cadastrar` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_primario(Componente("Button", 85, y_botoes, 180, 42, "btn_salvar", "Cadastrar", acao="Cadastrar no SQLite", campos_acao=nomes_campos)),

        # Executa `_estilo_botao_secundario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_atualizar` = texto literal utilizado nesta instrução.
        # `Alterar selecionado` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Atualizar registro` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_secundario(Componente("Button", 280, y_botoes, 180, 42, "btn_atualizar", "Alterar selecionado", acao="Atualizar registro", campos_acao=nomes_campos)),

        # Executa `_estilo_botao_perigo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_perigo` = identificador relacionado a um botão da interface, associado a estilo botao perigo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `475` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
        # `150` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_excluir` = texto literal utilizado nesta instrução.
        # `Excluir` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Excluir registro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_perigo(Componente("Button", 475, y_botoes, 150, 42, "btn_excluir", "Excluir", acao="Excluir registro")),

        # Executa `_estilo_botao_secundario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `640` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
        # `150` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `42` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_limpar` = texto literal utilizado nesta instrução.
        # `Limpar campos` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_secundario(Componente("Button", 640, y_botoes, 150, 42, "btn_limpar", "Limpar campos", acao="Limpar campos selecionados", campos_acao=nomes_campos)),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `815` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `4` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `orientacao_selecao` = texto literal utilizado nesta instrução.
        # `Selecione uma linha para alterar ou excluir.` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 100 em uma escala de 0 a 255.
        # canal verde = 116 em uma escala de 0 a 255.
        # canal azul = 139 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 815, y_botoes + 4, 285, 38, "orientacao_selecao", "Selecione uma linha para alterar ou excluir.", cor_fundo="#FFFFFF", cor_texto="#64748B"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `campo_filtro` o valor ou resultado definido nesta linha.
    # `campo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo filtro.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
    # `id` = texto literal utilizado nesta instrução.
    campo_filtro = definicoes[0]["nome"] if definicoes else "id"

    # Armazena ou associa em `y_pesquisa` o valor ou resultado definido nesta linha.
    # `y_pesquisa` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y pesquisa.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `120` = valor numérico associado a `y_pesquisa` nesta instrução.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `altura_form` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura form.
    # `25` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_pesquisa = 120 + altura_form + 25

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_pesquisa` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y pesquisa.
        # `1090` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `92` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_pesquisa` = texto literal utilizado nesta instrução.
        # `Pesquisa` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 45, y_pesquisa, 1090, 92, "painel_pesquisa", "Pesquisa", cor_fundo="#FFFFFF", cor_texto="#16324F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_pesquisa` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y pesquisa.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `36` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_filtro` = texto literal utilizado nesta instrução.
        # `Pesquisar` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 80, y_pesquisa + 36, 135, 30, "lbl_filtro", "Pesquisar", cor_fundo="#FFFFFF"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Filtro` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_pesquisa` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y pesquisa.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `32` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `540` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `36` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `filtro_principal` = texto literal utilizado nesta instrução.
        # `Digite para pesquisar` = texto literal utilizado nesta instrução.
        # `campo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo filtro.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `alvo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo filtro.
        # `tabela_dados` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Filtro", 200, y_pesquisa + 32, 540, 36, "filtro_principal", "Digite para pesquisar", campo_filtro=campo_filtro, alvo_filtro="tabela_dados"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `770` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_pesquisa` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y pesquisa.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `34` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `32` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `dica_filtro` = texto literal utilizado nesta instrução.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `definicoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a definicoes.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `principal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 100 em uma escala de 0 a 255.
        # canal verde = 116 em uma escala de 0 a 255.
        # canal azul = 139 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 770, y_pesquisa + 34, 320, 32, "dica_filtro", f"A pesquisa utiliza o campo {definicoes[0]['rotulo'] if definicoes else 'principal'}.", cor_fundo="#FFFFFF", cor_texto="#64748B"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `y_tabela` o valor ou resultado definido nesta linha.
    # `y_tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `y_pesquisa` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y pesquisa.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `112` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_tabela = y_pesquisa + 112

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `45` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y tabela.
        # `1090` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_registros` = texto literal utilizado nesta instrução.
        # `Registros cadastrados` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 45, y_tabela, 1090, 330, "painel_registros", "Registros cadastrados", cor_fundo="#FFFFFF", cor_texto="#16324F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Treeview` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `70` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y tabela.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `1040` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `260` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `tabela_dados` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Treeview", 70, y_tabela + 40, 1040, 260, "tabela_dados"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `altura_total` o valor ou resultado definido nesta linha.
    # `altura_total` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura total.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `y_tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y tabela.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `365` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    altura_total = y_tabela + 365

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome=nome_tela,

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo=titulo,

        # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `1180` = valor numérico utilizado para definir a largura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        largura=1180,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `max` = função que retorna o maior valor entre os valores informados.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `760` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `altura_total` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura total.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        altura=max(760, altura_total),

        # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela=tabela,

        # Define o argumento nomeado `componentes` da chamada iniciada nas linhas anteriores.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        componentes=componentes,

        # Define o argumento nomeado `campos_banco` da chamada iniciada nas linhas anteriores.
        # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campos_banco=campos,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `criar_tela_gerenciar_usuarios`, responsável por executar a lógica relacionada a criar tela gerenciar usuarios.
# `def` = define uma nova função ou um novo método.
# `criar_tela_gerenciar_usuarios` = função, método ou classe chamada para executar a operação relacionada a criar tela gerenciar usuarios.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def criar_tela_gerenciar_usuarios() -> Tela:

    # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
    tela = criar_tela_crud(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Usuários` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Usuários",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Gerenciamento de Usuários` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Gerenciamento de Usuários",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `usuarios` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "usuarios",

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Nome` = texto literal utilizado nesta instrução.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `True` = representa o valor lógico verdadeiro.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `usuario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Usuário` = texto literal utilizado nesta instrução.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `True` = representa o valor lógico verdadeiro.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "usuario", "rotulo": "Usuário", "obrigatorio": True},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `senha` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Nova senha` = texto literal utilizado nesta instrução.
            # `mascara` = texto literal utilizado nesta instrução.
            # `Senha` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "senha", "rotulo": "Nova senha", "mascara": "Senha"},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `perfil` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Perfil` = texto literal utilizado nesta instrução.
            # `widget` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Administrador` = texto literal utilizado nesta instrução.
            # `Operador` = texto literal utilizado nesta instrução.
            # `Consulta` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "perfil", "rotulo": "Perfil", "widget": "Combobox", "opcoes": ["Administrador", "Operador", "Consulta"]},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `status` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Status` = texto literal utilizado nesta instrução.
            # `widget` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Ativo` = texto literal utilizado nesta instrução.
            # `Inativo` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Ativo", "Inativo"]},

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `incluir_menu` da chamada iniciada nas linhas anteriores.
        # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        incluir_menu=True,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Armazena ou associa em `y_aviso` o valor ou resultado definido nesta linha.
    # `y_aviso` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y aviso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `470` = valor numérico associado a `y_aviso` nesta instrução.
    y_aviso = 470

    # Executa `tela.componentes.append` com os argumentos informados para realizar a operação correspondente.
    tela.componentes.append(

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `815` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_aviso` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y aviso.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `aviso_senha_usuario` = texto literal utilizado nesta instrução.
        # `Ao alterar um usuário, deixe Nova senha vazia para manter a senha atual.` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 100 em uma escala de 0 a 255.
        # canal verde = 116 em uma escala de 0 a 255.
        # canal azul = 139 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 815, y_aviso, 285, 55, "aviso_senha_usuario", "Ao alterar um usuário, deixe Nova senha vazia para manter a senha atual.", cor_fundo="#FFFFFF", cor_texto="#64748B")

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    return tela

# Define a rotina `_nome_menu`, responsável por executar a lógica relacionada a nome menu.
# `def` = define uma nova função ou um novo método.
# `_nome_menu` = função, método ou classe chamada para executar a operação relacionada a nome menu.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _nome_menu(texto):

    # Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
    # `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    import re

    # Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
    # `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
    # `unicodedata` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a unicodedata.
    import unicodedata

    # Armazena ou associa em `base` o valor ou resultado definido nesta linha.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `unicodedata` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a unicodedata.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `normalize` = função, método ou classe chamada para executar a operação relacionada a normalize.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `NFKD` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `encode` = função, método ou classe chamada para executar a operação relacionada a encode.
    # `ascii` = texto literal utilizado nesta instrução.
    # `ignore` = texto literal utilizado nesta instrução.
    # `decode` = função, método ou classe chamada para executar a operação relacionada a decode.
    # `lower` = função, método ou classe chamada para executar a operação relacionada a lower.
    base = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode("ascii").lower()

    # Armazena ou associa em `base` o valor ou resultado definido nesta linha.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `sub` = função, método ou classe chamada para executar a operação relacionada a sub.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `[^a-z0-9]+` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `_` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
    base = re.sub(r"[^a-z0-9]+", "_", base).strip("_")

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `area` = texto literal utilizado nesta instrução.
    return base or "area"

# Define a rotina `criar_tela_menu`, responsável por executar a lógica relacionada a criar tela menu.
# `def` = define uma nova função ou um novo método.
# `criar_tela_menu` = função, método ou classe chamada para executar a operação relacionada a criar tela menu.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Tela` = classe que representa uma tela do projeto visual.
def criar_tela_menu(nome_sistema: str, destinos) -> Tela:

    # Armazena ou associa em `destinos` o valor ou resultado definido nesta linha.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `dict` = função ou tipo utilizado para criar ou representar um dicionário.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `fromkeys` = função, método ou classe chamada para executar a operação relacionada a fromkeys.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    destinos = list(dict.fromkeys(destinos))

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `Usuários` = texto literal utilizado nesta instrução.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if "Usuários" not in destinos:

        # Executa `destinos.append` com os argumentos informados para realizar a operação correspondente.
        # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Usuários` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        destinos.append("Usuários")

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_estilo_titulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_titulo` = função, método ou classe chamada para executar a operação relacionada a estilo titulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `760` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `48` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `titulo` = texto literal utilizado nesta instrução.
        # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_titulo(Componente("Label", 55, 35, 760, 48, "titulo", nome_sistema)),

        # Executa `_estilo_subtitulo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_subtitulo` = função, método ou classe chamada para executar a operação relacionada a estilo subtitulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `82` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `760` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `instrucao` = texto literal utilizado nesta instrução.
        # `Painel principal • escolha uma área para continuar` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_subtitulo(Componente("Label", 55, 82, 760, 30, "instrucao", "Painel principal • escolha uma área para continuar")),

        # Executa `_estilo_botao_perigo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_perigo` = identificador relacionado a um botão da interface, associado a estilo botao perigo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `965` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_sair` = texto literal utilizado nesta instrução.
        # `Sair da conta` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_perigo(Componente("Button", 965, 38, 160, 40, "btn_sair", "Sair da conta", acao="Sair da conta")),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Frame` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `1070` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `painel_boas_vindas` = texto literal utilizado nesta instrução.
        # `Visão geral` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Frame", 55, 135, 1070, 105, "painel_boas_vindas", "Visão geral", cor_fundo="#FFFFFF", cor_texto="#16324F"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `85` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `172` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `610` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `resumo` = texto literal utilizado nesta instrução.
        # `O sistema está pronto para cadastrar, consultar, editar e excluir registros.` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#334155` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 51 em uma escala de 0 a 255.
        # canal verde = 65 em uma escala de 0 a 255.
        # canal azul = 85 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 85, 172, 610, 30, "resumo", "O sistema está pronto para cadastrar, consultar, editar e excluir registros.", cor_fundo="#FFFFFF", cor_texto="#334155"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `85` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `202` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `610` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `25` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `resumo_2` = texto literal utilizado nesta instrução.
        # `Todas as áreas abaixo utilizam o mesmo banco SQLite do projeto.` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 100 em uma escala de 0 a 255.
        # canal verde = 116 em uma escala de 0 a 255.
        # canal azul = 139 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 85, 202, 610, 25, "resumo_2", "Todas as áreas abaixo utilizam o mesmo banco SQLite do projeto.", cor_fundo="#FFFFFF", cor_texto="#64748B"),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `780` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `172` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `50` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `status_sistema` = texto literal utilizado nesta instrução.
        # `Status: sistema disponível` = texto literal utilizado nesta instrução.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 255 em uma escala de 0 a 255.
        # canal verde = 255 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#2F855A` = código hexadecimal que representa aproximadamente a cor verde.
        # canal vermelho = 47 em uma escala de 0 a 255.
        # canal verde = 133 em uma escala de 0 a 255.
        # canal azul = 90 em uma escala de 0 a 255.
        # `negrito` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a negrito.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 780, 172, 285, 50, "status_sistema", "Status: sistema disponível", cor_fundo="#FFFFFF", cor_texto="#2F855A", negrito=True),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `450` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `lbl_atalhos` = texto literal utilizado nesta instrução.
        # `Áreas do sistema` = texto literal utilizado nesta instrução.
        # `fonte` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fonte.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Segoe UI` = texto literal utilizado nesta instrução.
        # `tamanho_fonte` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tamanho fonte.
        # `14` = valor numérico utilizado para definir o tamanho da fonte.
        # `negrito` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a negrito.
        # `True` = representa o valor lógico verdadeiro.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 55, 275, 450, 35, "lbl_atalhos", "Áreas do sistema", fonte="Segoe UI", tamanho_fonte=14, negrito=True, cor_texto="#16324F"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `colunas` o valor ou resultado definido nesta linha.
    # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `3` = valor numérico associado a `colunas` nesta instrução.
    colunas = 3

    # Armazena ou associa em `largura` o valor ou resultado definido nesta linha.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `325` = valor numérico utilizado para definir a largura nesta instrução.
    largura = 325

    # Armazena ou associa em `altura` o valor ou resultado definido nesta linha.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `82` = valor numérico utilizado para definir a altura nesta instrução.
    altura = 82

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `enumerate` = função que percorre elementos fornecendo também o respectivo índice.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for i, destino in enumerate(destinos):

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `divmod` = função, método ou classe chamada para executar a operação relacionada a divmod.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        linha, coluna = divmod(i, colunas)

        # Armazena ou associa em `x` o valor ou resultado definido nesta linha.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `55` = coordenada numérica utilizada no eixo X nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `355` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        x = 55 + coluna * 355

        # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `325` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        y = 325 + linha * 115

        # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
        texto = destino

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Usuários` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if destino == "Usuários":

            # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
            # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Gerenciar usuários` = texto literal utilizado nesta instrução.
            texto = "Gerenciar usuários"

        # Armazena ou associa em `botao` o valor ou resultado definido nesta linha.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `_nome_menu` = função, método ou classe chamada para executar a operação relacionada a nome menu.
        # `destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destino.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `Abrir outra tela` = texto literal utilizado nesta instrução.
        # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
        botao = Componente("Button", x, y, largura, altura, f"abrir_{_nome_menu(destino)}", texto, acao="Abrir outra tela", tela_destino=destino)

        # Armazena ou associa em `botao.fonte` o valor ou resultado definido nesta linha.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `fonte` = atributo, método ou recurso acessado com o nome `fonte`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Segoe UI` = texto literal utilizado nesta instrução.
        botao.fonte = "Segoe UI"

        # Armazena ou associa em `botao.tamanho_fonte` o valor ou resultado definido nesta linha.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tamanho_fonte` = atributo, método ou recurso acessado com o nome `tamanho_fonte`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `11` = valor numérico utilizado para definir o tamanho da fonte.
        botao.tamanho_fonte = 11

        # Armazena ou associa em `botao.negrito` o valor ou resultado definido nesta linha.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `negrito` = atributo, método ou recurso acessado com o nome `negrito`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        botao.negrito = True

        # Armazena ou associa em `botao.cor_fundo` o valor ou resultado definido nesta linha.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#EAF2FF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 234 em uma escala de 0 a 255.
        # canal verde = 242 em uma escala de 0 a 255.
        # canal azul = 255 em uma escala de 0 a 255.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `%` = operador utilizado para obter o resto de uma divisão ou aplicar formatação, conforme o contexto.
        # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `#EEF3F7` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
        # canal vermelho = 238 em uma escala de 0 a 255.
        # canal verde = 243 em uma escala de 0 a 255.
        # canal azul = 247 em uma escala de 0 a 255.
        botao.cor_fundo = "#EAF2FF" if coluna % 2 == 0 else "#EEF3F7"

        # Armazena ou associa em `botao.cor_texto` o valor ou resultado definido nesta linha.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
        # canal vermelho = 22 em uma escala de 0 a 255.
        # canal verde = 50 em uma escala de 0 a 255.
        # canal azul = 79 em uma escala de 0 a 255.
        botao.cor_texto = "#16324F"

        # Armazena ou associa em `botao.alinhamento` o valor ou resultado definido nesta linha.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `alinhamento` = atributo, método ou recurso acessado com o nome `alinhamento`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Centro` = texto literal utilizado nesta instrução.
        botao.alinhamento = "Centro"

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `botao` = identificador relacionado a um botão da interface, associado a botao.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(botao)

    # Armazena ou associa em `linhas` o valor ou resultado definido nesta linha.
    # `linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linhas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `destinos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a destinos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `colunas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a colunas.
    # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `//` = operador utilizado para realizar divisão inteira.
    linhas = max(1, (len(destinos) + colunas - 1) // colunas)

    # Armazena ou associa em `y_rodape` o valor ou resultado definido nesta linha.
    # `y_rodape` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y rodape.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `325` = valor numérico associado a `y_rodape` nesta instrução.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linhas.
    # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
    # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_rodape = 325 + linhas * 115 + 30

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Separator` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_rodape` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y rodape.
        # `1070` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `8` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `separador_menu` = texto literal utilizado nesta instrução.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Separator", 55, y_rodape, 1070, 8, "separador_menu", ""),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y_rodape` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y rodape.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `25` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `760` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `rodape` = texto literal utilizado nesta instrução.
        # `Você pode personalizar qualquer tela e componente no Designer Visual.` = texto literal utilizado nesta instrução.
        # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
        # canal vermelho = 100 em uma escala de 0 a 255.
        # canal verde = 116 em uma escala de 0 a 255.
        # canal azul = 139 em uma escala de 0 a 255.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente("Label", 55, y_rodape + 25, 760, 30, "rodape", "Você pode personalizar qualquer tela e componente no Designer Visual.", cor_texto="#64748B"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Menu Principal` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Menu Principal",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo=nome_sistema,

        # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `1180` = valor numérico utilizado para definir a largura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        largura=1180,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `max` = função que retorna o maior valor entre os valores informados.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `700` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y_rodape` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y rodape.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `90` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        altura=max(700, y_rodape + 90),

        # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `menu` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="menu",

        # Define o argumento nomeado `componentes` da chamada iniciada nas linhas anteriores.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        componentes=componentes,

        # Define o argumento nomeado `campos_banco` da chamada iniciada nas linhas anteriores.
        # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campos_banco=[],

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `_tela_auxiliar`, responsável por executar a lógica relacionada a tela auxiliar.
# `def` = define uma nova função ou um novo método.
# `_tela_auxiliar` = função, método ou classe chamada para executar a operação relacionada a tela auxiliar.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
# `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
# `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _tela_auxiliar(nome, titulo, tabela, campos):

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `criar_tela_crud` = função, método ou classe chamada para executar a operação relacionada a criar tela crud.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return criar_tela_crud(nome, titulo, tabela, campos, incluir_menu=True)

# Define a rotina `_telas_complementares`, responsável por executar a lógica relacionada a telas complementares.
# `def` = define uma nova função ou um novo método.
# `_telas_complementares` = função, método ou classe chamada para executar a operação relacionada a telas complementares.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome projeto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _telas_complementares(nome_projeto):

    # Armazena ou associa em `dados` o valor ou resultado definido nesta linha.
    dados = {

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Cadastro de Clientes": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Histórico de Contatos", "Histórico de Contatos", "historico_contatos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `cliente` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Cliente` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "cliente", "rotulo": "Cliente", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `data` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Data` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "data", "rotulo": "Data", "mascara": "Data", "validacao": "Data"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `assunto` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Assunto` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "assunto", "rotulo": "Assunto"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `canal` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Canal` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `WhatsApp` = texto literal utilizado nesta instrução.
                # `Presencial` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "canal", "rotulo": "Canal", "widget": "Combobox", "opcoes": ["Telefone", "E-mail", "WhatsApp", "Presencial"]},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `observacao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Observação` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "observacao", "rotulo": "Observação", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Cadastro de Produtos": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Fornecedores", "Cadastro de Fornecedores", "fornecedores", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Fornecedor` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Fornecedor", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `contato` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Contato` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "contato", "rotulo": "Contato"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `cidade` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Cidade` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "cidade", "rotulo": "Cidade"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Ativo` = texto literal utilizado nesta instrução.
                # `Inativo` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Ativo", "Inativo"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Categorias", "Categorias de Produtos", "categorias_produtos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `categoria` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Categoria` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "categoria", "rotulo": "Categoria", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `descricao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Descrição` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "descricao", "rotulo": "Descrição", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Agenda de Contatos": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Grupos", "Grupos de Contatos", "grupos_contatos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `grupo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Grupo` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "grupo", "rotulo": "Grupo", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `descricao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Descrição` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "descricao", "rotulo": "Descrição", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Controle de Estoque": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Movimentações", "Entradas e Saídas de Estoque", "movimentacoes_estoque", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `produto` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Produto` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "produto", "rotulo": "Produto", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `tipo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Movimentação` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Entrada` = texto literal utilizado nesta instrução.
                # `Saída` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "tipo", "rotulo": "Movimentação", "widget": "Combobox", "opcoes": ["Entrada", "Saída"], "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `quantidade` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Quantidade` = texto literal utilizado nesta instrução.
                # `tipo_sql` = texto literal utilizado nesta instrução.
                # `INTEGER` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Spinbox` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `Inteiro` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "quantidade", "rotulo": "Quantidade", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `data` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Data` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "data", "rotulo": "Data", "mascara": "Data", "validacao": "Data"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `responsavel` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Responsável` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "responsavel", "rotulo": "Responsável"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `observacao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Observação` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "observacao", "rotulo": "Observação", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Fornecedores", "Fornecedores do Estoque", "fornecedores_estoque", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `fornecedor` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Fornecedor` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "fornecedor", "rotulo": "Fornecedor", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `contato` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Contato` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "contato", "rotulo": "Contato"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Ativo` = texto literal utilizado nesta instrução.
                # `Inativo` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Ativo", "Inativo"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Gerenciador de Tarefas": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Categorias", "Categorias de Tarefas", "categorias_tarefas", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `categoria` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Categoria` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "categoria", "rotulo": "Categoria", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `descricao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Descrição` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "descricao", "rotulo": "Descrição", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Cadastro de Alunos": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Cursos", "Cadastro de Cursos", "cursos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `curso` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Curso` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "curso", "rotulo": "Curso", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `carga_horaria` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Carga horária` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "carga_horaria", "rotulo": "Carga horária"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `modalidade` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Modalidade` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Presencial` = texto literal utilizado nesta instrução.
                # `Online` = texto literal utilizado nesta instrução.
                # `Híbrido` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "modalidade", "rotulo": "Modalidade", "widget": "Combobox", "opcoes": ["Presencial", "Online", "Híbrido"]},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Ativo` = texto literal utilizado nesta instrução.
                # `Inativo` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Ativo", "Inativo"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Turmas", "Cadastro de Turmas", "turmas", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `turma` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Turma` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "turma", "rotulo": "Turma", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `curso` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Curso` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "curso", "rotulo": "Curso"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `periodo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Período` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "periodo", "rotulo": "Período"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Aberta` = texto literal utilizado nesta instrução.
                # `Encerrada` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Aberta", "Encerrada"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Biblioteca de Livros": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Empréstimos", "Controle de Empréstimos", "emprestimos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `livro` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Livro` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "livro", "rotulo": "Livro", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `leitor` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Leitor` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "leitor", "rotulo": "Leitor", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `data_emprestimo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Data empréstimo` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `Data` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "data_emprestimo", "rotulo": "Data empréstimo", "mascara": "Data", "validacao": "Data"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `data_devolucao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Data devolução` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `Data` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "data_devolucao", "rotulo": "Data devolução", "mascara": "Data", "validacao": "Data"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Emprestado` = texto literal utilizado nesta instrução.
                # `Devolvido` = texto literal utilizado nesta instrução.
                # `Atrasado` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Emprestado", "Devolvido", "Atrasado"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Leitores", "Cadastro de Leitores", "leitores", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Nome` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `documento` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Documento` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "documento", "rotulo": "Documento"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Controle Financeiro": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Categorias", "Categorias Financeiras", "categorias_financeiras", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `categoria` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Categoria` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "categoria", "rotulo": "Categoria", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `tipo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Tipo` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Receita` = texto literal utilizado nesta instrução.
                # `Despesa` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "tipo", "rotulo": "Tipo", "widget": "Combobox", "opcoes": ["Receita", "Despesa"]},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `descricao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Descrição` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "descricao", "rotulo": "Descrição", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Agenda de Consultas": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Pacientes", "Cadastro de Pacientes", "pacientes", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Paciente` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Paciente", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `documento` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Documento` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "documento", "rotulo": "Documento"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `observacao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Observação` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "observacao", "rotulo": "Observação", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Profissionais", "Cadastro de Profissionais", "profissionais", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Profissional` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Profissional", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `especialidade` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Especialidade` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "especialidade", "rotulo": "Especialidade"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `registro` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Registro` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "registro", "rotulo": "Registro"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Ativo` = texto literal utilizado nesta instrução.
                # `Inativo` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Ativo", "Inativo"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Ordens de Serviço": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Clientes", "Clientes das Ordens", "clientes_os", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Cliente` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Cliente", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `documento` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Documento` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "documento", "rotulo": "Documento"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Serviços", "Catálogo de Serviços", "servicos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `servico` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Serviço` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "servico", "rotulo": "Serviço", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `valor` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Valor` = texto literal utilizado nesta instrução.
                # `tipo_sql` = texto literal utilizado nesta instrução.
                # `REAL` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `Moeda` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `Decimal` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "valor", "rotulo": "Valor", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `prazo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Prazo` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "prazo", "rotulo": "Prazo"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `descricao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Descrição` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "descricao", "rotulo": "Descrição", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Cadastro de Veículos": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Proprietários", "Cadastro de Proprietários", "proprietarios", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Nome` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Nome", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `documento` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Documento` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "documento", "rotulo": "Documento"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Controle de Eventos": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Participantes", "Participantes dos Eventos", "participantes_eventos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `evento` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Evento` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "evento", "rotulo": "Evento", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Participante` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Participante", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Confirmado` = texto literal utilizado nesta instrução.
                # `Pendente` = texto literal utilizado nesta instrução.
                # `Cancelado` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Confirmado", "Pendente", "Cancelado"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Gerenciador de Receitas": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Categorias", "Categorias de Receitas", "categorias_receitas", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `categoria` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Categoria` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "categoria", "rotulo": "Categoria", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `descricao` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Descrição` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Text` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "descricao", "rotulo": "Descrição", "widget": "Text"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Cadastro de Funcionários": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Departamentos", "Cadastro de Departamentos", "departamentos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `departamento` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Departamento` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "departamento", "rotulo": "Departamento", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `responsavel` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Responsável` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "responsavel", "rotulo": "Responsável"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `ramal` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Ramal` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "ramal", "rotulo": "Ramal"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `status` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Status` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Combobox` = texto literal utilizado nesta instrução.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Ativo` = texto literal utilizado nesta instrução.
                # `Inativo` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "status", "rotulo": "Status", "widget": "Combobox", "opcoes": ["Ativo", "Inativo"]},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "Controle de Pedidos": [

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Clientes", "Clientes dos Pedidos", "clientes_pedidos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Cliente` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "nome", "rotulo": "Cliente", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `telefone` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Telefone` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "telefone", "rotulo": "Telefone", "mascara": "Telefone"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `email` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `E-mail` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `cidade` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Cidade` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "cidade", "rotulo": "Cidade"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

            # Executa a instrução desta linha como parte da lógica atual do programa.
            ("Produtos", "Produtos dos Pedidos", "produtos_pedidos", [

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `produto` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Produto` = texto literal utilizado nesta instrução.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `True` = representa o valor lógico verdadeiro.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "produto", "rotulo": "Produto", "obrigatorio": True},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `codigo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Código` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "codigo", "rotulo": "Código"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `preco` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Preço` = texto literal utilizado nesta instrução.
                # `tipo_sql` = texto literal utilizado nesta instrução.
                # `REAL` = texto literal utilizado nesta instrução.
                # `mascara` = texto literal utilizado nesta instrução.
                # `Moeda` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `Decimal` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "preco", "rotulo": "Preço", "tipo_sql": "REAL", "mascara": "Moeda", "validacao": "Decimal"},

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `estoque` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `Estoque` = texto literal utilizado nesta instrução.
                # `tipo_sql` = texto literal utilizado nesta instrução.
                # `INTEGER` = texto literal utilizado nesta instrução.
                # `widget` = texto literal utilizado nesta instrução.
                # `Spinbox` = texto literal utilizado nesta instrução.
                # `validacao` = texto literal utilizado nesta instrução.
                # `Inteiro` = texto literal utilizado nesta instrução.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                {"nome": "estoque", "rotulo": "Estoque", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ]),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    }

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `_tela_auxiliar` = função, método ou classe chamada para executar a operação relacionada a tela auxiliar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
    # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `nome_projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome projeto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return [_tela_auxiliar(*item) for item in dados.get(nome_projeto, [])]

# Define a rotina `_aprimorar_calculadora`, responsável por executar a lógica relacionada a aprimorar calculadora.
# `def` = define uma nova função ou um novo método.
# `_aprimorar_calculadora` = função, método ou classe chamada para executar a operação relacionada a aprimorar calculadora.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _aprimorar_calculadora(tela):

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `!=` = operador de comparação utilizado para verificar se os valores são diferentes.
    # `Calculadora` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if tela.nome != "Calculadora":

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        return tela

    # Armazena ou associa em `tela.largura` o valor ou resultado definido nesta linha.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `largura` = atributo, método ou recurso acessado com o nome `largura`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `1180` = valor numérico utilizado para definir a largura nesta instrução.
    tela.largura = 1180

    # Armazena ou associa em `tela.altura` o valor ou resultado definido nesta linha.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `altura` = atributo, método ou recurso acessado com o nome `altura`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `700` = valor numérico utilizado para definir a altura nesta instrução.
    tela.altura = 700

    # Executa `tela.componentes.insert` com os argumentos informados para realizar a operação correspondente.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `insert` = função, método ou classe chamada para executar a operação relacionada a insert.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Componente` = classe que representa um componente inserido no Designer Visual.
    # `Frame` = texto literal utilizado nesta instrução.
    # `255` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `670` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `490` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `painel_calculadora` = texto literal utilizado nesta instrução.
    # `Calculadora` = texto literal utilizado nesta instrução.
    # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
    # canal vermelho = 255 em uma escala de 0 a 255.
    # canal verde = 255 em uma escala de 0 a 255.
    # canal azul = 255 em uma escala de 0 a 255.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `#16324F` = código hexadecimal que representa aproximadamente a cor azul escuro.
    # canal vermelho = 22 em uma escala de 0 a 255.
    # canal verde = 50 em uma escala de 0 a 255.
    # canal azul = 79 em uma escala de 0 a 255.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    tela.componentes.insert(0, Componente("Frame", 255, 105, 670, 490, "painel_calculadora", "Calculadora", cor_fundo="#FFFFFF", cor_texto="#16324F"))

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
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `titulo` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if comp.nome == "titulo":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `altura` = atributo, método ou recurso acessado com o nome `altura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `300` = valor numérico utilizado para definir a altura nesta instrução.
            # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `580` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `46` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            comp.x, comp.y, comp.largura, comp.altura = 300, 135, 580, 46

            # Executa `_estilo_titulo` com os argumentos informados para realizar a operação correspondente.
            # `_estilo_titulo` = função, método ou classe chamada para executar a operação relacionada a estilo titulo.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _estilo_titulo(comp)

            # Armazena ou associa em `comp.cor_fundo` o valor ou resultado definido nesta linha.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
            # canal vermelho = 255 em uma escala de 0 a 255.
            # canal verde = 255 em uma escala de 0 a 255.
            # canal azul = 255 em uma escala de 0 a 255.
            comp.cor_fundo = "#FFFFFF"

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `lbl_numero_1` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "lbl_numero_1":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `315` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `;` = separa instruções na mesma linha. Este símbolo pertence ao código original.
            # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
            # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
            # canal vermelho = 255 em uma escala de 0 a 255.
            # canal verde = 255 em uma escala de 0 a 255.
            # canal azul = 255 em uma escala de 0 a 255.
            comp.x, comp.y = 315, 215; comp.cor_fundo = "#FFFFFF"

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `numero_1` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "numero_1":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `500` = valor numérico utilizado para definir a largura nesta instrução.
            # `210` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            comp.x, comp.y, comp.largura = 500, 210, 360

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `lbl_operacao` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "lbl_operacao":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `315` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `;` = separa instruções na mesma linha. Este símbolo pertence ao código original.
            # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
            # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
            # canal vermelho = 255 em uma escala de 0 a 255.
            # canal verde = 255 em uma escala de 0 a 255.
            # canal azul = 255 em uma escala de 0 a 255.
            comp.x, comp.y = 315, 275; comp.cor_fundo = "#FFFFFF"

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `operacao` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "operacao":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `500` = valor numérico utilizado para definir a largura nesta instrução.
            # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            comp.x, comp.y, comp.largura = 500, 270, 360

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `lbl_numero_2` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "lbl_numero_2":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `315` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `335` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `;` = separa instruções na mesma linha. Este símbolo pertence ao código original.
            # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
            # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
            # canal vermelho = 255 em uma escala de 0 a 255.
            # canal verde = 255 em uma escala de 0 a 255.
            # canal azul = 255 em uma escala de 0 a 255.
            comp.x, comp.y = 315, 335; comp.cor_fundo = "#FFFFFF"

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `numero_2` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "numero_2":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `500` = valor numérico utilizado para definir a largura nesta instrução.
            # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            comp.x, comp.y, comp.largura = 500, 330, 360

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "btn_calcular":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `500` = valor numérico utilizado para definir a largura nesta instrução.
            # `400` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `;` = separa instruções na mesma linha. Este símbolo pertence ao código original.
            # `_estilo_botao_primario` = identificador relacionado a um botão da interface, associado a estilo botao primario.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            comp.x, comp.y, comp.largura = 500, 400, 170; _estilo_botao_primario(comp)

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `btn_limpar` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "btn_limpar":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `690` = valor numérico utilizado para definir a largura nesta instrução.
            # `400` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `;` = separa instruções na mesma linha. Este símbolo pertence ao código original.
            # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            comp.x, comp.y, comp.largura = 690, 400, 170; _estilo_botao_secundario(comp)

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `lbl_resultado` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "lbl_resultado":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `315` = coordenada numérica utilizada no eixo Y nesta instrução.
            # `475` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `;` = separa instruções na mesma linha. Este símbolo pertence ao código original.
            # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
            # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
            # canal vermelho = 255 em uma escala de 0 a 255.
            # canal verde = 255 em uma escala de 0 a 255.
            # canal azul = 255 em uma escala de 0 a 255.
            comp.x, comp.y = 315, 475; comp.cor_fundo = "#FFFFFF"

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `resultado` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "resultado":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `500` = valor numérico utilizado para definir a largura nesta instrução.
            # `470` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            comp.x, comp.y, comp.largura = 500, 470, 360

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `instrucao` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif comp.nome == "instrucao":

            # Executa a instrução desta linha como parte da lógica atual do programa.
            # `comp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comp.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `x` = atributo, método ou recurso acessado com o nome `x`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `y` = atributo, método ou recurso acessado com o nome `y`.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `315` = valor numérico utilizado para definir a largura nesta instrução.
            # `535` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `545` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `;` = separa instruções na mesma linha. Este símbolo pertence ao código original.
            # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
            # `#FFFFFF` = código hexadecimal que representa aproximadamente a cor branco ou quase branco.
            # canal vermelho = 255 em uma escala de 0 a 255.
            # canal verde = 255 em uma escala de 0 a 255.
            # canal azul = 255 em uma escala de 0 a 255.
            # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
            # `#64748B` = código hexadecimal que representa aproximadamente a cor azul.
            # canal vermelho = 100 em uma escala de 0 a 255.
            # canal verde = 116 em uma escala de 0 a 255.
            # canal azul = 139 em uma escala de 0 a 255.
            comp.x, comp.y, comp.largura = 315, 535, 545; comp.cor_fundo = "#FFFFFF"; comp.cor_texto = "#64748B"

    # Executa `tela.componentes.extend` com os argumentos informados para realizar a operação correspondente.
    tela.componentes.extend([

        # Executa `_estilo_botao_secundario` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_secundario` = identificador relacionado a um botão da interface, associado a estilo botao secundario.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `920` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_menu` = texto literal utilizado nesta instrução.
        # `Menu` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Abrir outra tela` = texto literal utilizado nesta instrução.
        # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
        # `Menu Principal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_secundario(Componente("Button", 920, 35, 100, 38, "btn_menu", "Menu", acao="Abrir outra tela", tela_destino="Menu Principal")),

        # Executa `_estilo_botao_perigo` com os argumentos informados para realizar a operação correspondente.
        # `_estilo_botao_perigo` = identificador relacionado a um botão da interface, associado a estilo botao perigo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `1035` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
        # `38` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `btn_sair` = texto literal utilizado nesta instrução.
        # `Sair` = texto literal utilizado nesta instrução.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Sair da conta` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _estilo_botao_perigo(Componente("Button", 1035, 35, 100, 38, "btn_sair", "Sair", acao="Sair da conta")),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    return tela

# Define a rotina `montar_projeto_com_fluxo`, responsável por executar a lógica relacionada a montar projeto com fluxo.
# `def` = define uma nova função ou um novo método.
# `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
# `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def montar_projeto_com_fluxo(nome, tema, telas_funcionais) -> Projeto:

    # Armazena ou associa em `telas_funcionais` o valor ou resultado definido nesta linha.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `_aprimorar_calculadora` = função, método ou classe chamada para executar a operação relacionada a aprimorar calculadora.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    telas_funcionais = [_aprimorar_calculadora(tela) for tela in list(telas_funcionais)]

    # Armazena ou associa em `nomes_existentes` o valor ou resultado definido nesta linha.
    # `nomes_existentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes existentes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    nomes_existentes = {t.nome for t in telas_funcionais}

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `_telas_complementares` = função, método ou classe chamada para executar a operação relacionada a telas complementares.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for tela in _telas_complementares(nome):

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `nomes_existentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes existentes.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if tela.nome not in nomes_existentes:

            # Executa `telas_funcionais.append` com os argumentos informados para realizar a operação correspondente.
            # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            telas_funcionais.append(tela)

            # Executa `nomes_existentes.add` com os argumentos informados para realizar a operação correspondente.
            # `nomes_existentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes existentes.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `add` = função, método ou classe chamada para executar a operação relacionada a add.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `nome` = atributo, método ou recurso acessado com o nome `nome`.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            nomes_existentes.add(tela.nome)

    # Armazena ou associa em `login` o valor ou resultado definido nesta linha.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_login` = função, método ou classe chamada para executar a operação relacionada a criar tela login.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Menu Principal` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    login = criar_tela_login("Menu Principal")

    # Armazena ou associa em `cadastro_usuario` o valor ou resultado definido nesta linha.
    # `cadastro_usuario` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a cadastro usuario.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_cadastro_usuario` = função, método ou classe chamada para executar a operação relacionada a criar tela cadastro usuario.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    cadastro_usuario = criar_tela_cadastro_usuario()

    # Armazena ou associa em `gerenciar_usuarios` o valor ou resultado definido nesta linha.
    # `gerenciar_usuarios` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a gerenciar usuarios.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_gerenciar_usuarios` = função, método ou classe chamada para executar a operação relacionada a criar tela gerenciar usuarios.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    gerenciar_usuarios = criar_tela_gerenciar_usuarios()

    # Armazena ou associa em `menu` o valor ou resultado definido nesta linha.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `criar_tela_menu` = função, método ou classe chamada para executar a operação relacionada a criar tela menu.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    menu = criar_tela_menu(nome, [t.nome for t in telas_funcionais])

    # Armazena ou associa em `telas` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `cadastro_usuario` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a cadastro usuario.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `gerenciar_usuarios` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a gerenciar usuarios.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `telas_funcionais` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas funcionais.
    telas = [login, cadastro_usuario, menu, gerenciar_usuarios] + telas_funcionais

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = Projeto(nome, tema, telas, login.id)

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

# Armazena ou associa em `_modelo_clientes_final_base` o valor ou resultado definido nesta linha.
# `_modelo_clientes_final_base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo clientes final base.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `modelo_clientes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo clientes.
_modelo_clientes_final_base = modelo_clientes

# Armazena ou associa em `_modelo_estoque_final_base` o valor ou resultado definido nesta linha.
# `_modelo_estoque_final_base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo estoque final base.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `modelo_estoque` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo estoque.
_modelo_estoque_final_base = modelo_estoque

# Define a rotina `_modelo_clientes_final`, responsável por executar a lógica relacionada a modelo clientes final.
# `def` = define uma nova função ou um novo método.
# `_modelo_clientes_final` = função, método ou classe chamada para executar a operação relacionada a modelo clientes final.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _modelo_clientes_final():

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_modelo_clientes_final_base` = função, método ou classe chamada para executar a operação relacionada a modelo clientes final base.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = _modelo_clientes_final_base()

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `telas` = atributo, método ou recurso acessado com o nome `telas`.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for tela in projeto.telas:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Histórico de Contatos` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if tela.nome == "Histórico de Contatos":

            # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            for componente in tela.componentes:

                # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
                # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
                # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `nome` = atributo, método ou recurso acessado com o nome `nome`.
                # `==` = operador de comparação utilizado para verificar se os valores são iguais.
                # `cliente` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                if componente.nome == "cliente":

                    # Armazena ou associa em `componente.tipo` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `Combobox` = texto literal utilizado nesta instrução.
                    componente.tipo = "Combobox"

                    # Armazena ou associa em `componente.opcoes` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `opcoes` = atributo, método ou recurso acessado com o nome `opcoes`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                    componente.opcoes = []

                    # Armazena ou associa em `componente.obrigatorio` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `obrigatorio` = atributo, método ou recurso acessado com o nome `obrigatorio`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `True` = representa o valor lógico verdadeiro.
                    componente.obrigatorio = True

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    return projeto

# Define a rotina `_modelo_estoque_final`, responsável por executar a lógica relacionada a modelo estoque final.
# `def` = define uma nova função ou um novo método.
# `_modelo_estoque_final` = função, método ou classe chamada para executar a operação relacionada a modelo estoque final.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _modelo_estoque_final():

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_modelo_estoque_final_base` = função, método ou classe chamada para executar a operação relacionada a modelo estoque final base.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = _modelo_estoque_final_base()

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `telas` = atributo, método ou recurso acessado com o nome `telas`.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for tela in projeto.telas:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Estoque` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if tela.nome == "Estoque":

            # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            for componente in tela.componentes:

                # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
                # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
                # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `nome` = atributo, método ou recurso acessado com o nome `nome`.
                # `==` = operador de comparação utilizado para verificar se os valores são iguais.
                # `fornecedor` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                if componente.nome == "fornecedor":

                    # Armazena ou associa em `componente.tipo` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `Combobox` = texto literal utilizado nesta instrução.
                    componente.tipo = "Combobox"

                    # Armazena ou associa em `componente.opcoes` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `opcoes` = atributo, método ou recurso acessado com o nome `opcoes`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                    componente.opcoes = []

        # Verifica uma condição alternativa quando a condição anterior não foi atendida.
        # `elif` = testa uma condição alternativa quando as condições anteriores não foram atendidas.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `nome` = atributo, método ou recurso acessado com o nome `nome`.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Movimentações` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        elif tela.nome == "Movimentações":

            # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            for componente in tela.componentes:

                # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
                # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
                # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `nome` = atributo, método ou recurso acessado com o nome `nome`.
                # `==` = operador de comparação utilizado para verificar se os valores são iguais.
                # `produto` = texto literal utilizado nesta instrução.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                if componente.nome == "produto":

                    # Armazena ou associa em `componente.tipo` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `tipo` = atributo, método ou recurso acessado com o nome `tipo`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `Combobox` = texto literal utilizado nesta instrução.
                    componente.tipo = "Combobox"

                    # Armazena ou associa em `componente.opcoes` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `opcoes` = atributo, método ou recurso acessado com o nome `opcoes`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                    componente.opcoes = []

                    # Armazena ou associa em `componente.obrigatorio` o valor ou resultado definido nesta linha.
                    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
                    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                    # `obrigatorio` = atributo, método ou recurso acessado com o nome `obrigatorio`.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `True` = representa o valor lógico verdadeiro.
                    componente.obrigatorio = True

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    return projeto

# Armazena ou associa em `MODELOS` o valor ou resultado definido nesta linha.
MODELOS = [

    # Executa a instrução desta linha como parte da lógica atual do programa.
    {

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `Cadastro de Clientes` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "nome": "Cadastro de Clientes",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "descricao": (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # texto literal = fornece o conteúdo textual utilizado por esta instrução.
            "Sistema completo com Login, criação e gerenciamento de usuários, Menu Principal, "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # texto literal = fornece o conteúdo textual utilizado por esta instrução.
            "cadastro de clientes, pesquisa, edição, exclusão e Histórico de Contatos vinculado "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `aos clientes já cadastrados.` = texto literal utilizado nesta instrução.
            "aos clientes já cadastrados."

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `fabrica` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `_modelo_clientes_final` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo clientes final.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "fabrica": _modelo_clientes_final,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    },

    # Executa a instrução desta linha como parte da lógica atual do programa.
    {

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `nome` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `Controle de Estoque` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "nome": "Controle de Estoque",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        "descricao": (

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # texto literal = fornece o conteúdo textual utilizado por esta instrução.
            "Sistema completo de estoque com Login, usuários, produtos, fornecedores, entradas e saídas. "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # texto literal = fornece o conteúdo textual utilizado por esta instrução.
            "Fornecedores e produtos são selecionados por listas do SQLite e as movimentações atualizam "

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `automaticamente o saldo do estoque.` = texto literal utilizado nesta instrução.
            "automaticamente o saldo do estoque."

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `fabrica` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `_modelo_estoque_final` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo estoque final.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "fabrica": _modelo_estoque_final,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    },

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `]` = fecha a lista, índice, acesso a elemento ou compreensão.
]
