from __future__ import annotations

from .acoes_genericas import normalizar_projeto
from .modelos import Componente, Projeto, Tela


def _label(x, y, texto, nome, largura=220, altura=28, **kwargs):
    return Componente(
        tipo="Label", x=x, y=y, largura=largura, altura=altura,
        nome=nome, texto=texto, **kwargs,
    )


def _campo(nome, rotulo, x, y, largura=260, tipo="Entry", opcoes=None,
           campo_banco="", mascara="Nenhuma", validacao="Nenhuma",
           obrigatorio=False, altura=None, **kwargs):
    if altura is None:
        altura = 120 if tipo in {"Text", "ScrolledText"} else 34
    return Componente(
        tipo=tipo, x=x, y=y, largura=largura, altura=altura,
        nome=nome, texto="", opcoes=list(opcoes or []),
        campo_banco=campo_banco, titulo_coluna=rotulo,
        mascara=mascara, validacao=validacao, obrigatorio=obrigatorio,
        **kwargs,
    )


def _botao(nome, texto, x, y, largura=180, acao="Nenhuma", **kwargs):
    return Componente(
        tipo="Button", x=x, y=y, largura=largura, altura=40,
        nome=nome, texto=texto, acao=acao, **kwargs,
    )


def _projeto(nome, componentes, tabela="dados", altura=680, tema="Claro", exibir_dados=False):
    tela = Tela(
        nome="Tela Principal", titulo=nome, largura=1000, altura=altura,
        tabela=tabela, componentes=componentes, campos_banco=[],
    )
    projeto = Projeto(
        nome=nome, tema=tema, telas=[tela], tela_ativa_id=tela.id,
        exibir_aba_dados=exibir_dados,
    )
    return normalizar_projeto(projeto, adicionar_botao_cadastro=False)


def projeto_31_cronometro():
    componentes = [
        _label(300, 35, "Cronômetro", "titulo", 400, 44),
        _label(235, 125, "Tempo decorrido", "lbl_tempo", 180),
        _campo("tempo_cronometro", "Tempo", 420, 118, 330, campo_banco=""),
        _botao("btn_iniciar", "Iniciar", 235, 190, 160,
               acao="Cronômetro: iniciar", campo_resultado="tempo_cronometro"),
        _botao("btn_pausar", "Pausar", 410, 190, 160,
               acao="Cronômetro: pausar", campo_resultado="tempo_cronometro"),
        _botao("btn_zerar", "Zerar", 585, 190, 165,
               acao="Cronômetro: zerar", campo_resultado="tempo_cronometro"),
        _label(235, 270, "O cronômetro mostra horas, minutos, segundos e décimos.",
               "lbl_instrucao", 520),
    ]
    return _projeto("Cronômetro", componentes, tabela="cronometro")


def projeto_32_temporizador():
    componentes = [
        _label(300, 35, "Temporizador", "titulo", 400, 44),
        _label(220, 120, "Segundos", "lbl_segundos", 160),
        _campo("segundos", "Segundos", 390, 113, 180, tipo="Spinbox", campo_banco=""),
        _label(220, 175, "Tempo restante", "lbl_restante", 160),
        _campo("tempo_restante", "Tempo restante", 390, 168, 360, campo_banco=""),
        _botao("btn_iniciar", "Iniciar", 220, 235, 165,
               acao="Temporizador: iniciar", campos_acao=["segundos"],
               campo_resultado="tempo_restante"),
        _botao("btn_pausar", "Pausar", 400, 235, 165,
               acao="Temporizador: pausar", campo_resultado="tempo_restante"),
        _botao("btn_zerar", "Zerar", 580, 235, 170,
               acao="Temporizador: zerar", campo_resultado="tempo_restante"),
    ]
    return _projeto("Temporizador", componentes, tabela="temporizador")


def projeto_33_gerador_senhas():
    componentes = [
        _label(250, 35, "Gerador de Senhas Seguras", "titulo", 520, 44),
        _label(190, 120, "Quantidade de caracteres", "lbl_tamanho", 210),
        _campo("tamanho_senha", "Tamanho", 410, 113, 160, tipo="Spinbox", campo_banco=""),
        Componente(tipo="Checkbutton", x=590, y=113, largura=220, altura=34,
                   nome="usar_simbolos", texto="Incluir símbolos", campo_banco=""),
        _label(190, 185, "Senha gerada", "lbl_senha", 210),
        _campo("senha_gerada", "Senha gerada", 410, 178, 400, campo_banco=""),
        _botao("btn_gerar", "Gerar senha segura", 410, 240, 400,
               acao="Gerar senha segura", campos_acao=["tamanho_senha", "usar_simbolos"],
               campo_resultado="senha_gerada"),
    ]
    return _projeto("Gerador de Senhas Seguras", componentes, tabela="senhas")


def projeto_34_idade_completa():
    componentes = [
        _label(250, 35, "Calculadora de Idade Completa", "titulo", 520, 44),
        _label(180, 125, "Data de nascimento", "lbl_nascimento", 220),
        _campo("data_nascimento", "Data de nascimento", 410, 118, 390,
               tipo="DateEntry", campo_banco="", mascara="Data", validacao="Data"),
        _label(180, 190, "Idade completa", "lbl_idade", 220),
        _campo("idade_completa", "Idade completa", 410, 183, 390, campo_banco=""),
        _botao("btn_calcular", "Calcular idade", 410, 248, 390,
               acao="Calcular idade completa", campos_acao=["data_nascimento"],
               campo_resultado="idade_completa"),
    ]
    return _projeto("Calculadora de Idade Completa", componentes, tabela="idade")


def projeto_35_sorteador_nomes():
    nomes = ["Ana", "Bruno", "Carla", "Diego", "Elaine", "Fabio", "Gabriela", "Henrique"]
    componentes = [
        _label(280, 30, "Sorteador de Nomes", "titulo", 450, 44),
        _label(130, 105, "Nomes disponíveis", "lbl_lista", 220),
        Componente(tipo="Listbox", x=130, y=140, largura=360, altura=300,
                   nome="lista_nomes", texto="", opcoes=nomes),
        _label(545, 105, "Nome sorteado", "lbl_resultado", 220),
        _campo("nome_sorteado", "Nome sorteado", 545, 140, 320, campo_banco=""),
        _botao("btn_sortear", "Sortear nome", 545, 200, 320,
               acao="Sortear nome", campos_acao=["lista_nomes"],
               campo_resultado="nome_sorteado"),
    ]
    return _projeto("Sorteador de Nomes", componentes, tabela="sorteador_nomes")


def projeto_36_numeros_sorteio():
    componentes = [
        _label(235, 30, "Gerador de Números para Sorteio", "titulo", 550, 44),
        _label(185, 110, "Quantidade de números", "lbl_qtd", 210),
        _campo("quantidade_numeros", "Quantidade", 405, 103, 180, tipo="Spinbox", campo_banco=""),
        _botao("btn_gerar", "Gerar números", 610, 103, 200,
               acao="Gerar números de sorteio", campos_acao=["quantidade_numeros"],
               campo_resultado="numeros_gerados"),
        _label(185, 175, "Números gerados", "lbl_numeros", 210),
        Componente(tipo="Listbox", x=405, y=168, largura=405, altura=285,
                   nome="numeros_gerados", texto="", opcoes=[]),
    ]
    return _projeto("Gerador de Números para Sorteio", componentes, tabela="numeros_sorteio")


def projeto_37_quiz_interativo():
    componentes = [
        _label(300, 25, "Quiz Interativo", "titulo", 400, 44),
        _label(90, 92, "1. Qual é a capital do Brasil?", "lbl_q1", 360),
        Componente(tipo="Radiobutton", x=110, y=130, largura=180, altura=34,
                   nome="q1_brasilia", texto="Brasília", campo_banco="resposta_1"),
        Componente(tipo="Radiobutton", x=300, y=130, largura=180, altura=34,
                   nome="q1_rio", texto="Rio de Janeiro", campo_banco="resposta_1"),
        Componente(tipo="Radiobutton", x=500, y=130, largura=180, altura=34,
                   nome="q1_sp", texto="São Paulo", campo_banco="resposta_1"),
        _label(90, 205, "2. Quanto é 7 × 8?", "lbl_q2", 360),
        Componente(tipo="Radiobutton", x=110, y=243, largura=120, altura=34,
                   nome="q2_48", texto="48", campo_banco="resposta_2"),
        Componente(tipo="Radiobutton", x=250, y=243, largura=120, altura=34,
                   nome="q2_56", texto="56", campo_banco="resposta_2"),
        Componente(tipo="Radiobutton", x=390, y=243, largura=120, altura=34,
                   nome="q2_64", texto="64", campo_banco="resposta_2"),
        _label(90, 320, "Resultado", "lbl_resultado", 180),
        _campo("resultado_quiz", "Resultado", 280, 313, 400, campo_banco=""),
        _botao("btn_corrigir", "Corrigir quiz", 280, 375, 400,
               acao="Calcular com campos", campos_acao=["q1_brasilia", "q2_56"],
               campo_resultado="resultado_quiz", operador="Expressão personalizada",
               expressao="(1 if A == 'Brasília' else 0) + (1 if B == 56 else 0)",
               formato_resultado="{resultado} de 2"),
    ]
    return _projeto("Quiz Interativo", componentes, tabela="quiz")


def projeto_38_preferencias_componentes():
    componentes = [
        _label(260, 25, "Preferências com Controles Visuais", "titulo", 520, 44),
        Componente(tipo="Frame", x=70, y=90, largura=860, altura=205,
                   nome="grupo_preferencias", texto="Preferências"),
        _label(100, 120, "Tema preferido", "lbl_tema", 180),
        Componente(tipo="Radiobutton", x=280, y=115, largura=150, altura=34,
                   nome="tema_claro", texto="Claro", campo_banco="tema_preferido"),
        Componente(tipo="Radiobutton", x=440, y=115, largura=150, altura=34,
                   nome="tema_escuro", texto="Escuro", campo_banco="tema_preferido"),
        Componente(tipo="Radiobutton", x=600, y=115, largura=180, altura=34,
                   nome="tema_azul", texto="Azul", campo_banco="tema_preferido"),
        Componente(tipo="Separator", x=100, y=165, largura=760, altura=8,
                   nome="separador_preferencias", texto=""),
        _label(100, 195, "Tamanho", "lbl_tamanho", 150),
        _campo("tamanho", "Tamanho", 280, 188, 150, tipo="Spinbox", campo_banco="tamanho"),
        _label(480, 195, "Intensidade", "lbl_intensidade", 150),
        _campo("intensidade", "Intensidade", 640, 188, 220, tipo="Scale", campo_banco="intensidade", altura=50),
        _botao("btn_cadastrar", "Cadastrar", 330, 335, 340,
               acao="Cadastrar no SQLite", campos_acao=["tema_claro", "tamanho", "intensidade"]),
    ]
    return _projeto("Preferências com Controles Visuais", componentes,
                    tabela="preferencias", exibir_dados=True)


def projeto_39_formulario_campos_especiais():
    componentes = [
        _label(245, 25, "Formulário com Campos Especiais", "titulo", 540, 44),
        _label(120, 100, "E-mail", "lbl_email", 160),
        _campo("email", "E-mail", 290, 93, 300, tipo="EmailEntry", campo_banco="email", validacao="E-mail"),
        _label(120, 160, "Senha", "lbl_senha", 160),
        _campo("senha", "Senha", 290, 153, 300, tipo="PasswordEntry", campo_banco="senha", mascara="Senha"),
        _label(120, 220, "Data", "lbl_data", 160),
        _campo("data", "Data", 290, 213, 300, tipo="DateEntry", campo_banco="data", mascara="Data", validacao="Data"),
        _label(120, 280, "Horário", "lbl_hora", 160),
        _campo("horario", "Horário", 290, 273, 300, tipo="TimeEntry", campo_banco="horario", mascara="Hora", validacao="Hora"),
        _botao("btn_cadastrar", "Cadastrar", 620, 93, 220,
               acao="Cadastrar no SQLite", campos_acao=["email", "senha", "data", "horario"]),
        _botao("btn_limpar", "Limpar", 620, 153, 220,
               acao="Limpar campos selecionados", campos_acao=["email", "senha", "data", "horario"]),
    ]
    return _projeto("Formulário com Campos Especiais", componentes,
                    tabela="campos_especiais", exibir_dados=True)


def projeto_40_editor_anotacoes():
    componentes = [
        _label(290, 25, "Editor de Anotações", "titulo", 430, 44),
        _label(100, 95, "Categoria", "lbl_categoria", 160),
        _campo("categoria", "Categoria", 270, 88, 250, tipo="Menubutton",
               opcoes=["Estudo", "Trabalho", "Pessoal", "Ideias"], campo_banco="categoria"),
        Componente(tipo="ToggleButton", x=550, y=88, largura=220, altura=34,
                   nome="favorita", texto="Marcar como favorita", campo_banco="favorita"),
        _label(100, 155, "Anotação", "lbl_anotacao", 160),
        _campo("anotacao", "Anotação", 270, 148, 500, tipo="ScrolledText",
               campo_banco="anotacao", altura=245),
        _botao("btn_cadastrar", "Salvar anotação", 270, 420, 245,
               acao="Cadastrar no SQLite", campos_acao=["categoria", "favorita", "anotacao"]),
        _botao("btn_limpar", "Limpar", 525, 420, 245,
               acao="Limpar campos selecionados", campos_acao=["categoria", "favorita", "anotacao"]),
    ]
    return _projeto("Editor de Anotações", componentes, tabela="anotacoes", exibir_dados=True)


def projeto_41_progresso_canvas():
    componentes = [
        _label(265, 25, "Painel de Progresso e Área de Desenho", "titulo", 540, 44),
        _label(80, 105, "Progresso da tarefa", "lbl_progresso", 220),
        Componente(tipo="Progressbar", x=80, y=145, largura=360, altura=30,
                   nome="barra_progresso", texto="65"),
        _label(80, 190, "65% concluído", "lbl_percentual", 220),
        Componente(tipo="VSeparator", x=490, y=95, largura=8, altura=330,
                   nome="separador_vertical", texto=""),
        _label(550, 105, "Área de desenho", "lbl_canvas", 220),
        Componente(tipo="Canvas", x=550, y=145, largura=340, altura=260,
                   nome="area_desenho", texto="Área para desenhos e elementos visuais"),
    ]
    return _projeto("Painel de Progresso e Área de Desenho", componentes,
                    tabela="painel_progresso")


def projeto_42_filtro_contador_exportacao():
    componentes = [
        _label(230, 20, "Lista com Filtro, Contador e Exportação", "titulo", 560, 44),
        _label(45, 90, "Nome", "lbl_nome", 120),
        _campo("nome", "Nome", 165, 83, 250, campo_banco="nome", obrigatorio=True),
        _label(440, 90, "Turma", "lbl_turma", 100),
        _campo("turma", "Turma", 540, 83, 220, tipo="Combobox",
               opcoes=["Turma A", "Turma B", "Turma C"], campo_banco="turma"),
        _botao("btn_cadastrar", "Cadastrar", 780, 82, 165,
               acao="Cadastrar no SQLite", campos_acao=["nome", "turma"]),
        Componente(tipo="Filtro", x=45, y=150, largura=330, altura=34,
                   nome="filtro", texto="Pesquisar", campo_filtro="nome", alvo_filtro="tabela_dados"),
        _label(395, 153, "Itens exibidos:", "contador_itens", 200,
               alvo_filtro="tabela_dados"),
        _botao("btn_exportar", "Exportar para Excel", 730, 145, 215,
               acao="Exportar dados para Excel", campos_acao=["tabela_dados"]),
        Componente(tipo="Treeview", x=45, y=205, largura=900, altura=300,
                   nome="tabela_dados", texto=""),
    ]
    return _projeto("Lista com Filtro, Contador e Exportação", componentes,
                    tabela="lista_exportacao", altura=620, exibir_dados=True)


def projeto_43_exportar_lista_excel():
    componentes = [
        _label(265, 25, "Exportar uma Lista para Excel", "titulo", 500, 44),
        _label(120, 95, "Itens da lista", "lbl_lista", 180),
        Componente(tipo="Listbox", x=120, y=135, largura=420, altura=300,
                   nome="lista_itens", texto="",
                   opcoes=["Caderno", "Caneta", "Lápis", "Borracha", "Régua", "Mochila"]),
        _label(580, 135, "Itens exibidos:", "contador_lista", 220,
               alvo_filtro="lista_itens"),
        _botao("btn_exportar", "Exportar lista para Excel", 580, 195, 280,
               acao="Exportar dados para Excel", campos_acao=["lista_itens"]),
    ]
    return _projeto("Exportar uma Lista para Excel", componentes,
                    tabela="lista_excel", altura=560)


def projeto_44_exportar_treeview_excel():
    componentes = [
        _label(225, 20, "Exportar Dados da Treeview para Excel", "titulo", 600, 44),
        _label(45, 90, "Produto", "lbl_produto", 100),
        _campo("produto", "Produto", 145, 83, 245, campo_banco="produto", obrigatorio=True),
        _label(415, 90, "Quantidade", "lbl_quantidade", 100),
        _campo("quantidade", "Quantidade", 515, 83, 150, tipo="Spinbox",
               campo_banco="quantidade", validacao="Inteiro"),
        _label(690, 90, "Valor", "lbl_valor", 70),
        _campo("valor", "Valor", 755, 83, 145, campo_banco="valor", validacao="Decimal"),
        _botao("btn_cadastrar", "Adicionar à Treeview", 45, 140, 220,
               acao="Cadastrar no SQLite", campos_acao=["produto", "quantidade", "valor"]),
        Componente(tipo="Filtro", x=285, y=143, largura=275, altura=34,
                   nome="filtro_treeview", texto="Pesquisar produto",
                   campo_filtro="produto", alvo_filtro="treeview_excel"),
        _label(580, 147, "Itens exibidos:", "contador_treeview", 165,
               alvo_filtro="treeview_excel"),
        _botao("btn_exportar", "Exportar Treeview para Excel", 745, 137, 210,
               acao="Exportar dados para Excel", campos_acao=["treeview_excel"]),
        Componente(tipo="Treeview", x=45, y=205, largura=910, altura=315,
                   nome="treeview_excel", texto=""),
        _label(45, 540,
               "A exportação usa exatamente os dados exibidos na Treeview, inclusive após aplicar um filtro.",
               "lbl_orientacao", 760),
    ]
    return _projeto("Exportar Dados da Treeview para Excel", componentes,
                    tabela="treeview_excel", altura=620, exibir_dados=True)


PROJETOS_EXTRAS = [
    {"nome": "Cronômetro", "fabrica": projeto_31_cronometro},
    {"nome": "Temporizador", "fabrica": projeto_32_temporizador},
    {"nome": "Gerador de Senhas Seguras", "fabrica": projeto_33_gerador_senhas},
    {"nome": "Calculadora de Idade Completa", "fabrica": projeto_34_idade_completa},
    {"nome": "Sorteador de Nomes", "fabrica": projeto_35_sorteador_nomes},
    {"nome": "Gerador de Números para Sorteio", "fabrica": projeto_36_numeros_sorteio},
    {"nome": "Quiz Interativo", "fabrica": projeto_37_quiz_interativo},
    {"nome": "Preferências com RadioButton, Spinbox, Scale, Separador e Frame", "fabrica": projeto_38_preferencias_componentes},
    {"nome": "Formulário com Senha, E-mail, Data e Horário", "fabrica": projeto_39_formulario_campos_especiais},
    {"nome": "Editor com ScrolledText, Menubutton e ToggleButton", "fabrica": projeto_40_editor_anotacoes},
    {"nome": "Painel com Progressbar, Separador Vertical e Canvas", "fabrica": projeto_41_progresso_canvas},
    {"nome": "Lista com Filtro, Contador e Exportação para Excel", "fabrica": projeto_42_filtro_contador_exportacao},
    {"nome": "Exportar Listbox para Excel", "fabrica": projeto_43_exportar_lista_excel},
    {"nome": "Exportar Dados da Treeview para Excel", "fabrica": projeto_44_exportar_treeview_excel},
]
