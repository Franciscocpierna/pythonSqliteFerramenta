# Importa recursos específicos de um módulo ou pacote para utilização neste arquivo.
# `from` = indica o módulo ou pacote de onde os recursos serão importados.
# `app` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a app.
# `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
# `interface` = atributo, método ou recurso acessado com o nome `interface`.
# `import` = importa um módulo ou recurso para que possa ser utilizado neste arquivo.
# `AplicativoGeradorVisual` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a AplicativoGeradorVisual.
from app.interface import AplicativoGeradorVisual

# Verifica a condição informada e executa o bloco seguinte somente quando ela for verdadeira.
# `if` = inicia uma estrutura condicional executada quando a condição for verdadeira.
# `__name__` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a name.
# `==` = operador de comparação utilizado para verificar se os valores são iguais.
# `__main__` = texto literal utilizado nesta instrução.
# `:` = separa partes da instrução e, conforme o contexto, marca anotação de tipo, chave e valor ou início de bloco.
if __name__ == "__main__":

    # Armazena ou associa em `app` o valor ou resultado definido nesta linha.
    # `app` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a app.
    # `=` = operador de atribuição utilizado para armazenar ou associar o valor da direita ao elemento da esquerda.
    # `AplicativoGeradorVisual` = função, método ou classe chamada para executar a operação relacionada a AplicativoGeradorVisual.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    app = AplicativoGeradorVisual()

    # Executa `app.mainloop` com os argumentos informados para realizar a operação correspondente.
    # `app` = identificador utilizado nesta linha para representar ou acessar o valor relacionado a app.
    # `.` = acessa um atributo, método ou recurso pertencente ao objeto indicado antes do ponto.
    # `mainloop` = função, método ou classe chamada para executar a operação relacionada a mainloop.
    # `(` = abre a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    # `)` = fecha a lista de argumentos, parâmetros, condição ou agrupamento correspondente.
    app.mainloop()
