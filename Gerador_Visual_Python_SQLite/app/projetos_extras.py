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
           obrigatorio=False, altura=None, texto="", **kwargs):
    if altura is None:
        altura = 120 if tipo in {"Text", "ScrolledText"} else 34
    return Componente(
        tipo=tipo, x=x, y=y, largura=largura, altura=altura,
        nome=nome, texto=texto, opcoes=list(opcoes or []),
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
        _label(225, 25, "Painel de Progresso e Área de Desenho", "titulo", 560, 44),
        _label(60, 95, "Valor do progresso (0 a 100)", "lbl_valor_progresso", 250),
        _campo("valor_progresso", "Valor do progresso", 60, 130, 220,
               tipo="Spinbox", campo_banco=""),
        _botao("btn_testar_progresso", "Testar progresso", 295, 127, 185,
               acao="Testar barra de progresso", campos_acao=["valor_progresso"],
               campo_resultado="barra_progresso", campo_resultado_2="lbl_percentual"),
        _label(60, 190, "Progresso da tarefa", "lbl_progresso", 220),
        Componente(tipo="Progressbar", x=60, y=225, largura=420, altura=30,
                   nome="barra_progresso", texto="0"),
        _label(60, 270, "0% concluído", "lbl_percentual", 220),
        _label(60, 315, "Informe um número e clique em Testar progresso.",
               "lbl_instrucao_progresso", 420),
        Componente(tipo="VSeparator", x=510, y=90, largura=8, altura=430,
                   nome="separador_vertical", texto=""),
        _label(550, 95, "Área de desenho", "lbl_canvas", 220),
        Componente(tipo="Canvas", x=550, y=135, largura=390, altura=325,
                   nome="area_desenho", texto="Arraste o mouse para desenhar"),
        _botao("btn_limpar_desenho", "Limpar desenho", 655, 480, 180,
               acao="Limpar área de desenho", campo_resultado="area_desenho"),
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


def projeto_45_rascunhos_outlook_excel():
    componentes = [
        _label(175, 20, "Criador de E-mails em Rascunho no Outlook", "titulo", 650, 44),
        _label(45, 88, "Planilha do Excel", "lbl_excel", 145),
        _campo("caminho_excel", "Planilha do Excel", 190, 81, 560, campo_banco="", recurso_outlook="caminho_excel"),
        _botao("btn_selecionar_excel", "Selecionar Excel", 765, 78, 190, acao="Outlook: selecionar planilha do Excel", recurso_outlook="selecionar_excel"),
        _label(45, 138, "Planilha/aba", "lbl_planilha", 145),
        _campo("planilha_excel", "Planilha/aba", 190, 131, 300, tipo="Combobox", opcoes=[], campo_banco="", recurso_outlook="planilha_excel"),
        _label(45, 187, "Colunas do Excel", "lbl_colunas", 180),
        Componente(
            tipo="Listbox", x=45, y=220, largura=280, altura=270,
            nome="lista_colunas_excel", texto="", opcoes=[], campo_banco="", recurso_outlook="colunas_excel",
        ),
        _label(
            45, 500,
            "Arraste uma coluna para Para, CC, CCO, Assunto, Corpo ou regra do anexo.",
            "lbl_arrastar", 910,
        ),
        _label(355, 138, "Para (.To)", "lbl_to", 115),
        _campo("email_to", "Para", 470, 131, 485, campo_banco="", recurso_outlook="email_to"),
        _label(355, 188, "CC (.CC)", "lbl_cc", 115),
        _campo("email_cc", "CC", 470, 181, 485, campo_banco="", recurso_outlook="email_cc"),
        _label(355, 238, "CCO (.BCC)", "lbl_bcc", 115),
        _campo("email_bcc", "CCO", 470, 231, 485, campo_banco="", recurso_outlook="email_bcc"),
        _label(355, 288, "Assunto", "lbl_assunto", 115),
        _campo("assunto_email", "Assunto", 470, 281, 485, campo_banco="", recurso_outlook="assunto"),
        _label(355, 338, "Pasta dos anexos", "lbl_pasta_anexos", 150),
        _campo("pasta_anexos", "Pasta dos anexos", 505, 331, 280, campo_banco="", recurso_outlook="pasta_anexos"),
        _botao("btn_pasta_anexos", "Escolher pasta", 800, 328, 155, acao="Outlook: escolher pasta de anexos", recurso_outlook="selecionar_pasta_anexos"),
        _label(355, 388, "Regra do anexo", "lbl_regra_anexo", 150),
        _campo("regra_anexo", "Regra do anexo", 505, 381, 450, campo_banco="", recurso_outlook="regra_anexo"),
        _label(
            355, 425,
            "Ex.: {Codigo}_boleto.pdf  ou  Contratos\\{Cliente}_contrato.pdf. Separe vários por ;",
            "lbl_exemplo_anexo", 600,
        ),
        Componente(
            tipo="Checkbutton", x=355, y=462, largura=310, altura=34,
            nome="exigir_anexo", texto="Só criar se o anexo for encontrado", campo_banco="", recurso_outlook="exigir_anexo",
        ),
        _label(45, 552, "Corpo do e-mail", "lbl_corpo", 180),
        _botao("btn_negrito_email", "Negrito", 200, 545, 85, acao="Outlook: aplicar negrito", recurso_outlook="negrito"),
        _botao("btn_italico_email", "Itálico", 290, 545, 85, acao="Outlook: aplicar itálico", recurso_outlook="italico"),
        _botao("btn_sublinhado_email", "Sublinhar", 380, 545, 100, acao="Outlook: aplicar sublinhado", recurso_outlook="sublinhado"),
        _botao("btn_cor_email", "Cor", 485, 545, 70, acao="Outlook: escolher cor do texto", recurso_outlook="cor_texto"),
        _campo(
            "tamanho_texto_email", "Tamanho", 560, 548, 70, tipo="Combobox", recurso_outlook="tamanho_texto",
            opcoes=["8", "9", "10", "11", "12", "14", "16", "18", "20", "24", "28", "32"], campo_banco="",
        ),
        _botao("btn_tamanho_email", "Aplicar tamanho", 635, 545, 120, acao="Outlook: aplicar tamanho do texto", recurso_outlook="aplicar_tamanho"),
        _botao("btn_link_email", "Link", 760, 545, 75, acao="Outlook: inserir link", recurso_outlook="link"),
        _botao("btn_imagem_email", "Imagem", 840, 545, 100, acao="Outlook: inserir imagem", recurso_outlook="imagem"),
        _campo("corpo_email", "Corpo do e-mail", 45, 595, 910, tipo="ScrolledText", campo_banco="", altura=240, recurso_outlook="corpo"),
        _label(45, 852, "Anexos fixos adicionais", "lbl_anexos_fixos", 200),
        Componente(
            tipo="Listbox", x=45, y=885, largura=610, altura=120,
            nome="lista_anexos_fixos", texto="", opcoes=[], campo_banco="", recurso_outlook="anexos_fixos",
        ),
        _botao("btn_adicionar_anexo", "Adicionar arquivo", 675, 885, 190, acao="Outlook: adicionar anexo fixo", recurso_outlook="adicionar_anexo"),
        _botao("btn_remover_anexo", "Remover selecionado", 675, 935, 190, acao="Outlook: remover anexo fixo", recurso_outlook="remover_anexo"),
        _botao("btn_criar_rascunhos", "Criar rascunhos no Outlook", 45, 1030, 390, acao="Outlook: criar rascunhos", recurso_outlook="criar_rascunhos"),
        _label(460, 1038, "Status: pronto para selecionar uma planilha.", "status_outlook", 495, recurso_outlook="status"),
        _label(
            45, 1090,
            "Cada linha do Excel pode gerar um rascunho. Nenhum e-mail é enviado automaticamente.",
            "lbl_seguranca", 910,
        ),
    ]
    projeto = _projeto(
        "Criador de E-mails em Rascunho no Outlook",
        componentes,
        tabela="rascunhos_outlook",
        altura=1160,
        exibir_dados=False,
    )
    return projeto


def projeto_46_quebrar_planilha_excel():
    componentes = [
        _label(170, 20, "Quebrar Planilha do Excel por Coluna", "titulo", 660, 44),
        _label(45, 85, "Arquivo do Excel", "lbl_excel", 145),
        _campo("qe46_caminho_excel", "Arquivo do Excel", 190, 78, 560, campo_banco="", recurso_outlook="qe46_caminho_excel"),
        _botao("qe46_btn_excel", "Selecionar Excel", 765, 75, 190, acao="Excel por coluna: selecionar arquivo", recurso_outlook="qe46_selecionar_excel"),
        _label(45, 135, "Aba de origem", "lbl_aba", 145),
        _campo("qe46_aba", "Aba de origem", 190, 128, 300, tipo="Combobox", opcoes=[], campo_banco="", recurso_outlook="qe46_aba"),
        _label(45, 185, "Colunas encontradas", "lbl_colunas", 180),
        Componente(
            tipo="Listbox", x=45, y=218, largura=285, altura=230,
            nome="qe46_lista_colunas", texto="", opcoes=[], campo_banco="", recurso_outlook="qe46_lista_colunas",
        ),
        _label(355, 135, "Coluna para fazer a quebra", "lbl_coluna_quebra", 220),
        _campo("qe46_coluna", "Coluna para quebra", 575, 128, 380, tipo="Combobox", opcoes=[], campo_banco="", recurso_outlook="qe46_coluna"),
        _botao("qe46_usar_coluna", "Usar coluna selecionada", 355, 178, 600, acao="Excel por coluna: usar coluna selecionada", recurso_outlook="qe46_usar_coluna"),
        _label(355, 235, "Resumo dos valores encontrados", "lbl_resumo", 310),
        Componente(
            tipo="Treeview", x=355, y=270, largura=600, altura=178,
            nome="qe46_resumo", texto="", campo_banco="", recurso_outlook="qe46_resumo",
        ),
        _label(45, 478, "Pasta de saída", "lbl_saida", 145),
        _campo("qe46_pasta_saida", "Pasta de saída", 190, 471, 560, campo_banco="", recurso_outlook="qe46_pasta_saida"),
        _botao("qe46_btn_pasta", "Escolher pasta", 765, 468, 190, acao="Excel por coluna: escolher pasta de saída", recurso_outlook="qe46_selecionar_pasta"),
        _label(45, 528, "Arquivo com várias abas", "lbl_nome_geral", 195),
        _campo("qe46_nome_geral", "Arquivo com várias abas", 240, 521, 715, campo_banco="", recurso_outlook="qe46_nome_geral"),
        _label(45, 578, "Nome dos arquivos separados", "lbl_nome_individual", 225),
        _campo("qe46_nome_individual", "Nome dos arquivos separados", 270, 571, 685, campo_banco="", recurso_outlook="qe46_nome_individual"),
        _label(
            45, 615,
            "Use {valor} para o conteúdo da coluna, {coluna} para o nome da coluna e {arquivo} para o nome do Excel original.",
            "lbl_modelo_nome", 910,
        ),
        _botao("qe46_btn_abas", "Gerar 1 arquivo com várias abas", 45, 665, 430, acao="Excel por coluna: gerar arquivo com várias abas", recurso_outlook="qe46_gerar_abas"),
        _botao("qe46_btn_arquivos", "Gerar arquivos separados", 495, 665, 460, acao="Excel por coluna: gerar arquivos separados", recurso_outlook="qe46_gerar_arquivos"),
        _label(45, 725, "Status: selecione um arquivo do Excel.", "qe46_status", 910, recurso_outlook="qe46_status"),
    ]
    return _projeto(
        "Quebrar Planilha do Excel por Coluna",
        componentes,
        tabela="quebra_excel_coluna",
        altura=790,
        exibir_dados=False,
    )


def projeto_47_quebrar_varias_abas_excel():
    componentes = [
        _label(145, 20, "Quebrar Arquivo com Várias Abas por Coluna", "titulo", 710, 44),
        _label(45, 85, "Arquivo do Excel", "lbl_excel", 145),
        _campo("qe47_caminho_excel", "Arquivo do Excel", 190, 78, 560, campo_banco="", recurso_outlook="qe47_caminho_excel"),
        _botao("qe47_btn_excel", "Selecionar Excel", 765, 75, 190, acao="Excel várias abas: selecionar arquivo", recurso_outlook="qe47_selecionar_excel"),
        _label(45, 140, "Abas encontradas", "lbl_abas", 180),
        Componente(
            tipo="Listbox", x=45, y=173, largura=285, altura=210,
            nome="qe47_lista_abas", texto="", opcoes=[], campo_banco="", recurso_outlook="qe47_lista_abas",
        ),
        _label(355, 140, "Colunas disponíveis em todas as abas", "lbl_colunas", 310),
        Componente(
            tipo="Listbox", x=355, y=173, largura=285, altura=210,
            nome="qe47_lista_colunas", texto="", opcoes=[], campo_banco="", recurso_outlook="qe47_lista_colunas",
        ),
        _label(665, 140, "Coluna para fazer a quebra", "lbl_coluna_quebra", 255),
        _campo("qe47_coluna", "Coluna para quebra", 665, 173, 290, tipo="Combobox", opcoes=[], campo_banco="", recurso_outlook="qe47_coluna"),
        _botao("qe47_usar_coluna", "Usar coluna selecionada", 665, 218, 290, acao="Excel várias abas: usar coluna selecionada", recurso_outlook="qe47_usar_coluna"),
        _label(665, 275, "Resumo geral", "lbl_resumo", 180),
        Componente(
            tipo="Treeview", x=665, y=308, largura=290, altura=190,
            nome="qe47_resumo", texto="", campo_banco="", recurso_outlook="qe47_resumo",
        ),
        _label(45, 418, "Pasta de saída", "lbl_saida", 145),
        _campo("qe47_pasta_saida", "Pasta de saída", 190, 411, 560, campo_banco="", recurso_outlook="qe47_pasta_saida"),
        _botao("qe47_btn_pasta", "Escolher pasta", 765, 408, 190, acao="Excel várias abas: escolher pasta de saída", recurso_outlook="qe47_selecionar_pasta"),
        _label(45, 468, "Nome dos arquivos", "lbl_nome", 145),
        _campo("qe47_nome_arquivo", "Nome dos arquivos", 190, 461, 765, campo_banco="", recurso_outlook="qe47_nome_arquivo"),
        _label(
            45, 505,
            "Ex.: {valor}_relatorio.xlsx. Também pode usar {coluna} e {arquivo}. Cada arquivo manterá as abas do Excel original filtradas pelo valor.",
            "lbl_modelo_nome", 910,
        ),
        _botao("qe47_btn_gerar", "Quebrar todas as abas e gerar arquivos", 45, 555, 910, acao="Excel várias abas: gerar arquivos", recurso_outlook="qe47_gerar"),
        _label(45, 615, "Status: selecione um arquivo com várias abas.", "qe47_status", 910, recurso_outlook="qe47_status"),
    ]
    return _projeto(
        "Quebrar Arquivo com Várias Abas por Coluna",
        componentes,
        tabela="quebra_excel_varias_abas",
        altura=690,
        exibir_dados=False,
    )


def projeto_48_gerenciador_itens_listbox():
    componentes = [
        _label(220, 25, "Gerenciador de Itens na Listbox", "titulo", 560, 44),
        _label(70, 100, "Novo item", "lbl_novo_item", 140),
        _campo("novo_item_lista", "Novo item", 210, 93, 390, campo_banco=""),
        _botao(
            "btn_adicionar_item", "Adicionar item", 620, 90, 170,
            acao="Listbox: adicionar item",
            campos_acao=["novo_item_lista"],
            campo_resultado="lista_itens_48",
        ),
        Componente(
            tipo="Listbox", x=70, y=160, largura=600, altura=330,
            nome="lista_itens_48", texto="",
            opcoes=["Caderno", "Caneta", "Lápis"], campo_banco="",
        ),
        _label(700, 165, "Itens exibidos:", "contador_itens_48", 220,
               alvo_filtro="lista_itens_48"),
        _botao(
            "btn_excluir_item", "Excluir selecionado", 700, 225, 220,
            acao="Listbox: excluir item selecionado",
            campo_resultado="lista_itens_48",
        ),
        _botao(
            "btn_limpar_lista", "Limpar lista", 700, 280, 220,
            acao="Listbox: limpar lista",
            campo_resultado="lista_itens_48",
        ),
        _botao(
            "btn_alterar_item", "Alterar selecionado", 700, 335, 220,
            acao="Listbox: alterar item selecionado",
            campos_acao=["novo_item_lista"],
            campo_resultado="lista_itens_48",
        ),
        _label(
            70, 515,
            "Digite um item, clique em Adicionar item e selecione qualquer item da lista para excluí-lo.",
            "lbl_orientacao_48", 850,
        ),
    ]
    return _projeto(
        "Gerenciador de Itens na Listbox", componentes,
        tabela="gerenciador_listbox", altura=610,
    )


def projeto_49_lista_compras_listbox():
    componentes = [
        _label(245, 25, "Lista de Compras Interativa", "titulo", 520, 44),
        _label(70, 98, "Produto", "lbl_produto_49", 120),
        _campo("produto_lista_49", "Produto", 190, 91, 390, campo_banco=""),
        _botao(
            "btn_incluir_produto_49", "Incluir na lista", 600, 88, 190,
            acao="Listbox: adicionar item",
            campos_acao=["produto_lista_49"],
            campo_resultado="lista_compras_49",
        ),
        Componente(
            tipo="Listbox", x=70, y=158, largura=600, altura=335,
            nome="lista_compras_49", texto="",
            opcoes=["Arroz", "Feijão", "Leite", "Café"], campo_banco="",
        ),
        _label(700, 163, "Produtos na lista:", "contador_compras_49", 225,
               alvo_filtro="lista_compras_49"),
        _botao(
            "btn_remover_produto_49", "Remover selecionado", 700, 225, 225,
            acao="Listbox: excluir item selecionado",
            campo_resultado="lista_compras_49",
        ),
        _botao(
            "btn_esvaziar_49", "Esvaziar lista", 700, 280, 225,
            acao="Listbox: limpar lista",
            campo_resultado="lista_compras_49",
        ),
        _botao(
            "btn_alterar_produto_49", "Alterar selecionado", 700, 335, 225,
            acao="Listbox: alterar item selecionado",
            campos_acao=["produto_lista_49"],
            campo_resultado="lista_compras_49",
        ),
        _label(
            70, 515,
            "A mesma lógica de incluir e excluir pode ser reutilizada em qualquer Listbox criada no Designer.",
            "lbl_orientacao_49", 850,
        ),
    ]
    return _projeto(
        "Lista de Compras Interativa", componentes,
        tabela="lista_compras", altura=610,
    )


def projeto_50_gerador_sequencia_numerica():
    componentes = [
        _label(205, 25, "Gerador de Sequência Numérica em Lista", "titulo", 610, 44),
        _label(70, 98, "Quantidade de números", "lbl_quantidade_50", 190),
        Componente(
            tipo="Entry", x=260, y=91, largura=220, altura=34,
            nome="quantidade_lista_50", texto="600", campo_banco="",
            titulo_coluna="Quantidade de números", validacao="Inteiro",
        ),
        _botao(
            "btn_gerar_sequencia_50", "Gerar números", 500, 88, 210,
            acao="Listbox: gerar sequência numérica",
            campos_acao=["quantidade_lista_50"],
            campo_resultado="lista_numeros_50",
        ),
        _botao(
            "btn_limpar_numeros_50", "Limpar lista", 730, 88, 190,
            acao="Listbox: limpar lista",
            campo_resultado="lista_numeros_50",
        ),
        Componente(
            tipo="Listbox", x=70, y=158, largura=850, altura=360,
            nome="lista_numeros_50", texto="", opcoes=[], campo_banco="",
            fonte="Consolas", tamanho_fonte=11,
        ),
        _label(70, 540, "Itens exibidos:", "contador_numeros_50", 240,
               alvo_filtro="lista_numeros_50"),
        _label(
            330, 540,
            "Informe 600, 1.000, 5.000 ou outra quantidade positiva. A lista é criada de 1 até o valor informado.",
            "lbl_orientacao_50", 590,
        ),
    ]
    return _projeto(
        "Gerador de Sequência Numérica em Lista", componentes,
        tabela="sequencia_numerica", altura=630,
    )


def projeto_51_treeview_personalizada():
    componentes = [
        _label(225, 20, "Treeview Personalizada", "titulo", 560, 44),
        _label(45, 92, "Produto", "lbl_produto_51", 95),
        _campo("produto_51", "Produto", 140, 85, 235, campo_banco="produto", obrigatorio=True),
        _label(395, 92, "Categoria", "lbl_categoria_51", 95),
        _campo(
            "categoria_51", "Categoria", 490, 85, 185,
            tipo="Combobox", opcoes=["Informática", "Escritório", "Casa"],
            campo_banco="categoria",
        ),
        _label(695, 92, "Status", "lbl_status_51", 70),
        _campo(
            "status_51", "Status", 765, 85, 190,
            tipo="Combobox", opcoes=["Disponível", "Reservado", "Indisponível"],
            campo_banco="status",
        ),
        _botao(
            "btn_cadastrar_51", "Cadastrar", 45, 140, 210,
            acao="Cadastrar no SQLite",
            campos_acao=["produto_51", "categoria_51", "status_51"],
        ),
        _label(
            280, 147,
            "Selecione a Treeview no Designer para trocar fonte, tamanho, negrito, cor do texto e cor do fundo.",
            "lbl_dica_treeview_51", 675,
        ),
        Componente(
            tipo="Treeview", x=45, y=205, largura=910, altura=330,
            nome="treeview_personalizada_51", texto="",
            fonte="Segoe UI", tamanho_fonte=12, negrito=False,
            cor_texto="#17365D", cor_fundo="#EAF2F8",
        ),
        _label(
            45, 555,
            "Este exemplo já usa uma Treeview com fonte maior e cores próprias para demonstrar a personalização visual.",
            "lbl_orientacao_51", 900,
        ),
    ]
    return _projeto(
        "Treeview Personalizada", componentes,
        tabela="treeview_personalizada", altura=640, exibir_dados=True,
    )


def projeto_52_campos_obrigatorios_bloqueados():
    componentes = [
        _label(185, 20, "Campos Obrigatórios e Campos Bloqueados", "titulo", 650, 44),
        _label(90, 95, "Código", "lbl_codigo_52", 125),
        Componente(
            tipo="Entry", x=215, y=88, largura=300, altura=34,
            nome="codigo_cliente_52", texto="CLI-0001",
            campo_banco="codigo_cliente", titulo_coluna="Código",
            bloqueado=True,
        ),
        _label(535, 95, "Somente leitura", "lbl_bloqueado_52", 200),
        _label(90, 155, "Nome *", "lbl_nome_52", 125),
        _campo(
            "nome_cliente_52", "Nome", 215, 148, 520,
            campo_banco="nome", obrigatorio=True,
        ),
        _label(90, 215, "E-mail *", "lbl_email_52", 125),
        _campo(
            "email_cliente_52", "E-mail", 215, 208, 520,
            campo_banco="email", validacao="E-mail", obrigatorio=True,
        ),
        _label(90, 275, "Cidade", "lbl_cidade_52", 125),
        _campo(
            "cidade_cliente_52", "Cidade", 215, 268, 520,
            campo_banco="cidade",
        ),
        _botao(
            "btn_cadastrar_52", "Cadastrar", 215, 330, 250,
            acao="Cadastrar no SQLite",
            campos_acao=["codigo_cliente_52", "nome_cliente_52", "email_cliente_52", "cidade_cliente_52"],
        ),
        _botao(
            "btn_limpar_52", "Limpar campos editáveis", 485, 330, 250,
            acao="Limpar campos selecionados",
            campos_acao=["nome_cliente_52", "email_cliente_52", "cidade_cliente_52"],
        ),
        _label(
            90, 395,
            "Os campos com * são obrigatórios. O Código está bloqueado e o usuário não pode alterar o valor durante a execução.",
            "lbl_orientacao_52", 820,
        ),
        Componente(
            tipo="Treeview", x=90, y=440, largura=820, altura=190,
            nome="treeview_campos_52", texto="",
        ),
    ]
    return _projeto(
        "Campos Obrigatórios e Campos Bloqueados", componentes,
        tabela="campos_controlados", altura=700, exibir_dados=True,
    )



def projeto_53_contador_texto():
    componentes = [
        _label(245, 22, "Contador de Palavras e Caracteres", "titulo", 530, 44),
        _label(65, 92, "Digite ou cole um texto", "lbl_texto_53", 260),
        _campo(
            "texto_53", "Texto", 65, 128, 600, tipo="ScrolledText",
            campo_banco="", altura=340, fonte="Segoe UI", tamanho_fonte=11,
        ),
        _botao(
            "btn_contar_53", "Analisar texto", 695, 128, 235,
            acao="Texto: contar palavras e caracteres",
            campos_acao=["texto_53"], campo_resultado="resultado_texto_53",
        ),
        _label(695, 195, "Resultado", "lbl_resultado_53", 235),
        _campo(
            "resultado_texto_53", "Resultado", 695, 228, 235,
            tipo="ScrolledText", campo_banco="", altura=240,
            fonte="Consolas", tamanho_fonte=11,
        ),
        _label(
            65, 495,
            "O programa informa palavras, caracteres com e sem espaços e quantidade de linhas.",
            "lbl_dica_53", 865,
        ),
    ]
    return _projeto(
        "Contador de Palavras e Caracteres", componentes,
        tabela="contador_texto", altura=590,
    )


def projeto_54_localizar_substituir_texto():
    componentes = [
        _label(225, 20, "Localizar e Substituir em um Texto", "titulo", 570, 44),
        _label(55, 86, "Texto", "lbl_texto_54", 100),
        _campo(
            "texto_editor_54", "Texto", 55, 120, 890, tipo="ScrolledText",
            campo_banco="", altura=300, fonte="Segoe UI", tamanho_fonte=11,
            texto="Python é simples de aprender. Python também é muito usado em automação.",
        ),
        _label(55, 450, "Localizar", "lbl_localizar_54", 110),
        _campo("localizar_54", "Localizar", 165, 443, 230, campo_banco=""),
        _label(420, 450, "Substituir por", "lbl_substituir_54", 130),
        _campo("substituir_54", "Substituir por", 550, 443, 230, campo_banco=""),
        _botao(
            "btn_substituir_54", "Substituir ocorrências", 795, 440, 150,
            acao="Texto: localizar e substituir",
            campos_acao=["texto_editor_54", "localizar_54", "substituir_54"],
            campo_resultado="texto_editor_54", campo_resultado_2="resultado_substituicao_54",
        ),
        _label(55, 510, "Ocorrências substituídas", "lbl_resultado_54", 210),
        _campo("resultado_substituicao_54", "Ocorrências", 265, 503, 180, campo_banco="", bloqueado=True),
        _label(
            475, 510,
            "Experimente localizar Python e substituir por Tkinter.",
            "lbl_dica_54", 470,
        ),
    ]
    return _projeto(
        "Localizar e Substituir em um Texto", componentes,
        tabela="localizar_substituir", altura=600,
    )


def projeto_55_editor_arquivo_txt():
    componentes = [
        _label(290, 18, "Editor de Arquivo TXT", "titulo", 420, 44),
        _botao(
            "btn_abrir_txt_55", "Abrir arquivo TXT", 65, 82, 205,
            acao="Arquivo TXT: abrir", campo_resultado="editor_txt_55",
            campo_resultado_2="caminho_txt_55",
        ),
        _botao(
            "btn_salvar_txt_55", "Salvar arquivo TXT", 285, 82, 205,
            acao="Arquivo TXT: salvar", campos_acao=["editor_txt_55", "caminho_txt_55"],
        ),
        _botao(
            "btn_novo_txt_55", "Limpar editor", 505, 82, 180,
            acao="Limpar campos selecionados", campos_acao=["editor_txt_55", "caminho_txt_55"],
        ),
        _label(65, 143, "Arquivo", "lbl_caminho_55", 95),
        _campo("caminho_txt_55", "Arquivo", 160, 136, 785, campo_banco="", bloqueado=True),
        _campo(
            "editor_txt_55", "Editor", 65, 195, 880, tipo="ScrolledText",
            campo_banco="", altura=385, fonte="Consolas", tamanho_fonte=11,
        ),
        _label(
            65, 605,
            "Abra um .txt existente, edite o conteúdo e salve no mesmo arquivo ou escolha um novo nome.",
            "lbl_dica_55", 880,
        ),
    ]
    return _projeto(
        "Editor de Arquivo TXT", componentes,
        tabela="editor_txt", altura=680,
    )


def projeto_56_intervalo_datas():
    componentes = [
        _label(230, 24, "Calculadora de Intervalo entre Datas", "titulo", 570, 44),
        _label(120, 115, "Data inicial", "lbl_inicio_56", 160),
        _campo(
            "data_inicial_56", "Data inicial", 280, 108, 250,
            tipo="DateEntry", campo_banco="", mascara="Data", validacao="Data",
        ),
        _label(120, 175, "Data final", "lbl_final_56", 160),
        _campo(
            "data_final_56", "Data final", 280, 168, 250,
            tipo="DateEntry", campo_banco="", mascara="Data", validacao="Data",
        ),
        _botao(
            "btn_calcular_datas_56", "Calcular intervalo", 560, 108, 260,
            acao="Datas: calcular intervalo",
            campos_acao=["data_inicial_56", "data_final_56"],
            campo_resultado="resultado_datas_56",
        ),
        _label(120, 255, "Resultado", "lbl_resultado_56", 160),
        _campo(
            "resultado_datas_56", "Resultado", 280, 248, 540,
            tipo="ScrolledText", campo_banco="", altura=180,
            fonte="Segoe UI", tamanho_fonte=11,
        ),
        _label(
            120, 455,
            "O resultado mostra dias corridos, semanas completas e dias restantes entre as duas datas.",
            "lbl_dica_56", 700,
        ),
    ]
    return _projeto(
        "Calculadora de Intervalo entre Datas", componentes,
        tabela="intervalo_datas", altura=560,
    )


def projeto_57_organizador_listbox():
    componentes = [
        _label(245, 20, "Organizador de Lista", "titulo", 510, 44),
        _label(75, 92, "Itens", "lbl_itens_57", 110),
        Componente(
            tipo="Listbox", x=75, y=128, largura=560, altura=360,
            nome="lista_organizar_57", texto="",
            opcoes=["Banana", "Maçã", "Uva", "Banana", "Abacaxi", "Manga", "Uva", "Pera"],
            campo_banco="", fonte="Segoe UI", tamanho_fonte=11,
        ),
        _botao(
            "btn_az_57", "Ordenar A → Z", 675, 128, 235,
            acao="Listbox: ordenar A-Z", campo_resultado="lista_organizar_57",
        ),
        _botao(
            "btn_za_57", "Ordenar Z → A", 675, 188, 235,
            acao="Listbox: ordenar Z-A", campo_resultado="lista_organizar_57",
        ),
        _botao(
            "btn_duplicados_57", "Remover duplicados", 675, 248, 235,
            acao="Listbox: remover duplicados", campo_resultado="lista_organizar_57",
        ),
        _label(675, 323, "Itens na lista:", "contador_lista_57", 235, alvo_filtro="lista_organizar_57"),
        _label(
            75, 515,
            "Este exemplo trabalha ordenação alfabética e remoção de valores repetidos sem apagar a lista inteira.",
            "lbl_dica_57", 835,
        ),
    ]
    return _projeto(
        "Organizador de Lista", componentes,
        tabela="organizador_lista", altura=600,
    )


def projeto_58_importador_csv_treeview():
    componentes = [
        _label(220, 18, "Importador de CSV para Treeview", "titulo", 570, 44),
        _botao(
            "btn_importar_csv_58", "Selecionar e importar CSV", 55, 82, 260,
            acao="CSV: importar para Treeview",
            campo_resultado="tabela_csv_58", campo_resultado_2="status_csv_58",
        ),
        _label(340, 92, "Status", "lbl_status_58", 90),
        _campo("status_csv_58", "Status", 430, 85, 515, campo_banco="", bloqueado=True),
        Componente(
            tipo="Treeview", x=55, y=150, largura=890, altura=390,
            nome="tabela_csv_58", texto="", campo_banco="",
            fonte="Segoe UI", tamanho_fonte=10,
        ),
        _label(
            55, 565,
            "O cabeçalho do CSV vira as colunas da Treeview e todas as linhas do arquivo são exibidas na tabela.",
            "lbl_dica_58", 890,
        ),
    ]
    return _projeto(
        "Importador de CSV para Treeview", componentes,
        tabela="importador_csv", altura=640,
    )


def projeto_59_estatisticas_lista_numerica():
    componentes = [
        _label(195, 18, "Estatísticas de uma Lista Numérica", "titulo", 610, 44),
        _label(65, 90, "Números", "lbl_numeros_59", 130),
        _campo(
            "numeros_estatistica_59", "Números", 65, 125, 540,
            tipo="ScrolledText", campo_banco="", altura=330,
            fonte="Consolas", tamanho_fonte=11,
            texto="10\n25\n18\n42\n35\n20\n50",
        ),
        _botao(
            "btn_estatisticas_59", "Calcular estatísticas", 640, 125, 285,
            acao="Lista numérica: calcular estatísticas",
            campos_acao=["numeros_estatistica_59"], campo_resultado="resultado_estatistica_59",
        ),
        _label(640, 195, "Resultado", "lbl_resultado_59", 285),
        _campo(
            "resultado_estatistica_59", "Resultado", 640, 230, 285,
            tipo="ScrolledText", campo_banco="", altura=225,
            fonte="Consolas", tamanho_fonte=11,
        ),
        _label(
            65, 485,
            "Digite números separados por linha, vírgula, ponto e vírgula ou espaço.",
            "lbl_dica_59", 860,
        ),
    ]
    return _projeto(
        "Estatísticas de uma Lista Numérica", componentes,
        tabela="estatisticas_lista", altura=565,
    )


def projeto_60_conversor_texto():
    componentes = [
        _label(260, 18, "Conversor de Texto", "titulo", 480, 44),
        _label(65, 86, "Texto", "lbl_texto_60", 100),
        _campo(
            "texto_converter_60", "Texto", 65, 120, 870,
            tipo="ScrolledText", campo_banco="", altura=340,
            fonte="Segoe UI", tamanho_fonte=11,
            texto="aprendendo python com tkinter",
        ),
        _botao(
            "btn_maiusculas_60", "MAIÚSCULAS", 65, 490, 265,
            acao="Texto: converter para maiúsculas",
            campos_acao=["texto_converter_60"], campo_resultado="texto_converter_60",
        ),
        _botao(
            "btn_minusculas_60", "minúsculas", 365, 490, 265,
            acao="Texto: converter para minúsculas",
            campos_acao=["texto_converter_60"], campo_resultado="texto_converter_60",
        ),
        _botao(
            "btn_titulo_60", "Formato de Título", 665, 490, 270,
            acao="Texto: converter para título",
            campos_acao=["texto_converter_60"], campo_resultado="texto_converter_60",
        ),
        _label(
            65, 550,
            "Os três botões alteram o mesmo conteúdo, demonstrando manipulação de strings em uma área de texto.",
            "lbl_dica_60", 870,
        ),
    ]
    return _projeto(
        "Conversor de Texto", componentes,
        tabela="conversor_texto", altura=625,
    )


def projeto_61_calendario_mensal():
    componentes = [
        _label(260, 20, "Gerador de Calendário Mensal", "titulo", 500, 44),
        _label(115, 103, "Mês (1 a 12)", "lbl_mes_61", 160),
        Componente(
            tipo="Entry", x=275, y=96, largura=170, altura=34,
            nome="mes_calendario_61", texto="9", campo_banco="",
            titulo_coluna="Mês", validacao="Inteiro",
        ),
        _label(485, 103, "Ano", "lbl_ano_61", 90),
        Componente(
            tipo="Entry", x=575, y=96, largura=170, altura=34,
            nome="ano_calendario_61", texto="2026", campo_banco="",
            titulo_coluna="Ano", validacao="Inteiro",
        ),
        _botao(
            "btn_calendario_61", "Gerar calendário", 765, 93, 170,
            acao="Calendário: gerar mês",
            campos_acao=["mes_calendario_61", "ano_calendario_61"],
            campo_resultado="resultado_calendario_61",
        ),
        _campo(
            "resultado_calendario_61", "Calendário", 115, 165, 820,
            tipo="ScrolledText", campo_banco="", altura=360,
            fonte="Consolas", tamanho_fonte=13,
        ),
        _label(
            115, 550,
            "Informe mês e ano para montar o calendário completo com os dias organizados por semana.",
            "lbl_dica_61", 820,
        ),
    ]
    return _projeto(
        "Gerador de Calendário Mensal", componentes,
        tabela="calendario_mensal", altura=625,
    )


def projeto_62_analisador_senha():
    componentes = [
        _label(250, 20, "Analisador de Força de Senha", "titulo", 520, 44),
        _label(120, 105, "Senha para analisar", "lbl_senha_62", 190),
        _campo(
            "senha_analisar_62", "Senha", 310, 98, 430,
            tipo="PasswordEntry", campo_banco="", mascara="Senha",
        ),
        _botao(
            "btn_analisar_senha_62", "Analisar senha", 760, 95, 170,
            acao="Senha: analisar força",
            campos_acao=["senha_analisar_62"], campo_resultado="resultado_senha_62",
        ),
        _label(120, 175, "Análise", "lbl_analise_62", 150),
        _campo(
            "resultado_senha_62", "Análise", 120, 210, 810,
            tipo="ScrolledText", campo_banco="", altura=290,
            fonte="Segoe UI", tamanho_fonte=11,
        ),
        _label(
            120, 530,
            "São verificados comprimento, letras maiúsculas e minúsculas, números e símbolos.",
            "lbl_dica_62", 810,
        ),
    ]
    return _projeto(
        "Analisador de Força de Senha", componentes,
        tabela="analise_senha", altura=610,
    )


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
    {"nome": "Criador de E-mails em Rascunho no Outlook", "fabrica": projeto_45_rascunhos_outlook_excel},
    {"nome": "Quebrar Planilha do Excel por Coluna", "fabrica": projeto_46_quebrar_planilha_excel},
    {"nome": "Quebrar Arquivo com Várias Abas por Coluna", "fabrica": projeto_47_quebrar_varias_abas_excel},
    {"nome": "Gerenciador de Itens na Listbox", "fabrica": projeto_48_gerenciador_itens_listbox},
    {"nome": "Lista de Compras Interativa", "fabrica": projeto_49_lista_compras_listbox},
    {"nome": "Gerador de Sequência Numérica em Lista", "fabrica": projeto_50_gerador_sequencia_numerica},
    {"nome": "Treeview Personalizada", "fabrica": projeto_51_treeview_personalizada},
    {"nome": "Campos Obrigatórios e Campos Bloqueados", "fabrica": projeto_52_campos_obrigatorios_bloqueados},
    {"nome": "Contador de Palavras e Caracteres", "fabrica": projeto_53_contador_texto},
    {"nome": "Localizar e Substituir em um Texto", "fabrica": projeto_54_localizar_substituir_texto},
    {"nome": "Editor de Arquivo TXT", "fabrica": projeto_55_editor_arquivo_txt},
    {"nome": "Calculadora de Intervalo entre Datas", "fabrica": projeto_56_intervalo_datas},
    {"nome": "Organizador de Lista", "fabrica": projeto_57_organizador_listbox},
    {"nome": "Importador de CSV para Treeview", "fabrica": projeto_58_importador_csv_treeview},
    {"nome": "Estatísticas de uma Lista Numérica", "fabrica": projeto_59_estatisticas_lista_numerica},
    {"nome": "Conversor de Texto", "fabrica": projeto_60_conversor_texto},
    {"nome": "Gerador de Calendário Mensal", "fabrica": projeto_61_calendario_mensal},
    {"nome": "Analisador de Força de Senha", "fabrica": projeto_62_analisador_senha},
]
