# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `__future__` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a future.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `annotations` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a annotations.
from __future__ import annotations

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `dataclasses` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dataclasses.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `asdict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a asdict.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `dataclass` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dataclass.
# `field` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a field.
# `fields` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fields.
from dataclasses import asdict, dataclass, field, fields

# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `typing` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a typing.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
# `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
# `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
# `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
from typing import Any, Dict, List

# Importa um ou mais módulos para disponibilizar seus recursos neste arquivo.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `uuid` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a uuid.
import uuid

# Define a rotina `_id_curto`, responsável por executar a lógica relacionada a id curto.
# `def` = define uma nova função ou um novo método.
# `_id_curto` = função, método ou classe chamada para executar a operação relacionada a id curto.
# `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
# `->` = indica a anotação do tipo de valor retornado pela função ou método.
# `str` = função ou tipo utilizado para representar e converter valores para texto.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
def _id_curto() -> str:

    # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
    # `return` = encerra a rotina atual e devolve o valor especificado.
    # `uuid` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a uuid.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `uuid4` = função, método ou classe chamada para executar a operação relacionada a uuid4.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `hex` = atributo, método ou recurso acessado com o nome `hex`.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `10` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    return uuid.uuid4().hex[:10]

# Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
# `@` = aplica um decorador à função ou classe definida logo abaixo.
# `dataclass` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dataclass.
@dataclass

# Define a classe `Componente`, responsável por agrupar dados e comportamentos relacionados a Componente.
# `class` = define uma nova classe.
# `Componente` = classe que representa um componente inserido no Designer Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
class Componente:

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    tipo: str

    # Declara `x` com anotação de tipo e armazena o valor definido nesta linha.
    # `x` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a x.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `20` = valor numérico associado a `int` nesta instrução.
    x: int = 20

    # Declara `y` com anotação de tipo e armazena o valor definido nesta linha.
    # `y` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a y.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `20` = valor numérico associado a `int` nesta instrução.
    y: int = 20

    # Declara `largura` com anotação de tipo e armazena o valor definido nesta linha.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `160` = valor numérico associado a `int` nesta instrução.
    largura: int = 160

    # Declara `altura` com anotação de tipo e armazena o valor definido nesta linha.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `34` = valor numérico associado a `int` nesta instrução.
    altura: int = 34

    # Declara `nome` com anotação de tipo e armazena o valor definido nesta linha.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    nome: str = ""

    # Declara `texto` com anotação de tipo e armazena o valor definido nesta linha.
    # `texto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a texto.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    texto: str = ""

    # Declara `opcoes` com anotação de tipo e armazena o valor definido nesta linha.
    # `opcoes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a opcoes.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `field` = função, método ou classe chamada para executar a operação relacionada a field.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `default_factory` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default factory.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    opcoes: List[str] = field(default_factory=list)

    # Declara `campo_banco` com anotação de tipo e armazena o valor definido nesta linha.
    # `campo_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo banco.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    campo_banco: str = ""

    # Declara `titulo_coluna` com anotação de tipo e armazena o valor definido nesta linha.
    # `titulo_coluna` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo coluna.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    titulo_coluna: str = ""

    # Declara `fonte` com anotação de tipo e armazena o valor definido nesta linha.
    # `fonte` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a fonte.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    fonte: str = ""

    # Declara `tamanho_fonte` com anotação de tipo e armazena o valor definido nesta linha.
    # `tamanho_fonte` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tamanho fonte.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `0` = valor numérico associado a `int` nesta instrução.
    tamanho_fonte: int = 0

    # Declara `negrito` com anotação de tipo e armazena o valor definido nesta linha.
    # `negrito` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a negrito.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    negrito: bool = False

    # Declara `italico` com anotação de tipo e armazena o valor definido nesta linha.
    # `italico` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a italico.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    italico: bool = False

    # Declara `sublinhado` com anotação de tipo e armazena o valor definido nesta linha.
    # `sublinhado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a sublinhado.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    sublinhado: bool = False

    # Declara `cor_texto` com anotação de tipo e armazena o valor definido nesta linha.
    # `cor_texto` = identificador utilizado para armazenar ou acessar a cor relacionada a cor texto.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    cor_texto: str = ""

    # Declara `cor_fundo` com anotação de tipo e armazena o valor definido nesta linha.
    # `cor_fundo` = identificador utilizado para armazenar ou acessar a cor relacionada a cor fundo.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    cor_fundo: str = ""

    # Declara `alinhamento` com anotação de tipo e armazena o valor definido nesta linha.
    # `alinhamento` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alinhamento.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Padrão` = texto literal utilizado nesta instrução.
    alinhamento: str = "Padrão"

    # Declara `campo_filtro` com anotação de tipo e armazena o valor definido nesta linha.
    # `campo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo filtro.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    campo_filtro: str = ""

    # Declara `alvo_filtro` com anotação de tipo e armazena o valor definido nesta linha.
    # `alvo_filtro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo filtro.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    alvo_filtro: str = ""

    # Declara `acao` com anotação de tipo e armazena o valor definido nesta linha.
    # `acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a acao.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Nenhuma` = texto literal utilizado nesta instrução.
    acao: str = "Nenhuma"

    # Declara `campos_acao` com anotação de tipo e armazena o valor definido nesta linha.
    # `campos_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos acao.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `field` = função, método ou classe chamada para executar a operação relacionada a field.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `default_factory` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default factory.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    campos_acao: List[str] = field(default_factory=list)

    # Declara `campo_resultado` com anotação de tipo e armazena o valor definido nesta linha.
    # `campo_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    campo_resultado: str = ""

    # Declara `campo_resultado_2` com anotação de tipo e armazena o valor definido nesta linha.
    # `campo_resultado_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campo resultado 2.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    campo_resultado_2: str = ""

    # Declara `operador` com anotação de tipo e armazena o valor definido nesta linha.
    # `operador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a operador.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    operador: str = ""

    # Declara `expressao` com anotação de tipo e armazena o valor definido nesta linha.
    # `expressao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    expressao: str = ""

    # Declara `expressao_2` com anotação de tipo e armazena o valor definido nesta linha.
    # `expressao_2` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a expressao 2.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    expressao_2: str = ""

    # Declara `comparador` com anotação de tipo e armazena o valor definido nesta linha.
    # `comparador` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a comparador.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    comparador: str = ""

    # Declara `valor_acao` com anotação de tipo e armazena o valor definido nesta linha.
    # `valor_acao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a valor acao.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    valor_acao: str = ""

    # Declara `resultado_verdadeiro` com anotação de tipo e armazena o valor definido nesta linha.
    # `resultado_verdadeiro` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado verdadeiro.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    resultado_verdadeiro: str = ""

    # Declara `resultado_falso` com anotação de tipo e armazena o valor definido nesta linha.
    # `resultado_falso` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a resultado falso.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    resultado_falso: str = ""

    # Declara `modo_insercao` com anotação de tipo e armazena o valor definido nesta linha.
    # `modo_insercao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a modo insercao.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Adicionar` = texto literal utilizado nesta instrução.
    modo_insercao: str = "Adicionar"

    # Declara `repeticao_inicio` com anotação de tipo e armazena o valor definido nesta linha.
    # `repeticao_inicio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a repeticao inicio.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `1` = texto literal utilizado nesta instrução.
    repeticao_inicio: str = "1"

    # Declara `repeticao_fim` com anotação de tipo e armazena o valor definido nesta linha.
    # `repeticao_fim` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a repeticao fim.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `10` = texto literal utilizado nesta instrução.
    repeticao_fim: str = "10"

    # Declara `formato_resultado` com anotação de tipo e armazena o valor definido nesta linha.
    # `formato_resultado` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a formato resultado.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    formato_resultado: str = ""

    # Declara `alvo_auxiliar` com anotação de tipo e armazena o valor definido nesta linha.
    # `alvo_auxiliar` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a alvo auxiliar.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    alvo_auxiliar: str = ""

    # Declara `tela_destino` com anotação de tipo e armazena o valor definido nesta linha.
    # `tela_destino` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela destino.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    tela_destino: str = ""

    # Declara `mensagem` com anotação de tipo e armazena o valor definido nesta linha.
    # `mensagem` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mensagem.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    mensagem: str = ""

    # Declara `mascara` com anotação de tipo e armazena o valor definido nesta linha.
    # `mascara` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a mascara.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Nenhuma` = texto literal utilizado nesta instrução.
    mascara: str = "Nenhuma"

    # Declara `validacao` com anotação de tipo e armazena o valor definido nesta linha.
    # `validacao` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a validacao.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Nenhuma` = texto literal utilizado nesta instrução.
    validacao: str = "Nenhuma"

    # Declara `obrigatorio` com anotação de tipo e armazena o valor definido nesta linha.
    # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    obrigatorio: bool = False

    # Declara `id` com anotação de tipo e armazena o valor definido nesta linha.
    # `id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a id.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `field` = função, método ou classe chamada para executar a operação relacionada a field.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `default_factory` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default factory.
    # `_id_curto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a id curto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    id: str = field(default_factory=_id_curto)

    # Define a rotina `para_dict`, responsável por executar a lógica relacionada a para dict.
    # `def` = define uma nova função ou um novo método.
    # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def para_dict(self) -> Dict[str, Any]:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `asdict` = função, método ou classe chamada para executar a operação relacionada a asdict.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return asdict(self)

    # Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
    # `@` = aplica um decorador à função ou classe definida logo abaixo.
    # `classmethod` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a classmethod.
    @classmethod

    # Define a rotina `de_dict`, responsável por executar a lógica relacionada a de dict.
    # `def` = define uma nova função ou um novo método.
    # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `cls` = representa a própria classe dentro de um método de classe.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Componente` = texto literal utilizado nesta instrução.
    def de_dict(cls, dados: Dict[str, Any]) -> "Componente":

        # Armazena ou associa em `permitidos` o valor ou resultado definido nesta linha.
        # `permitidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a permitidos.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `f` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a f.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `name` = atributo, método ou recurso acessado com o nome `name`.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `fields` = função, método ou classe chamada para executar a operação relacionada a fields.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `cls` = representa a própria classe dentro de um método de classe.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        permitidos = {f.name for f in fields(cls)}

        # Armazena ou associa em `filtrados` o valor ou resultado definido nesta linha.
        # `filtrados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a filtrados.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `valor` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a valor.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `items` = função, método ou classe chamada para executar a operação relacionada a items.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `permitidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a permitidos.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        filtrados = {chave: valor for chave, valor in dados.items() if chave in permitidos}

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `cls` = representa a própria classe dentro de um método de classe.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `**` = operador utilizado para realizar potenciação.
        # `filtrados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a filtrados.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return cls(**filtrados)

# Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
# `@` = aplica um decorador à função ou classe definida logo abaixo.
# `dataclass` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dataclass.
@dataclass

# Define a classe `CampoBanco`, responsável por agrupar dados e comportamentos relacionados a CampoBanco.
# `class` = define uma nova classe.
# `CampoBanco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a CampoBanco.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
class CampoBanco:

    # Executa a instrução desta linha como parte da lógica atual do programa.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    nome: str

    # Declara `tipo` com anotação de tipo e armazena o valor definido nesta linha.
    # `tipo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tipo.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `TEXT` = texto literal utilizado nesta instrução.
    tipo: str = "TEXT"

    # Declara `obrigatorio` com anotação de tipo e armazena o valor definido nesta linha.
    # `obrigatorio` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a obrigatorio.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    obrigatorio: bool = False

    # Declara `chave_primaria` com anotação de tipo e armazena o valor definido nesta linha.
    # `chave_primaria` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave primaria.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    chave_primaria: bool = False

    # Define a rotina `para_dict`, responsável por executar a lógica relacionada a para dict.
    # `def` = define uma nova função ou um novo método.
    # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def para_dict(self) -> Dict[str, Any]:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `asdict` = função, método ou classe chamada para executar a operação relacionada a asdict.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return asdict(self)

    # Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
    # `@` = aplica um decorador à função ou classe definida logo abaixo.
    # `classmethod` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a classmethod.
    @classmethod

    # Define a rotina `de_dict`, responsável por executar a lógica relacionada a de dict.
    # `def` = define uma nova função ou um novo método.
    # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `cls` = representa a própria classe dentro de um método de classe.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `CampoBanco` = texto literal utilizado nesta instrução.
    def de_dict(cls, dados: Dict[str, Any]) -> "CampoBanco":

        # Armazena ou associa em `permitidos` o valor ou resultado definido nesta linha.
        # `permitidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a permitidos.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `f` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a f.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `name` = atributo, método ou recurso acessado com o nome `name`.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `fields` = função, método ou classe chamada para executar a operação relacionada a fields.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `cls` = representa a própria classe dentro de um método de classe.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        permitidos = {f.name for f in fields(cls)}

        # Armazena ou associa em `filtrados` o valor ou resultado definido nesta linha.
        # `filtrados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a filtrados.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `{` = abre um dicionário, conjunto ou estrutura de compreensão.
        # `chave` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a chave.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        # `valor` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a valor.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `items` = função, método ou classe chamada para executar a operação relacionada a items.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `permitidos` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a permitidos.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        filtrados = {chave: valor for chave, valor in dados.items() if chave in permitidos}

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `cls` = representa a própria classe dentro de um método de classe.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `**` = operador utilizado para realizar potenciação.
        # `filtrados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a filtrados.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return cls(**filtrados)

# Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
# `@` = aplica um decorador à função ou classe definida logo abaixo.
# `dataclass` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dataclass.
@dataclass

# Define a classe `Tela`, responsável por agrupar dados e comportamentos relacionados a Tela.
# `class` = define uma nova classe.
# `Tela` = classe que representa uma tela do projeto visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
class Tela:

    # Declara `nome` com anotação de tipo e armazena o valor definido nesta linha.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Tela Principal` = texto literal utilizado nesta instrução.
    nome: str = "Tela Principal"

    # Declara `titulo` com anotação de tipo e armazena o valor definido nesta linha.
    # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Meu Sistema` = texto literal utilizado nesta instrução.
    titulo: str = "Meu Sistema"

    # Declara `largura` com anotação de tipo e armazena o valor definido nesta linha.
    # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `1000` = valor numérico associado a `int` nesta instrução.
    largura: int = 1000

    # Declara `altura` com anotação de tipo e armazena o valor definido nesta linha.
    # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `650` = valor numérico associado a `int` nesta instrução.
    altura: int = 650

    # Declara `tabela` com anotação de tipo e armazena o valor definido nesta linha.
    # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `registros` = texto literal utilizado nesta instrução.
    tabela: str = "registros"

    # Declara `componentes` com anotação de tipo e armazena o valor definido nesta linha.
    # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `Componente` = classe que representa um componente inserido no Designer Visual.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `field` = função, método ou classe chamada para executar a operação relacionada a field.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `default_factory` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default factory.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    componentes: List[Componente] = field(default_factory=list)

    # Declara `campos_banco` com anotação de tipo e armazena o valor definido nesta linha.
    # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `CampoBanco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a CampoBanco.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `field` = função, método ou classe chamada para executar a operação relacionada a field.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `default_factory` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default factory.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    campos_banco: List[CampoBanco] = field(default_factory=list)

    # Declara `id` com anotação de tipo e armazena o valor definido nesta linha.
    # `id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a id.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `field` = função, método ou classe chamada para executar a operação relacionada a field.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `default_factory` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default factory.
    # `_id_curto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a id curto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    id: str = field(default_factory=_id_curto)

    # Define a rotina `para_dict`, responsável por executar a lógica relacionada a para dict.
    # `def` = define uma nova função ou um novo método.
    # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def para_dict(self) -> Dict[str, Any]:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        return {

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `nome` = atributo, método ou recurso acessado com o nome `nome`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "nome": self.nome,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `titulo` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `titulo` = atributo, método ou recurso acessado com o nome `titulo`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "titulo": self.titulo,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `largura` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `largura` = atributo, método ou recurso acessado com o nome `largura`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "largura": self.largura,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `altura` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `altura` = atributo, método ou recurso acessado com o nome `altura`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "altura": self.altura,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `tabela` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `tabela` = atributo, método ou recurso acessado com o nome `tabela`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "tabela": self.tabela,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `componentes` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "componentes": [c.para_dict() for c in self.componentes],

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `campos_banco` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `c` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a c.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "campos_banco": [c.para_dict() for c in self.campos_banco],

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `id` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `id` = atributo, método ou recurso acessado com o nome `id`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "id": self.id,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        }

    # Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
    # `@` = aplica um decorador à função ou classe definida logo abaixo.
    # `classmethod` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a classmethod.
    @classmethod

    # Define a rotina `de_dict`, responsável por executar a lógica relacionada a de dict.
    # `def` = define uma nova função ou um novo método.
    # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `cls` = representa a própria classe dentro de um método de classe.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Tela` = texto literal utilizado nesta instrução.
    def de_dict(cls, dados: Dict[str, Any]) -> "Tela":

        # Armazena ou associa em `tela` o valor ou resultado definido nesta linha.
        tela = cls(

            # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `nome` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Tela Principal` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            nome=dados.get("nome", "Tela Principal"),

            # Define o argumento nomeado `titulo` da chamada iniciada nas linhas anteriores.
            # `titulo` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a titulo.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `titulo` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `titulo_janela` = texto literal utilizado nesta instrução.
            # `Meu Sistema` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            titulo=dados.get("titulo", dados.get("titulo_janela", "Meu Sistema")),

            # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
            # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `largura` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `largura_janela` = texto literal utilizado nesta instrução.
            # `1000` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            largura=int(dados.get("largura", dados.get("largura_janela", 1000))),

            # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
            # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `altura` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `altura_janela` = texto literal utilizado nesta instrução.
            # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            altura=int(dados.get("altura", dados.get("altura_janela", 650))),

            # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
            # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tabela` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `registros` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            tabela=dados.get("tabela", "registros"),

            # Define o argumento nomeado `id` da chamada iniciada nas linhas anteriores.
            # `id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a id.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `id` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `or` = operador lógico OU, que aceita que pelo menos uma das condições seja verdadeira.
            # `_id_curto` = função, método ou classe chamada para executar a operação relacionada a id curto.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            id=dados.get("id") or _id_curto(),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Armazena ou associa em `tela.componentes` o valor ou resultado definido nesta linha.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `componentes` = atributo, método ou recurso acessado com o nome `componentes`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `Componente` = classe que representa um componente inserido no Designer Visual.
        # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `componentes` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        tela.componentes = [Componente.de_dict(item) for item in dados.get("componentes", [])]

        # Armazena ou associa em `tela.campos_banco` o valor ou resultado definido nesta linha.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `campos_banco` = atributo, método ou recurso acessado com o nome `campos_banco`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `CampoBanco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a CampoBanco.
        # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
        # `get` = função, método ou classe chamada para executar a operação relacionada a get.
        # `campos_banco` = texto literal utilizado nesta instrução.
        # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        tela.campos_banco = [CampoBanco.de_dict(item) for item in dados.get("campos_banco", [])]

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        return tela

# Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
# `@` = aplica um decorador à função ou classe definida logo abaixo.
# `dataclass` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dataclass.
@dataclass

# Define a classe `Projeto`, responsável por agrupar dados e comportamentos relacionados a Projeto.
# `class` = define uma nova classe.
# `Projeto` = classe que representa um projeto criado no Gerador Visual.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
class Projeto:

    # Declara `nome` com anotação de tipo e armazena o valor definido nesta linha.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Novo Projeto` = texto literal utilizado nesta instrução.
    nome: str = "Novo Projeto"

    # Declara `tema` com anotação de tipo e armazena o valor definido nesta linha.
    # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `Claro` = texto literal utilizado nesta instrução.
    tema: str = "Claro"

    # Declara `telas` com anotação de tipo e armazena o valor definido nesta linha.
    # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `List` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a List.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `Tela` = classe que representa uma tela do projeto visual.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `field` = função, método ou classe chamada para executar a operação relacionada a field.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `default_factory` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a default factory.
    # `list` = função ou tipo utilizado para criar ou representar uma lista.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    telas: List[Tela] = field(default_factory=list)

    # Declara `tela_ativa_id` com anotação de tipo e armazena o valor definido nesta linha.
    # `tela_ativa_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela ativa id.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # texto vazio = representa uma string sem caracteres.
    tela_ativa_id: str = ""

    # Declara `exibir_aba_dados` com anotação de tipo e armazena o valor definido nesta linha.
    # `exibir_aba_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir aba dados.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `False` = representa o valor lógico falso.
    exibir_aba_dados: bool = False

    # Declara `projeto_id` com anotação de tipo e armazena o valor definido nesta linha.
    # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
    # `|` = combina alternativas, inclusive tipos aceitos em uma anotação.
    # `None` = representa ausência de valor.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    projeto_id: int | None = None

    # Define a rotina `garantir_tela`, responsável por executar a lógica relacionada a garantir tela.
    # `def` = define uma nova função ou um novo método.
    # `garantir_tela` = função, método ou classe chamada para executar a operação relacionada a garantir tela.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Tela` = classe que representa uma tela do projeto visual.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def garantir_tela(self) -> Tela:

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `telas` = atributo, método ou recurso acessado com o nome `telas`.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if not self.telas:

            # Executa `self.telas.append` com os argumentos informados para realizar a operação correspondente.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `telas` = atributo, método ou recurso acessado com o nome `telas`.
            # `append` = função, método ou classe chamada para executar a operação relacionada a append.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `Tela` = classe que representa uma tela do projeto visual.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            self.telas.append(Tela())

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `telas` = atributo, método ou recurso acessado com o nome `telas`.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for tela in self.telas:

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `id` = atributo, método ou recurso acessado com o nome `id`.
            # `==` = operador de comparação utilizado para verificar se os valores são iguais.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `tela_ativa_id` = atributo, método ou recurso acessado com o nome `tela_ativa_id`.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if tela.id == self.tela_ativa_id:

                # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
                # `return` = encerra a rotina atual e devolve o valor especificado.
                # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
                return tela

        # Armazena ou associa em `self.tela_ativa_id` o valor ou resultado definido nesta linha.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `tela_ativa_id` = atributo, método ou recurso acessado com o nome `tela_ativa_id`.
        # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
        # `telas` = atributo, método ou recurso acessado com o nome `telas`.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        # `id` = atributo, método ou recurso acessado com o nome `id`.
        self.tela_ativa_id = self.telas[0].id

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `telas` = atributo, método ou recurso acessado com o nome `telas`.
        # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
        # `0` = valor numérico zero utilizado como valor inicial, índice, limite ou ausência de quantidade, conforme o contexto desta linha.
        # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
        return self.telas[0]

    # Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
    # `@` = aplica um decorador à função ou classe definida logo abaixo.
    # `property` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a property.
    @property

    # Define a rotina `tela_ativa`, responsável por executar a lógica relacionada a tela ativa.
    # `def` = define uma nova função ou um novo método.
    # `tela_ativa` = função, método ou classe chamada para executar a operação relacionada a tela ativa.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Tela` = classe que representa uma tela do projeto visual.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def tela_ativa(self) -> Tela:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `garantir_tela` = função, método ou classe chamada para executar a operação relacionada a garantir tela.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        return self.garantir_tela()

    # Define a rotina `definir_tela_ativa_por_nome`, responsável por executar a lógica relacionada a definir tela ativa por nome.
    # `def` = define uma nova função ou um novo método.
    # `definir_tela_ativa_por_nome` = função, método ou classe chamada para executar a operação relacionada a definir tela ativa por nome.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
    def definir_tela_ativa_por_nome(self, nome: str) -> bool:

        # Percorre os elementos da sequência indicada e executa o bloco para cada item encontrado.
        # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
        # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `telas` = atributo, método ou recurso acessado com o nome `telas`.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        for tela in self.telas:

            # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
            # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
            # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `nome` = atributo, método ou recurso acessado com o nome `nome`.
            # `==` = operador de comparação utilizado para verificar se os valores são iguais.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            if tela.nome == nome:

                # Armazena ou associa em `self.tela_ativa_id` o valor ou resultado definido nesta linha.
                # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `tela_ativa_id` = atributo, método ou recurso acessado com o nome `tela_ativa_id`.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `tela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela.
                # `id` = atributo, método ou recurso acessado com o nome `id`.
                self.tela_ativa_id = tela.id

                # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
                # `return` = encerra a rotina atual e devolve o valor especificado.
                # `True` = representa o valor lógico verdadeiro.
                return True

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `False` = representa o valor lógico falso.
        return False

    # Define a rotina `para_dict`, responsável por executar a lógica relacionada a para dict.
    # `def` = define uma nova função ou um novo método.
    # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    def para_dict(self) -> Dict[str, Any]:

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        return {

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `nome` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `nome` = atributo, método ou recurso acessado com o nome `nome`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "nome": self.nome,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `tema` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `tema` = atributo, método ou recurso acessado com o nome `tema`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "tema": self.tema,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `telas` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `t` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a t.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `para_dict` = função, método ou classe chamada para executar a operação relacionada a para dict.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `telas` = atributo, método ou recurso acessado com o nome `telas`.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "telas": [t.para_dict() for t in self.telas],

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `tela_ativa_id` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `tela_ativa_id` = atributo, método ou recurso acessado com o nome `tela_ativa_id`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "tela_ativa_id": self.tela_ativa_id,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `exibir_aba_dados` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `exibir_aba_dados` = atributo, método ou recurso acessado com o nome `exibir_aba_dados`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "exibir_aba_dados": self.exibir_aba_dados,

            # Fornece o texto literal utilizado como argumento, valor ou conteúdo da instrução iniciada nas linhas anteriores.
            # `projeto_id` = texto literal utilizado nesta instrução.
            # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
            # `self` = representa a própria instância da classe e permite acessar seus atributos e métodos.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `projeto_id` = atributo, método ou recurso acessado com o nome `projeto_id`.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            "projeto_id": self.projeto_id,

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `}` = fecha o dicionário, conjunto ou estrutura de compreensão.
        }

    # Aplica um decorador para configurar o comportamento da função ou classe definida logo abaixo.
    # `@` = aplica um decorador à função ou classe definida logo abaixo.
    # `classmethod` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a classmethod.
    @classmethod

    # Define a rotina `de_dict`, responsável por executar a lógica relacionada a de dict.
    # `def` = define uma nova função ou um novo método.
    # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `cls` = representa a própria classe dentro de um método de classe.
    # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
    # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
    # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
    # `Dict` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Dict.
    # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
    # `str` = função ou tipo utilizado para representar e converter valores para texto.
    # `Any` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a Any.
    # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `->` = indica a anotação do tipo de valor retornado pela função ou método.
    # `Projeto` = texto literal utilizado nesta instrução.
    def de_dict(cls, dados: Dict[str, Any]) -> "Projeto":

        # Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
        # `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
        # `telas` = texto literal utilizado nesta instrução.
        # `not` = inverte o resultado lógico da expressão seguinte.
        # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
        # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
        # `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
        if "telas" not in dados:

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
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `titulo_janela` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Meu Sistema` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                titulo=dados.get("titulo_janela", "Meu Sistema"),

                # Define o argumento nomeado `largura` da chamada iniciada nas linhas anteriores.
                # `largura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a largura.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `largura_janela` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `1000` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                largura=int(dados.get("largura_janela", 1000)),

                # Define o argumento nomeado `altura` da chamada iniciada nas linhas anteriores.
                # `altura` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a altura.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `int` = função ou tipo utilizado para representar e converter valores para números inteiros.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `altura_janela` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `650` = valor numérico utilizado nesta linha para configurar, comparar, calcular ou representar a quantidade correspondente.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                altura=int(dados.get("altura_janela", 650)),

                # Define o argumento nomeado `tabela` da chamada iniciada nas linhas anteriores.
                # `tabela` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tabela.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `tabela` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `registros` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                tabela=dados.get("tabela", "registros"),

                # Define o argumento nomeado `componentes` da chamada iniciada nas linhas anteriores.
                # `componentes` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a componentes.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `Componente` = classe que representa um componente inserido no Designer Visual.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
                # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `componentes` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                componentes=[Componente.de_dict(item) for item in dados.get("componentes", [])],

                # Define o argumento nomeado `campos_banco` da chamada iniciada nas linhas anteriores.
                # `campos_banco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a campos banco.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
                # `CampoBanco` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a CampoBanco.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
                # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `campos_banco` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
                campos_banco=[CampoBanco.de_dict(item) for item in dados.get("campos_banco", [])],

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            )

            # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
            projeto = cls(

                # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
                # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `nome` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Projeto importado` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                nome=dados.get("nome", "Projeto importado"),

                # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
                # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `tema` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `Claro` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                tema=dados.get("tema", "Claro"),

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
                # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `exibir_aba_dados` = texto literal utilizado nesta instrução.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                # `True` = representa o valor lógico verdadeiro.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                exibir_aba_dados=bool(dados.get("exibir_aba_dados", True)),

                # Define o argumento nomeado `projeto_id` da chamada iniciada nas linhas anteriores.
                # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
                # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
                # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
                # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
                # `get` = função, método ou classe chamada para executar a operação relacionada a get.
                # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `projeto_id` = texto literal utilizado nesta instrução.
                # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
                # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
                projeto_id=dados.get("projeto_id"),

            # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            )

            # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
            # `return` = encerra a rotina atual e devolve o valor especificado.
            # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
            return projeto

        # Armazena ou associa em `projeto` o valor ou resultado definido nesta linha.
        projeto = cls(

            # Define o argumento nomeado `nome` da chamada iniciada nas linhas anteriores.
            # `nome` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a nome.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `nome` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Novo Projeto` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            nome=dados.get("nome", "Novo Projeto"),

            # Define o argumento nomeado `tema` da chamada iniciada nas linhas anteriores.
            # `tema` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tema.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tema` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `Claro` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            tema=dados.get("tema", "Claro"),

            # Define o argumento nomeado `telas` da chamada iniciada nas linhas anteriores.
            # `telas` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a telas.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `[` = abre uma lista, índice, acesso a elemento ou compreensão.
            # `Tela` = classe que representa uma tela do projeto visual.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `de_dict` = função, método ou classe chamada para executar a operação relacionada a de dict.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `item` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a item.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `for` = inicia uma repetição que percorre os elementos de uma sequência ou iterável.
            # `in` = verifica pertinência ou indica a sequência percorrida, conforme o contexto.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `telas` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `]` = fecha a lista, índice, acesso a elemento ou compreensão.
            telas=[Tela.de_dict(item) for item in dados.get("telas", [])],

            # Define o argumento nomeado `tela_ativa_id` da chamada iniciada nas linhas anteriores.
            # `tela_ativa_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a tela ativa id.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `tela_ativa_id` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # texto vazio = representa uma string sem caracteres.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            tela_ativa_id=dados.get("tela_ativa_id", ""),

            # Define o argumento nomeado `exibir_aba_dados` da chamada iniciada nas linhas anteriores.
            # `exibir_aba_dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a exibir aba dados.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `bool` = tipo lógico que representa os valores verdadeiro ou falso.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `exibir_aba_dados` = texto literal utilizado nesta instrução.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            # `True` = representa o valor lógico verdadeiro.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            exibir_aba_dados=bool(dados.get("exibir_aba_dados", True)),

            # Define o argumento nomeado `projeto_id` da chamada iniciada nas linhas anteriores.
            # `projeto_id` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto id.
            # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
            # `dados` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a dados.
            # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
            # `get` = função, método ou classe chamada para executar a operação relacionada a get.
            # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `projeto_id` = texto literal utilizado nesta instrução.
            # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
            # `,` = separa argumentos, parâmetros, propriedades ou elementos desta estrutura.
            projeto_id=dados.get("projeto_id"),

        # Fecha a estrutura iniciada nas linhas anteriores e conclui esta parte da instrução.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        )

        # Executa `projeto.garantir_tela` com os argumentos informados para realizar a operação correspondente.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
        # `garantir_tela` = função, método ou classe chamada para executar a operação relacionada a garantir tela.
        # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
        projeto.garantir_tela()

        # Retorna o resultado desta linha para o ponto do programa que chamou a rotina atual.
        # `return` = encerra a rotina atual e devolve o valor especificado.
        # `projeto` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a projeto.
        return projeto
