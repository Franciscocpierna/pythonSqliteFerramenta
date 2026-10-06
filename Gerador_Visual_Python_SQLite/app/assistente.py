# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `__future__` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a future.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `annotations` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a annotations.
from __future__ import annotations

# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
import json

# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `re` = módulo utilizado para trabalhar com expressões regulares.
import re

# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `unicodedata` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a unicodedata.
import unicodedata

# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `urllib` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a urllib.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `error` = atributo, método ou recurso acessado com o nome `error`.
import urllib.error

# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `urllib` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a urllib.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `request` = atributo, método ou recurso acessado com o nome `request`.
import urllib.request

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `typing` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a typing.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
from typing import Any

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `modelos` = atributo, método ou recurso acessado com o nome `modelos`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
from .modelos import Projeto

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `modelos_prontos` = atributo, método ou recurso acessado com o nome `modelos_prontos`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `criar_tela_crud` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a criar tela crud.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `montar_projeto_com_fluxo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a montar projeto com fluxo.
# `criar_tela_login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a criar tela login.
# `criar_tela_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a criar tela menu.
# `modelo_calculadora` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo calculadora.
from .modelos_prontos import criar_tela_crud, montar_projeto_com_fluxo, criar_tela_login, criar_tela_menu, modelo_calculadora

# Define a rotina `_normalizar`, responsável por executar a lógica relacionada a normalizar.
# `def` = define uma nova função ou um novo método.
# `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
def _normalizar(texto: str) -> str:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # texto vazio = representa uma string sem caracteres.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `join` = função, método ou classe chamada para executar a operação relacionada a join.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `unicodedata` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a unicodedata.
    # `normalize` = função, método ou classe chamada para executar a operação relacionada a normalize.
    # `NFD` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `lower` = função, método ou classe chamada para executar a operação relacionada a lower.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `category` = função, método ou classe chamada para executar a operação relacionada a category.
    # `!=` = operador de comparação utilizado para verificar se os valores são diferentes.
    # `Mn` = texto literal utilizado nesta instrução.
    return "".join(c for c in unicodedata.normalize("NFD", texto.lower()) if unicodedata.category(c) != "Mn")

# Define a rotina `_slug`, responsável por executar a lógica relacionada a slug.
# `def` = define uma nova função ou um novo método.
# `_slug` = função, método ou classe chamada para executar a operação relacionada a slug.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `campo` = texto literal utilizado nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
def _slug(texto: str, padrao="campo") -> str:

    # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    texto = _normalizar(texto)

    # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
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
    texto = re.sub(r"[^a-z0-9]+", "_", texto).strip("_")

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not texto:

        # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
        texto = padrao

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `isdigit` = função, método ou classe chamada para executar a operação relacionada a isdigit.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if texto[0].isdigit():

        # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        texto = f"{padrao}_{texto}"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    return texto

# Armazena ou associa em `CAMPOS` o valor ou resultado definido nesta linha.
CAMPOS = {

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `nome` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `obrigatorio` = texto literal utilizado nesta instrução.
    # `True` = representa o valor lógico verdadeiro.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "nome": {"rotulo": "Nome", "tipo_sql": "TEXT", "widget": "Entry", "obrigatorio": True},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `cpf` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `CPF` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "cpf": {"rotulo": "CPF", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "CPF", "validacao": "CPF"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `cnpj` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `CNPJ` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "cnpj": {"rotulo": "CNPJ", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "CNPJ", "validacao": "CNPJ"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `email` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `E-mail` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "email": {"rotulo": "E-mail", "tipo_sql": "TEXT", "widget": "Entry", "validacao": "E-mail"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `telefone` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Telefone` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "telefone": {"rotulo": "Telefone", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "Telefone", "validacao": "Telefone"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `celular` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Celular` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `Telefone` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "celular": {"rotulo": "Celular", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "Telefone", "validacao": "Telefone"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `cep` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `CEP` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "cep": {"rotulo": "CEP", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "CEP", "validacao": "CEP"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `cidade` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Cidade` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "cidade": {"rotulo": "Cidade", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `estado` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Estado` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
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
    "estado": {"rotulo": "Estado", "tipo_sql": "TEXT", "widget": "Combobox", "opcoes": ["SP", "RJ", "MG", "PR", "SC", "RS", "BA", "GO", "PE", "CE"]},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `endereco` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Endereço` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "endereco": {"rotulo": "Endereço", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `bairro` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Bairro` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "bairro": {"rotulo": "Bairro", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `numero` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Número` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "numero": {"rotulo": "Número", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `produto` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Produto` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `obrigatorio` = texto literal utilizado nesta instrução.
    # `True` = representa o valor lógico verdadeiro.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "produto": {"rotulo": "Produto", "tipo_sql": "TEXT", "widget": "Entry", "obrigatorio": True},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `codigo` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Código` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "codigo": {"rotulo": "Código", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `categoria` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Categoria` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Combobox` = texto literal utilizado nesta instrução.
    # `opcoes` = texto literal utilizado nesta instrução.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `Opção 1` = texto literal utilizado nesta instrução.
    # `Opção 2` = texto literal utilizado nesta instrução.
    # `Opção 3` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "categoria": {"rotulo": "Categoria", "tipo_sql": "TEXT", "widget": "Combobox", "opcoes": ["Opção 1", "Opção 2", "Opção 3"]},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `preco` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Preço` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `REAL` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `Moeda` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `Decimal` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "preco": {"rotulo": "Preço", "tipo_sql": "REAL", "widget": "Entry", "mascara": "Moeda", "validacao": "Decimal"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `valor` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Valor` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `REAL` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `Moeda` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `Decimal` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "valor": {"rotulo": "Valor", "tipo_sql": "REAL", "widget": "Entry", "mascara": "Moeda", "validacao": "Decimal"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `valor_total` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Valor Total` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `REAL` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `Moeda` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `Decimal` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "valor_total": {"rotulo": "Valor Total", "tipo_sql": "REAL", "widget": "Entry", "mascara": "Moeda", "validacao": "Decimal"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `quantidade` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Quantidade` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `INTEGER` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Spinbox` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `Inteiro` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "quantidade": {"rotulo": "Quantidade", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `estoque` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Estoque` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `INTEGER` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Spinbox` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `Inteiro` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "estoque": {"rotulo": "Estoque", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `estoque_minimo` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Estoque mínimo` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `INTEGER` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Spinbox` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `Inteiro` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "estoque_minimo": {"rotulo": "Estoque mínimo", "tipo_sql": "INTEGER", "widget": "Spinbox", "validacao": "Inteiro"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `descricao` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Descrição` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Text` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "descricao": {"rotulo": "Descrição", "tipo_sql": "TEXT", "widget": "Text"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `observacoes` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Observações` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Text` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "observacoes": {"rotulo": "Observações", "tipo_sql": "TEXT", "widget": "Text"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `status` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Status` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Combobox` = texto literal utilizado nesta instrução.
    # `opcoes` = texto literal utilizado nesta instrução.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `Ativo` = texto literal utilizado nesta instrução.
    # `Inativo` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "status": {"rotulo": "Status", "tipo_sql": "TEXT", "widget": "Combobox", "opcoes": ["Ativo", "Inativo"]},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `prioridade` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Prioridade` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
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
    "prioridade": {"rotulo": "Prioridade", "tipo_sql": "TEXT", "widget": "Combobox", "opcoes": ["Baixa", "Média", "Alta", "Urgente"]},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `data` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Data` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "data": {"rotulo": "Data", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "Data", "validacao": "Data"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `data_nascimento` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Data de Nascimento` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `Data` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "data_nascimento": {"rotulo": "Data de Nascimento", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "Data", "validacao": "Data"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `prazo` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Prazo` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `Data` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "prazo": {"rotulo": "Prazo", "tipo_sql": "TEXT", "widget": "Entry", "mascara": "Data", "validacao": "Data"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `cliente` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Cliente` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `obrigatorio` = texto literal utilizado nesta instrução.
    # `True` = representa o valor lógico verdadeiro.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "cliente": {"rotulo": "Cliente", "tipo_sql": "TEXT", "widget": "Entry", "obrigatorio": True},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `fornecedor` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Fornecedor` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "fornecedor": {"rotulo": "Fornecedor", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `responsavel` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Responsável` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "responsavel": {"rotulo": "Responsável", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `empresa` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Empresa` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "empresa": {"rotulo": "Empresa", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `tarefa` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Tarefa` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `obrigatorio` = texto literal utilizado nesta instrução.
    # `True` = representa o valor lógico verdadeiro.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "tarefa": {"rotulo": "Tarefa", "tipo_sql": "TEXT", "widget": "Entry", "obrigatorio": True},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `cargo` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Cargo` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "cargo": {"rotulo": "Cargo", "tipo_sql": "TEXT", "widget": "Entry"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `salario` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Salário` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `REAL` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `mascara` = texto literal utilizado nesta instrução.
    # `Moeda` = texto literal utilizado nesta instrução.
    # `validacao` = texto literal utilizado nesta instrução.
    # `Decimal` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "salario": {"rotulo": "Salário", "tipo_sql": "REAL", "widget": "Entry", "mascara": "Moeda", "validacao": "Decimal"},

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `pedido` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `Pedido` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `obrigatorio` = texto literal utilizado nesta instrução.
    # `True` = representa o valor lógico verdadeiro.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    "pedido": {"rotulo": "Pedido", "tipo_sql": "TEXT", "widget": "Entry", "obrigatorio": True},

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
}

# Armazena ou associa em `MODULOS` o valor ou resultado definido nesta linha.
MODULOS = {

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Clientes` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `cpf` = texto literal utilizado nesta instrução.
    # `email` = texto literal utilizado nesta instrução.
    # `telefone` = texto literal utilizado nesta instrução.
    # `cidade` = texto literal utilizado nesta instrução.
    # `estado` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Clientes": ["nome", "cpf", "email", "telefone", "cidade", "estado"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Produtos` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `produto` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `codigo` = texto literal utilizado nesta instrução.
    # `categoria` = texto literal utilizado nesta instrução.
    # `preco` = texto literal utilizado nesta instrução.
    # `estoque` = texto literal utilizado nesta instrução.
    # `fornecedor` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Produtos": ["produto", "codigo", "categoria", "preco", "estoque", "fornecedor"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Contatos` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `telefone` = texto literal utilizado nesta instrução.
    # `email` = texto literal utilizado nesta instrução.
    # `empresa` = texto literal utilizado nesta instrução.
    # `cidade` = texto literal utilizado nesta instrução.
    # `observacoes` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Contatos": ["nome", "telefone", "email", "empresa", "cidade", "observacoes"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Estoque` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `produto` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `codigo` = texto literal utilizado nesta instrução.
    # `quantidade` = texto literal utilizado nesta instrução.
    # `estoque_minimo` = texto literal utilizado nesta instrução.
    # `fornecedor` = texto literal utilizado nesta instrução.
    # `localizacao` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Estoque": ["produto", "codigo", "quantidade", "estoque_minimo", "fornecedor", "localizacao"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Tarefas` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `tarefa` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `prioridade` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `prazo` = texto literal utilizado nesta instrução.
    # `responsavel` = texto literal utilizado nesta instrução.
    # `categoria` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Tarefas": ["tarefa", "prioridade", "status", "prazo", "responsavel", "categoria"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Vendas` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `cliente` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `produto` = texto literal utilizado nesta instrução.
    # `quantidade` = texto literal utilizado nesta instrução.
    # `valor_total` = texto literal utilizado nesta instrução.
    # `data` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Vendas": ["cliente", "produto", "quantidade", "valor_total", "data", "status"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Fornecedores` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `cnpj` = texto literal utilizado nesta instrução.
    # `email` = texto literal utilizado nesta instrução.
    # `telefone` = texto literal utilizado nesta instrução.
    # `cidade` = texto literal utilizado nesta instrução.
    # `estado` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Fornecedores": ["nome", "cnpj", "email", "telefone", "cidade", "estado"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Funcionários` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `cpf` = texto literal utilizado nesta instrução.
    # `email` = texto literal utilizado nesta instrução.
    # `telefone` = texto literal utilizado nesta instrução.
    # `cargo` = texto literal utilizado nesta instrução.
    # `salario` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Funcionários": ["nome", "cpf", "email", "telefone", "cargo", "salario"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Pedidos` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `pedido` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `cliente` = texto literal utilizado nesta instrução.
    # `produto` = texto literal utilizado nesta instrução.
    # `quantidade` = texto literal utilizado nesta instrução.
    # `valor_total` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Pedidos": ["pedido", "cliente", "produto", "quantidade", "valor_total", "status"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Pacientes` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `cpf` = texto literal utilizado nesta instrução.
    # `data_nascimento` = texto literal utilizado nesta instrução.
    # `telefone` = texto literal utilizado nesta instrução.
    # `email` = texto literal utilizado nesta instrução.
    # `cidade` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Pacientes": ["nome", "cpf", "data_nascimento", "telefone", "email", "cidade"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Médicos` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `codigo` = texto literal utilizado nesta instrução.
    # `especialidade` = texto literal utilizado nesta instrução.
    # `telefone` = texto literal utilizado nesta instrução.
    # `email` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Médicos": ["nome", "codigo", "especialidade", "telefone", "email", "status"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Consultas` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `paciente` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `medico` = texto literal utilizado nesta instrução.
    # `data` = texto literal utilizado nesta instrução.
    # `horario` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `observacoes` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Consultas": ["paciente", "medico", "data", "horario", "status", "observacoes"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Usuários` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `email` = texto literal utilizado nesta instrução.
    # `usuario` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Usuários": ["nome", "email", "usuario", "status"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Financeiro` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `descricao` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `categoria` = texto literal utilizado nesta instrução.
    # `valor` = texto literal utilizado nesta instrução.
    # `data` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `observacoes` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Financeiro": ["descricao", "categoria", "valor", "data", "status", "observacoes"],

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Relatórios` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `descricao` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `data` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    "Relatórios": ["descricao", "data", "status"],

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
}

# Armazena ou associa em `ALIASES_MODULOS` o valor ou resultado definido nesta linha.
ALIASES_MODULOS = {

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `cliente` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Clientes` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `clientes` = texto literal utilizado nesta instrução.
    "cliente": "Clientes", "clientes": "Clientes",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `produto` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Produtos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `produtos` = texto literal utilizado nesta instrução.
    "produto": "Produtos", "produtos": "Produtos",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `contato` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Contatos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `contatos` = texto literal utilizado nesta instrução.
    # `agenda` = texto literal utilizado nesta instrução.
    "contato": "Contatos", "contatos": "Contatos", "agenda": "Contatos",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `estoque` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Estoque` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    "estoque": "Estoque",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `tarefa` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Tarefas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tarefas` = texto literal utilizado nesta instrução.
    "tarefa": "Tarefas", "tarefas": "Tarefas",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `venda` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Vendas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `vendas` = texto literal utilizado nesta instrução.
    "venda": "Vendas", "vendas": "Vendas",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `fornecedor` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Fornecedores` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fornecedores` = texto literal utilizado nesta instrução.
    "fornecedor": "Fornecedores", "fornecedores": "Fornecedores",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `funcionario` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Funcionários` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `funcionarios` = texto literal utilizado nesta instrução.
    # `colaborador` = texto literal utilizado nesta instrução.
    # `colaboradores` = texto literal utilizado nesta instrução.
    "funcionario": "Funcionários", "funcionarios": "Funcionários", "colaborador": "Funcionários", "colaboradores": "Funcionários",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `pedido` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Pedidos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `pedidos` = texto literal utilizado nesta instrução.
    "pedido": "Pedidos", "pedidos": "Pedidos",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `paciente` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Pacientes` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `pacientes` = texto literal utilizado nesta instrução.
    "paciente": "Pacientes", "pacientes": "Pacientes",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `medico` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Médicos` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `medicos` = texto literal utilizado nesta instrução.
    "medico": "Médicos", "medicos": "Médicos",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `consulta` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Consultas` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `consultas` = texto literal utilizado nesta instrução.
    "consulta": "Consultas", "consultas": "Consultas",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `usuario` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Usuários` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `usuarios` = texto literal utilizado nesta instrução.
    "usuario": "Usuários", "usuarios": "Usuários",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `financeiro` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Financeiro` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `financas` = texto literal utilizado nesta instrução.
    "financeiro": "Financeiro", "financas": "Financeiro",

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `relatorio` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Relatórios` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `relatorios` = texto literal utilizado nesta instrução.
    "relatorio": "Relatórios", "relatorios": "Relatórios",

# Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
# `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
}

# Define a rotina `listar_modelos_ollama`, responsável por executar a lógica relacionada a listar modelos ollama.
# `def` = define uma nova função ou um novo método.
# `listar_modelos_ollama` = função, método ou classe chamada para executar a operação relacionada a listar modelos ollama.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `timeout` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a timeout.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `0.7` = valor numérico associado a `timeout` nesta instrução.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def listar_modelos_ollama(timeout=0.7):

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Lista modelos do Ollama local. Retorna [] quando o Ollama não está disponível.` = texto literal utilizado nesta instrução.
    """Lista modelos do Ollama local. Retorna [] quando o Ollama não está disponível."""

    # Inicia um bloco protegido para permitir o tratamento de possíveis erros durante sua execução.
    # `try` = inicia um bloco protegido para tratamento de possíveis exceções.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    try:

        # Armazena ou associa em `req` o valor ou resultado definido nesta linha.
        # `req` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a req.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `urllib` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a urllib.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `request` = atributo, método ou recurso acessado com o nome `request`.
        # `Request` = função, método ou classe chamada para executar a operação relacionada a Request.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `http://127.0.0.1:11434/api/tags` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `method` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a method.
        # `GET` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        req = urllib.request.Request("http://127.0.0.1:11434/api/tags", method="GET")

        # Abre um contexto controlado para utilizar o recurso indicado e finalizar seu gerenciamento automaticamente ao sair do bloco.
        # `with` = inicia um gerenciador de contexto para controlar automaticamente o recurso utilizado no bloco.
        # `urllib` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a urllib.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `request` = atributo, método ou recurso acessado com o nome `request`.
        # `urlopen` = função, método ou classe chamada para executar a operação relacionada a urlopen.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `req` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a req.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `timeout` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a timeout.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
        # `resp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resp.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        with urllib.request.urlopen(req, timeout=timeout) as resp:

            # Armazena ou associa em `dados` o valor ou resultado definido nesta linha.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `loads` = função, método ou classe chamada para executar a operação relacionada a loads.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `resp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resp.
            # `read` = função, método ou classe chamada para executar a operação relacionada a read.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `decode` = função, método ou classe chamada para executar a operação relacionada a decode.
            # `utf-8` = texto literal utilizado nesta instrução.
            dados = json.loads(resp.read().decode("utf-8"))

        # Armazena ou associa em `nomes` o valor ou resultado definido nesta linha.
        # `nomes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        nomes = []

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `models` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for item in dados.get("models", []):

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `name` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
            # `model` = texto literal utilizado nesta instrução.
            nome = item.get("name") or item.get("model")

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if nome:

                # Executa `nomes.append` com os argumentos informados para realizar a operação correspondente.
                # `nomes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `append` = função, método ou classe chamada para executar a operação relacionada a append.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                nomes.append(nome)

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `nomes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nomes.
        return nomes

    # Define o tratamento executado quando ocorre a exceção indicada durante o bloco protegido.
    # `except` = define o bloco executado quando ocorre a exceção indicada.
    # `Exception` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Exception.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    except Exception:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        return []

# Define a rotina `_campo_def`, responsável por executar a lógica relacionada a campo def.
# `def` = define uma nova função ou um novo método.
# `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
# `|` = combina alternativas, inclusive tipos aceitos em uma anotação.
# `None` = representa ausência de valor.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `**` = operador utilizado para realizar potenciação.
# `extras` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a extras.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
def _campo_def(nome: str, rotulo: str | None = None, **extras):

    # Armazena ou associa em `chave` o valor ou resultado definido nesta linha.
    # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_slug` = função, método ou classe chamada para executar a operação relacionada a slug.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    chave = _slug(nome)

    # Armazena ou associa em `base` o valor ou resultado definido nesta linha.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `dict` = função ou tipo utilizado para criar ou representar um dicionário.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `CAMPOS` = constante utilizada para armazenar o valor relacionado a campos.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `rotulo` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `replace` = função, método ou classe chamada para executar a operação relacionada a replace.
    # `_` = texto literal utilizado nesta instrução.
    # ` ` = texto literal utilizado nesta instrução.
    # `title` = função, método ou classe chamada para executar a operação relacionada a title.
    # `tipo_sql` = texto literal utilizado nesta instrução.
    # `TEXT` = texto literal utilizado nesta instrução.
    # `widget` = texto literal utilizado nesta instrução.
    # `Entry` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    base = dict(CAMPOS.get(chave, {"rotulo": (rotulo or nome).replace("_", " ").title(), "tipo_sql": "TEXT", "widget": "Entry"}))

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if rotulo:

        # Executa a instrução desta linha como parte da lógica atual do programa.
        # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `rotulo` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `rotulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a rotulo.
        base["rotulo"] = rotulo

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `nome` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
    base["nome"] = chave

    # Executa `base.update` com os argumentos informados para realizar a operação correspondente.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `update` = função, método ou classe chamada para executar a operação relacionada a update.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `k` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a k.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `v` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a v.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `extras` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a extras.
    # `items` = função, método ou classe chamada para executar a operação relacionada a items.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `None` = representa ausência de valor.
    # texto vazio = representa uma string sem caracteres.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    base.update({k: v for k, v in extras.items() if v not in (None, "")})

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    return base

# Define a rotina `_detectar_modulos`, responsável por executar a lógica relacionada a detectar modulos.
# `def` = define uma nova função ou um novo método.
# `_detectar_modulos` = função, método ou classe chamada para executar a operação relacionada a detectar modulos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
def _detectar_modulos(texto: str):

    # Armazena ou associa em `normal` o valor ou resultado definido nesta linha.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    normal = _normalizar(texto)

    # Define a rotina `converter_lista`, responsável por executar a lógica relacionada a converter lista.
    # `def` = define uma nova função ou um novo método.
    # `converter_lista` = função, método ou classe chamada para executar a operação relacionada a converter lista.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def converter_lista(trecho):

        # Armazena ou associa em `achados` o valor ou resultado definido nesta linha.
        # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        achados = []

        # Armazena ou associa em `trecho` o valor ou resultado definido nesta linha.
        # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `split` = função, método ou classe chamada para executar a operação relacionada a split.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `\\b(?:onde|que tera|que deve|com campos|contendo)\\b` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        trecho = re.split(r"\b(?:onde|que tera|que deve|com campos|contendo)\b", trecho, 1)[0]

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `split` = função, método ou classe chamada para executar a operação relacionada a split.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `\\s*,\\s*|\\s*;\\s*|\\s+e\\s+|\\s*/\\s*` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for item in re.split(r"\s*,\s*|\s*;\s*|\s+e\s+|\s*/\s*", trecho):

            # Armazena ou associa em `item` o valor ou resultado definido nesta linha.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `re` = módulo utilizado para trabalhar com expressões regulares.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `sub` = função, método ou classe chamada para executar a operação relacionada a sub.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `\\b(login|menu principal|menu)\\b` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # texto vazio = representa uma string sem caracteres.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
            # ` -` = texto literal utilizado nesta instrução.
            item = re.sub(r"\b(login|menu principal|menu)\b", "", item).strip(" -")

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `not` = inverte o resultado lógico da expressão seguinte.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
            # `len` = função que retorna a quantidade de elementos do objeto informado.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `split` = função, método ou classe chamada para executar a operação relacionada a split.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `>` = operador de comparação utilizado para verificar se o valor da esquerda é maior.
            # `3` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if not item or len(item.split()) > 3:

                # Encerra a iteração atual e continua o laço a partir da próxima repetição.
                # `continue` = interrompe a iteração atual e avança para a próxima repetição.
                continue

            # Armazena ou associa em `chave` o valor ou resultado definido nesta linha.
            # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            chave = _normalizar(item)

            # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `ALIASES_MODULOS` = constante utilizada para armazenar o valor relacionado a aliases modulos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `title` = função, método ou classe chamada para executar a operação relacionada a title.
            nome = ALIASES_MODULOS.get(chave) or item.title()

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
            # `not` = inverte o resultado lógico da expressão seguinte.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if nome and nome not in achados:

                # Executa `achados.append` com os argumentos informados para realizar a operação correspondente.
                # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `append` = função, método ou classe chamada para executar a operação relacionada a append.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                achados.append(nome)

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
        return achados

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    for padrao in [

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `(?:telas?|modulos?)\\s+(?:de\\s+)?([^.;!?]+)` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        r"(?:telas?|modulos?)\s+(?:de\s+)?([^.;!?]+)",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `(?:quero|preciso de|tenha)\\s+(?:as\\s+)?telas?\\s+(?:de\\s+)?([^.;!?]+)` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        r"(?:quero|preciso de|tenha)\s+(?:as\s+)?telas?\s+(?:de\s+)?([^.;!?]+)",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    ]:

        # Armazena ou associa em `m` o valor ou resultado definido nesta linha.
        # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `search` = função, método ou classe chamada para executar a operação relacionada a search.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        m = re.search(padrao, normal)

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if m:

            # Armazena ou associa em `itens` o valor ou resultado definido nesta linha.
            # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `converter_lista` = função, método ou classe chamada para executar a operação relacionada a converter lista.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `group` = função, método ou classe chamada para executar a operação relacionada a group.
            # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            itens = converter_lista(m.group(1))

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if itens:

                # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
                # `return` = encerra a rotina atual e devolve o valor especificado.
                # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
                # `8` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                return itens[:8]

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    for padrao in [

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `cadastro\\s+de\\s+([a-z0-9_-]+)` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        r"cadastro\s+de\s+([a-z0-9_-]+)",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `controle\\s+de\\s+([a-z0-9_-]+)` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        r"controle\s+de\s+([a-z0-9_-]+)",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `agenda\\s+de\\s+([a-z0-9_-]+)` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        r"agenda\s+de\s+([a-z0-9_-]+)",

        # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
        # `sistema\\s+de\\s+([a-z0-9_-]+)` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        r"sistema\s+de\s+([a-z0-9_-]+)",

    # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    ]:

        # Armazena ou associa em `m` o valor ou resultado definido nesta linha.
        # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `search` = função, método ou classe chamada para executar a operação relacionada a search.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        m = re.search(padrao, normal)

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if m:

            # Armazena ou associa em `chave` o valor ou resultado definido nesta linha.
            # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `group` = função, método ou classe chamada para executar a operação relacionada a group.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            chave = m.group(1)

            # Armazena ou associa em `conhecido` o valor ou resultado definido nesta linha.
            # `conhecido` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conhecido.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `ALIASES_MODULOS` = constante utilizada para armazenar o valor relacionado a aliases modulos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            conhecido = ALIASES_MODULOS.get(chave)

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `conhecido` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conhecido.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if conhecido:

                # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
                # `return` = encerra a rotina atual e devolve o valor especificado.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `conhecido` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conhecido.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                return [conhecido]

    # Armazena ou associa em `m` o valor ou resultado definido nesta linha.
    # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `search` = função, método ou classe chamada para executar a operação relacionada a search.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `sistema[^.!?]*?\\scom\\s+([^.!?]+)` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    m = re.search(r"sistema[^.!?]*?\scom\s+([^.!?]+)", normal)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if m:

        # Armazena ou associa em `candidatos` o valor ou resultado definido nesta linha.
        # `candidatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatos.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `converter_lista` = função, método ou classe chamada para executar a operação relacionada a converter lista.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `group` = função, método ou classe chamada para executar a operação relacionada a group.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        candidatos = converter_lista(m.group(1))

        # Armazena ou associa em `conhecidos` o valor ou resultado definido nesta linha.
        # `conhecidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conhecidos.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `candidatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatos.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `MODULOS` = constante utilizada para armazenar o valor relacionado a modulos.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        conhecidos = [x for x in candidatos if x in MODULOS]

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `len` = função que retorna a quantidade de elementos do objeto informado.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `conhecidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conhecidos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `>=` = operador de comparação utilizado para verificar se o valor da esquerda é maior ou igual.
        # `2` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if len(conhecidos) >= 2:

            # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
            # `return` = encerra a rotina atual e devolve o valor especificado.
            # `conhecidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conhecidos.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `8` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            return conhecidos[:8]

    # Armazena ou associa em `achados` o valor ou resultado definido nesta linha.
    # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    achados = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `alias` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alias.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `ALIASES_MODULOS` = constante utilizada para armazenar o valor relacionado a aliases modulos.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `items` = função, método ou classe chamada para executar a operação relacionada a items.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for alias, nome in ALIASES_MODULOS.items():

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `alias` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alias.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `estoque` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `status` = texto literal utilizado nesta instrução.
        # `usuario` = texto literal utilizado nesta instrução.
        # `usuarios` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if alias in {"estoque", "status", "usuario", "usuarios"}:

            # Encerra a iteração atual e continua o laço a partir da próxima repetição.
            # `continue` = interrompe a iteração atual e avança para a próxima repetição.
            continue

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `search` = função, método ou classe chamada para executar a operação relacionada a search.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `escape` = função, método ou classe chamada para executar a operação relacionada a escape.
        # `alias` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alias.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if re.search(rf"\b{re.escape(alias)}\b", normal) and nome not in achados:

            # Executa `achados.append` com os argumentos informados para realizar a operação correspondente.
            # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            achados.append(nome)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `achados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a achados.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `8` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return achados[:8]

# Define a rotina `_extrair_entidade`, responsável por executar a lógica relacionada a extrair entidade.
# `def` = define uma nova função ou um novo método.
# `_extrair_entidade` = função, método ou classe chamada para executar a operação relacionada a extrair entidade.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
def _extrair_entidade(texto: str) -> str:

    # Armazena ou associa em `normal` o valor ou resultado definido nesta linha.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    normal = _normalizar(texto)

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `cadastro\\s+de\\s+([a-z0-9 _-]+?)(?:\\s+com|[.,;]|$)` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `sistema\\s+de\\s+([a-z0-9 _-]+?)(?:\\s+com|[.,;]|$)` = texto literal utilizado nesta instrução.
    # `controle\\s+de\\s+([a-z0-9 _-]+?)(?:\\s+com|[.,;]|$)` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for padrao in [r"cadastro\s+de\s+([a-z0-9 _-]+?)(?:\s+com|[.,;]|$)", r"sistema\s+de\s+([a-z0-9 _-]+?)(?:\s+com|[.,;]|$)", r"controle\s+de\s+([a-z0-9 _-]+?)(?:\s+com|[.,;]|$)"]:

        # Armazena ou associa em `m` o valor ou resultado definido nesta linha.
        # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `search` = função, método ou classe chamada para executar a operação relacionada a search.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        m = re.search(padrao, normal)

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if m:

            # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
            # `return` = encerra a rotina atual e devolve o valor especificado.
            # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `group` = função, método ou classe chamada para executar a operação relacionada a group.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
            # `title` = função, método ou classe chamada para executar a operação relacionada a title.
            return m.group(1).strip().title()

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Registros` = texto literal utilizado nesta instrução.
    return "Registros"

# Define a rotina `_extrair_campos_explicitos`, responsável por executar a lógica relacionada a extrair campos explicitos.
# `def` = define uma nova função ou um novo método.
# `_extrair_campos_explicitos` = função, método ou classe chamada para executar a operação relacionada a extrair campos explicitos.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
def _extrair_campos_explicitos(texto: str):

    # Armazena ou associa em `normal` o valor ou resultado definido nesta linha.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    normal = _normalizar(texto)

    # Armazena ou associa em `trecho` o valor ou resultado definido nesta linha.
    # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    trecho = ""

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # ` com ` = texto literal utilizado nesta instrução.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if " com " in normal:

        # Armazena ou associa em `trecho` o valor ou resultado definido nesta linha.
        # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `split` = função, método ou classe chamada para executar a operação relacionada a split.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # ` com ` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        trecho = normal.split(" com ", 1)[1]

        # Armazena ou associa em `trecho` o valor ou resultado definido nesta linha.
        # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `split` = função, método ou classe chamada para executar a operação relacionada a split.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `[.!?]` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        trecho = re.split(r"[.!?]", trecho, 1)[0]

        # Armazena ou associa em `trecho` o valor ou resultado definido nesta linha.
        # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `split` = função, método ou classe chamada para executar a operação relacionada a split.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `\\b(?:quero|inclua|adicione|coloque|botoes|telas|menu|login)\\b` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        trecho = re.split(r"\b(?:quero|inclua|adicione|coloque|botoes|telas|menu|login)\b", trecho, 1)[0]

    # Armazena ou associa em `candidatos` o valor ou resultado definido nesta linha.
    # `candidatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    candidatos = []

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if trecho:

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `replace` = função, método ou classe chamada para executar a operação relacionada a replace.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # ` e ` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `,` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `;` = texto literal utilizado nesta instrução.
        # `/` = texto literal utilizado nesta instrução.
        # `split` = função, método ou classe chamada para executar a operação relacionada a split.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for item in trecho.replace(" e ", ",").replace(";", ",").replace("/", ",").split(","):

            # Armazena ou associa em `item` o valor ou resultado definido nesta linha.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `_slug` = função, método ou classe chamada para executar a operação relacionada a slug.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # texto vazio = representa uma string sem caracteres.
            item = _slug(item.strip(), "")

            # Armazena ou associa em `item` o valor ou resultado definido nesta linha.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `re` = módulo utilizado para trabalhar com expressões regulares.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `sub` = função, método ou classe chamada para executar a operação relacionada a sub.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `^(campo_|um_|uma_)` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # texto vazio = representa uma string sem caracteres.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            item = re.sub(r"^(campo_|um_|uma_)", "", item)

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if item:

                # Executa `candidatos.append` com os argumentos informados para realizar a operação correspondente.
                # `candidatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatos.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `append` = função, método ou classe chamada para executar a operação relacionada a append.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                candidatos.append(item)

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `CAMPOS` = constante utilizada para armazenar o valor relacionado a campos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for chave in CAMPOS:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `replace` = função, método ou classe chamada para executar a operação relacionada a replace.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `_` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # ` ` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `candidatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatos.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if chave.replace("_", " ") in normal and chave not in candidatos:

            # Executa `candidatos.append` com os argumentos informados para realizar a operação correspondente.
            # `candidatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            candidatos.append(chave)

    # Armazena ou associa em `saida` o valor ou resultado definido nesta linha.
    # `saida` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a saida.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    saida = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `candidatos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a candidatos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for c in candidatos:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `e_mail` = texto literal utilizado nesta instrução.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `email` = texto literal utilizado nesta instrução.
        if c == "e_mail": c = "email"

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `mail` = texto literal utilizado nesta instrução.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `email` = texto literal utilizado nesta instrução.
        if "mail" in c: c = "email"

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `nascimento` = texto literal utilizado nesta instrução.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `data_nascimento` = texto literal utilizado nesta instrução.
        if "nascimento" in c: c = "data_nascimento"

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `fone` = texto literal utilizado nesta instrução.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `telefone` = texto literal utilizado nesta instrução.
        if "fone" in c: c = "telefone"

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `saida` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a saida.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if c not in saida:

            # Executa `saida.append` com os argumentos informados para realizar a operação correspondente.
            # `saida` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a saida.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            saida.append(c)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `data_nascimento` = texto literal utilizado nesta instrução.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `saida` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a saida.
    # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
    # `data` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if "data_nascimento" in saida and "data" in saida:

        # Executa `saida.remove` com os argumentos informados para realizar a operação correspondente.
        # `saida` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a saida.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `remove` = função, método ou classe chamada para executar a operação relacionada a remove.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `data` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        saida.remove("data")

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `saida` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a saida.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `14` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return saida[:14]

# Define a rotina `_extrair_campos_do_modulo`, responsável por executar a lógica relacionada a extrair campos do modulo.
# `def` = define uma nova função ou um novo método.
# `_extrair_campos_do_modulo` = função, método ou classe chamada para executar a operação relacionada a extrair campos do modulo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
def _extrair_campos_do_modulo(texto: str, nome_modulo: str):

    # Armazena ou associa em `normal` o valor ou resultado definido nesta linha.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    normal = _normalizar(texto)

    # Armazena ou associa em `nome_norm` o valor ou resultado definido nesta linha.
    # `nome_norm` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome norm.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    nome_norm = _normalizar(nome_modulo)

    # Armazena ou associa em `singular` o valor ou resultado definido nesta linha.
    # `singular` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a singular.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `nome_norm` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome norm.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `-` = operador utilizado para realizar subtração ou representar um valor negativo, conforme o contexto.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `endswith` = função, método ou classe chamada para executar a operação relacionada a endswith.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `s` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
    singular = nome_norm[:-1] if nome_norm.endswith("s") else nome_norm

    # Armazena ou associa em `padrao` o valor ou resultado definido nesta linha.
    # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `escape` = função, método ou classe chamada para executar a operação relacionada a escape.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome_norm` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome norm.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    # `singular` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a singular.
    padrao = rf"(?:{re.escape(nome_norm)}|{re.escape(singular)})\s+(?:deve\s+ter|deve\s+conter|com|tera|tem)\s+([^.!?]+)"

    # Armazena ou associa em `m` o valor ou resultado definido nesta linha.
    # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `search` = função, método ou classe chamada para executar a operação relacionada a search.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `padrao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a padrao.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    m = re.search(padrao, normal)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not m:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        return []

    # Armazena ou associa em `trecho` o valor ou resultado definido nesta linha.
    # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `split` = função, método ou classe chamada para executar a operação relacionada a split.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `\\b(?:em todos|na tela|e quero|tambem quero|com botoes|quero botoes)\\b` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `m` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a m.
    # `group` = função, método ou classe chamada para executar a operação relacionada a group.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    trecho = re.split(r"\b(?:em todos|na tela|e quero|tambem quero|com botoes|quero botoes)\b", m.group(1), 1)[0]

    # Armazena ou associa em `itens` o valor ou resultado definido nesta linha.
    # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    itens = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `split` = função, método ou classe chamada para executar a operação relacionada a split.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `\\s*,\\s*|\\s*;\\s*|\\s+e\\s+` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `trecho` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a trecho.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for item in re.split(r"\s*,\s*|\s*;\s*|\s+e\s+", trecho):

        # Armazena ou associa em `chave` o valor ou resultado definido nesta linha.
        # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `_slug` = função, método ou classe chamada para executar a operação relacionada a slug.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # texto vazio = representa uma string sem caracteres.
        chave = _slug(item.strip(), "")

        # Armazena ou associa em `chave` o valor ou resultado definido nesta linha.
        # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `sub` = função, método ou classe chamada para executar a operação relacionada a sub.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `^(campo_|um_|uma_)` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        chave = re.sub(r"^(campo_|um_|uma_)", "", chave)

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if chave and chave not in itens:

            # Executa `itens.append` com os argumentos informados para realizar a operação correspondente.
            # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            itens.append(chave)

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `itens` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a itens.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `14` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return itens[:14]

# Define a rotina `_defs_modulo`, responsável por executar a lógica relacionada a defs modulo.
# `def` = define uma nova função ou um novo método.
# `_defs_modulo` = função, método ou classe chamada para executar a operação relacionada a defs modulo.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
def _defs_modulo(nome_modulo: str, texto: str):

    # Armazena ou associa em `especificos` o valor ou resultado definido nesta linha.
    # `especificos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a especificos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_extrair_campos_do_modulo` = função, método ou classe chamada para executar a operação relacionada a extrair campos do modulo.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    especificos = _extrair_campos_do_modulo(texto, nome_modulo)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `especificos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a especificos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if especificos:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `especificos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a especificos.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        return [_campo_def(c) for c in especificos]

    # Armazena ou associa em `base` o valor ou resultado definido nesta linha.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `MODULOS` = constante utilizada para armazenar o valor relacionado a modulos.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    base = MODULOS.get(nome_modulo)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if base:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `base` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a base.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        return [_campo_def(c) for c in base]

    # Armazena ou associa em `explicitos` o valor ou resultado definido nesta linha.
    # `explicitos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a explicitos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_extrair_campos_explicitos` = função, método ou classe chamada para executar a operação relacionada a extrair campos explicitos.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    explicitos = _extrair_campos_explicitos(texto)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `explicitos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a explicitos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if explicitos:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `explicitos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a explicitos.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `8` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        return [_campo_def(c) for c in explicitos[:8]]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = texto literal utilizado nesta instrução.
    # `status` = texto literal utilizado nesta instrução.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return [_campo_def("nome"), _campo_def("descricao"), _campo_def("status")]

# Define a rotina `_projeto_interpretador_local`, responsável por executar a lógica relacionada a projeto interpretador local.
# `def` = define uma nova função ou um novo método.
# `_projeto_interpretador_local` = função, método ou classe chamada para executar a operação relacionada a projeto interpretador local.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
def _projeto_interpretador_local(descricao: str) -> Projeto:

    # Armazena ou associa em `normal` o valor ou resultado definido nesta linha.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    normal = _normalizar(descricao)

    # Armazena ou associa em `modulos` o valor ou resultado definido nesta linha.
    # `modulos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modulos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_detectar_modulos` = função, método ou classe chamada para executar a operação relacionada a detectar modulos.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    modulos = _detectar_modulos(descricao)

    # Armazena ou associa em `campos_explicitos` o valor ou resultado definido nesta linha.
    # `campos_explicitos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos explicitos.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_extrair_campos_explicitos` = função, método ou classe chamada para executar a operação relacionada a extrair campos explicitos.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    campos_explicitos = _extrair_campos_explicitos(descricao)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `modulos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modulos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not modulos:

        # Armazena ou associa em `entidade` o valor ou resultado definido nesta linha.
        # `entidade` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a entidade.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `_extrair_entidade` = função, método ou classe chamada para executar a operação relacionada a extrair entidade.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        entidade = _extrair_entidade(descricao)

        # Armazena ou associa em `nome_tela` o valor ou resultado definido nesta linha.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `entidade` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a entidade.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `!=` = operador de comparação utilizado para verificar se os valores são diferentes.
        # `Registros` = texto literal utilizado nesta instrução.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `Cadastro` = texto literal utilizado nesta instrução.
        nome_tela = entidade if entidade != "Registros" else "Cadastro"

        # Armazena ou associa em `defs` o valor ou resultado definido nesta linha.
        # `defs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a defs.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `campos_explicitos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos explicitos.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `nome` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `descricao` = texto literal utilizado nesta instrução.
        # `status` = texto literal utilizado nesta instrução.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        defs = [_campo_def(c) for c in (campos_explicitos or ["nome", "descricao", "status"])]

        # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `criar_tela_crud` = função, método ou classe chamada para executar a operação relacionada a criar tela crud.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `entidade` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a entidade.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `_slug` = função, método ou classe chamada para executar a operação relacionada a slug.
        # `registros` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `defs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a defs.
        # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
        # `False` = representa o valor lógico falso.
        tela = criar_tela_crud(nome_tela, f"Cadastro de {entidade}", _slug(entidade, "registros"), defs, incluir_menu=False)

        # Armazena ou associa em `quer_login` o valor ou resultado definido nesta linha.
        # `quer_login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a quer login.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `re` = módulo utilizado para trabalhar com expressões regulares.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `search` = função, método ou classe chamada para executar a operação relacionada a search.
        # `\\b(login|senha|autenticacao|acesso)\\b` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        quer_login = bool(re.search(r"\b(login|senha|autenticacao|acesso)\b", normal))

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `quer_login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a quer login.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if quer_login:

            # Armazena ou associa em `login` o valor ou resultado definido nesta linha.
            # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `criar_tela_login` = função, método ou classe chamada para executar a operação relacionada a criar tela login.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            login = criar_tela_login(nome_tela)

            # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
            # `return` = encerra a rotina atual e devolve o valor especificado.
            # `Projeto` = classe que representa um projeto criado no Gerador Visual.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
            # `entidade` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a entidade.
            # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Azul corporativo` = texto literal utilizado nesta instrução.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `id` = atributo, método ou recurso acessado com o nome `id`.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            return Projeto(f"Sistema de {entidade}", "Azul corporativo", [login, tela], login.id)

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `Projeto` = classe que representa um projeto criado no Gerador Visual.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `entidade` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a entidade.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Azul corporativo` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `id` = atributo, método ou recurso acessado com o nome `id`.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return Projeto(f"Sistema de {entidade}", "Azul corporativo", [tela], tela.id)

    # Armazena ou associa em `telas` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    telas = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `modulos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modulos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    for nome_modulo in modulos:

        # Armazena ou associa em `defs` o valor ou resultado definido nesta linha.
        # `defs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a defs.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `_defs_modulo` = função, método ou classe chamada para executar a operação relacionada a defs modulo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        defs = _defs_modulo(nome_modulo, descricao)

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `len` = função que retorna a quantidade de elementos do objeto informado.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `modulos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modulos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `==` = operador de comparação utilizado para verificar se os valores são iguais.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
        # `campos_explicitos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos explicitos.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if len(modulos) == 1 and campos_explicitos:

            # Armazena ou associa em `defs` o valor ou resultado definido nesta linha.
            # `defs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a defs.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `campos_explicitos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos explicitos.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            defs = [_campo_def(c) for c in campos_explicitos]

        # Armazena ou associa em `tabela` o valor ou resultado definido nesta linha.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `_slug` = função, método ou classe chamada para executar a operação relacionada a slug.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `registros` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        tabela = _slug(nome_modulo, "registros")

        # Armazena ou associa em `titulo` o valor ou resultado definido nesta linha.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `Vendas` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Estoque` = texto literal utilizado nesta instrução.
        # `Tarefas` = texto literal utilizado nesta instrução.
        # `Pedidos` = texto literal utilizado nesta instrução.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        titulo = f"Cadastro de {nome_modulo}" if nome_modulo not in {"Vendas", "Estoque", "Tarefas", "Pedidos"} else nome_modulo

        # Executa `telas.append` com os argumentos informados para realizar a operação correspondente.
        # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `criar_tela_crud` = função, método ou classe chamada para executar a operação relacionada a criar tela crud.
        # `nome_modulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome modulo.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `defs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a defs.
        # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        telas.append(criar_tela_crud(nome_modulo, titulo, tabela, defs, incluir_menu=True))

    # Armazena ou associa em `nome_sistema` o valor ou resultado definido nesta linha.
    # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `_extrair_entidade` = função, método ou classe chamada para executar a operação relacionada a extrair entidade.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    nome_sistema = _extrair_entidade(descricao)

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
    # `==` = operador de comparação utilizado para verificar se os valores são iguais.
    # `Registros` = texto literal utilizado nesta instrução.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `modulos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modulos.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if nome_sistema == "Registros" or nome_sistema in modulos:

        # Armazena ou associa em `nome_sistema` o valor ou resultado definido nesta linha.
        # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Sistema ` = texto literal utilizado nesta instrução.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `Integrado` = texto literal utilizado nesta instrução.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `len` = função que retorna a quantidade de elementos do objeto informado.
        # `modulos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modulos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `>` = operador de comparação utilizado para verificar se o valor da esquerda é maior.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        nome_sistema = "Sistema " + ("Integrado" if len(modulos) > 1 else modulos[0])

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `>` = operador de comparação utilizado para verificar se o valor da esquerda é maior.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `search` = função, método ou classe chamada para executar a operação relacionada a search.
    # `\\b(login|menu|senha|autenticacao)\\b` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `normal` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a normal.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if len(telas) > 1 or re.search(r"\b(login|menu|senha|autenticacao)\b", normal):

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Azul corporativo` = texto literal utilizado nesta instrução.
        # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return montar_projeto_com_fluxo(nome_sistema, "Azul corporativo", telas)

    # Armazena ou associa em `telas[0].componentes` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `btn_menu` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `btn_sair` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    telas[0].componentes = [c for c in telas[0].componentes if c.nome not in {"btn_menu", "btn_sair"}]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome_sistema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome sistema.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Azul corporativo` = texto literal utilizado nesta instrução.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return Projeto(nome_sistema, "Azul corporativo", telas, telas[0].id)

# Define a rotina `_limpar_json_resposta`, responsável por executar a lógica relacionada a limpar json resposta.
# `def` = define uma nova função ou um novo método.
# `_limpar_json_resposta` = função, método ou classe chamada para executar a operação relacionada a limpar json resposta.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
def _limpar_json_resposta(texto: str):

    # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    texto = texto.strip()

    # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `sub` = função, método ou classe chamada para executar a operação relacionada a sub.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `^```(?:json)?` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # texto vazio = representa uma string sem caracteres.
    # `flags` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a flags.
    # `I` = constante utilizada para armazenar o valor relacionado a i.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
    texto = re.sub(r"^```(?:json)?", "", texto, flags=re.I).strip()

    # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `re` = módulo utilizado para trabalhar com expressões regulares.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `sub` = função, método ou classe chamada para executar a operação relacionada a sub.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # ````$` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # texto vazio = representa uma string sem caracteres.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
    texto = re.sub(r"```$", "", texto).strip()

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `ini` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ini.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `fim` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fim.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `find` = função, método ou classe chamada para executar a operação relacionada a find.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `{` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `rfind` = função, método ou classe chamada para executar a operação relacionada a rfind.
    # `}` = texto literal utilizado nesta instrução.
    ini, fim = texto.find("{"), texto.rfind("}")

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `ini` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ini.
    # `>=` = operador de comparação utilizado para verificar se o valor da esquerda é maior ou igual.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `and` = operador lógico E, que exige que as condições relacionadas sejam verdadeiras.
    # `fim` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fim.
    # `>` = operador de comparação utilizado para verificar se o valor da esquerda é maior.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if ini >= 0 and fim > ini:

        # Armazena ou associa em `texto` o valor ou resultado definido nesta linha.
        # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `ini` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ini.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `fim` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fim.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        texto = texto[ini:fim+1]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    return texto

# Define a rotina `_projeto_de_especificacao`, responsável por executar a lógica relacionada a projeto de especificacao.
# `def` = define uma nova função ou um novo método.
# `_projeto_de_especificacao` = função, método ou classe chamada para executar a operação relacionada a projeto de especificacao.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `dict` = função ou tipo utilizado para criar ou representar um dicionário.
# `[` = abre uma lista, índice, acesso a elemento ou compreensão.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
# `]` = fecha a lista, índice, acesso a elemento ou compreensão.
# `descricao_original` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao original.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
def _projeto_de_especificacao(spec: dict[str, Any], descricao_original: str) -> Projeto:

    # Armazena ou associa em `nome` o valor ou resultado definido nesta linha.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `nome` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `name` = texto literal utilizado nesta instrução.
    # `Sistema Inteligente` = texto literal utilizado nesta instrução.
    # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
    nome = str(spec.get("nome") or spec.get("name") or "Sistema Inteligente").strip()

    # Armazena ou associa em `tema` o valor ou resultado definido nesta linha.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `tema` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `theme` = texto literal utilizado nesta instrução.
    # `Azul corporativo` = texto literal utilizado nesta instrução.
    tema = str(spec.get("tema") or spec.get("theme") or "Azul corporativo")

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `Claro` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Escuro` = texto literal utilizado nesta instrução.
    # `Azul corporativo` = texto literal utilizado nesta instrução.
    # `Verde` = texto literal utilizado nesta instrução.
    # `Minimalista` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if tema not in {"Claro", "Escuro", "Azul corporativo", "Verde", "Minimalista"}:

        # Armazena ou associa em `tema` o valor ou resultado definido nesta linha.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `Azul corporativo` = texto literal utilizado nesta instrução.
        tema = "Azul corporativo"

    # Armazena ou associa em `telas_specs` o valor ou resultado definido nesta linha.
    # `telas_specs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas specs.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `telas` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `screens` = texto literal utilizado nesta instrução.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    telas_specs = spec.get("telas") or spec.get("screens") or []

    # Armazena ou associa em `telas` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    telas = []

    # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `ts` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ts.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `enumerate` = função que percorre elementos fornecendo também o respectivo índice.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `telas_specs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas specs.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `8` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    for i, ts in enumerate(telas_specs[:8]):

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `isinstance` = função que verifica se um objeto pertence ao tipo ou classe informado.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `ts` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ts.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `dict` = função ou tipo utilizado para criar ou representar um dicionário.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not isinstance(ts, dict):

            # Encerra a iteração atual e continua o laço a partir da próxima repetição.
            # `continue` = interrompe a iteração atual e avança para a próxima repetição.
            continue

        # Armazena ou associa em `nome_tela` o valor ou resultado definido nesta linha.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `str` = função ou tipo utilizado para representar e converter valores para texto.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `ts` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ts.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `nome` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `name` = texto literal utilizado nesta instrução.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `strip` = função, método ou classe chamada para executar a operação relacionada a strip.
        nome_tela = str(ts.get("nome") or ts.get("name") or f"Tela {i+1}").strip()

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `login` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `menu` = texto literal utilizado nesta instrução.
        # `menu principal` = texto literal utilizado nesta instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if _normalizar(nome_tela) in {"login", "menu", "menu principal"}:

            # Encerra a iteração atual e continua o laço a partir da próxima repetição.
            # `continue` = interrompe a iteração atual e avança para a próxima repetição.
            continue

        # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        campos = []

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `ts` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ts.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `campos` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `fields` = texto literal utilizado nesta instrução.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `14` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
        for fs in (ts.get("campos") or ts.get("fields") or [])[:14]:

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `isinstance` = função que verifica se um objeto pertence ao tipo ou classe informado.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `str` = função ou tipo utilizado para representar e converter valores para texto.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if isinstance(fs, str):

                # Executa `campos.append` com os argumentos informados para realizar a operação correspondente.
                # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `append` = função, método ou classe chamada para executar a operação relacionada a append.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `_campo_def` = função, método ou classe chamada para executar a operação relacionada a campo def.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                campos.append(_campo_def(fs))

                # Encerra a iteração atual e continua o laço a partir da próxima repetição.
                # `continue` = interrompe a iteração atual e avança para a próxima repetição.
                continue

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `not` = inverte o resultado lógico da expressão seguinte.
            # `isinstance` = função que verifica se um objeto pertence ao tipo ou classe informado.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `dict` = função ou tipo utilizado para criar ou representar um dicionário.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if not isinstance(fs, dict):

                # Encerra a iteração atual e continua o laço a partir da próxima repetição.
                # `continue` = interrompe a iteração atual e avança para a próxima repetição.
                continue

            # Armazena ou associa em `n` o valor ou resultado definido nesta linha.
            # `n` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a n.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `nome` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
            # `name` = texto literal utilizado nesta instrução.
            # `campo` = texto literal utilizado nesta instrução.
            n = fs.get("nome") or fs.get("name") or "campo"

            # Executa `campos.append` com os argumentos informados para realizar a operação correspondente.
            campos.append(_campo_def(

                # Adiciona ou configura este valor na estrutura ou chamada iniciada nas linhas anteriores.
                # `n` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a n.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                n,

                # Executa `fs.get` com os argumentos informados para realizar a operação correspondente.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `rotulo` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
                # `label` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                fs.get("rotulo") or fs.get("label"),

                # Define o argumento nomeado `tipo_sql` da chamada iniciada nas linhas anteriores.
                # `tipo_sql` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo sql.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `tipo_sql` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
                # `sql_type` = texto literal utilizado nesta instrução.
                # `TEXT` = texto literal utilizado nesta instrução.
                # `upper` = função, método ou classe chamada para executar a operação relacionada a upper.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                tipo_sql=(fs.get("tipo_sql") or fs.get("sql_type") or "TEXT").upper(),

                # Define o argumento nomeado `widget` da chamada iniciada nas linhas anteriores.
                # `widget` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a widget.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `widget` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
                # `Entry` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                widget=fs.get("widget") or "Entry",

                # Define o argumento nomeado `obrigatorio` da chamada iniciada nas linhas anteriores.
                # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `obrigatorio` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
                # `required` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `False` = representa o valor lógico falso.
                obrigatorio=bool(fs.get("obrigatorio") or fs.get("required", False)),

                # Define o argumento nomeado `opcoes` da chamada iniciada nas linhas anteriores.
                # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `opcoes` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
                # `options` = texto literal utilizado nesta instrução.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                opcoes=fs.get("opcoes") or fs.get("options") or [],

                # Define o argumento nomeado `mascara` da chamada iniciada nas linhas anteriores.
                # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `mascara` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
                # `mask` = texto literal utilizado nesta instrução.
                # `Nenhuma` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                mascara=fs.get("mascara") or fs.get("mask") or "Nenhuma",

                # Define o argumento nomeado `validacao` da chamada iniciada nas linhas anteriores.
                # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `fs` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fs.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `validacao` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
                # `validation` = texto literal utilizado nesta instrução.
                # `Nenhuma` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                validacao=fs.get("validacao") or fs.get("validation") or "Nenhuma",

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            ))

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not campos:

            # Armazena ou associa em `campos` o valor ou resultado definido nesta linha.
            # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `_defs_modulo` = função, método ou classe chamada para executar a operação relacionada a defs modulo.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `descricao_original` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao original.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            campos = _defs_modulo(nome_tela, descricao_original)

        # Armazena ou associa em `tabela` o valor ou resultado definido nesta linha.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `_slug` = função, método ou classe chamada para executar a operação relacionada a slug.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `ts` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ts.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `tabela` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `table` = texto literal utilizado nesta instrução.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `i` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a i.
        # `+` = operador utilizado para realizar soma ou concatenação, conforme os valores envolvidos.
        # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        tabela = _slug(ts.get("tabela") or ts.get("table") or nome_tela, f"dados_{i+1}")

        # Armazena ou associa em `titulo` o valor ou resultado definido nesta linha.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `str` = função ou tipo utilizado para representar e converter valores para texto.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `ts` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a ts.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `titulo` = texto literal utilizado nesta instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
        # `title` = texto literal utilizado nesta instrução.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        titulo = str(ts.get("titulo") or ts.get("title") or nome_tela)

        # Executa `telas.append` com os argumentos informados para realizar a operação correspondente.
        # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `append` = função, método ou classe chamada para executar a operação relacionada a append.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `criar_tela_crud` = função, método ou classe chamada para executar a operação relacionada a criar tela crud.
        # `nome_tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome tela.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
        # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
        # `campos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos.
        # `incluir_menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a incluir menu.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `True` = representa o valor lógico verdadeiro.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        telas.append(criar_tela_crud(nome_tela, titulo, tabela, campos, incluir_menu=True))

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if not telas:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `_projeto_interpretador_local` = função, método ou classe chamada para executar a operação relacionada a projeto interpretador local.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `descricao_original` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao original.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return _projeto_interpretador_local(descricao_original)

    # Armazena ou associa em `login` o valor ou resultado definido nesta linha.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `login` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `>` = operador de comparação utilizado para verificar se o valor da esquerda é maior.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    login = bool(spec.get("login", len(telas) > 1))

    # Armazena ou associa em `menu` o valor ou resultado definido nesta linha.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `menu` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `>` = operador de comparação utilizado para verificar se o valor da esquerda é maior.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    menu = bool(spec.get("menu", len(telas) > 1))

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `login` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a login.
    # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
    # `menu` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a menu.
    # `len` = função que retorna a quantidade de elementos do objeto informado.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `>` = operador de comparação utilizado para verificar se o valor da esquerda é maior.
    # `1` = valor numérico um utilizado como unidade, incremento, índice ou valor lógico numérico, conforme o contexto desta linha.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if login or menu or len(telas) > 1:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `montar_projeto_com_fluxo` = função, método ou classe chamada para executar a operação relacionada a montar projeto com fluxo.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
        # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return montar_projeto_com_fluxo(nome, tema, telas)

    # Armazena ou associa em `telas[0].componentes` o valor ou resultado definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
    # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `nome` = atributo, método ou recurso acessado com o nome `nome`.
    # `not` = inverte o resultado lógico da expressão seguinte.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `btn_menu` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `btn_sair` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    telas[0].componentes = [c for c in telas[0].componentes if c.nome not in {"btn_menu", "btn_sair"}]

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `Projeto` = classe que representa um projeto criado no Gerador Visual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `id` = atributo, método ou recurso acessado com o nome `id`.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return Projeto(nome, tema, telas, telas[0].id)

# Define a rotina `_criar_com_ollama`, responsável por executar a lógica relacionada a criar com ollama.
# `def` = define uma nova função ou um novo método.
# `_criar_com_ollama` = função, método ou classe chamada para executar a operação relacionada a criar com ollama.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `modelo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
def _criar_com_ollama(descricao: str, modelo: str) -> Projeto:

    # Inicia ou fornece um texto de múltiplas linhas utilizado por esta instrução.
    # string de múltiplas linhas = mantém um conteúdo textual contínuo que deve permanecer intacto para o funcionamento desta instrução.
    prompt = f"""Você é um arquiteto de sistemas desktop Python/Tkinter/SQLite. Converta o pedido do usuário em uma especificação JSON para um gerador visual educacional.

REGRAS:
- Responda SOMENTE JSON válido.
- Quando houver mais de uma tela funcional, defina login=true e menu=true.
- Não inclua Login nem Menu dentro de "telas"; o gerador os criará automaticamente.
- Cada tela funcional deve ter campos suficientes para um CRUD útil.
- widget permitido: Entry, Text, Combobox, Spinbox, Checkbutton.
- tipo_sql permitido: TEXT, INTEGER, REAL, NUMERIC.
- mascara: Nenhuma, CPF, CNPJ, Telefone, CEP, Data, Moeda.
- validacao: Nenhuma, E-mail, Inteiro, Decimal, CPF, CNPJ, Telefone, CEP, Data.
- Use português nos nomes e rótulos.

FORMATO:
{{
  "nome": "Nome do sistema",
  "tema": "Azul corporativo",
  "login": true,
  "menu": true,
  "telas": [
    {{
      "nome": "Clientes",
      "titulo": "Cadastro de Clientes",
      "tabela": "clientes",
      "campos": [
        {{"nome":"nome","rotulo":"Nome","tipo_sql":"TEXT","widget":"Entry","obrigatorio":true,"opcoes":[],"mascara":"Nenhuma","validacao":"Nenhuma"}}
      ]
    }}
  ]
}}

PEDIDO DO USUÁRIO:
{descricao}
"""

    # Armazena ou associa em `payload` o valor ou resultado definido nesta linha.
    # `payload` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a payload.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `dumps` = função, método ou classe chamada para executar a operação relacionada a dumps.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `model` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `modelo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `prompt` = texto literal utilizado nesta instrução.
    # `prompt` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a prompt.
    # `stream` = texto literal utilizado nesta instrução.
    # `False` = representa o valor lógico falso.
    # `format` = texto literal utilizado nesta instrução.
    # `json` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `encode` = função, método ou classe chamada para executar a operação relacionada a encode.
    # `utf-8` = texto literal utilizado nesta instrução.
    payload = json.dumps({"model": modelo, "prompt": prompt, "stream": False, "format": "json"}).encode("utf-8")

    # Armazena ou associa em `req` o valor ou resultado definido nesta linha.
    # `req` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a req.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `urllib` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a urllib.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `request` = atributo, método ou recurso acessado com o nome `request`.
    # `Request` = função, método ou classe chamada para executar a operação relacionada a Request.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `http://127.0.0.1:11434/api/generate` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `data` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a data.
    # `payload` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a payload.
    # `headers` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a headers.
    # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
    # `Content-Type` = texto literal utilizado nesta instrução.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `application/json` = texto literal utilizado nesta instrução.
    # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
    # `method` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a method.
    # `POST` = texto literal utilizado nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=payload, headers={"Content-Type": "application/json"}, method="POST")

    # Abre um contexto controlado para utilizar o recurso indicado e finalizar seu gerenciamento automaticamente ao sair do bloco.
    # `with` = inicia um gerenciador de contexto para controlar automaticamente o recurso utilizado no bloco.
    # `urllib` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a urllib.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `request` = atributo, método ou recurso acessado com o nome `request`.
    # `urlopen` = função, método ou classe chamada para executar a operação relacionada a urlopen.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `req` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a req.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `timeout` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a timeout.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `120` = valor numérico associado a `timeout` nesta instrução.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
    # `resp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resp.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    with urllib.request.urlopen(req, timeout=120) as resp:

        # Armazena ou associa em `resposta` o valor ou resultado definido nesta linha.
        # `resposta` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resposta.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `loads` = função, método ou classe chamada para executar a operação relacionada a loads.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `resp` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resp.
        # `read` = função, método ou classe chamada para executar a operação relacionada a read.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `decode` = função, método ou classe chamada para executar a operação relacionada a decode.
        # `utf-8` = texto literal utilizado nesta instrução.
        resposta = json.loads(resp.read().decode("utf-8"))

    # Armazena ou associa em `conteudo` o valor ou resultado definido nesta linha.
    # `conteudo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conteudo.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `resposta` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resposta.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `get` = função, método ou classe chamada para executar a operação relacionada a get.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `response` = texto literal utilizado nesta instrução.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # texto vazio = representa uma string sem caracteres.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    conteudo = resposta.get("response", "")

    # Armazena ou associa em `spec` o valor ou resultado definido nesta linha.
    # `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `json` = módulo utilizado para converter dados entre objetos Python e o formato JSON.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `loads` = função, método ou classe chamada para executar a operação relacionada a loads.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `_limpar_json_resposta` = função, método ou classe chamada para executar a operação relacionada a limpar json resposta.
    # `conteudo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a conteudo.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    spec = json.loads(_limpar_json_resposta(conteudo))

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_de_especificacao` = função, método ou classe chamada para executar a operação relacionada a projeto de especificacao.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `spec` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a spec.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_de_especificacao(spec, descricao)

# Define a rotina `criar_projeto_inteligente`, responsável por executar a lógica relacionada a criar projeto inteligente.
# `def` = define uma nova função ou um novo método.
# `criar_projeto_inteligente` = função, método ou classe chamada para executar a operação relacionada a criar projeto inteligente.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `preferir_ollama` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a preferir ollama.
# `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
# `True` = representa o valor lógico verdadeiro.
# `modelo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo.
# texto vazio = representa uma string sem caracteres.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
def criar_projeto_inteligente(descricao: str, preferir_ollama=True, modelo=""):

    # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
    # `Retorna (Projeto, descrição_do_motor). Nunca depende de chave de API.` = texto literal utilizado nesta instrução.
    """Retorna (Projeto, descrição_do_motor). Nunca depende de chave de API."""

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `calculadora` = texto literal utilizado nesta instrução.
    # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
    # `_normalizar` = função, método ou classe chamada para executar a operação relacionada a normalizar.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if "calculadora" in _normalizar(descricao):

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `modelo_calculadora` = função, método ou classe chamada para executar a operação relacionada a modelo calculadora.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `Gerador funcional interno` = texto literal utilizado nesta instrução.
        return modelo_calculadora(), "Gerador funcional interno"

    # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
    # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
    # `preferir_ollama` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a preferir ollama.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    if preferir_ollama:

        # Armazena ou associa em `modelos` o valor ou resultado definido nesta linha.
        # `modelos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelos.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `listar_modelos_ollama` = função, método ou classe chamada para executar a operação relacionada a listar modelos ollama.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        modelos = listar_modelos_ollama()

        # Armazena ou associa em `escolhido` o valor ou resultado definido nesta linha.
        # `escolhido` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a escolhido.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `modelo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelo.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `modelos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modelos.
        # `else` = inicia o bloco executado quando as condições anteriores não forem atendidas.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # texto vazio = representa uma string sem caracteres.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        escolhido = modelo if modelo in modelos else (modelos[0] if modelos else "")

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `escolhido` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a escolhido.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if escolhido:

            # Inicia um bloco protegido para permitir o tratamento de possíveis erros durante sua execução.
            # `try` = inicia um bloco protegido para tratamento de possíveis exceções.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            try:

                # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
                # `return` = encerra a rotina atual e devolve o valor especificado.
                # `_criar_com_ollama` = função, método ou classe chamada para executar a operação relacionada a criar com ollama.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `escolhido` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a escolhido.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                return _criar_com_ollama(descricao, escolhido), f"IA local Ollama ({escolhido})"

            # Define o tratamento executado quando ocorre a exceção indicada durante o bloco protegido.
            # `except` = define o bloco executado quando ocorre a exceção indicada.
            # `Exception` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Exception.
            # `as` = define um nome alternativo para o recurso importado ou para o valor capturado no contexto.
            # `erro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a erro.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            except Exception as erro:

                # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
                # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `_projeto_interpretador_local` = função, método ou classe chamada para executar a operação relacionada a projeto interpretador local.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                projeto = _projeto_interpretador_local(descricao)

                # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
                # `return` = encerra a rotina atual e devolve o valor especificado.
                # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
                # `type` = função, método ou classe chamada para executar a operação relacionada a type.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `erro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a erro.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `__name__` = atributo, método ou recurso acessado com o nome `__name__`.
                # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
                return projeto, f"Interpretador local avançado (Ollama indisponível nesta tentativa: {type(erro).__name__})"

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_interpretador_local` = função, método ou classe chamada para executar a operação relacionada a projeto interpretador local.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Interpretador local avançado` = texto literal utilizado nesta instrução.
    return _projeto_interpretador_local(descricao), "Interpretador local avançado"

# Define a rotina `criar_projeto_por_descricao`, responsável por executar a lógica relacionada a criar projeto por descricao.
# `def` = define uma nova função ou um novo método.
# `criar_projeto_por_descricao` = função, método ou classe chamada para executar a operação relacionada a criar projeto por descricao.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
def criar_projeto_por_descricao(descricao: str) -> Projeto:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `_projeto_interpretador_local` = função, método ou classe chamada para executar a operação relacionada a projeto interpretador local.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `descricao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a descricao.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    return _projeto_interpretador_local(descricao)
