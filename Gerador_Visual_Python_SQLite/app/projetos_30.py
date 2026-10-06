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
# `acoes_genericas` = atributo, método ou recurso acessado com o nome `acoes_genericas`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `normalizar_projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normalizar projeto.
from .acoes_genericas import normalizar_projeto

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `modelos` = atributo, método ou recurso acessado com o nome `modelos`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `Componente` = classe que representa um componente inserido no Designer Visual.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `Tela` = classe que representa uma tela do projeto visual.
from .modelos import Componente, Projeto, Tela

# Define a rotina `_label`, responsável por executar a lógica relacionada a label.
# `def` = define uma nova função ou um novo método.
# `_label` = identificador relacionado a um rótulo de texto da interface.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `None` = representa ausência de valor.
# `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
# `180` = valor numérico utilizado para definir a largura nesta instrução.
# `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
# `28` = valor numérico utilizado para definir a altura nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _label(x, y, texto, nome=None, largura=180, altura=28):

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Componente(

        # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Label` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tipo="Label",

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
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=altura,

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `abs` = função que retorna o valor absoluto do número informado.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `hash` = função, método ou classe chamada para executar a operação relacionada a hash.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `%` = operador utilizado para obter o resto de uma divisão ou aplicar formatação, conforme o contexto.
        # `100000` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        nome=nome or f"lbl_{abs(hash((x, y, texto))) % 100000}",

        # Define o argumento nomeado `texto` da chamada iniciada nas linhas anteriores.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        texto=texto,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `_campo`, responsável por executar a lógica relacionada a campo.
def _campo(

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    nome,

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    rotulo,

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    x,

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    y,

    # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `240` = valor numérico utilizado para definir a largura nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    largura=240,

    # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
    # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Entry` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    tipo="Entry",

    # Define o argumento nomeado `opcoes` da chamada iniciada nas linhas anteriores.
    # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `None` = representa ausência de valor.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    opcoes=None,

    # Define o argumento nomeado `mascara` da chamada iniciada nas linhas anteriores.
    # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Nenhuma` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    mascara="Nenhuma",

    # Define o argumento nomeado `validacao` da chamada iniciada nas linhas anteriores.
    # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Nenhuma` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    validacao="Nenhuma",

    # Define o argumento nomeado `obrigatorio` da chamada iniciada nas linhas anteriores.
    # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    obrigatorio=False,

    # Define o argumento nomeado `campo_banco` da chamada iniciada nas linhas anteriores.
    # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `None` = representa ausência de valor.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    campo_banco=None,

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
):

    # Armazena ou associa em `campo_sql` o valor ou resultado definido nesta linha.
    # `campo_sql` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo sql.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
    # `is` = compara a identidade entre objetos.
    # `None` = representa ausência de valor.
    # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
    campo_sql = nome if campo_banco is None else campo_banco

    # Armazena ou associa em `componente` o valor ou resultado definido nesta linha.
    componente = Componente(

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
        # `96` = valor numérico utilizado para definir a altura nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `Text` = texto literal utilizado nesta instrução.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `34` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=96 if tipo == "Text" else 34,

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome=nome,

        # Define o argumento nomeado `texto` da chamada iniciada nas linhas anteriores.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # texto vazio = representa uma string sem caracteres.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        texto="",

        # Define o argumento nomeado `opcoes` da chamada iniciada nas linhas anteriores.
        # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `list` = função ou tipo utilizado para criar ou representar uma lista.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        opcoes=list(opcoes or []),

        # Define o argumento nomeado `campo_banco` da chamada iniciada nas linhas anteriores.
        # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `campo_sql` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo sql.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campo_banco=campo_sql,

        # Define o argumento nomeado `titulo_coluna` da chamada iniciada nas linhas anteriores.
        # `titulo_coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo coluna.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo_coluna=rotulo,

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

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `componente` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componente.
    return componente

# Define a rotina `_botao`, responsável por executar a lógica relacionada a botao.
# `def` = define uma nova função ou um novo método.
# `_botao` = identificador relacionado a um botão da interface, associado a botao.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
# `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
# `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `180` = valor numérico utilizado para definir a largura nesta instrução.
# `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
# `Nenhuma` = texto literal utilizado nesta instrução.
# `**` = operador utilizado para realizar potenciação.
# `kwargs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a kwargs.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _botao(nome, texto, x, y, largura=180, acao="Nenhuma", **kwargs):

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return Componente(

        # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Button` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tipo="Button",

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
        # `40` = valor numérico utilizado para definir a altura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=40,

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

        # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        acao=acao,

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `**` = operador utilizado para realizar potenciação.
        # `kwargs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a kwargs.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        **kwargs,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `_projeto_uma_tela`, responsável por executar a lógica relacionada a projeto uma tela.
# `def` = define uma nova função ou um novo método.
# `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
# `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
# `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `dados` = texto literal utilizado nesta instrução.
# `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
# `650` = valor numérico utilizado para definir a altura nesta instrução.
# `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
# `Claro` = texto literal utilizado nesta instrução.
# `exibir_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir dados.
# `False` = representa o valor lógico falso.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _projeto_uma_tela(nome, componentes, *, tabela="dados", altura=650, tema="Claro", exibir_dados=False):

    # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
    tela = Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Tela Principal` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Tela Principal",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo=nome,

        # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `1000` = valor numérico utilizado para definir a largura nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        largura=1000,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=altura,

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
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        campos_banco=[],

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    projeto = Projeto(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome=nome,

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema=tema,

        # Define o argumento nomeado `telas` da chamada iniciada nas linhas anteriores.
        # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        telas=[tela],

        # Define o argumento nomeado `tela_ativa_id` da chamada iniciada nas linhas anteriores.
        # `tela_ativa_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela ativa id.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `id` = atributo, método ou recurso acessado com o nome `id`.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tela_ativa_id=tela.id,

        # Define o argumento nomeado `exibir_aba_dados` da chamada iniciada nas linhas anteriores.
        # `exibir_aba_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir aba dados.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `exibir_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir dados.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        exibir_aba_dados=exibir_dados,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `normalizar_projeto` = função, método ou classe chamada para executar a operação relacionada a normalizar projeto.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `adicionar_botao_cadastro` = identificador relacionado a um botão da interface, associado a adicionar botao cadastro.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return normalizar_projeto(projeto, adicionar_botao_cadastro=False)

# Define a rotina `_crud_simples`, responsável por executar a lógica relacionada a crud simples.
# `def` = define uma nova função ou um novo método.
# `_crud_simples` = função, método ou classe chamada para executar a operação relacionada a crud simples.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
# `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
# `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
# `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `Claro` = texto literal utilizado nesta instrução.
# `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
# `720` = valor numérico utilizado para definir a altura nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _crud_simples(nome, tabela, campos, *, tema="Claro", altura=720):

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `24` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `700` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(35, 24, nome, "titulo", largura=700, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `64` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Preencha os campos e use os botões abaixo.` = texto literal utilizado nesta instrução.
        # `instrucao` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `600` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(35, 64, "Preencha os campos e use os botões abaixo.", "instrucao", largura=600),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `nomes_campos` o valor ou resultado definido nesta linha.
    # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    nomes_campos = []

    # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `112` = coordenada numérica utilizada no eixo Y nesta instrução.
    y = 112

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `enumerate` = função que percorre elementos fornecendo também o respectivo índice.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for indice, item in enumerate(campos):

        # Armazena ou associa em `coluna` o valor ou resultado definido nesta linha.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
        # `%` = operador utilizado para obter o resto de uma divisão ou aplicar formatação, conforme o contexto.
        # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        coluna = indice % 2

        # Armazena ou associa em `linha` o valor ou resultado definido nesta linha.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
        # `//` = operador utilizado para realizar divisão inteira.
        # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        linha = indice // 2

        # Armazena ou associa em `x_label` o valor ou resultado definido nesta linha.
        # `x_label` = identificador relacionado a um rótulo de texto da interface.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `35` = valor numérico associado a `x_label` nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `515` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        x_label = 35 if coluna == 0 else 515

        # Armazena ou associa em `x_campo` o valor ou resultado definido nesta linha.
        # `x_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x campo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `175` = valor numérico associado a `x_campo` nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `655` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        x_campo = 175 if coluna == 0 else 655

        # Armazena ou associa em `y_item` o valor ou resultado definido nesta linha.
        # `y_item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y item.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `58` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        y_item = y + linha * 58

        # Armazena ou associa em `tipo` o valor ou resultado definido nesta linha.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tipo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Entry` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        tipo = item.get("tipo", "Entry")

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `x_label` = identificador relacionado a um rótulo de texto da interface.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y_item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y item.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `3` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `130` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_label(x_label, y_item + 3, item["rotulo"], f"lbl_{item['nome']}", largura=130))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        componentes.append(

            # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
            _campo(

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `nome` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                item["nome"],

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                item["rotulo"],

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `x_campo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x campo.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                x_campo,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `y_item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y item.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y_item,

                # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
                # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `285` = valor numérico utilizado para definir a largura nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                largura=285,

                # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
                # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                tipo=tipo,

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

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Executa `nomes_campos.append` com os argumentos informados para realizar a operação correspondente.
        # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `nome` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        nomes_campos.append(item["nome"])

    # Armazena ou associa em `linhas` o valor ou resultado definido nesta linha.
    # `linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linhas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `//` = operador utilizado para realizar divisão inteira.
    # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    linhas = (len(campos) + 1) // 2

    # Armazena ou associa em `y_botoes` o valor ou resultado definido nesta linha.
    # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `linhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linhas.
    # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
    # `58` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `18` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    y_botoes = y + linhas * 58 + 18

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend(

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            _botao(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `btn_cadastrar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "btn_cadastrar",

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `Cadastrar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "Cadastrar",

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                35,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y_botoes,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                170,

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

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            _botao(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `btn_atualizar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "btn_atualizar",

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `Atualizar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "Atualizar",

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                215,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y_botoes,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                145,

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

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            # `_botao` = identificador relacionado a um botão da interface, associado a botao.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `btn_excluir` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Excluir` = texto literal utilizado nesta instrução.
            # `370` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
            # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Excluir registro` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _botao("btn_excluir", "Excluir", 370, y_botoes, 135, acao="Excluir registro"),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            _botao(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `btn_limpar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "btn_limpar",

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `Limpar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "Limpar",

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `515` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                515,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y_botoes,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                135,

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

            # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
            Componente(

                # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
                # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `Filtro` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                tipo="Filtro",

                # Define o argumento nomeado `x` da chamada iniciada nas linhas anteriores.
                # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `35` = coordenada numérica utilizada no eixo X nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                x=35,

                # Define o argumento nomeado `y` da chamada iniciada nas linhas anteriores.
                # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
                # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
                # `62` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y=y_botoes + 62,

                # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
                # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `350` = valor numérico utilizado para definir a largura nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                largura=350,

                # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
                # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `34` = valor numérico utilizado para definir a altura nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                altura=34,

                # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `filtro` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                nome="filtro",

                # Define o argumento nomeado `texto` da chamada iniciada nas linhas anteriores.
                # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `Pesquisar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                texto="Pesquisar",

                # Define o argumento nomeado `campo_filtro` da chamada iniciada nas linhas anteriores.
                # `campo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo filtro.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `nomes_campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes campos.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
                # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
                # texto vazio = representa uma string sem caracteres.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                campo_filtro=nomes_campos[0] if nomes_campos else "",

                # Define o argumento nomeado `alvo_filtro` da chamada iniciada nas linhas anteriores.
                # `alvo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo filtro.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `tabela_dados` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                alvo_filtro="tabela_dados",

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ),

            # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
            Componente(

                # Define o argumento nomeado `tipo` da chamada iniciada nas linhas anteriores.
                # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `Treeview` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                tipo="Treeview",

                # Define o argumento nomeado `x` da chamada iniciada nas linhas anteriores.
                # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `35` = coordenada numérica utilizada no eixo X nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                x=35,

                # Define o argumento nomeado `y` da chamada iniciada nas linhas anteriores.
                # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
                # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
                # `112` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y=y_botoes + 112,

                # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
                # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `905` = valor numérico utilizado para definir a largura nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                largura=905,

                # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
                # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `235` = valor numérico utilizado para definir a altura nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                altura=235,

                # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `tabela_dados` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                nome="tabela_dados",

                # Define o argumento nomeado `texto` da chamada iniciada nas linhas anteriores.
                # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # texto vazio = representa uma string sem caracteres.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                texto="",

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        ]

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Armazena ou associa em `altura_final` o valor ou resultado definido nesta linha.
    # `altura_final` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura final.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `max` = função que retorna o maior valor entre os valores informados.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `y_botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y botoes.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `380` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    altura_final = max(altura, y_botoes + 380)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _projeto_uma_tela(

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome,

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        componentes,

        # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela=tabela,

        # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `altura_final` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura final.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        altura=altura_final,

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema=tema,

        # Define o argumento nomeado `exibir_dados` da chamada iniciada nas linhas anteriores.
        # `exibir_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir dados.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        exibir_dados=True,

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_01_cadastro_alunos`, responsável por executar a lógica relacionada a projeto 01 cadastro alunos.
# `def` = define uma nova função ou um novo método.
# `projeto_01_cadastro_alunos` = função, método ou classe chamada para executar a operação relacionada a projeto 01 cadastro alunos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_01_cadastro_alunos():

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _crud_simples(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Cadastro de Alunos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Cadastro de Alunos",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `alunos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "alunos",

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
            # `idade` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Idade` = texto literal utilizado nesta instrução.
            # `validacao` = texto literal utilizado nesta instrução.
            # `Inteiro` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "idade", "rotulo": "Idade", "validacao": "Inteiro"},

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
            # `sexo` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Sexo` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Masculino` = texto literal utilizado nesta instrução.
            # `Feminino` = texto literal utilizado nesta instrução.
            # `Outro` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "sexo", "rotulo": "Sexo", "tipo": "Combobox", "opcoes": ["Masculino", "Feminino", "Outro"]},

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

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Azul corporativo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema="Azul corporativo",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_02_cadastro_produtos`, responsável por executar a lógica relacionada a projeto 02 cadastro produtos.
# `def` = define uma nova função ou um novo método.
# `projeto_02_cadastro_produtos` = função, método ou classe chamada para executar a operação relacionada a projeto 02 cadastro produtos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_02_cadastro_produtos():

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _crud_simples(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Cadastro de Produtos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Cadastro de Produtos",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `produtos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "produtos",

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

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
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Alimentos` = texto literal utilizado nesta instrução.
            # `Casa` = texto literal utilizado nesta instrução.
            # `Informática` = texto literal utilizado nesta instrução.
            # `Outros` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "categoria", "rotulo": "Categoria", "tipo": "Combobox", "opcoes": ["Alimentos", "Casa", "Informática", "Outros"]},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `preco` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Preço` = texto literal utilizado nesta instrução.
            # `validacao` = texto literal utilizado nesta instrução.
            # `Decimal` = texto literal utilizado nesta instrução.
            # `mascara` = texto literal utilizado nesta instrução.
            # `Moeda` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "preco", "rotulo": "Preço", "validacao": "Decimal", "mascara": "Moeda"},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `quantidade` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Quantidade` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Spinbox` = texto literal utilizado nesta instrução.
            # `validacao` = texto literal utilizado nesta instrução.
            # `Inteiro` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "quantidade", "rotulo": "Quantidade", "tipo": "Spinbox", "validacao": "Inteiro"},

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

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Verde` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema="Verde",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_03_calculadora_teclado`, responsável por executar a lógica relacionada a projeto 03 calculadora teclado.
# `def` = define uma nova função ou um novo método.
# `projeto_03_calculadora_teclado` = função, método ou classe chamada para executar a operação relacionada a projeto 03 calculadora teclado.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_03_calculadora_teclado():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora Básica com Teclado` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `540` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 28, "Calculadora Básica com Teclado", "titulo", largura=540, altura=42),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `visor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Visor` = texto literal utilizado nesta instrução.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `88` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `360` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("visor", "Visor", 320, 88, largura=360),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `historico_atual` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `134` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `360` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("historico_atual", "Resultado", 320, 134, largura=360),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Armazena ou associa em `botoes` o valor ou resultado definido nesta linha.
    botoes = [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `7` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `8` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `9` = texto literal utilizado nesta instrução.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `/` = texto literal utilizado nesta instrução.
        # `590` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        ("7", 320, 200), ("8", 410, 200), ("9", 500, 200), ("/", 590, 200),

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `4` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `5` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `6` = texto literal utilizado nesta instrução.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `*` = texto literal utilizado nesta instrução.
        # `590` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        ("4", 320, 250), ("5", 410, 250), ("6", 500, 250), ("*", 590, 250),

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `1` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `2` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `3` = texto literal utilizado nesta instrução.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `-` = texto literal utilizado nesta instrução.
        # `590` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        ("1", 320, 300), ("2", 410, 300), ("3", 500, 300), ("-", 590, 300),

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `0` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `350` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `.` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `350` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `+` = texto literal utilizado nesta instrução.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `350` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        ("0", 320, 350), (".", 410, 350), ("+", 500, 350),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `enumerate` = função que percorre elementos fornecendo também o respectivo índice.
    # `botoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a botoes.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for indice, (texto, x, y) in enumerate(botoes, 1):

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        componentes.append(

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            _botao(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                f"btn_tecla_{indice}",

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                texto,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                x,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                y,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                80,

                # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
                # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `Inserir valor em campo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                acao="Inserir valor em campo",

                # Define o argumento nomeado `campo_resultado` da chamada iniciada nas linhas anteriores.
                # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `visor` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                campo_resultado="visor",

                # Define o argumento nomeado `valor_acao` da chamada iniciada nas linhas anteriores.
                # `valor_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a valor acao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                valor_acao=texto,

                # Define o argumento nomeado `modo_insercao` da chamada iniciada nas linhas anteriores.
                # `modo_insercao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modo insercao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `Adicionar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                modo_insercao="Adicionar",

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            )

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend(

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            _botao(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `btn_igual` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "btn_igual",

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `=` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "=",

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `590` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                590,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `350` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                350,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                80,

                # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
                # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `Calcular expressão de um campo` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                acao="Calcular expressão de um campo",

                # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
                # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `visor` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                campos_acao=["visor"],

                # Define o argumento nomeado `campo_resultado` da chamada iniciada nas linhas anteriores.
                # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `historico_atual` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                campo_resultado="historico_atual",

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            _botao(

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `btn_limpar` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "btn_limpar",

                # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
                # `C` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                "C",

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                320,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                410,

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `350` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                350,

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
                # `visor` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `historico_atual` = texto literal utilizado nesta instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                campos_acao=["visor", "historico_atual"],

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            ),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        ]

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora Básica com Teclado` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `calculadora` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora Básica com Teclado", componentes, tabela="calculadora")

# Define a rotina `projeto_04_media_escolar`, responsável por executar a lógica relacionada a projeto 04 media escolar.
# `def` = define uma nova função ou um novo método.
# `projeto_04_media_escolar` = função, método ou classe chamada para executar a operação relacionada a projeto 04 media escolar.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_04_media_escolar():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `_label` = identificador relacionado a um rótulo de texto da interface.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `255` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `Calculadora de Média Escolar` = texto literal utilizado nesta instrução.
    # `titulo` = texto literal utilizado nesta instrução.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `520` = valor numérico utilizado para definir a largura nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `42` = valor numérico utilizado para definir a altura nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    componentes = [_label(255, 28, "Calculadora de Média Escolar", "titulo", largura=520, altura=42)]

    # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
    # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    campos = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `range` = função que cria uma sequência numérica utilizada normalmente em repetições.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `5` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for i in range(1, 5):

        # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `95` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        y = 95 + (i - 1) * 55

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `245` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `3` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `120` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_label(245, y + 3, f"Nota {i}", f"lbl_nota_{i}", largura=120))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `390` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_campo(f"nota_{i}", f"Nota {i}", 390, y, 300, validacao="Decimal"))

        # Executa `campos.append` com os argumentos informados para realizar a operação correspondente.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        campos.append(f"nota_{i}")

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `245` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `325` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Média` = texto literal utilizado nesta instrução.
        # `lbl_media` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `120` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(245, 325, "Média", "lbl_media", largura=120),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `media` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Média` = texto literal utilizado nesta instrução.
        # `390` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `322` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("media", "Média", 390, 322, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular média` = texto literal utilizado nesta instrução.
        # `390` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `382` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `media` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Média` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Calcular média", 390, 382, 300, acao="Calcular com campos", campos_acao=campos, campo_resultado="media", operador="Média"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora de Média Escolar` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `media_escolar` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora de Média Escolar", componentes, tabela="media_escolar")

# Define a rotina `projeto_05_imc`, responsável por executar a lógica relacionada a projeto 05 imc.
# `def` = define uma nova função ou um novo método.
# `projeto_05_imc` = função, método ou classe chamada para executar a operação relacionada a projeto 05 imc.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_05_imc():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora de IMC` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `420` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(300, 35, "Calculadora de IMC", "titulo", largura=420, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Peso (kg)` = texto literal utilizado nesta instrução.
        # `lbl_peso` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 115, "Peso (kg)", "lbl_peso", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `peso` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Peso` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `290` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("peso", "Peso", 420, 110, 290, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Altura (m)` = texto literal utilizado nesta instrução.
        # `lbl_altura` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 170, "Altura (m)", "lbl_altura", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `altura` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Altura` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `165` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `290` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("altura", "Altura", 420, 165, 290, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `225` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `IMC` = texto literal utilizado nesta instrução.
        # `lbl_imc` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 225, "IMC", "lbl_imc", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `imc` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `IMC` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `290` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("imc", "IMC", 420, 220, 290),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Classificação` = texto literal utilizado nesta instrução.
        # `lbl_classificacao` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 280, "Classificação", "lbl_classificacao", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `classificacao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Classificação` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `290` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("classificacao", "Classificação", 420, 275, 290),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        _botao(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_calcular` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "btn_calcular",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Calcular IMC` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Calcular IMC",

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            420,

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `340` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            340,

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `290` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            290,

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
            # `peso` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `altura` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            campos_acao=["peso", "altura"],

            # Define o argumento nomeado `campo_resultado` da chamada iniciada nas linhas anteriores.
            # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `imc` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campo_resultado="imc",

            # Define o argumento nomeado `operador` da chamada iniciada nas linhas anteriores.
            # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            operador="Expressão personalizada",

            # Define o argumento nomeado `expressao` da chamada iniciada nas linhas anteriores.
            # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `A / (B ** 2)` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            expressao="A / (B ** 2)",

            # Define o argumento nomeado `campo_resultado_2` da chamada iniciada nas linhas anteriores.
            # `campo_resultado_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado 2.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `classificacao` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campo_resultado_2="classificacao",

            # Define o argumento nomeado `expressao_2` da chamada iniciada nas linhas anteriores.
            # `expressao_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao 2.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # texto literal = fornece o conteúdo textual utilizado por esta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            expressao_2="'Abaixo do peso' if R < 18.5 else 'Peso adequado' if R < 25 else 'Sobrepeso' if R < 30 else 'Obesidade'",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora de IMC` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `imc` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora de IMC", componentes, tabela="imc")

# Define a rotina `projeto_06_desconto`, responsável por executar a lógica relacionada a projeto 06 desconto.
# `def` = define uma nova função ou um novo método.
# `projeto_06_desconto` = função, método ou classe chamada para executar a operação relacionada a projeto 06 desconto.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_06_desconto():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `290` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora de Desconto` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `460` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(290, 35, "Calculadora de Desconto", "titulo", largura=460, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Valor original` = texto literal utilizado nesta instrução.
        # `lbl_valor` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `160` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 120, "Valor original", "lbl_valor", largura=160),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `valor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Valor original` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("valor", "Valor original", 420, 115, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `175` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Desconto (%)` = texto literal utilizado nesta instrução.
        # `lbl_percentual` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `160` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 175, "Desconto (%)", "lbl_percentual", largura=160),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `percentual` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Desconto (%)` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("percentual", "Desconto (%)", 420, 170, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Valor do desconto` = texto literal utilizado nesta instrução.
        # `lbl_desconto` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `160` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 230, "Valor do desconto", "lbl_desconto", largura=160),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `desconto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Valor do desconto` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `225` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("desconto", "Valor do desconto", 420, 225, 300),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Valor final` = texto literal utilizado nesta instrução.
        # `lbl_final` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `160` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 285, "Valor final", "lbl_final", largura=160),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `valor_final` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Valor final` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("valor_final", "Valor final", 420, 280, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        _botao(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_calcular` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Calcular desconto` = texto literal utilizado nesta instrução.
            # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `345` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            "btn_calcular", "Calcular desconto", 420, 345, 300,

            # Armazena ou associa em `acao` o valor ou resultado definido nesta linha.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Calcular com campos` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `valor` = texto literal utilizado nesta instrução.
            # `percentual` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            acao="Calcular com campos", campos_acao=["valor", "percentual"],

            # Armazena ou associa em `campo_resultado` o valor ou resultado definido nesta linha.
            # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `desconto` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
            # `Porcentagem` = texto literal utilizado nesta instrução.
            campo_resultado="desconto", operador="Porcentagem",

            # Armazena ou associa em `campo_resultado_2` o valor ou resultado definido nesta linha.
            # `campo_resultado_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado 2.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `valor_final` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `expressao_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao 2.
            # `A - R` = texto literal utilizado nesta instrução.
            campo_resultado_2="valor_final", expressao_2="A - R",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora de Desconto` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `descontos` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora de Desconto", componentes, tabela="descontos")

# Define a rotina `projeto_07_comissao_vendas`, responsável por executar a lógica relacionada a projeto 07 comissao vendas.
# `def` = define uma nova função ou um novo método.
# `projeto_07_comissao_vendas` = função, método ou classe chamada para executar a operação relacionada a projeto 07 comissao vendas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_07_comissao_vendas():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora de Comissão de Vendas` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `560` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 35, "Calculadora de Comissão de Vendas", "titulo", largura=560, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `125` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Total de vendas` = texto literal utilizado nesta instrução.
        # `lbl_vendas` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 125, "Total de vendas", "lbl_vendas", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `vendas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Total de vendas` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("vendas", "Total de vendas", 430, 120, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Comissão (%)` = texto literal utilizado nesta instrução.
        # `lbl_percentual` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 180, "Comissão (%)", "lbl_percentual", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `percentual` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Comissão (%)` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `175` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("percentual", "Comissão (%)", 430, 175, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `235` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Comissão` = texto literal utilizado nesta instrução.
        # `lbl_comissao` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 235, "Comissão", "lbl_comissao", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `comissao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Comissão` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("comissao", "Comissão", 430, 230, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular comissão` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `vendas` = texto literal utilizado nesta instrução.
        # `percentual` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `comissao` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Porcentagem` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Calcular comissão", 430, 300, 300, acao="Calcular com campos", campos_acao=["vendas", "percentual"], campo_resultado="comissao", operador="Porcentagem"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora de Comissão de Vendas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `comissoes` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora de Comissão de Vendas", componentes, tabela="comissoes")

# Define a rotina `projeto_08_conversor_temperatura`, responsável por executar a lógica relacionada a projeto 08 conversor temperatura.
# `def` = define uma nova função ou um novo método.
# `projeto_08_conversor_temperatura` = função, método ou classe chamada para executar a operação relacionada a projeto 08 conversor temperatura.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_08_conversor_temperatura():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Conversor de Temperatura` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `470` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(285, 40, "Conversor de Temperatura", "titulo", largura=470, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Celsius` = texto literal utilizado nesta instrução.
        # `lbl_celsius` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 135, "Celsius", "lbl_celsius", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `celsius` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Celsius` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("celsius", "Celsius", 420, 130, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `195` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Fahrenheit` = texto literal utilizado nesta instrução.
        # `lbl_fahrenheit` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 195, "Fahrenheit", "lbl_fahrenheit", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `fahrenheit` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Fahrenheit` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("fahrenheit", "Fahrenheit", 420, 190, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_converter` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Converter` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `255` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `celsius` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `fahrenheit` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `A * 9 / 5 + 32` = texto literal utilizado nesta instrução.
        # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
        # `{resultado} °F` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_converter", "Converter", 420, 255, 300, acao="Calcular com campos", campos_acao=["celsius"], campo_resultado="fahrenheit", operador="Expressão personalizada", expressao="A * 9 / 5 + 32", formato_resultado="{resultado} °F"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Conversor de Temperatura` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `temperaturas` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Conversor de Temperatura", componentes, tabela="temperaturas")

# Define a rotina `projeto_09_km_milhas`, responsável por executar a lógica relacionada a projeto 09 km milhas.
# `def` = define uma nova função ou um novo método.
# `projeto_09_km_milhas` = função, método ou classe chamada para executar a operação relacionada a projeto 09 km milhas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_09_km_milhas():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `245` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Conversor de Quilômetros para Milhas` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `580` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(245, 40, "Conversor de Quilômetros para Milhas", "titulo", largura=580, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Quilômetros` = texto literal utilizado nesta instrução.
        # `lbl_km` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `150` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 135, "Quilômetros", "lbl_km", largura=150),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `quilometros` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Quilômetros` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("quilometros", "Quilômetros", 420, 130, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `195` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Milhas` = texto literal utilizado nesta instrução.
        # `lbl_milhas` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `150` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 195, "Milhas", "lbl_milhas", largura=150),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `milhas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Milhas` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("milhas", "Milhas", 420, 190, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_converter` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Converter` = texto literal utilizado nesta instrução.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `255` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `quilometros` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `milhas` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `A * 0.621371` = texto literal utilizado nesta instrução.
        # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
        # `{resultado} milhas` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_converter", "Converter", 420, 255, 300, acao="Calcular com campos", campos_acao=["quilometros"], campo_resultado="milhas", operador="Expressão personalizada", expressao="A * 0.621371", formato_resultado="{resultado} milhas"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Conversor de Quilômetros para Milhas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `conversoes` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Conversor de Quilômetros para Milhas", componentes, tabela="conversoes")

# Define a rotina `projeto_10_tabuada`, responsável por executar a lógica relacionada a projeto 10 tabuada.
# `def` = define uma nova função ou um novo método.
# `projeto_10_tabuada` = função, método ou classe chamada para executar a operação relacionada a projeto 10 tabuada.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_10_tabuada():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `315` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `30` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Gerador de Tabuada` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `400` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(315, 30, "Gerador de Tabuada", "titulo", largura=400, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Número` = texto literal utilizado nesta instrução.
        # `lbl_numero` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `120` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(200, 105, "Número", "lbl_numero", largura=120),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `numero` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Número` = texto literal utilizado nesta instrução.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("numero", "Número", 330, 100, 300, validacao="Decimal"),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_gerar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Gerar tabuada` = texto literal utilizado nesta instrução.
        # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Gerar lista por repetição` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `numero` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `resultado_tabuada` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Multiplicar` = texto literal utilizado nesta instrução.
        # `repeticao_inicio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a repeticao inicio.
        # `1` = texto literal utilizado nesta instrução.
        # `repeticao_fim` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a repeticao fim.
        # `10` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `{A} x {N} = {resultado}` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_gerar", "Gerar tabuada", 650, 100, 170, acao="Gerar lista por repetição", campos_acao=["numero"], campo_resultado="resultado_tabuada", operador="Multiplicar", repeticao_inicio="1", repeticao_fim="10", expressao="{A} x {N} = {resultado}"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `165` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `lbl_resultado` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `120` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(200, 165, "Resultado", "lbl_resultado", largura=120),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Listbox` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `330` = coordenada numérica utilizada no eixo X nesta instrução.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `160` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `490` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `330` = valor numérico utilizado para definir a altura nesta instrução.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `resultado_tabuada` = texto literal utilizado nesta instrução.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente(tipo="Listbox", x=330, y=160, largura=490, altura=330, nome="resultado_tabuada", texto=""),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Gerador de Tabuada` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `tabuada` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Gerador de Tabuada", componentes, tabela="tabuada")

# Define a rotina `projeto_11_par_impar`, responsável por executar a lógica relacionada a projeto 11 par impar.
# `def` = define uma nova função ou um novo método.
# `projeto_11_par_impar` = função, método ou classe chamada para executar a operação relacionada a projeto 11 par impar.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_11_par_impar():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `260` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Verificador de Número Par ou Ímpar` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `540` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(260, 40, "Verificador de Número Par ou Ímpar", "titulo", largura=540, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Número` = texto literal utilizado nesta instrução.
        # `lbl_numero` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `130` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 145, "Número", "lbl_numero", largura=130),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `numero` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Número` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `140` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("numero", "Número", 410, 140, 310, validacao="Inteiro"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `205` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `lbl_resultado` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `130` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 205, "Resultado", "lbl_resultado", largura=130),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `resultado` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("resultado", "Resultado", 410, 200, 310),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_verificar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Verificar` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `numero` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `resultado` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `'Par' if A % 2 == 0 else 'Ímpar'` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_verificar", "Verificar", 410, 270, 310, acao="Calcular com campos", campos_acao=["numero"], campo_resultado="resultado", operador="Expressão personalizada", expressao="'Par' if A % 2 == 0 else 'Ímpar'"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Verificador de Número Par ou Ímpar` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `verificacoes` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Verificador de Número Par ou Ímpar", componentes, tabela="verificacoes")

# Define a rotina `projeto_12_maioridade`, responsável por executar a lógica relacionada a projeto 12 maioridade.
# `def` = define uma nova função ou um novo método.
# `projeto_12_maioridade` = função, método ou classe chamada para executar a operação relacionada a projeto 12 maioridade.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_12_maioridade():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Verificador de Maioridade` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `450` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(300, 40, "Verificador de Maioridade", "titulo", largura=450, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Idade` = texto literal utilizado nesta instrução.
        # `lbl_idade` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `130` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 145, "Idade", "lbl_idade", largura=130),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `idade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Idade` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `140` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("idade", "Idade", 410, 140, 310, validacao="Inteiro"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `205` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `lbl_resultado` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `130` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 205, "Resultado", "lbl_resultado", largura=130),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `resultado` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("resultado", "Resultado", 410, 200, 310),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_verificar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Verificar` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Aplicar condição` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `idade` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `resultado` = texto literal utilizado nesta instrução.
        # `comparador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comparador.
        # `>=` = texto literal utilizado nesta instrução.
        # `valor_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a valor acao.
        # `18` = texto literal utilizado nesta instrução.
        # `resultado_verdadeiro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado verdadeiro.
        # `Maior de idade` = texto literal utilizado nesta instrução.
        # `resultado_falso` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado falso.
        # `Menor de idade` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_verificar", "Verificar", 410, 270, 310, acao="Aplicar condição", campos_acao=["idade"], campo_resultado="resultado", comparador=">=", valor_acao="18", resultado_verdadeiro="Maior de idade", resultado_falso="Menor de idade"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Verificador de Maioridade` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `maioridade` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Verificador de Maioridade", componentes, tabela="maioridade")

# Define a rotina `projeto_13_classificador_nota`, responsável por executar a lógica relacionada a projeto 13 classificador nota.
# `def` = define uma nova função ou um novo método.
# `projeto_13_classificador_nota` = função, método ou classe chamada para executar a operação relacionada a projeto 13 classificador nota.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_13_classificador_nota():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `315` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Classificador de Nota` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `400` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(315, 40, "Classificador de Nota", "titulo", largura=400, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `145` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Nota` = texto literal utilizado nesta instrução.
        # `lbl_nota` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `130` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 145, "Nota", "lbl_nota", largura=130),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nota` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Nota` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `140` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("nota", "Nota", 410, 140, 310, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `205` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Conceito` = texto literal utilizado nesta instrução.
        # `lbl_conceito` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `130` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(250, 205, "Conceito", "lbl_conceito", largura=130),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `conceito` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Conceito` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `200` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("conceito", "Conceito", 410, 200, 310),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_classificar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Classificar` = texto literal utilizado nesta instrução.
        # `410` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `nota` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `conceito` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `'A' if A >= 9 else 'B' if A >= 7 else 'C' if A >= 5 else 'D'` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_classificar", "Classificar", 410, 270, 310, acao="Calcular com campos", campos_acao=["nota"], campo_resultado="conceito", operador="Expressão personalizada", expressao="'A' if A >= 9 else 'B' if A >= 7 else 'C' if A >= 5 else 'D'"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Classificador de Nota` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `notas` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Classificador de Nota", componentes, tabela="notas")

# Define a rotina `projeto_14_salario_liquido`, responsável por executar a lógica relacionada a projeto 14 salario liquido.
# `def` = define uma nova função ou um novo método.
# `projeto_14_salario_liquido` = função, método ou classe chamada para executar a operação relacionada a projeto 14 salario liquido.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_14_salario_liquido():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora de Salário Líquido` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `470` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(285, 35, "Calculadora de Salário Líquido", "titulo", largura=470, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Salário bruto` = texto literal utilizado nesta instrução.
        # `lbl_bruto` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 120, "Salário bruto", "lbl_bruto", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `salario_bruto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Salário bruto` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("salario_bruto", "Salário bruto", 430, 115, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `175` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Descontos (%)` = texto literal utilizado nesta instrução.
        # `lbl_desc` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 175, "Descontos (%)", "lbl_desc", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `descontos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Descontos (%)` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("descontos", "Descontos (%)", 430, 170, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Benefícios` = texto literal utilizado nesta instrução.
        # `lbl_benef` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 230, "Benefícios", "lbl_benef", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `beneficios` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Benefícios` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `225` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("beneficios", "Benefícios", 430, 225, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Salário líquido` = texto literal utilizado nesta instrução.
        # `lbl_liquido` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 285, "Salário líquido", "lbl_liquido", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `salario_liquido` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Salário líquido` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("salario_liquido", "Salário líquido", 430, 280, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular salário` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `345` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `salario_bruto` = texto literal utilizado nesta instrução.
        # `descontos` = texto literal utilizado nesta instrução.
        # `beneficios` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `salario_liquido` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `A - (A * B / 100) + C` = texto literal utilizado nesta instrução.
        # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
        # `R$ {resultado}` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Calcular salário", 430, 345, 300, acao="Calcular com campos", campos_acao=["salario_bruto", "descontos", "beneficios"], campo_resultado="salario_liquido", operador="Expressão personalizada", expressao="A - (A * B / 100) + C", formato_resultado="R$ {resultado}"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora de Salário Líquido` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `salarios` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora de Salário Líquido", componentes, tabela="salarios")

# Define a rotina `projeto_15_horas_trabalhadas`, responsável por executar a lógica relacionada a projeto 15 horas trabalhadas.
# `def` = define uma nova função ou um novo método.
# `projeto_15_horas_trabalhadas` = função, método ou classe chamada para executar a operação relacionada a projeto 15 horas trabalhadas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_15_horas_trabalhadas():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora de Horas Trabalhadas` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `500` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(275, 35, "Calculadora de Horas Trabalhadas", "titulo", largura=500, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Horas normais` = texto literal utilizado nesta instrução.
        # `lbl_horas` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 115, "Horas normais", "lbl_horas", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `horas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Horas normais` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("horas", "Horas normais", 430, 110, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Valor por hora` = texto literal utilizado nesta instrução.
        # `lbl_valor_hora` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 170, "Valor por hora", "lbl_valor_hora", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `valor_hora` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Valor por hora` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `165` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("valor_hora", "Valor por hora", 430, 165, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `225` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Horas extras` = texto literal utilizado nesta instrução.
        # `lbl_extras` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 225, "Horas extras", "lbl_extras", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `horas_extras` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Horas extras` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("horas_extras", "Horas extras", 430, 220, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Total` = texto literal utilizado nesta instrução.
        # `lbl_total` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 280, "Total", "lbl_total", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `total` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Total` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("total", "Total", 430, 275, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular pagamento` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `340` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `horas` = texto literal utilizado nesta instrução.
        # `valor_hora` = texto literal utilizado nesta instrução.
        # `horas_extras` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `total` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `A * B + C * B * 1.5` = texto literal utilizado nesta instrução.
        # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
        # `R$ {resultado}` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Calcular pagamento", 430, 340, 300, acao="Calcular com campos", campos_acao=["horas", "valor_hora", "horas_extras"], campo_resultado="total", operador="Expressão personalizada", expressao="A * B + C * B * 1.5", formato_resultado="R$ {resultado}"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora de Horas Trabalhadas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `horas` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora de Horas Trabalhadas", componentes, tabela="horas")

# Define a rotina `projeto_16_consumo_combustivel`, responsável por executar a lógica relacionada a projeto 16 consumo combustivel.
# `def` = define uma nova função ou um novo método.
# `projeto_16_consumo_combustivel` = função, método ou classe chamada para executar a operação relacionada a projeto 16 consumo combustivel.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_16_consumo_combustivel():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `255` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora de Consumo de Combustível` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `550` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(255, 35, "Calculadora de Consumo de Combustível", "titulo", largura=550, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `125` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Distância (km)` = texto literal utilizado nesta instrução.
        # `lbl_dist` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 125, "Distância (km)", "lbl_dist", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `distancia` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Distância (km)` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("distancia", "Distância (km)", 430, 120, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Litros usados` = texto literal utilizado nesta instrução.
        # `lbl_litros` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 180, "Litros usados", "lbl_litros", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `litros` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Litros usados` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `175` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("litros", "Litros usados", 430, 175, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `235` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Consumo médio` = texto literal utilizado nesta instrução.
        # `lbl_consumo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 235, "Consumo médio", "lbl_consumo", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `consumo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Consumo médio` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("consumo", "Consumo médio", 430, 230, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular consumo` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `distancia` = texto literal utilizado nesta instrução.
        # `litros` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `consumo` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Dividir` = texto literal utilizado nesta instrução.
        # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
        # `{resultado} km/l` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Calcular consumo", 430, 300, 300, acao="Calcular com campos", campos_acao=["distancia", "litros"], campo_resultado="consumo", operador="Dividir", formato_resultado="{resultado} km/l"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora de Consumo de Combustível` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `consumo` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora de Consumo de Combustível", componentes, tabela="consumo")

# Define a rotina `projeto_17_troco`, responsável por executar a lógica relacionada a projeto 17 troco.
# `def` = define uma nova função ou um novo método.
# `projeto_17_troco` = função, método ou classe chamada para executar a operação relacionada a projeto 17 troco.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_17_troco():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `320` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `40` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Simulador de Troco` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `390` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(320, 40, "Simulador de Troco", "titulo", largura=390, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `135` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Total da compra` = texto literal utilizado nesta instrução.
        # `lbl_total` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 135, "Total da compra", "lbl_total", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `total_compra` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Total da compra` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("total_compra", "Total da compra", 430, 130, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Valor pago` = texto literal utilizado nesta instrução.
        # `lbl_pago` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 190, "Valor pago", "lbl_pago", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `valor_pago` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Valor pago` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `185` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("valor_pago", "Valor pago", 430, 185, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `230` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `245` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Troco` = texto literal utilizado nesta instrução.
        # `lbl_troco` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `170` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(230, 245, "Troco", "lbl_troco", largura=170),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `troco` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Troco` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `240` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("troco", "Troco", 430, 240, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular troco` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `total_compra` = texto literal utilizado nesta instrução.
        # `valor_pago` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `troco` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `B - A` = texto literal utilizado nesta instrução.
        # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
        # `R$ {resultado}` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Calcular troco", 430, 310, 300, acao="Calcular com campos", campos_acao=["total_compra", "valor_pago"], campo_resultado="troco", operador="Expressão personalizada", expressao="B - A", formato_resultado="R$ {resultado}"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Simulador de Troco` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `troco` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Simulador de Troco", componentes, tabela="troco")

# Define a rotina `projeto_18_parcelamento`, responsável por executar a lógica relacionada a projeto 18 parcelamento.
# `def` = define uma nova função ou um novo método.
# `projeto_18_parcelamento` = função, método ou classe chamada para executar a operação relacionada a projeto 18 parcelamento.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_18_parcelamento():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `295` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Simulador de Parcelamento` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `450` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(295, 35, "Simulador de Parcelamento", "titulo", largura=450, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Valor` = texto literal utilizado nesta instrução.
        # `lbl_valor` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 110, "Valor", "lbl_valor", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `valor` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Valor` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("valor", "Valor", 430, 105, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `165` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Juros (%)` = texto literal utilizado nesta instrução.
        # `lbl_juros` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 165, "Juros (%)", "lbl_juros", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `juros` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Juros (%)` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("juros", "Juros (%)", 430, 160, 300, validacao="Decimal"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Parcelas` = texto literal utilizado nesta instrução.
        # `lbl_parcelas` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 220, "Parcelas", "lbl_parcelas", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `parcelas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Parcelas` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Spinbox` = texto literal utilizado nesta instrução.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("parcelas", "Parcelas", 430, 215, 300, tipo="Spinbox", validacao="Inteiro"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Valor da parcela` = texto literal utilizado nesta instrução.
        # `lbl_parcela` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 275, "Valor da parcela", "lbl_parcela", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `valor_parcela` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Valor da parcela` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("valor_parcela", "Valor da parcela", 430, 270, 300),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Total com juros` = texto literal utilizado nesta instrução.
        # `lbl_total` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 330, "Total com juros", "lbl_total", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `total_juros` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Total com juros` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `325` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("total_juros", "Total com juros", 430, 325, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Simular` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `390` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `valor` = texto literal utilizado nesta instrução.
        # `juros` = texto literal utilizado nesta instrução.
        # `parcelas` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `valor_parcela` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `A * (1 + B / 100) / C` = texto literal utilizado nesta instrução.
        # `campo_resultado_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado 2.
        # `total_juros` = texto literal utilizado nesta instrução.
        # `expressao_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao 2.
        # `A * (1 + B / 100)` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Simular", 430, 390, 300, acao="Calcular com campos", campos_acao=["valor", "juros", "parcelas"], campo_resultado="valor_parcela", operador="Expressão personalizada", expressao="A * (1 + B / 100) / C", campo_resultado_2="total_juros", expressao_2="A * (1 + B / 100)"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Simulador de Parcelamento` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `parcelamento` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Simulador de Parcelamento", componentes, tabela="parcelamento")

# Define a rotina `projeto_19_orcamento`, responsável por executar a lógica relacionada a projeto 19 orcamento.
# `def` = define uma nova função ou um novo método.
# `projeto_19_orcamento` = função, método ou classe chamada para executar a operação relacionada a projeto 19 orcamento.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_19_orcamento():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `_label` = identificador relacionado a um rótulo de texto da interface.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `20` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `Gerador de Orçamento Simples` = texto literal utilizado nesta instrução.
    # `titulo` = texto literal utilizado nesta instrução.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `460` = valor numérico utilizado para definir a largura nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `42` = valor numérico utilizado para definir a altura nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    componentes = [_label(300, 20, "Gerador de Orçamento Simples", "titulo", largura=460, altura=42)]

    # Armazena ou associa em `campos_numericos` o valor ou resultado definido nesta linha.
    # `campos_numericos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos numericos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    campos_numericos = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `range` = função que cria uma sequência numérica utilizada normalmente em repetições.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `5` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for i in range(1, 5):

        # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `85` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `70` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        y = 85 + (i - 1) * 70

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `3` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `80` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_label(35, y + 3, f"Item {i}", f"lbl_item_{i}", largura=80))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `115` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `250` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_campo(f"item_{i}", f"Item {i}", 115, y, 250))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `390` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `3` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Qtd.` = texto literal utilizado nesta instrução.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `60` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_label(390, y + 3, "Qtd.", f"lbl_qtd_{i}", largura=60))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `450` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_campo(f"qtd_{i}", f"Quantidade {i}", 450, y, 120, validacao="Decimal"))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `590` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `3` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Preço` = texto literal utilizado nesta instrução.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `70` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_label(590, y + 3, "Preço", f"lbl_preco_{i}", largura=70))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `660` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_campo(f"preco_{i}", f"Preço {i}", 660, y, 190, validacao="Decimal"))

        # Executa `campos_numericos.extend` com os argumentos informados para realizar a operação correspondente.
        # `campos_numericos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos numericos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `extend` = função, método ou classe chamada para executar a operação relacionada a extend.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        campos_numericos.extend([f"qtd_{i}", f"preco_{i}"])

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `390` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `390` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Total` = texto literal utilizado nesta instrução.
        # `lbl_total` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `80` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(390, 390, "Total", "lbl_total", largura=80),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `total` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Total` = texto literal utilizado nesta instrução.
        # `480` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `385` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `370` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("total", "Total", 480, 385, 370),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        _botao(

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `btn_calcular` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "btn_calcular",

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `Calcular orçamento` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "Calcular orçamento",

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `480` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            480,

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `445` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            445,

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `370` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            370,

            # Define o argumento nomeado `acao` da chamada iniciada nas linhas anteriores.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Calcular com campos` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            acao="Calcular com campos",

            # Define o argumento nomeado `campos_acao` da chamada iniciada nas linhas anteriores.
            # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `campos_numericos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos numericos.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campos_acao=campos_numericos,

            # Define o argumento nomeado `campo_resultado` da chamada iniciada nas linhas anteriores.
            # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `total` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            campo_resultado="total",

            # Define o argumento nomeado `operador` da chamada iniciada nas linhas anteriores.
            # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Expressão personalizada` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            operador="Expressão personalizada",

            # Define o argumento nomeado `expressao` da chamada iniciada nas linhas anteriores.
            # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `A*B + C*D + E*F + G*H` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            expressao="A*B + C*D + E*F + G*H",

            # Define o argumento nomeado `formato_resultado` da chamada iniciada nas linhas anteriores.
            # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `R$ {resultado}` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            formato_resultado="R$ {resultado}",

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Gerador de Orçamento Simples` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `orcamentos` = texto literal utilizado nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `650` = valor numérico utilizado para definir a altura nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Gerador de Orçamento Simples", componentes, tabela="orcamentos", altura=650)

# Define a rotina `projeto_20_notas_academicas`, responsável por executar a lógica relacionada a projeto 20 notas academicas.
# `def` = define uma nova função ou um novo método.
# `projeto_20_notas_academicas` = função, método ou classe chamada para executar a operação relacionada a projeto 20 notas academicas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_20_notas_academicas():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `_label` = identificador relacionado a um rótulo de texto da interface.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `18` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `Controle de Notas Acadêmicas` = texto literal utilizado nesta instrução.
    # `titulo` = texto literal utilizado nesta instrução.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `480` = valor numérico utilizado para definir a largura nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `42` = valor numérico utilizado para definir a altura nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    componentes = [_label(280, 18, "Controle de Notas Acadêmicas", "titulo", largura=480, altura=42)]

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `72` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Aluno` = texto literal utilizado nesta instrução.
        # `lbl_aluno` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `100` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(35, 72, "Aluno", "lbl_aluno", largura=100),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `aluno` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Aluno` = texto literal utilizado nesta instrução.
        # `140` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `68` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `350` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("aluno", "Aluno", 140, 68, 350, obrigatorio=True),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `notas` o valor ou resultado definido nesta linha.
    # `notas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a notas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    notas = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `range` = função que cria uma sequência numérica utilizada normalmente em repetições.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `9` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for i in range(1, 9):

        # Armazena ou associa em `coluna` o valor ou resultado definido nesta linha.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `%` = operador utilizado para obter o resto de uma divisão ou aplicar formatação, conforme o contexto.
        # `4` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        coluna = (i - 1) % 4

        # Armazena ou associa em `linha` o valor ou resultado definido nesta linha.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `//` = operador utilizado para realizar divisão inteira.
        # `4` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        linha = (i - 1) // 4

        # Armazena ou associa em `x` o valor ou resultado definido nesta linha.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `35` = coordenada numérica utilizada no eixo X nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a coluna.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `235` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        x = 35 + coluna * 235

        # Armazena ou associa em `y` o valor ou resultado definido nesta linha.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `135` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `linha` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a linha.
        # `*` = operador utilizado para realizar multiplicação ou expansão de elementos, conforme o contexto.
        # `62` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        y = 135 + linha * 62

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `3` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `70` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_label(x, y + 3, f"Nota {i}", f"lbl_nota_{i}", largura=70))

        # Executa `componentes.append` com os argumentos informados para realizar a operação correspondente.
        # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `76` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `120` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Decimal` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        componentes.append(_campo(f"nota_{i}", f"Nota {i}", x + 76, y, 120, validacao="Decimal"))

        # Executa `notas.append` com os argumentos informados para realizar a operação correspondente.
        # `notas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a notas.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        notas.append(f"nota_{i}")

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Média` = texto literal utilizado nesta instrução.
        # `lbl_media` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `100` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(35, 275, "Média", "lbl_media", largura=100),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `media` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Média` = texto literal utilizado nesta instrução.
        # `140` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("media", "Média", 140, 270, 220),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_media` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular média das 8 notas` = texto literal utilizado nesta instrução.
        # `380` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `260` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `notas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a notas.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `media` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Média` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_media", "Calcular média das 8 notas", 380, 270, 260, acao="Calcular com campos", campos_acao=notas, campo_resultado="media", operador="Média"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Armazena ou associa em `todos` o valor ou resultado definido nesta linha.
    # `todos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a todos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `aluno` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
    # `notas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a notas.
    # `media` = texto literal utilizado nesta instrução.
    todos = ["aluno"] + notas + ["media"]

    # Executa `componentes.extend` com os argumentos informados para realizar a operação correspondente.
    componentes.extend([

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_cadastrar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Cadastrar` = texto literal utilizado nesta instrução.
        # `35` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `335` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `todos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a todos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_cadastrar", "Cadastrar", 35, 335, 170, acao="Cadastrar no SQLite", campos_acao=todos),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_atualizar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Atualizar` = texto literal utilizado nesta instrução.
        # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `335` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `150` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Atualizar registro` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `todos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a todos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_atualizar", "Atualizar", 215, 335, 150, acao="Atualizar registro", campos_acao=todos),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_excluir` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Excluir` = texto literal utilizado nesta instrução.
        # `375` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `335` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Excluir registro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_excluir", "Excluir", 375, 335, 130, acao="Excluir registro"),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_limpar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Limpar` = texto literal utilizado nesta instrução.
        # `515` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `335` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `130` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `todos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a todos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_limpar", "Limpar", 515, 335, 130, acao="Limpar campos selecionados", campos_acao=todos),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Treeview` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `35` = coordenada numérica utilizada no eixo X nesta instrução.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `400` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `910` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `265` = valor numérico utilizado para definir a altura nesta instrução.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `tabela_dados` = texto literal utilizado nesta instrução.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente(tipo="Treeview", x=35, y=400, largura=910, altura=265, nome="tabela_dados", texto=""),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    ])

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Controle de Notas Acadêmicas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `notas_academicas` = texto literal utilizado nesta instrução.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `720` = valor numérico utilizado para definir a altura nesta instrução.
    # `exibir_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir dados.
    # `True` = representa o valor lógico verdadeiro.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Controle de Notas Acadêmicas", componentes, tabela="notas_academicas", altura=720, exibir_dados=True)

# Define a rotina `projeto_21_lista_tarefas`, responsável por executar a lógica relacionada a projeto 21 lista tarefas.
# `def` = define uma nova função ou um novo método.
# `projeto_21_lista_tarefas` = função, método ou classe chamada para executar a operação relacionada a projeto 21 lista tarefas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_21_lista_tarefas():

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _crud_simples(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Lista de Tarefas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Lista de Tarefas",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `tarefas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "tarefas",

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

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
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Baixa` = texto literal utilizado nesta instrução.
            # `Média` = texto literal utilizado nesta instrução.
            # `Alta` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "prioridade", "rotulo": "Prioridade", "tipo": "Combobox", "opcoes": ["Baixa", "Média", "Alta"]},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `status` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Status` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Pendente` = texto literal utilizado nesta instrução.
            # `Em andamento` = texto literal utilizado nesta instrução.
            # `Concluída` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "status", "rotulo": "Status", "tipo": "Combobox", "opcoes": ["Pendente", "Em andamento", "Concluída"]},

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

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Claro` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema="Claro",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_22_agenda_compromissos`, responsável por executar a lógica relacionada a projeto 22 agenda compromissos.
# `def` = define uma nova função ou um novo método.
# `projeto_22_agenda_compromissos` = função, método ou classe chamada para executar a operação relacionada a projeto 22 agenda compromissos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_22_agenda_compromissos():

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _crud_simples(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Agenda de Compromissos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Agenda de Compromissos",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `compromissos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "compromissos",

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `compromisso` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Compromisso` = texto literal utilizado nesta instrução.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `True` = representa o valor lógico verdadeiro.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "compromisso", "rotulo": "Compromisso", "obrigatorio": True},

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
            # `observacoes` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Observações` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "observacoes", "rotulo": "Observações"},

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Azul corporativo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema="Azul corporativo",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_23_emprestimos_livros`, responsável por executar a lógica relacionada a projeto 23 emprestimos livros.
# `def` = define uma nova função ou um novo método.
# `projeto_23_emprestimos_livros` = função, método ou classe chamada para executar a operação relacionada a projeto 23 emprestimos livros.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_23_emprestimos_livros():

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _crud_simples(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Controle de Empréstimos de Livros` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Controle de Empréstimos de Livros",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `emprestimos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "emprestimos",

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

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
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Emprestado` = texto literal utilizado nesta instrução.
            # `Devolvido` = texto literal utilizado nesta instrução.
            # `Atrasado` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "status", "rotulo": "Status", "tipo": "Combobox", "opcoes": ["Emprestado", "Devolvido", "Atrasado"]},

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Verde` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema="Verde",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_24_estoque_minimo`, responsável por executar a lógica relacionada a projeto 24 estoque minimo.
# `def` = define uma nova função ou um novo método.
# `projeto_24_estoque_minimo` = função, método ou classe chamada para executar a operação relacionada a projeto 24 estoque minimo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_24_estoque_minimo():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `295` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `25` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Alerta de Estoque Mínimo` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `450` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(295, 25, "Alerta de Estoque Mínimo", "titulo", largura=450, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Produto` = texto literal utilizado nesta instrução.
        # `lbl_produto` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 110, "Produto", "lbl_produto", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `produto` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Produto` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("produto", "Produto", 430, 105, 300),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `165` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Quantidade atual` = texto literal utilizado nesta instrução.
        # `lbl_qtd` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 165, "Quantidade atual", "lbl_qtd", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `quantidade` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Quantidade atual` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("quantidade", "Quantidade atual", 430, 160, 300, validacao="Inteiro"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Estoque mínimo` = texto literal utilizado nesta instrução.
        # `lbl_minimo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 220, "Estoque mínimo", "lbl_minimo", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `estoque_minimo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Estoque mínimo` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Inteiro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("estoque_minimo", "Estoque mínimo", 430, 215, 300, validacao="Inteiro"),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Situação` = texto literal utilizado nesta instrução.
        # `lbl_situacao` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `180` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(220, 275, "Situação", "lbl_situacao", largura=180),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `situacao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Situação` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("situacao", "Situação", 430, 270, 300),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_verificar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Verificar estoque` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `330` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `quantidade` = texto literal utilizado nesta instrução.
        # `estoque_minimo` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `situacao` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `'REPOR ESTOQUE' if A <= B else 'Estoque suficiente'` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_verificar", "Verificar estoque", 430, 330, 300, acao="Calcular com campos", campos_acao=["quantidade", "estoque_minimo"], campo_resultado="situacao", operador="Expressão personalizada", expressao="'REPOR ESTOQUE' if A <= B else 'Estoque suficiente'"),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_cadastrar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Cadastrar situação` = texto literal utilizado nesta instrução.
        # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `385` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Cadastrar no SQLite` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `produto` = texto literal utilizado nesta instrução.
        # `quantidade` = texto literal utilizado nesta instrução.
        # `estoque_minimo` = texto literal utilizado nesta instrução.
        # `situacao` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_cadastrar", "Cadastrar situação", 430, 385, 300, acao="Cadastrar no SQLite", campos_acao=["produto", "quantidade", "estoque_minimo", "situacao"]),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Alerta de Estoque Mínimo` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `estoque_minimo` = texto literal utilizado nesta instrução.
    # `exibir_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir dados.
    # `True` = representa o valor lógico verdadeiro.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Alerta de Estoque Mínimo", componentes, tabela="estoque_minimo", exibir_dados=True)

# Define a rotina `projeto_25_satisfacao`, responsável por executar a lógica relacionada a projeto 25 satisfacao.
# `def` = define uma nova função ou um novo método.
# `projeto_25_satisfacao` = função, método ou classe chamada para executar a operação relacionada a projeto 25 satisfacao.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_25_satisfacao():

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _crud_simples(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Pesquisa de Satisfação` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Pesquisa de Satisfação",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `satisfacao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "satisfacao",

        # Executa a instrução desta linha como parte da lógica atual do programa.
        [

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Nome` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "nome", "rotulo": "Nome"},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `nota` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Nota` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Scale` = texto literal utilizado nesta instrução.
            # `validacao` = texto literal utilizado nesta instrução.
            # `Decimal` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "nota", "rotulo": "Nota", "tipo": "Scale", "validacao": "Decimal"},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `atendimento` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Atendimento` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Ruim` = texto literal utilizado nesta instrução.
            # `Regular` = texto literal utilizado nesta instrução.
            # `Bom` = texto literal utilizado nesta instrução.
            # `Excelente` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "atendimento", "rotulo": "Atendimento", "tipo": "Combobox", "opcoes": ["Ruim", "Regular", "Bom", "Excelente"]},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `recomendaria` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Recomendaria?` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Sim` = texto literal utilizado nesta instrução.
            # `Não` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "recomendaria", "rotulo": "Recomendaria?", "tipo": "Combobox", "opcoes": ["Sim", "Não"]},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `comentario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Comentário` = texto literal utilizado nesta instrução.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "comentario", "rotulo": "Comentário"},

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Claro` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema="Claro",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_26_questionario`, responsável por executar a lógica relacionada a projeto 26 questionario.
# `def` = define uma nova função ou um novo método.
# `projeto_26_questionario` = função, método ou classe chamada para executar a operação relacionada a projeto 26 questionario.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_26_questionario():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `22` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Questionário de Múltipla Escolha` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `500` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(285, 22, "Questionário de Múltipla Escolha", "titulo", largura=500, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `90` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `1. Capital da França` = texto literal utilizado nesta instrução.
        # `lbl_q1` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `260` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(80, 90, "1. Capital da França", "lbl_q1", largura=260),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `resposta_1` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Resposta 1` = texto literal utilizado nesta instrução.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `85` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Paris` = texto literal utilizado nesta instrução.
        # `Londres` = texto literal utilizado nesta instrução.
        # `Roma` = texto literal utilizado nesta instrução.
        # `Madrid` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("resposta_1", "Resposta 1", 360, 85, 420, tipo="Combobox", opcoes=["Paris", "Londres", "Roma", "Madrid"]),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `155` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `2. 2 + 2` = texto literal utilizado nesta instrução.
        # `lbl_q2` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `260` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(80, 155, "2. 2 + 2", "lbl_q2", largura=260),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `resposta_2` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Resposta 2` = texto literal utilizado nesta instrução.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `150` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `3` = texto literal utilizado nesta instrução.
        # `4` = texto literal utilizado nesta instrução.
        # `5` = texto literal utilizado nesta instrução.
        # `6` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("resposta_2", "Resposta 2", 360, 150, 420, tipo="Combobox", opcoes=["3", "4", "5", "6"]),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `220` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `3. Linguagem deste projeto` = texto literal utilizado nesta instrução.
        # `lbl_q3` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `260` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(80, 220, "3. Linguagem deste projeto", "lbl_q3", largura=260),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `resposta_3` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Resposta 3` = texto literal utilizado nesta instrução.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Combobox` = texto literal utilizado nesta instrução.
        # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Python` = texto literal utilizado nesta instrução.
        # `Java` = texto literal utilizado nesta instrução.
        # `C` = texto literal utilizado nesta instrução.
        # `PHP` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("resposta_3", "Resposta 3", 360, 215, 420, tipo="Combobox", opcoes=["Python", "Java", "C", "PHP"]),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `285` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Acertos` = texto literal utilizado nesta instrução.
        # `lbl_pontos` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `260` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(80, 285, "Acertos", "lbl_pontos", largura=260),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `acertos` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Acertos` = texto literal utilizado nesta instrução.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("acertos", "Acertos", 360, 280, 420),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_corrigir` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Corrigir questionário` = texto literal utilizado nesta instrução.
        # `360` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `345` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `420` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular com campos` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `resposta_1` = texto literal utilizado nesta instrução.
        # `resposta_2` = texto literal utilizado nesta instrução.
        # `resposta_3` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `acertos` = texto literal utilizado nesta instrução.
        # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
        # `Expressão personalizada` = texto literal utilizado nesta instrução.
        # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
        # `(1 if A == 'Paris' else 0) + (1 if B == 4 else 0) + (1 if C == 'Python' else 0)` = texto literal utilizado nesta instrução.
        # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
        # `{resultado} de 3` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_corrigir", "Corrigir questionário", 360, 345, 420, acao="Calcular com campos", campos_acao=["resposta_1", "resposta_2", "resposta_3"], campo_resultado="acertos", operador="Expressão personalizada", expressao="(1 if A == 'Paris' else 0) + (1 if B == 4 else 0) + (1 if C == 'Python' else 0)", formato_resultado="{resultado} de 3"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Questionário de Múltipla Escolha` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `questionario` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Questionário de Múltipla Escolha", componentes, tabela="questionario")

# Define a rotina `projeto_27_inscricao_evento`, responsável por executar a lógica relacionada a projeto 27 inscricao evento.
# `def` = define uma nova função ou um novo método.
# `projeto_27_inscricao_evento` = função, método ou classe chamada para executar a operação relacionada a projeto 27 inscricao evento.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_27_inscricao_evento():

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    return _crud_simples(

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `Formulário de Inscrição em Evento` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "Formulário de Inscrição em Evento",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `inscricoes_evento` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        "inscricoes_evento",

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
            # `email` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `E-mail` = texto literal utilizado nesta instrução.
            # `validacao` = texto literal utilizado nesta instrução.
            # `obrigatorio` = texto literal utilizado nesta instrução.
            # `True` = representa o valor lógico verdadeiro.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "email", "rotulo": "E-mail", "validacao": "E-mail", "obrigatorio": True},

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
            # `evento` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Evento` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Workshop` = texto literal utilizado nesta instrução.
            # `Palestra` = texto literal utilizado nesta instrução.
            # `Seminário` = texto literal utilizado nesta instrução.
            # `Curso` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "evento", "rotulo": "Evento", "tipo": "Combobox", "opcoes": ["Workshop", "Palestra", "Seminário", "Curso"]},

            # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `tipo_ingresso` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `rotulo` = texto literal utilizado nesta instrução.
            # `Ingresso` = texto literal utilizado nesta instrução.
            # `tipo` = texto literal utilizado nesta instrução.
            # `Combobox` = texto literal utilizado nesta instrução.
            # `opcoes` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Normal` = texto literal utilizado nesta instrução.
            # `VIP` = texto literal utilizado nesta instrução.
            # `Estudante` = texto literal utilizado nesta instrução.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            {"nome": "tipo_ingresso", "rotulo": "Ingresso", "tipo": "Combobox", "opcoes": ["Normal", "VIP", "Estudante"]},

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
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

        # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Azul corporativo` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tema="Azul corporativo",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    )

# Define a rotina `projeto_28_login`, responsável por executar a lógica relacionada a projeto 28 login.
# `def` = define uma nova função ou um novo método.
# `projeto_28_login` = função, método ou classe chamada para executar a operação relacionada a projeto 28 login.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_28_login():

    # Armazena ou associa em `login` o valor ou resultado definido nesta linha.
    login = Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Login` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Login",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Sistema de Login Simples` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Sistema de Login Simples",

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

        # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
        componentes=[

            # Executa `_label` com os argumentos informados para realizar a operação correspondente.
            # `_label` = identificador relacionado a um rótulo de texto da interface.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `65` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `Sistema de Login Simples` = texto literal utilizado nesta instrução.
            # `titulo` = texto literal utilizado nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `420` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `42` = valor numérico utilizado para definir a altura nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _label(300, 65, "Sistema de Login Simples", "titulo", largura=420, altura=42),

            # Executa `_label` com os argumentos informados para realizar a operação correspondente.
            # `_label` = identificador relacionado a um rótulo de texto da interface.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `155` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `Usuário` = texto literal utilizado nesta instrução.
            # `lbl_usuario` = texto literal utilizado nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `130` = valor numérico utilizado para definir a largura nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _label(300, 155, "Usuário", "lbl_usuario", largura=130),

            # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
            # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `usuario` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Usuário` = texto literal utilizado nesta instrução.
            # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `150` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `True` = representa o valor lógico verdadeiro.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _campo("usuario", "Usuário", 430, 150, 300, obrigatorio=True),

            # Executa `_label` com os argumentos informados para realizar a operação correspondente.
            # `_label` = identificador relacionado a um rótulo de texto da interface.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `215` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `Senha` = texto literal utilizado nesta instrução.
            # `lbl_senha` = texto literal utilizado nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `130` = valor numérico utilizado para definir a largura nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _label(300, 215, "Senha", "lbl_senha", largura=130),

            # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
            # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `senha` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Senha` = texto literal utilizado nesta instrução.
            # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `210` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
            # `True` = representa o valor lógico verdadeiro.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _campo("senha", "Senha", 430, 210, 300, mascara="Senha", obrigatorio=True),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            # `_botao` = identificador relacionado a um botão da interface, associado a botao.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `btn_entrar` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Entrar` = texto literal utilizado nesta instrução.
            # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `280` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Entrar / validar login` = texto literal utilizado nesta instrução.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Área Principal` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _botao("btn_entrar", "Entrar", 430, 280, 300, acao="Entrar / validar login", tela_destino="Área Principal"),

            # Executa `_label` com os argumentos informados para realizar a operação correspondente.
            # `_label` = identificador relacionado a um rótulo de texto da interface.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `430` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `340` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `Primeiro acesso: admin / admin` = texto literal utilizado nesta instrução.
            # `credenciais` = texto literal utilizado nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `320` = valor numérico utilizado para definir a largura nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _label(430, 340, "Primeiro acesso: admin / admin", "credenciais", largura=320),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

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

    # Armazena ou associa em `area` o valor ou resultado definido nesta linha.
    area = Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Área Principal` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Área Principal",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Área Principal` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Área Principal",

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
        # `area_principal` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="area_principal",

        # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
        componentes=[

            # Executa `_label` com os argumentos informados para realizar a operação correspondente.
            # `_label` = identificador relacionado a um rótulo de texto da interface.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `80` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `Login realizado com sucesso` = texto literal utilizado nesta instrução.
            # `titulo` = texto literal utilizado nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `500` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `46` = valor numérico utilizado para definir a altura nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _label(270, 80, "Login realizado com sucesso", "titulo", largura=500, altura=46),

            # Executa `_label` com os argumentos informados para realizar a operação correspondente.
            # `_label` = identificador relacionado a um rótulo de texto da interface.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `150` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `Esta é a área protegida do sistema.` = texto literal utilizado nesta instrução.
            # `texto` = texto literal utilizado nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `500` = valor numérico utilizado para definir a largura nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _label(270, 150, "Esta é a área protegida do sistema.", "texto", largura=500),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            # `_botao` = identificador relacionado a um botão da interface, associado a botao.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `btn_sair` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Sair da conta` = texto literal utilizado nesta instrução.
            # `350` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `240` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _botao("btn_sair", "Sair da conta", 350, 240, 300, acao="Sair da conta"),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

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

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `Sistema de Login Simples` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `Azul corporativo` = texto literal utilizado nesta instrução.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `area` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a area.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `tela_ativa_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela ativa id.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = Projeto(nome="Sistema de Login Simples", tema="Azul corporativo", telas=[login, area], tela_ativa_id=login.id)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `normalizar_projeto` = função, método ou classe chamada para executar a operação relacionada a normalizar projeto.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `adicionar_botao_cadastro` = identificador relacionado a um botão da interface, associado a adicionar botao cadastro.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return normalizar_projeto(projeto, adicionar_botao_cadastro=False)

# Define a rotina `projeto_29_varias_telas`, responsável por executar a lógica relacionada a projeto 29 varias telas.
# `def` = define uma nova função ou um novo método.
# `projeto_29_varias_telas` = função, método ou classe chamada para executar a operação relacionada a projeto 29 varias telas.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_29_varias_telas():

    # Armazena ou associa em `menu` o valor ou resultado definido nesta linha.
    menu = Tela(

        # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Menu Principal` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        nome="Menu Principal",

        # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Menu com Várias Telas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        titulo="Menu com Várias Telas",

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
        # `menu` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        tabela="menu",

        # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
        componentes=[

            # Executa `_label` com os argumentos informados para realizar a operação correspondente.
            # `_label` = identificador relacionado a um rótulo de texto da interface.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `55` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `Menu com Várias Telas` = texto literal utilizado nesta instrução.
            # `titulo` = texto literal utilizado nesta instrução.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `440` = valor numérico utilizado para definir a largura nesta instrução.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `42` = valor numérico utilizado para definir a altura nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _label(300, 55, "Menu com Várias Telas", "titulo", largura=440, altura=42),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            # `_botao` = identificador relacionado a um botão da interface, associado a botao.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `btn_tela_1` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Abrir Cadastro` = texto literal utilizado nesta instrução.
            # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Cadastro` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _botao("btn_tela_1", "Abrir Cadastro", 180, 180, 190, acao="Abrir outra tela", tela_destino="Cadastro"),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            # `_botao` = identificador relacionado a um botão da interface, associado a botao.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `btn_tela_2` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Abrir Relatórios` = texto literal utilizado nesta instrução.
            # `405` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Relatórios` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _botao("btn_tela_2", "Abrir Relatórios", 405, 180, 190, acao="Abrir outra tela", tela_destino="Relatórios"),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            # `_botao` = identificador relacionado a um botão da interface, associado a botao.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `btn_tela_3` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Abrir Configurações` = texto literal utilizado nesta instrução.
            # `630` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `180` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `Abrir outra tela` = texto literal utilizado nesta instrução.
            # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
            # `Configurações` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _botao("btn_tela_3", "Abrir Configurações", 630, 180, 190, acao="Abrir outra tela", tela_destino="Configurações"),

            # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
            # `_botao` = identificador relacionado a um botão da interface, associado a botao.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `btn_fechar` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Fechar sistema` = texto literal utilizado nesta instrução.
            # `405` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `270` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            _botao("btn_fechar", "Fechar sistema", 405, 270, 190, acao="Fechar sistema"),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        ],

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

    # Armazena ou associa em `telas` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    telas = [menu]

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    for nome, texto in [

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Cadastro` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Tela de Cadastro` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        ("Cadastro", "Tela de Cadastro"),

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Relatórios` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Tela de Relatórios` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        ("Relatórios", "Tela de Relatórios"),

        # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Configurações` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Tela de Configurações` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        ("Configurações", "Tela de Configurações"),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    ]:

        # Executa `telas.append` com os argumentos informados para realizar a operação correspondente.
        telas.append(

            # Executa `Tela` com os argumentos informados para realizar a operação correspondente.
            Tela(

                # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                nome=nome,

                # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
                # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                titulo=texto,

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
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `lower` = função, método ou classe chamada para executar a operação relacionada a lower.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `replace` = função, método ou classe chamada para executar a operação relacionada a replace.
                # `ç` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `c` = texto literal utilizado nesta instrução.
                # `õ` = texto literal utilizado nesta instrução.
                # `o` = texto literal utilizado nesta instrução.
                # ` ` = texto literal utilizado nesta instrução.
                # `_` = texto literal utilizado nesta instrução.
                tabela=nome.lower().replace("ç", "c").replace("õ", "o").replace(" ", "_"),

                # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
                componentes=[

                    # Executa `_label` com os argumentos informados para realizar a operação correspondente.
                    # `_label` = identificador relacionado a um rótulo de texto da interface.
                    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    # `100` = valor numérico cem utilizado como total, limite ou base percentual, conforme o cálculo desta linha.
                    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
                    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `430` = valor numérico utilizado para definir a largura nesta instrução.
                    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
                    # `42` = valor numérico utilizado para definir a altura nesta instrução.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    _label(300, 100, texto, f"titulo_{nome}", largura=430, altura=42),

                    # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
                    # `_botao` = identificador relacionado a um botão da interface, associado a botao.
                    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                    # `Voltar` = texto literal utilizado nesta instrução.
                    # `405` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                    # `210` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                    # `190` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
                    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                    # `Voltar para tela anterior` = texto literal utilizado nesta instrução.
                    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                    _botao(f"btn_voltar_{nome}", "Voltar", 405, 210, 190, acao="Voltar para tela anterior"),

                # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                ],

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

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `Menu com Várias Telas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `Claro` = texto literal utilizado nesta instrução.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `tela_ativa_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela ativa id.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = Projeto(nome="Menu com Várias Telas", tema="Claro", telas=telas, tela_ativa_id=menu.id)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `normalizar_projeto` = função, método ou classe chamada para executar a operação relacionada a normalizar projeto.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `adicionar_botao_cadastro` = identificador relacionado a um botão da interface, associado a adicionar botao cadastro.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return normalizar_projeto(projeto, adicionar_botao_cadastro=False)

# Define a rotina `projeto_30_calculadora_historico`, responsável por executar a lógica relacionada a projeto 30 calculadora historico.
# `def` = define uma nova função ou um novo método.
# `projeto_30_calculadora_historico` = função, método ou classe chamada para executar a operação relacionada a projeto 30 calculadora historico.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def projeto_30_calculadora_historico():

    # Armazena ou associa em `componentes` o valor ou resultado definido nesta linha.
    componentes = [

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `275` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `28` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Calculadora com Histórico` = texto literal utilizado nesta instrução.
        # `titulo` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `480` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `42` = valor numérico utilizado para definir a altura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(275, 28, "Calculadora com Histórico", "titulo", largura=480, altura=42),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `110` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Expressão` = texto literal utilizado nesta instrução.
        # `lbl_expressao` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(160, 110, "Expressão", "lbl_expressao", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `expressao` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Expressão` = texto literal utilizado nesta instrução.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `105` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("expressao", "Expressão", 310, 105, 500),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `170` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `lbl_resultado` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(160, 170, "Resultado", "lbl_resultado", largura=140),

        # Executa `_campo` com os argumentos informados para realizar a operação correspondente.
        # `_campo` = função, método ou classe chamada para executar a operação relacionada a campo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `resultado` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Resultado` = texto literal utilizado nesta instrução.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `165` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `500` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _campo("resultado", "Resultado", 310, 165, 500),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_calcular` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Calcular` = texto literal utilizado nesta instrução.
        # `310` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `225` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `240` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Calcular expressão de um campo` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `expressao` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
        # `resultado` = texto literal utilizado nesta instrução.
        # `alvo_auxiliar` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo auxiliar.
        # `historico` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_calcular", "Calcular", 310, 225, 240, acao="Calcular expressão de um campo", campos_acao=["expressao"], campo_resultado="resultado", alvo_auxiliar="historico"),

        # Executa `_botao` com os argumentos informados para realizar a operação correspondente.
        # `_botao` = identificador relacionado a um botão da interface, associado a botao.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `btn_limpar` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Limpar` = texto literal utilizado nesta instrução.
        # `570` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `225` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `240` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Limpar campos selecionados` = texto literal utilizado nesta instrução.
        # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `expressao` = texto literal utilizado nesta instrução.
        # `resultado` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _botao("btn_limpar", "Limpar", 570, 225, 240, acao="Limpar campos selecionados", campos_acao=["expressao", "resultado"]),

        # Executa `_label` com os argumentos informados para realizar a operação correspondente.
        # `_label` = identificador relacionado a um rótulo de texto da interface.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `160` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `300` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `Histórico` = texto literal utilizado nesta instrução.
        # `lbl_historico` = texto literal utilizado nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `140` = valor numérico utilizado para definir a largura nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        _label(160, 300, "Histórico", "lbl_historico", largura=140),

        # Executa `Componente` com os argumentos informados para realizar a operação correspondente.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Listbox` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `310` = coordenada numérica utilizada no eixo X nesta instrução.
        # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
        # `295` = coordenada numérica utilizada no eixo Y nesta instrução.
        # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
        # `500` = valor numérico utilizado para definir a largura nesta instrução.
        # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
        # `230` = valor numérico utilizado para definir a altura nesta instrução.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `historico` = texto literal utilizado nesta instrução.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        Componente(tipo="Listbox", x=310, y=295, largura=500, altura=230, nome="historico", texto=""),

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    ]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_uma_tela` = função, método ou classe chamada para executar a operação relacionada a projeto uma tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `Calculadora com Histórico` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `calculadora_historico` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_uma_tela("Calculadora com Histórico", componentes, tabela="calculadora_historico")

# Armazena ou associa em `PROJETOS_30` o valor ou resultado definido nesta linha.
PROJETOS_30 = [

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Cadastro de Alunos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_01_cadastro_alunos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 01 cadastro alunos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Cadastro de Alunos", "fabrica": projeto_01_cadastro_alunos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Cadastro de Produtos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_02_cadastro_produtos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 02 cadastro produtos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Cadastro de Produtos", "fabrica": projeto_02_cadastro_produtos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora Básica com Teclado` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_03_calculadora_teclado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 03 calculadora teclado.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora Básica com Teclado", "fabrica": projeto_03_calculadora_teclado},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora de Média Escolar` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_04_media_escolar` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 04 media escolar.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora de Média Escolar", "fabrica": projeto_04_media_escolar},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora de IMC` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_05_imc` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 05 imc.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora de IMC", "fabrica": projeto_05_imc},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora de Desconto` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_06_desconto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 06 desconto.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora de Desconto", "fabrica": projeto_06_desconto},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora de Comissão de Vendas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_07_comissao_vendas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 07 comissao vendas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora de Comissão de Vendas", "fabrica": projeto_07_comissao_vendas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Conversor de Temperatura` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_08_conversor_temperatura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 08 conversor temperatura.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Conversor de Temperatura", "fabrica": projeto_08_conversor_temperatura},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Conversor de Quilômetros para Milhas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_09_km_milhas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 09 km milhas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Conversor de Quilômetros para Milhas", "fabrica": projeto_09_km_milhas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Gerador de Tabuada` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_10_tabuada` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 10 tabuada.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Gerador de Tabuada", "fabrica": projeto_10_tabuada},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Verificador de Número Par ou Ímpar` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_11_par_impar` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 11 par impar.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Verificador de Número Par ou Ímpar", "fabrica": projeto_11_par_impar},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Verificador de Maioridade` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_12_maioridade` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 12 maioridade.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Verificador de Maioridade", "fabrica": projeto_12_maioridade},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Classificador de Nota` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_13_classificador_nota` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 13 classificador nota.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Classificador de Nota", "fabrica": projeto_13_classificador_nota},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora de Salário Líquido` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_14_salario_liquido` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 14 salario liquido.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora de Salário Líquido", "fabrica": projeto_14_salario_liquido},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora de Horas Trabalhadas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_15_horas_trabalhadas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 15 horas trabalhadas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora de Horas Trabalhadas", "fabrica": projeto_15_horas_trabalhadas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora de Consumo de Combustível` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_16_consumo_combustivel` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 16 consumo combustivel.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora de Consumo de Combustível", "fabrica": projeto_16_consumo_combustivel},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Simulador de Troco` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_17_troco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 17 troco.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Simulador de Troco", "fabrica": projeto_17_troco},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Simulador de Parcelamento` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_18_parcelamento` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 18 parcelamento.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Simulador de Parcelamento", "fabrica": projeto_18_parcelamento},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Gerador de Orçamento Simples` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_19_orcamento` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 19 orcamento.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Gerador de Orçamento Simples", "fabrica": projeto_19_orcamento},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Controle de Notas Acadêmicas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_20_notas_academicas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 20 notas academicas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Controle de Notas Acadêmicas", "fabrica": projeto_20_notas_academicas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Lista de Tarefas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_21_lista_tarefas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 21 lista tarefas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Lista de Tarefas", "fabrica": projeto_21_lista_tarefas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Agenda de Compromissos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_22_agenda_compromissos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 22 agenda compromissos.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Agenda de Compromissos", "fabrica": projeto_22_agenda_compromissos},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Controle de Empréstimos de Livros` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_23_emprestimos_livros` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 23 emprestimos livros.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Controle de Empréstimos de Livros", "fabrica": projeto_23_emprestimos_livros},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Alerta de Estoque Mínimo` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_24_estoque_minimo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 24 estoque minimo.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Alerta de Estoque Mínimo", "fabrica": projeto_24_estoque_minimo},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Pesquisa de Satisfação` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_25_satisfacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 25 satisfacao.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Pesquisa de Satisfação", "fabrica": projeto_25_satisfacao},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Questionário de Múltipla Escolha` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_26_questionario` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 26 questionario.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Questionário de Múltipla Escolha", "fabrica": projeto_26_questionario},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Formulário de Inscrição em Evento` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_27_inscricao_evento` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 27 inscricao evento.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Formulário de Inscrição em Evento", "fabrica": projeto_27_inscricao_evento},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Sistema de Login Simples` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_28_login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 28 login.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Sistema de Login Simples", "fabrica": projeto_28_login},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Menu com Várias Telas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_29_varias_telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 29 varias telas.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Menu com Várias Telas", "fabrica": projeto_29_varias_telas},

    # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Calculadora com Histórico` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `projeto_30_calculadora_historico` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto 30 calculadora historico.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    {"nome": "Calculadora com Histórico", "fabrica": projeto_30_calculadora_historico},

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `]` = fecha a lista, índice, acesso a elemento ou compreensão.
]

# Acrescenta os exemplos adicionais ao mesmo menu de projetos.
from .projetos_extras import PROJETOS_EXTRAS

PROJETOS_30.extend(PROJETOS_EXTRAS)


# Define a rotina `obter_projeto_30`, responsável por executar a lógica relacionada a obter projeto 30.
# `def` = define uma nova função ou um novo método.
# `obter_projeto_30` = função, método ou classe chamada para executar a operação relacionada a obter projeto 30.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
def obter_projeto_30(indice: int) -> Projeto:

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
    # `<` = operador de comparação utilizado para verificar se o valor da esquerda é menor.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `>=` = operador de comparação utilizado para verificar se o valor da esquerda é maior ou igual.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `PROJETOS_30` = constante utilizada para armazenar o valor relacionado a projetos 30.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if indice < 0 or indice >= len(PROJETOS_30):

        # Gera explicitamente a exceção indicada nesta linha.
        # `raise` = gera explicitamente uma exceção.
        # `IndexError` = função, método ou classe chamada para executar a operação relacionada a IndexError.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Projeto fora da lista de 30 projetos.` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        raise IndexError("Projeto fora da lista de projetos de exemplo.")

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `deepcopy` = função, método ou classe chamada para executar a operação relacionada a deepcopy.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `PROJETOS_30` = constante utilizada para armazenar o valor relacionado a projetos 30.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `indice` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a indice.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `fabrica` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = deepcopy(PROJETOS_30[indice]["fabrica"]())

    # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `normalizar_projeto` = função, método ou classe chamada para executar a operação relacionada a normalizar projeto.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `adicionar_botao_cadastro` = identificador relacionado a um botão da interface, associado a adicionar botao cadastro.
    # `True` = representa o valor lógico verdadeiro.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    projeto = normalizar_projeto(projeto, adicionar_botao_cadastro=(indice < 30))

    # Armazena ou associa em `projeto.exibir_aba_dados` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `exibir_aba_dados` = atributo, método ou recurso acessado com o nome `exibir_aba_dados`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    if indice < 30:
        projeto.exibir_aba_dados = True

    # Armazena ou associa em `projeto._origem_30_projetos` o valor ou resultado definido nesta linha.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `_origem_30_projetos` = atributo, método ou recurso acessado com o nome `_origem_30_projetos`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `True` = representa o valor lógico verdadeiro.
    projeto._origem_30_projetos = True

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
    return projeto
