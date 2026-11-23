import ast
import re
import hashlib
import sqlite3
import os
import tkinter as tk
import random
import secrets
import string
import time
import calendar
import csv
from datetime import datetime, date
from tkinter import ttk, messagebox, scrolledtext, filedialog


class AplicacaoGerada(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Quebrar Planilha do Excel por Coluna')
        self.geometry('1000x870')
        self.minsize(820, 560)
        self.cor_fundo = '#eef2f7'
        self.cor_cartao = '#ffffff'
        self.cor_texto = '#203044'
        self.cor_destaque = '#2d6cdf'
        self.configure(bg=self.cor_fundo)
        self.historico_telas = []
        self.usuario_logado = None
        self.nome_usuario_logado = ''
        self.nome_tela_login = 'Tela Principal'
        self._metadados_tabelas = {'Tela Principal': {'tabela': 'quebra_excel_coluna', 'pk': 'id', 'colunas': ['qe46_caminho_excel', 'qe46_aba', 'qe46_coluna', 'qe46_pasta_saida', 'qe46_nome_geral', 'qe46_nome_individual'], 'titulos': {'qe46_caminho_excel': 'Arquivo do Excel', 'qe46_aba': 'Aba de origem', 'qe46_coluna': 'Coluna para quebra', 'qe46_pasta_saida': 'Pasta de saída', 'qe46_nome_geral': 'Arquivo com várias abas', 'qe46_nome_individual': 'Nome dos arquivos separados'}}}
        self._configurar_estilos()
        self.conexao = sqlite3.connect('dados_sistema.db')

        self.notebook_principal = ttk.Notebook(self)
        self.aba_sistema = ttk.Frame(
            self.notebook_principal,
            style='App.TFrame',
        )
        self.notebook_principal.add(
            self.aba_sistema, text='Programa'
        )
        self.notebook_principal.pack(fill='both', expand=True)

        self.container = ttk.Frame(
            self.aba_sistema, style='App.TFrame'
        )
        self.container.pack(fill='both', expand=True)
        self.telas = {}
        self.telas['Tela Principal'] = Tela1_TelaPrincipal(self.container, self)
        self.telas['Tela Principal'].place(x=0, y=0, relwidth=1, relheight=1)
        self.mostrar_tela('Tela Principal', registrar=False)

    def _configurar_estilos(self):
        estilo = ttk.Style(self)
        try:
            estilo.theme_use('clam')
        except tk.TclError:
            pass
        estilo.configure(
            'App.TFrame', background=self.cor_fundo
        )
        estilo.configure(
            'TFrame', background=self.cor_fundo
        )
        estilo.configure(
            'TLabel', background=self.cor_fundo,
            foreground=self.cor_texto, font=('Segoe UI', 10)
        )
        estilo.configure(
            'Title.TLabel', background=self.cor_fundo,
            foreground=self.cor_texto,
            font=('Segoe UI Semibold', 19)
        )
        estilo.configure(
            'TButton', font=('Segoe UI Semibold', 10),
            padding=(11, 7)
        )
        estilo.configure(
            'Treeview', font=('Segoe UI', 10), rowheight=28
        )
        estilo.configure(
            'Treeview.Heading',
            font=('Segoe UI Semibold', 10)
        )

    def _estilo_componente(self, nome_estilo, tipo, fonte, cor_texto='', cor_fundo=''):
        estilo = ttk.Style(self)
        opcoes = {}
        if fonte:
            opcoes['font'] = fonte
        if cor_texto:
            opcoes['foreground'] = cor_texto
        if cor_fundo:
            opcoes['background'] = cor_fundo
            if tipo in {'TEntry', 'TCombobox', 'TSpinbox', 'Treeview'}:
                opcoes['fieldbackground'] = cor_fundo
            if tipo == 'TScale':
                opcoes['troughcolor'] = cor_fundo
        if opcoes:
            estilo.configure(nome_estilo, **opcoes)

        if tipo == 'TCombobox':
            mapa = {}
            if cor_fundo:
                mapa['fieldbackground'] = [('readonly', cor_fundo)]
            if cor_texto:
                mapa['foreground'] = [('readonly', cor_texto)]
            if mapa:
                estilo.map(nome_estilo, **mapa)

        if tipo == 'TButton' and cor_fundo:
            estilo.map(nome_estilo, background=[('active', cor_fundo), ('pressed', cor_fundo)])

        if tipo == 'Treeview':
            cabecalho = nome_estilo + '.Heading'
            opcoes_cabecalho = {}
            if fonte:
                opcoes_cabecalho['font'] = fonte
            if cor_texto:
                opcoes_cabecalho['foreground'] = cor_texto
            if cor_fundo:
                opcoes_cabecalho['background'] = cor_fundo
            if opcoes_cabecalho:
                estilo.configure(cabecalho, **opcoes_cabecalho)

        if tipo == 'TLabelframe':
            rotulo = nome_estilo + '.Label'
            opcoes_rotulo = {}
            if fonte:
                opcoes_rotulo['font'] = fonte
            if cor_texto:
                opcoes_rotulo['foreground'] = cor_texto
            if cor_fundo:
                opcoes_rotulo['background'] = cor_fundo
            if opcoes_rotulo:
                estilo.configure(rotulo, **opcoes_rotulo)

        return nome_estilo

    def mostrar_tela(self, nome, registrar=True):
        tela = self.telas.get(nome)
        if tela is None:
            messagebox.showwarning(
                'Navegação',
                f'A tela {nome} não existe neste projeto.',
            )
            return

        atual = getattr(self, '_tela_atual', None)
        if registrar and atual and atual != nome:
            self.historico_telas.append(atual)

        self._tela_atual = nome
        self.notebook_principal.select(self.aba_sistema)
        tela.lift()

    def voltar_tela(self):
        if self.historico_telas:
            nome = self.historico_telas.pop()
            self.mostrar_tela(nome, registrar=False)

    def sair_da_conta(self):
        self.usuario_logado = None
        self.nome_usuario_logado = ''
        self.historico_telas.clear()
        self.mostrar_tela(
            self.nome_tela_login, registrar=False
        )

    def fechar(self):
        try:
            self.conexao.close()
        finally:
            self.destroy()


class Tela1_TelaPrincipal(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, style='App.TFrame')
        self.app = app
        self._id_selecionado = None
        self._criar_banco()
        self._criar_interface()
        self._atualizar_contadores()
        self.carregar_dados()


    def _criar_area_rolavel(self, largura, altura):
        self._largura_area = largura
        self._altura_area = altura
        self.canvas_rolavel = tk.Canvas(self, highlightthickness=0, bg=self.app.cor_fundo)
        self.barra_vertical = ttk.Scrollbar(self, orient='vertical', command=self.canvas_rolavel.yview)
        self.canvas_rolavel.configure(yscrollcommand=self.barra_vertical.set)
        self.canvas_rolavel.pack(side='left', fill='both', expand=True)
        self.barra_vertical.pack(side='right', fill='y')
        self.area = ttk.Frame(self.canvas_rolavel, style='App.TFrame', width=largura, height=altura)
        self.area.pack_propagate(False)
        self._janela_area = self.canvas_rolavel.create_window((0, 8), window=self.area, anchor='nw')
        self.canvas_rolavel.bind('<Configure>', self._ajustar_area_rolavel)
        self.area.bind('<Configure>', self._atualizar_scroll_area)
        self.canvas_rolavel.bind('<Enter>', lambda e: self.canvas_rolavel.bind_all('<MouseWheel>', self._ao_rolar_mouse))
        self.canvas_rolavel.bind('<Leave>', lambda e: self.canvas_rolavel.unbind_all('<MouseWheel>'))
        self.after(60, self._ajustar_area_rolavel)

    def _ajustar_area_rolavel(self, event=None):
        largura_canvas = max(1, self.canvas_rolavel.winfo_width())
        x = 0 if largura_canvas <= self._largura_area else int((largura_canvas - self._largura_area) / 2)
        self.canvas_rolavel.coords(self._janela_area, x, 8)
        self._atualizar_scroll_area()

    def _atualizar_scroll_area(self, event=None):
        largura_total = max(self._largura_area, self.canvas_rolavel.winfo_width())
        altura_total = max(self._altura_area + 16, self.canvas_rolavel.winfo_height())
        self.canvas_rolavel.configure(scrollregion=(0, 0, largura_total, altura_total))

    def _ao_rolar_mouse(self, event):
        try:
            deslocamento = int(-1 * (event.delta / 120))
            if deslocamento != 0:
                self.canvas_rolavel.yview_scroll(deslocamento, 'units')
        except Exception:
            pass

    def _criar_banco(self):
        self.app.conexao.execute('CREATE TABLE IF NOT EXISTS quebra_excel_coluna (id INTEGER PRIMARY KEY AUTOINCREMENT, qe46_caminho_excel TEXT, qe46_aba TEXT, qe46_coluna TEXT, qe46_pasta_saida TEXT, qe46_nome_geral TEXT, qe46_nome_individual TEXT)')
        colunas_existentes = {linha[1] for linha in self.app.conexao.execute('PRAGMA table_info(quebra_excel_coluna)').fetchall()}
        if 'qe46_caminho_excel' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE quebra_excel_coluna ADD COLUMN qe46_caminho_excel TEXT')
        if 'qe46_aba' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE quebra_excel_coluna ADD COLUMN qe46_aba TEXT')
        if 'qe46_coluna' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE quebra_excel_coluna ADD COLUMN qe46_coluna TEXT')
        if 'qe46_pasta_saida' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE quebra_excel_coluna ADD COLUMN qe46_pasta_saida TEXT')
        if 'qe46_nome_geral' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE quebra_excel_coluna ADD COLUMN qe46_nome_geral TEXT')
        if 'qe46_nome_individual' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE quebra_excel_coluna ADD COLUMN qe46_nome_individual TEXT')
        self.app.conexao.commit()

    def _criar_interface(self):
        self._criar_area_rolavel(1000, 790)
        self.titulo = ttk.Label(self.area, text='Quebrar Planilha do Excel por Coluna', style='Title.TLabel')
        self.titulo.place(x=170, y=20, width=660, height=44)
        self.lbl_excel = ttk.Label(self.area, text='Arquivo do Excel', style='TLabel')
        self.lbl_excel.place(x=45, y=85, width=145, height=28)
        self.var_qe46_caminho_excel = tk.StringVar(value='')
        self.qe46_caminho_excel = ttk.Entry(self.area, textvariable=self.var_qe46_caminho_excel)
        self.qe46_caminho_excel.place(x=190, y=78, width=560, height=34)
        self.qe46_btn_excel = ttk.Button(self.area, text='Selecionar Excel', command=lambda: None)
        self.qe46_btn_excel.place(x=765, y=75, width=190, height=40)
        self.lbl_aba = ttk.Label(self.area, text='Aba de origem', style='TLabel')
        self.lbl_aba.place(x=45, y=135, width=145, height=28)
        self.var_qe46_aba = tk.StringVar()
        self.qe46_aba = ttk.Combobox(self.area, textvariable=self.var_qe46_aba, values=[], state='readonly')
        self.qe46_aba.place(x=190, y=128, width=300, height=34)
        self.lbl_colunas = ttk.Label(self.area, text='Colunas encontradas', style='TLabel')
        self.lbl_colunas.place(x=45, y=185, width=180, height=28)
        self.qe46_lista_colunas = tk.Listbox(self.area, font=('Segoe UI', 10), relief='solid', bd=1, bg=self.app.cor_cartao, fg=self.app.cor_texto)
        self.qe46_lista_colunas.place(x=45, y=218, width=285, height=230)
        self.lbl_coluna_quebra = ttk.Label(self.area, text='Coluna para fazer a quebra', style='TLabel')
        self.lbl_coluna_quebra.place(x=355, y=135, width=220, height=28)
        self.var_qe46_coluna = tk.StringVar()
        self.qe46_coluna = ttk.Combobox(self.area, textvariable=self.var_qe46_coluna, values=[], state='readonly')
        self.qe46_coluna.place(x=575, y=128, width=380, height=34)
        self.qe46_usar_coluna = ttk.Button(self.area, text='Usar coluna selecionada', command=lambda: None)
        self.qe46_usar_coluna.place(x=355, y=178, width=600, height=40)
        self.lbl_resumo = ttk.Label(self.area, text='Resumo dos valores encontrados', style='TLabel')
        self.lbl_resumo.place(x=355, y=235, width=310, height=28)
        self.qe46_resumo = ttk.Treeview(self.area, columns=['qe46_caminho_excel', 'qe46_aba', 'qe46_coluna', 'qe46_pasta_saida', 'qe46_nome_geral', 'qe46_nome_individual'], show='headings')
        self.qe46_resumo.heading('qe46_caminho_excel', text='Arquivo do Excel')
        self.qe46_resumo.column('qe46_caminho_excel', width=140, anchor='w')
        self.qe46_resumo.heading('qe46_aba', text='Aba de origem')
        self.qe46_resumo.column('qe46_aba', width=140, anchor='w')
        self.qe46_resumo.heading('qe46_coluna', text='Coluna para quebra')
        self.qe46_resumo.column('qe46_coluna', width=140, anchor='w')
        self.qe46_resumo.heading('qe46_pasta_saida', text='Pasta de saída')
        self.qe46_resumo.column('qe46_pasta_saida', width=140, anchor='w')
        self.qe46_resumo.heading('qe46_nome_geral', text='Arquivo com várias abas')
        self.qe46_resumo.column('qe46_nome_geral', width=140, anchor='w')
        self.qe46_resumo.heading('qe46_nome_individual', text='Nome dos arquivos separados')
        self.qe46_resumo.column('qe46_nome_individual', width=140, anchor='w')
        self.qe46_resumo.place(x=355, y=270, width=600, height=178)
        self.qe46_resumo.bind('<<TreeviewSelect>>', self.preencher_formulario)
        self.lbl_saida = ttk.Label(self.area, text='Pasta de saída', style='TLabel')
        self.lbl_saida.place(x=45, y=478, width=145, height=28)
        self.var_qe46_pasta_saida = tk.StringVar(value='')
        self.qe46_pasta_saida = ttk.Entry(self.area, textvariable=self.var_qe46_pasta_saida)
        self.qe46_pasta_saida.place(x=190, y=471, width=560, height=34)
        self.qe46_btn_pasta = ttk.Button(self.area, text='Escolher pasta', command=lambda: None)
        self.qe46_btn_pasta.place(x=765, y=468, width=190, height=40)
        self.lbl_nome_geral = ttk.Label(self.area, text='Arquivo com várias abas', style='TLabel')
        self.lbl_nome_geral.place(x=45, y=528, width=195, height=28)
        self.var_qe46_nome_geral = tk.StringVar(value='')
        self.qe46_nome_geral = ttk.Entry(self.area, textvariable=self.var_qe46_nome_geral)
        self.qe46_nome_geral.place(x=240, y=521, width=715, height=34)
        self.lbl_nome_individual = ttk.Label(self.area, text='Nome dos arquivos separados', style='TLabel')
        self.lbl_nome_individual.place(x=45, y=578, width=225, height=28)
        self.var_qe46_nome_individual = tk.StringVar(value='')
        self.qe46_nome_individual = ttk.Entry(self.area, textvariable=self.var_qe46_nome_individual)
        self.qe46_nome_individual.place(x=270, y=571, width=685, height=34)
        self.lbl_modelo_nome = ttk.Label(self.area, text='Use {valor} para o conteúdo da coluna, {coluna} para o nome da coluna e {arquivo} para o nome do Excel original.', style='TLabel')
        self.lbl_modelo_nome.place(x=45, y=615, width=910, height=28)
        self.qe46_btn_abas = ttk.Button(self.area, text='Gerar 1 arquivo com várias abas', command=lambda: None)
        self.qe46_btn_abas.place(x=45, y=665, width=430, height=40)
        self.qe46_btn_arquivos = ttk.Button(self.area, text='Gerar arquivos separados', command=lambda: None)
        self.qe46_btn_arquivos.place(x=495, y=665, width=460, height=40)
        self.qe46_status = ttk.Label(self.area, text='Status: selecione um arquivo do Excel.', style='TLabel')
        self.qe46_status.place(x=45, y=725, width=910, height=28)

        self._configurar_quebra_excel_46()

    def _configurar_quebra_excel_46(self):
        self._qe46_cabecalhos = []
        self._qe46_contagens = {}

        getattr(self, 'qe46_btn_excel').configure(command=self._qe46_selecionar_excel)
        getattr(self, 'qe46_btn_pasta').configure(command=self._qe46_selecionar_pasta)
        getattr(self, 'qe46_usar_coluna').configure(command=self._qe46_usar_coluna)
        getattr(self, 'qe46_btn_abas').configure(command=self._qe46_gerar_arquivo_com_abas)
        getattr(self, 'qe46_btn_arquivos').configure(command=self._qe46_gerar_arquivos_separados)

        combo_aba = getattr(self, 'qe46_aba')
        combo_aba.bind('<<ComboboxSelected>>', lambda e: self._qe46_carregar_colunas())
        combo_coluna = getattr(self, 'qe46_coluna')
        combo_coluna.bind('<<ComboboxSelected>>', lambda e: self._qe46_atualizar_resumo())
        lista = getattr(self, 'qe46_lista_colunas')
        lista.bind('<Double-Button-1>', lambda e: self._qe46_usar_coluna())

        resumo = getattr(self, 'qe46_resumo')
        resumo.configure(columns=('valor', 'quantidade'), show='headings')
        resumo.heading('valor', text='Valor encontrado')
        resumo.heading('quantidade', text='Quantidade de linhas')
        resumo.column('valor', width=390, anchor='w')
        resumo.column('quantidade', width=170, anchor='center')

        if not str(self._valor_componente('qe46_nome_geral')).strip():
            self._definir_valor_componente('qe46_nome_geral', 'Quebra_{coluna}.xlsx')
        if not str(self._valor_componente('qe46_nome_individual')).strip():
            self._definir_valor_componente('qe46_nome_individual', '{valor}_dados.xlsx')
        self._qe46_status('selecione um arquivo do Excel.')

    def _qe46_status(self, texto):
        widget = getattr(self, 'qe46_status', None)
        if widget is not None:
            try:
                widget.configure(text='Status: ' + str(texto))
            except tk.TclError:
                pass

    def _qe_excel_texto_valor(self, valor):
        from datetime import datetime as _dt, date as _date
        if valor is None:
            return ''
        if isinstance(valor, _dt):
            return valor.strftime('%d-%m-%Y_%H-%M-%S')
        if isinstance(valor, _date):
            return valor.strftime('%d-%m-%Y')
        if isinstance(valor, float) and valor.is_integer():
            return str(int(valor))
        return str(valor).strip()

    def _qe_excel_nome_seguro(self, texto, padrao='arquivo'):
        import re as _re
        texto = self._qe_excel_texto_valor(texto).strip()
        texto = _re.sub(r'[<>:"/\\|?*]+', '_', texto)
        texto = _re.sub(r'\s+', ' ', texto).strip(' .')
        if not texto:
            texto = padrao
        reservados = {'CON', 'PRN', 'AUX', 'NUL'} | {f'COM{i}' for i in range(1, 10)} | {f'LPT{i}' for i in range(1, 10)}
        if texto.upper() in reservados:
            texto = '_' + texto
        return texto[:180]

    def _qe_excel_nome_aba(self, texto, usados):
        import re as _re
        nome = self._qe_excel_texto_valor(texto).strip()
        nome = _re.sub(r'[\\/*?:\[\]]+', '_', nome).strip(" '")
        if not nome:
            nome = 'Sem valor'
        nome = nome[:31]
        base = nome
        contador = 2
        while nome.casefold() in usados:
            sufixo = f'_{contador}'
            nome = (base[:31-len(sufixo)] + sufixo)[:31]
            contador += 1
        usados.add(nome.casefold())
        return nome

    def _qe_excel_modelo_nome(self, modelo, valor='', coluna='', arquivo=''):
        texto = str(modelo or '').strip()
        if not texto:
            texto = '{valor}.xlsx'
        trocas = {
            '{valor}': self._qe_excel_nome_seguro(valor, 'Sem_valor'),
            '{coluna}': self._qe_excel_nome_seguro(coluna, 'Coluna'),
            '{arquivo}': self._qe_excel_nome_seguro(arquivo, 'Arquivo'),
        }
        for marcador, conteudo in trocas.items():
            texto = texto.replace(marcador, conteudo)
        texto = self._qe_excel_nome_seguro(texto, 'arquivo.xlsx')
        if not texto.lower().endswith('.xlsx'):
            texto += '.xlsx'
        return texto

    def _qe_excel_copiar_linha(self, origem, destino, linha_origem, linha_destino, max_col):
        from copy import copy
        for coluna in range(1, max_col + 1):
            celula_origem = origem.cell(row=linha_origem, column=coluna)
            celula_destino = destino.cell(row=linha_destino, column=coluna, value=celula_origem.value)
            if celula_origem.has_style:
                celula_destino.font = copy(celula_origem.font)
                celula_destino.fill = copy(celula_origem.fill)
                celula_destino.border = copy(celula_origem.border)
                celula_destino.alignment = copy(celula_origem.alignment)
                celula_destino.protection = copy(celula_origem.protection)
                celula_destino.number_format = celula_origem.number_format
            if celula_origem.hyperlink:
                celula_destino._hyperlink = copy(celula_origem.hyperlink)
            if celula_origem.comment:
                celula_destino.comment = copy(celula_origem.comment)
        altura = origem.row_dimensions[linha_origem].height
        if altura is not None:
            destino.row_dimensions[linha_destino].height = altura

    def _qe_excel_copiar_configuracao(self, origem, destino, ultima_linha, max_col):
        from copy import copy
        from openpyxl.utils import get_column_letter
        for coluna in range(1, max_col + 1):
            letra = get_column_letter(coluna)
            dimensao = origem.column_dimensions.get(letra)
            if dimensao is not None and dimensao.width is not None:
                destino.column_dimensions[letra].width = dimensao.width
        destino.freeze_panes = origem.freeze_panes
        destino.sheet_view.showGridLines = origem.sheet_view.showGridLines
        try:
            destino.sheet_properties.tabColor = copy(origem.sheet_properties.tabColor)
        except Exception:
            pass
        if ultima_linha >= 1 and max_col >= 1:
            destino.auto_filter.ref = f'A1:{get_column_letter(max_col)}{ultima_linha}'

    def _qe46_selecionar_excel(self):
        try:
            from openpyxl import load_workbook
        except ImportError:
            messagebox.showerror('Excel', 'Para usar este projeto, instale a biblioteca openpyxl com:\n\npip install openpyxl')
            return
        caminho = filedialog.askopenfilename(
            parent=self,
            title='Selecionar arquivo do Excel',
            filetypes=[('Planilhas do Excel', '*.xlsx *.xlsm'), ('Arquivo .xlsx', '*.xlsx'), ('Todos os arquivos', '*.*')],
        )
        if not caminho:
            return
        self._definir_valor_componente('qe46_caminho_excel', caminho)
        try:
            wb = load_workbook(caminho, read_only=True, data_only=False)
            abas = list(wb.sheetnames)
            wb.close()
        except Exception as erro:
            messagebox.showerror('Excel', f'Não foi possível abrir o arquivo.\n\n{erro}')
            return
        combo = getattr(self, 'qe46_aba')
        combo.configure(values=abas)
        if abas:
            self._definir_valor_componente('qe46_aba', abas[0])
            self._qe46_carregar_colunas()
        pasta_padrao = os.path.join(os.path.dirname(caminho), 'Arquivos_Quebrados')
        if not str(self._valor_componente('qe46_pasta_saida')).strip():
            self._definir_valor_componente('qe46_pasta_saida', pasta_padrao)
        self._qe46_status(f'{len(abas)} aba(s) encontrada(s).')

    def _qe46_carregar_colunas(self):
        try:
            from openpyxl import load_workbook
        except ImportError:
            return
        caminho = str(self._valor_componente('qe46_caminho_excel')).strip()
        aba = str(self._valor_componente('qe46_aba')).strip()
        if not caminho or not aba:
            return
        try:
            wb = load_workbook(caminho, read_only=True, data_only=False)
            ws = wb[aba]
            primeira = next(ws.iter_rows(min_row=1, max_row=1, values_only=True), ())
            cabecalhos = []
            usados = {}
            for indice, valor in enumerate(primeira, 1):
                nome = str(valor).strip() if valor not in (None, '') else f'Coluna_{indice}'
                qtd = usados.get(nome.casefold(), 0) + 1
                usados[nome.casefold()] = qtd
                if qtd > 1:
                    nome = f'{nome}_{qtd}'
                cabecalhos.append(nome)
            wb.close()
        except Exception as erro:
            messagebox.showerror('Excel', f'Não foi possível ler os cabeçalhos.\n\n{erro}')
            return
        self._qe46_cabecalhos = cabecalhos
        lista = getattr(self, 'qe46_lista_colunas')
        lista.delete(0, tk.END)
        for nome in cabecalhos:
            lista.insert(tk.END, nome)
        combo = getattr(self, 'qe46_coluna')
        combo.configure(values=cabecalhos)
        if cabecalhos:
            self._definir_valor_componente('qe46_coluna', cabecalhos[0])
            self._qe46_atualizar_resumo()
        self._qe46_status(f'{len(cabecalhos)} coluna(s) encontrada(s) na aba {aba}.')

    def _qe46_usar_coluna(self):
        lista = getattr(self, 'qe46_lista_colunas')
        selecao = lista.curselection()
        if not selecao:
            messagebox.showinfo('Coluna', 'Selecione uma coluna na lista.')
            return
        coluna = str(lista.get(selecao[0]))
        self._definir_valor_componente('qe46_coluna', coluna)
        self._qe46_atualizar_resumo()

    def _qe46_coluna_indice(self, cabecalhos, selecionada):
        alvo = str(selecionada).strip().casefold()
        for indice, nome in enumerate(cabecalhos, 1):
            if str(nome).strip().casefold() == alvo:
                return indice
        return None

    def _qe46_atualizar_resumo(self):
        try:
            from openpyxl import load_workbook
        except ImportError:
            return
        caminho = str(self._valor_componente('qe46_caminho_excel')).strip()
        aba = str(self._valor_componente('qe46_aba')).strip()
        coluna = str(self._valor_componente('qe46_coluna')).strip()
        if not caminho or not aba or not coluna:
            return
        try:
            wb = load_workbook(caminho, read_only=True, data_only=True)
            ws = wb[aba]
            cabecalhos = list(self._qe46_cabecalhos)
            indice = self._qe46_coluna_indice(cabecalhos, coluna)
            if indice is None:
                wb.close()
                return
            contagens = {}
            for linha in ws.iter_rows(min_row=2, values_only=True):
                valor = linha[indice - 1] if indice - 1 < len(linha) else None
                texto = self._qe_excel_texto_valor(valor)
                if not texto:
                    continue
                contagens[texto] = contagens.get(texto, 0) + 1
            wb.close()
        except Exception as erro:
            messagebox.showerror('Excel', f'Não foi possível analisar a coluna.\n\n{erro}')
            return
        self._qe46_contagens = contagens
        tree = getattr(self, 'qe46_resumo')
        for item in tree.get_children():
            tree.delete(item)
        for valor in sorted(contagens, key=lambda x: x.casefold()):
            tree.insert('', tk.END, values=(valor, contagens[valor]))
        self._qe46_status(f'{len(contagens)} valor(es) diferente(s) encontrado(s); {sum(contagens.values())} linha(s) serão consideradas.')

    def _qe46_selecionar_pasta(self):
        pasta = filedialog.askdirectory(parent=self, title='Selecionar pasta de saída')
        if pasta:
            self._definir_valor_componente('qe46_pasta_saida', pasta)

    def _qe46_obter_dados_quebra(self, data_only=False):
        from openpyxl import load_workbook
        caminho = str(self._valor_componente('qe46_caminho_excel')).strip()
        aba = str(self._valor_componente('qe46_aba')).strip()
        coluna = str(self._valor_componente('qe46_coluna')).strip()
        if not caminho or not os.path.isfile(caminho):
            raise ValueError('Selecione um arquivo do Excel válido.')
        if not aba:
            raise ValueError('Escolha a aba de origem.')
        if not coluna:
            raise ValueError('Escolha a coluna usada para fazer a quebra.')
        wb = load_workbook(caminho, data_only=data_only)
        if aba not in wb.sheetnames:
            wb.close()
            raise ValueError('A aba escolhida não existe mais no arquivo.')
        ws = wb[aba]
        cabecalhos_reais = []
        usados = {}
        for indice in range(1, ws.max_column + 1):
            valor = ws.cell(row=1, column=indice).value
            nome = str(valor).strip() if valor not in (None, '') else f'Coluna_{indice}'
            qtd = usados.get(nome.casefold(), 0) + 1
            usados[nome.casefold()] = qtd
            if qtd > 1:
                nome = f'{nome}_{qtd}'
            cabecalhos_reais.append(nome)
        indice_coluna = self._qe46_coluna_indice(cabecalhos_reais, coluna)
        if indice_coluna is None:
            wb.close()
            raise ValueError(f'A coluna {coluna} não foi encontrada na aba {aba}.')
        grupos = {}
        for numero_linha in range(2, ws.max_row + 1):
            valor = ws.cell(row=numero_linha, column=indice_coluna).value
            texto = self._qe_excel_texto_valor(valor)
            if not texto:
                continue
            grupos.setdefault(texto, []).append(numero_linha)
        if not grupos:
            wb.close()
            raise ValueError('Nenhum valor preenchido foi encontrado na coluna escolhida.')
        return wb, ws, coluna, grupos

    def _qe46_gerar_arquivo_com_abas(self):
        try:
            from openpyxl import Workbook
            wb_origem, ws_origem, coluna, grupos = self._qe46_obter_dados_quebra(data_only=False)
        except ImportError:
            messagebox.showerror('Excel', 'Instale a biblioteca openpyxl com:\n\npip install openpyxl')
            return
        except Exception as erro:
            messagebox.showwarning('Quebra do Excel', str(erro))
            return
        pasta = str(self._valor_componente('qe46_pasta_saida')).strip()
        if not pasta:
            wb_origem.close()
            messagebox.showwarning('Pasta de saída', 'Escolha a pasta onde o arquivo será criado.')
            return
        os.makedirs(pasta, exist_ok=True)
        arquivo_base = os.path.splitext(os.path.basename(str(self._valor_componente('qe46_caminho_excel'))))[0]
        nome_modelo = str(self._valor_componente('qe46_nome_geral')).strip()
        nome_saida = self._qe_excel_modelo_nome(nome_modelo, valor='Todos', coluna=coluna, arquivo=arquivo_base)
        caminho_saida = os.path.join(pasta, nome_saida)
        if os.path.exists(caminho_saida) and not messagebox.askyesno('Sobrescrever arquivo', f'O arquivo já existe:\n\n{caminho_saida}\n\nDeseja substituí-lo?'):
            wb_origem.close()
            return
        try:
            wb_saida = Workbook()
            wb_saida.remove(wb_saida.active)
            usados = set()
            total = len(grupos)
            for posicao, (valor, linhas) in enumerate(grupos.items(), 1):
                self._qe46_status(f'criando aba {posicao} de {total}: {valor}')
                self.update_idletasks()
                titulo = self._qe_excel_nome_aba(valor, usados)
                ws_saida = wb_saida.create_sheet(titulo)
                self._qe_excel_copiar_linha(ws_origem, ws_saida, 1, 1, ws_origem.max_column)
                destino = 2
                for linha in linhas:
                    self._qe_excel_copiar_linha(ws_origem, ws_saida, linha, destino, ws_origem.max_column)
                    destino += 1
                self._qe_excel_copiar_configuracao(ws_origem, ws_saida, destino - 1, ws_origem.max_column)
            wb_saida.save(caminho_saida)
            wb_saida.close()
            wb_origem.close()
        except Exception as erro:
            try:
                wb_origem.close()
            except Exception:
                pass
            messagebox.showerror('Quebra do Excel', f'Não foi possível gerar o arquivo.\n\n{erro}')
            return
        self._qe46_status(f'arquivo criado com {len(grupos)} aba(s).')
        messagebox.showinfo('Quebra concluída', f'Arquivo criado com sucesso:\n\n{caminho_saida}\n\nAbas criadas: {len(grupos)}')

    def _qe46_gerar_arquivos_separados(self):
        try:
            from openpyxl import Workbook
            wb_origem, ws_origem, coluna, grupos = self._qe46_obter_dados_quebra(data_only=False)
        except ImportError:
            messagebox.showerror('Excel', 'Instale a biblioteca openpyxl com:\n\npip install openpyxl')
            return
        except Exception as erro:
            messagebox.showwarning('Quebra do Excel', str(erro))
            return
        pasta = str(self._valor_componente('qe46_pasta_saida')).strip()
        if not pasta:
            wb_origem.close()
            messagebox.showwarning('Pasta de saída', 'Escolha a pasta onde os arquivos serão criados.')
            return
        os.makedirs(pasta, exist_ok=True)
        arquivo_base = os.path.splitext(os.path.basename(str(self._valor_componente('qe46_caminho_excel'))))[0]
        modelo = str(self._valor_componente('qe46_nome_individual')).strip()
        caminhos = []
        nomes_usados = set()
        for valor in grupos:
            nome = self._qe_excel_modelo_nome(modelo, valor=valor, coluna=coluna, arquivo=arquivo_base)
            base, ext = os.path.splitext(nome)
            candidato = nome
            numero = 2
            while candidato.casefold() in nomes_usados:
                candidato = f'{base}_{numero}{ext}'
                numero += 1
            nomes_usados.add(candidato.casefold())
            caminhos.append((valor, candidato, os.path.join(pasta, candidato)))
        existentes = [caminho for _valor, _nome, caminho in caminhos if os.path.exists(caminho)]
        if existentes and not messagebox.askyesno('Sobrescrever arquivos', f'{len(existentes)} arquivo(s) já existem na pasta de saída.\n\nDeseja substituí-los?'):
            wb_origem.close()
            return
        try:
            total = len(caminhos)
            nome_aba = self._qe_excel_nome_aba(ws_origem.title, set())
            for posicao, (valor, _nome, caminho_saida) in enumerate(caminhos, 1):
                self._qe46_status(f'criando arquivo {posicao} de {total}: {valor}')
                self.update_idletasks()
                wb_saida = Workbook()
                ws_saida = wb_saida.active
                ws_saida.title = nome_aba
                self._qe_excel_copiar_linha(ws_origem, ws_saida, 1, 1, ws_origem.max_column)
                destino = 2
                for linha in grupos[valor]:
                    self._qe_excel_copiar_linha(ws_origem, ws_saida, linha, destino, ws_origem.max_column)
                    destino += 1
                self._qe_excel_copiar_configuracao(ws_origem, ws_saida, destino - 1, ws_origem.max_column)
                wb_saida.save(caminho_saida)
                wb_saida.close()
            wb_origem.close()
        except Exception as erro:
            try:
                wb_origem.close()
            except Exception:
                pass
            messagebox.showerror('Quebra do Excel', f'Não foi possível gerar os arquivos.\n\n{erro}')
            return
        self._qe46_status(f'{len(caminhos)} arquivo(s) separado(s) criado(s).')
        messagebox.showinfo('Quebra concluída', f'Foram criados {len(caminhos)} arquivo(s) em:\n\n{pasta}')

    def _valor_componente(self, nome):
        variavel = getattr(self, f'var_{nome}', None)
        if variavel is not None:
            return variavel.get()
        widget = getattr(self, nome, None)
        if isinstance(widget, tk.Text):
            return widget.get('1.0', 'end-1c')
        if isinstance(widget, tk.Listbox):
            selecao = widget.curselection()
            if selecao:
                return widget.get(selecao[0])
            return '\n'.join(widget.get(0, tk.END))
        return ''

    def _definir_valor_componente(self, nome, valor):
        valor = '' if valor is None else valor
        variavel = getattr(self, f'var_{nome}', None)
        if variavel is not None:
            variavel.set(valor)
            return True
        widget = getattr(self, nome, None)
        if isinstance(widget, tk.Text):
            widget.delete('1.0', tk.END)
            texto = '\n'.join(str(x) for x in valor) if isinstance(valor, (list, tuple)) else str(valor)
            widget.insert('1.0', texto)
            return True
        if isinstance(widget, tk.Listbox):
            widget.delete(0, tk.END)
            itens = valor if isinstance(valor, (list, tuple)) else str(valor).splitlines()
            for item in itens:
                widget.insert(tk.END, item)
            return True
        return False

    def _atualizar_contadores(self):
        pass

    def exportar_dados_excel(self, alvos=None):
        try:
            from openpyxl import Workbook
        except ImportError:
            messagebox.showerror('Excel', 'Para exportar arquivos .xlsx, instale a biblioteca openpyxl com: pip install openpyxl')
            return
        nomes = list(alvos or [])
        if not nomes:
            nomes = [nome for nome, widget in self.__dict__.items() if isinstance(widget, (ttk.Treeview, tk.Listbox))]
        fontes = [(nome, getattr(self, nome, None)) for nome in nomes]
        fontes = [(nome, widget) for nome, widget in fontes if isinstance(widget, (ttk.Treeview, tk.Listbox))]
        if not fontes:
            messagebox.showwarning('Excel', 'Selecione uma Treeview ou uma Listbox nos Campos da ação.')
            return
        caminho = filedialog.asksaveasfilename(parent=self, title='Exportar para Excel', defaultextension='.xlsx', filetypes=[('Arquivo do Excel', '*.xlsx')])
        if not caminho:
            return
        wb = Workbook()
        wb.remove(wb.active)
        def valor_seguro(valor):
            if isinstance(valor, str) and valor[:1] in ('=', '+', '-', '@'):
                return "'" + valor
            return valor
        for indice, (nome, widget) in enumerate(fontes, 1):
            titulo = re.sub(r'[:\\/?*\[\]]', '_', str(nome))[:31] or f'Dados{indice}'
            base = titulo
            contador = 2
            while titulo in wb.sheetnames:
                sufixo = f'_{contador}'
                titulo = base[:31-len(sufixo)] + sufixo
                contador += 1
            ws = wb.create_sheet(titulo)
            if isinstance(widget, ttk.Treeview):
                colunas = list(widget['columns'])
                cabecalhos = [widget.heading(coluna, 'text') or str(coluna) for coluna in colunas]
                ws.append(cabecalhos)
                for item in widget.get_children():
                    ws.append([valor_seguro(v) for v in widget.item(item, 'values')])
            else:
                ws.append(['Item'])
                for item in widget.get(0, tk.END):
                    ws.append([valor_seguro(item)])
            for coluna in ws.columns:
                letra = coluna[0].column_letter
                maior = max((len(str(celula.value or '')) for celula in coluna), default=10)
                ws.column_dimensions[letra].width = min(max(maior + 2, 12), 60)
        try:
            wb.save(caminho)
        except OSError as erro:
            messagebox.showerror('Excel', f'Não foi possível salvar o arquivo: {erro}')
            return
        messagebox.showinfo('Excel', 'Dados exportados para o Excel com sucesso!')

    def _formatar_tempo(self, segundos):
        segundos = max(0.0, float(segundos))
        horas = int(segundos // 3600)
        minutos = int((segundos % 3600) // 60)
        resto = segundos % 60
        return f'{horas:02d}:{minutos:02d}:{resto:04.1f}'

    def cronometro_iniciar(self, destino):
        if getattr(self, '_cronometro_rodando', False):
            return
        self._cronometro_rodando = True
        self._cronometro_acumulado = float(getattr(self, '_cronometro_acumulado', 0.0))
        self._cronometro_inicio = time.perf_counter()
        self._cronometro_tick(destino)

    def _cronometro_tick(self, destino):
        if not getattr(self, '_cronometro_rodando', False):
            return
        atual = self._cronometro_acumulado + (time.perf_counter() - self._cronometro_inicio)
        self._definir_valor_componente(destino, self._formatar_tempo(atual))
        self.after(100, lambda: self._cronometro_tick(destino))

    def cronometro_pausar(self, destino):
        if getattr(self, '_cronometro_rodando', False):
            self._cronometro_acumulado += time.perf_counter() - self._cronometro_inicio
        self._cronometro_rodando = False
        self._definir_valor_componente(destino, self._formatar_tempo(getattr(self, '_cronometro_acumulado', 0.0)))

    def cronometro_zerar(self, destino):
        self._cronometro_rodando = False
        self._cronometro_acumulado = 0.0
        self._definir_valor_componente(destino, '00:00:00.0')

    def temporizador_iniciar(self, origem, destino):
        if getattr(self, '_temporizador_rodando', False):
            return
        try:
            valor = int(float(str(self._valor_componente(origem)).replace(',', '.')))
        except (TypeError, ValueError):
            valor = 0
        if valor <= 0:
            messagebox.showwarning('Temporizador', 'Informe uma quantidade de segundos maior que zero.')
            return
        self._temporizador_restante = valor
        self._temporizador_rodando = True
        self._temporizador_tick(destino)

    def _temporizador_tick(self, destino):
        if not getattr(self, '_temporizador_rodando', False):
            return
        restante = int(getattr(self, '_temporizador_restante', 0))
        self._definir_valor_componente(destino, self._formatar_tempo(restante))
        if restante <= 0:
            self._temporizador_rodando = False
            messagebox.showinfo('Temporizador', 'Tempo encerrado!')
            return
        self._temporizador_restante = restante - 1
        self.after(1000, lambda: self._temporizador_tick(destino))

    def temporizador_pausar(self, destino):
        self._temporizador_rodando = False
        self._definir_valor_componente(destino, self._formatar_tempo(getattr(self, '_temporizador_restante', 0)))

    def temporizador_zerar(self, destino):
        self._temporizador_rodando = False
        self._temporizador_restante = 0
        self._definir_valor_componente(destino, '00:00:00.0')

    def gerar_senha_segura(self, campo_tamanho, campo_simbolos, destino):
        try:
            tamanho = int(float(str(self._valor_componente(campo_tamanho)).replace(',', '.')))
        except (TypeError, ValueError):
            tamanho = 12
        tamanho = min(max(tamanho, 8), 128)
        usar_simbolos = bool(self._valor_componente(campo_simbolos)) if campo_simbolos else True
        alfabeto = string.ascii_letters + string.digits
        if usar_simbolos:
            alfabeto += '!@#$%&*_-+=?'
        senha = ''.join(secrets.choice(alfabeto) for _ in range(tamanho))
        self._definir_valor_componente(destino, senha)

    def calcular_idade_completa(self, origem, destino):
        texto = str(self._valor_componente(origem)).strip()
        try:
            nascimento = datetime.strptime(texto, '%d/%m/%Y').date()
        except ValueError:
            messagebox.showwarning('Idade', 'Informe a data de nascimento no formato dd/mm/aaaa.')
            return
        hoje = date.today()
        if nascimento > hoje:
            messagebox.showwarning('Idade', 'A data de nascimento não pode estar no futuro.')
            return
        anos = hoje.year - nascimento.year
        meses = hoje.month - nascimento.month
        dias = hoje.day - nascimento.day
        if dias < 0:
            meses -= 1
            mes_anterior = hoje.month - 1 or 12
            ano_mes_anterior = hoje.year if hoje.month > 1 else hoje.year - 1
            dias += calendar.monthrange(ano_mes_anterior, mes_anterior)[1]
        if meses < 0:
            anos -= 1
            meses += 12
        self._definir_valor_componente(destino, f'{anos} anos, {meses} meses e {dias} dias')

    def sortear_nome(self, origem, destino):
        widget = getattr(self, origem, None)
        if isinstance(widget, tk.Listbox):
            nomes = [str(x).strip() for x in widget.get(0, tk.END) if str(x).strip()]
        else:
            nomes = [x.strip() for x in str(self._valor_componente(origem)).splitlines() if x.strip()]
        if not nomes:
            messagebox.showwarning('Sorteio', 'A lista de nomes está vazia.')
            return
        self._definir_valor_componente(destino, random.choice(nomes))

    def gerar_numeros_sorteio(self, origem, destino):
        try:
            quantidade = int(float(str(self._valor_componente(origem)).replace(',', '.')))
        except (TypeError, ValueError):
            quantidade = 6
        if quantidade <= 0:
            quantidade = 6
        quantidade = min(quantidade, 60)
        numeros = sorted(random.sample(range(1, 61), quantidade))
        self._definir_valor_componente(destino, [f'{numero:02d}' for numero in numeros])
        self._atualizar_contadores()

    def testar_barra_progresso(self, origem, destino, label_percentual=''):
        try:
            alvo = int(float(str(self._valor_componente(origem)).replace(',', '.')))
        except (TypeError, ValueError):
            messagebox.showwarning('Progresso', 'Informe um número de 0 a 100.')
            return
        alvo = max(0, min(100, alvo))
        barra = getattr(self, destino, None)
        if not isinstance(barra, ttk.Progressbar):
            messagebox.showwarning('Progresso', 'Selecione uma Progressbar em Campo de resultado.')
            return
        self._progresso_execucao = int(getattr(self, '_progresso_execucao', 0)) + 1
        execucao = self._progresso_execucao
        try:
            atual = int(float(barra['value']))
        except (TypeError, ValueError):
            atual = 0
        passo = 1 if alvo >= atual else -1
        def atualizar(valor):
            if execucao != getattr(self, '_progresso_execucao', 0):
                return
            barra['value'] = valor
            rotulo = getattr(self, label_percentual, None) if label_percentual else None
            if rotulo is not None and hasattr(rotulo, 'configure'):
                rotulo.configure(text=f'{valor}% concluído')
            if valor == alvo:
                return
            self.after(25, lambda: atualizar(valor + passo))
        atualizar(atual)

    def _iniciar_desenho(self, nome_canvas, evento):
        canvas = getattr(self, nome_canvas, None)
        if not isinstance(canvas, tk.Canvas):
            return
        canvas.delete('instrucao')
        if not hasattr(self, '_pontos_desenho'):
            self._pontos_desenho = {}
        self._pontos_desenho[nome_canvas] = (evento.x, evento.y)

    def _continuar_desenho(self, nome_canvas, evento):
        canvas = getattr(self, nome_canvas, None)
        if not isinstance(canvas, tk.Canvas):
            return
        pontos = getattr(self, '_pontos_desenho', {})
        anterior = pontos.get(nome_canvas)
        if anterior is None:
            anterior = (evento.x, evento.y)
        cor = getattr(canvas, '_cor_lapis', '#233247')
        canvas.create_line(anterior[0], anterior[1], evento.x, evento.y, fill=cor, width=3, capstyle=tk.ROUND, smooth=True, tags=('desenho',))
        pontos[nome_canvas] = (evento.x, evento.y)
        self._pontos_desenho = pontos

    def _finalizar_desenho(self, nome_canvas, evento=None):
        pontos = getattr(self, '_pontos_desenho', {})
        pontos.pop(nome_canvas, None)
        self._pontos_desenho = pontos

    def limpar_area_desenho(self, nome_canvas):
        canvas = getattr(self, nome_canvas, None)
        if not isinstance(canvas, tk.Canvas):
            messagebox.showwarning('Desenho', 'Selecione um Canvas em Campo de resultado.')
            return
        canvas.delete('desenho')
        canvas.delete('instrucao')
        texto = getattr(canvas, '_texto_instrucao', 'Arraste o mouse para desenhar')
        cor = getattr(canvas, '_cor_lapis', '#233247')
        canvas.update_idletasks()
        largura = max(1, canvas.winfo_width())
        altura = max(1, canvas.winfo_height())
        canvas.create_text(largura // 2, altura // 2, text=texto, fill=cor, anchor='center', tags=('instrucao',))

    def listbox_adicionar_item(self, origem, destino):
        lista = getattr(self, destino, None)
        if not isinstance(lista, tk.Listbox):
            messagebox.showwarning('Listbox', 'Selecione uma Listbox em Campo de resultado.')
            return
        valor = str(self._valor_componente(origem)).strip() if origem else ''
        if not valor:
            messagebox.showwarning('Listbox', 'Digite o item que deseja incluir.')
            return
        lista.insert(tk.END, valor)
        self._definir_valor_componente(origem, '')
        lista.see(tk.END)
        self._atualizar_contadores()

    def listbox_excluir_selecionado(self, destino):
        lista = getattr(self, destino, None)
        if not isinstance(lista, tk.Listbox):
            messagebox.showwarning('Listbox', 'Selecione uma Listbox em Campo de resultado.')
            return
        selecionados = list(lista.curselection())
        if not selecionados:
            messagebox.showwarning('Listbox', 'Selecione um item da lista para excluir.')
            return
        for indice in reversed(selecionados):
            lista.delete(indice)
        self._atualizar_contadores()

    def listbox_limpar(self, destino):
        lista = getattr(self, destino, None)
        if not isinstance(lista, tk.Listbox):
            messagebox.showwarning('Listbox', 'Selecione uma Listbox em Campo de resultado.')
            return
        lista.delete(0, tk.END)
        self._atualizar_contadores()

    def listbox_gerar_sequencia(self, origem, destino):
        lista = getattr(self, destino, None)
        if not isinstance(lista, tk.Listbox):
            messagebox.showwarning('Listbox', 'Selecione uma Listbox em Campo de resultado.')
            return
        try:
            quantidade = int(float(str(self._valor_componente(origem)).replace(',', '.')))
        except (TypeError, ValueError):
            messagebox.showwarning('Listbox', 'Informe uma quantidade numérica maior que zero.')
            return
        if quantidade <= 0:
            messagebox.showwarning('Listbox', 'Informe uma quantidade maior que zero.')
            return
        lista.delete(0, tk.END)
        for numero in range(1, quantidade + 1):
            lista.insert(tk.END, str(numero))
        if quantidade:
            lista.see(tk.END)
            lista.see(0)
        self._atualizar_contadores()

    def texto_contar(self, origem, destino):
        texto = str(self._valor_componente(origem))
        palavras = re.findall(r'\b\w+\b', texto, flags=re.UNICODE)
        caracteres = len(texto)
        sem_espacos = len(re.sub(r'\s', '', texto))
        linhas = 0 if not texto else len(texto.splitlines())
        resultado = f'Palavras: {len(palavras)}\nCaracteres com espaços: {caracteres}\nCaracteres sem espaços: {sem_espacos}\nLinhas: {linhas}'
        self._definir_valor_componente(destino, resultado)

    def texto_localizar_substituir(self, origem, campo_localizar, campo_substituir, destino, destino_contador=''):
        texto = str(self._valor_componente(origem))
        localizar = str(self._valor_componente(campo_localizar))
        substituir = str(self._valor_componente(campo_substituir))
        if not localizar:
            messagebox.showwarning('Texto', 'Informe o texto que deseja localizar.')
            return
        quantidade = texto.count(localizar)
        novo_texto = texto.replace(localizar, substituir)
        self._definir_valor_componente(destino, novo_texto)
        if destino_contador:
            self._definir_valor_componente(destino_contador, str(quantidade))

    def arquivo_txt_abrir(self, destino, destino_caminho=''):
        caminho = filedialog.askopenfilename(parent=self, title='Abrir arquivo TXT', filetypes=[('Arquivo de texto', '*.txt'), ('Todos os arquivos', '*.*')])
        if not caminho:
            return
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
        except UnicodeDecodeError:
            try:
                with open(caminho, 'r', encoding='latin-1') as arquivo:
                    conteudo = arquivo.read()
            except OSError as erro:
                messagebox.showerror('Arquivo TXT', f'Não foi possível abrir o arquivo: {erro}')
                return
        except OSError as erro:
            messagebox.showerror('Arquivo TXT', f'Não foi possível abrir o arquivo: {erro}')
            return
        self._definir_valor_componente(destino, conteudo)
        if destino_caminho:
            self._definir_valor_componente(destino_caminho, caminho)

    def arquivo_txt_salvar(self, origem, campo_caminho=''):
        conteudo = str(self._valor_componente(origem))
        caminho_atual = str(self._valor_componente(campo_caminho)).strip() if campo_caminho else ''
        if caminho_atual:
            caminho = filedialog.asksaveasfilename(parent=self, title='Salvar arquivo TXT', initialfile=caminho_atual.split('/')[-1].split('\\')[-1], defaultextension='.txt', filetypes=[('Arquivo de texto', '*.txt'), ('Todos os arquivos', '*.*')])
        else:
            caminho = filedialog.asksaveasfilename(parent=self, title='Salvar arquivo TXT', defaultextension='.txt', filetypes=[('Arquivo de texto', '*.txt'), ('Todos os arquivos', '*.*')])
        if not caminho:
            return
        try:
            with open(caminho, 'w', encoding='utf-8') as arquivo:
                arquivo.write(conteudo)
        except OSError as erro:
            messagebox.showerror('Arquivo TXT', f'Não foi possível salvar o arquivo: {erro}')
            return
        if campo_caminho:
            self._definir_valor_componente(campo_caminho, caminho)
        messagebox.showinfo('Arquivo TXT', 'Arquivo salvo com sucesso!')

    def datas_calcular_intervalo(self, campo_inicio, campo_fim, destino):
        inicio_texto = str(self._valor_componente(campo_inicio)).strip()
        fim_texto = str(self._valor_componente(campo_fim)).strip()
        try:
            inicio = datetime.strptime(inicio_texto, '%d/%m/%Y').date()
            fim = datetime.strptime(fim_texto, '%d/%m/%Y').date()
        except ValueError:
            messagebox.showwarning('Datas', 'Informe as duas datas no formato dd/mm/aaaa.')
            return
        sinal = 1 if fim >= inicio else -1
        dias = abs((fim - inicio).days)
        semanas, dias_restantes = divmod(dias, 7)
        ordem = 'depois' if sinal >= 0 else 'antes'
        resultado = f'Dias corridos: {dias}\nSemanas completas: {semanas}\nDias restantes: {dias_restantes}\nA data final está {dias} dia(s) {ordem} da data inicial.'
        self._definir_valor_componente(destino, resultado)

    def listbox_ordenar(self, destino, reverso=False):
        lista = getattr(self, destino, None)
        if not isinstance(lista, tk.Listbox):
            messagebox.showwarning('Listbox', 'Selecione uma Listbox em Campo de resultado.')
            return
        itens = list(lista.get(0, tk.END))
        itens.sort(key=lambda item: str(item).casefold(), reverse=bool(reverso))
        lista.delete(0, tk.END)
        for item in itens:
            lista.insert(tk.END, item)
        self._atualizar_contadores()

    def listbox_remover_duplicados(self, destino):
        lista = getattr(self, destino, None)
        if not isinstance(lista, tk.Listbox):
            messagebox.showwarning('Listbox', 'Selecione uma Listbox em Campo de resultado.')
            return
        vistos = set()
        unicos = []
        for item in lista.get(0, tk.END):
            chave = str(item).casefold()
            if chave not in vistos:
                vistos.add(chave)
                unicos.append(item)
        lista.delete(0, tk.END)
        for item in unicos:
            lista.insert(tk.END, item)
        self._atualizar_contadores()

    def csv_importar_treeview(self, destino, destino_status=''):
        tabela = getattr(self, destino, None)
        if not isinstance(tabela, ttk.Treeview):
            messagebox.showwarning('CSV', 'Selecione uma Treeview em Campo de resultado.')
            return
        caminho = filedialog.askopenfilename(parent=self, title='Selecionar arquivo CSV', filetypes=[('Arquivo CSV', '*.csv'), ('Todos os arquivos', '*.*')])
        if not caminho:
            return
        linhas = None
        ultimo_erro = None
        for codificacao in ('utf-8-sig', 'utf-8', 'latin-1'):
            try:
                with open(caminho, 'r', encoding=codificacao, newline='') as arquivo:
                    amostra = arquivo.read(4096)
                    arquivo.seek(0)
                    try:
                        dialeto = csv.Sniffer().sniff(amostra, delimiters=',;\t|')
                        leitor = csv.reader(arquivo, dialeto)
                    except csv.Error:
                        leitor = csv.reader(arquivo, delimiter=';')
                    linhas = list(leitor)
                break
            except (UnicodeDecodeError, OSError) as erro:
                ultimo_erro = erro
        if linhas is None:
            messagebox.showerror('CSV', f'Não foi possível abrir o arquivo: {ultimo_erro}')
            return
        linhas = [linha for linha in linhas if any(str(valor).strip() for valor in linha)]
        if not linhas:
            messagebox.showwarning('CSV', 'O arquivo CSV está vazio.')
            return
        cabecalhos = [str(valor).strip() or f'Coluna {indice + 1}' for indice, valor in enumerate(linhas[0])]
        ids = [f'csv_{indice}' for indice in range(len(cabecalhos))]
        tabela.delete(*tabela.get_children())
        tabela['columns'] = ids
        tabela['show'] = 'headings'
        for coluna, titulo in zip(ids, cabecalhos):
            tabela.heading(coluna, text=titulo)
            tabela.column(coluna, width=max(90, min(240, len(titulo) * 12 + 35)), anchor='w')
        total = 0
        for linha in linhas[1:]:
            valores = list(linha[:len(ids)]) + [''] * max(0, len(ids) - len(linha))
            tabela.insert('', 'end', values=valores[:len(ids)])
            total += 1
        if destino_status:
            self._definir_valor_componente(destino_status, f'{total} linha(s) importada(s) | {len(ids)} coluna(s)')

    def lista_calcular_estatisticas(self, origem, destino):
        texto = str(self._valor_componente(origem)).strip()
        partes = [p for p in re.split(r'[;,\s]+', texto) if p]
        numeros = []
        invalidos = []
        for parte in partes:
            try:
                numeros.append(float(parte.replace(',', '.')))
            except ValueError:
                invalidos.append(parte)
        if not numeros:
            messagebox.showwarning('Estatísticas', 'Informe pelo menos um número válido.')
            return
        total = sum(numeros)
        media = total / len(numeros)
        ordenados = sorted(numeros)
        meio = len(ordenados) // 2
        mediana = ordenados[meio] if len(ordenados) % 2 else (ordenados[meio - 1] + ordenados[meio]) / 2
        resultado = f'Quantidade: {len(numeros)}\nSoma: {total:g}\nMédia: {media:.2f}\nMediana: {mediana:g}\nMenor: {min(numeros):g}\nMaior: {max(numeros):g}'
        if invalidos:
            resultado += '\nIgnorados: ' + ', '.join(invalidos[:10])
        self._definir_valor_componente(destino, resultado)

    def texto_converter(self, origem, destino, modo):
        texto = str(self._valor_componente(origem))
        if modo == 'maiusculas':
            resultado = texto.upper()
        elif modo == 'minusculas':
            resultado = texto.lower()
        else:
            resultado = texto.title()
        self._definir_valor_componente(destino, resultado)

    def calendario_gerar_mes(self, campo_mes, campo_ano, destino):
        try:
            mes = int(str(self._valor_componente(campo_mes)).strip())
            ano = int(str(self._valor_componente(campo_ano)).strip())
        except ValueError:
            messagebox.showwarning('Calendário', 'Informe mês e ano com números válidos.')
            return
        if mes < 1 or mes > 12 or ano < 1 or ano > 9999:
            messagebox.showwarning('Calendário', 'Informe um mês de 1 a 12 e um ano válido.')
            return
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        semanas = calendar.Calendar(firstweekday=0).monthdayscalendar(ano, mes)
        linhas = [f'{meses[mes - 1]} {ano}'.center(27), 'Seg Ter Qua Qui Sex Sáb Dom']
        for semana in semanas:
            linhas.append(' '.join('   ' if dia == 0 else f'{dia:>3}' for dia in semana))
        self._definir_valor_componente(destino, '\n'.join(linhas))

    def senha_analisar_forca(self, origem, destino):
        senha = str(self._valor_componente(origem))
        criterios = [
            ('Pelo menos 8 caracteres', len(senha) >= 8),
            ('Pelo menos 12 caracteres', len(senha) >= 12),
            ('Letra maiúscula', bool(re.search(r'[A-ZÁÉÍÓÚÂÊÔÃÕÇ]', senha))),
            ('Letra minúscula', bool(re.search(r'[a-záéíóúâêôãõç]', senha))),
            ('Número', bool(re.search(r'\d', senha))),
            ('Símbolo', bool(re.search(r'[^\w\s]', senha))),
        ]
        pontos = sum(1 for _nome, ok in criterios if ok)
        if not senha:
            nivel = 'Nenhuma senha informada'
        elif pontos <= 2:
            nivel = 'Fraca'
        elif pontos <= 4:
            nivel = 'Média'
        elif pontos == 5:
            nivel = 'Forte'
        else:
            nivel = 'Muito forte'
        linhas = [f'Classificação: {nivel}', f'Comprimento: {len(senha)} caracteres', '']
        for nome, ok in criterios:
            linhas.append(('[OK] ' if ok else '[  ] ') + nome)
        self._definir_valor_componente(destino, '\n'.join(linhas))

    def validar_formulario(self):
        return True

    def _aplicar_mascara(self, nome, mascara):
        valor = str(self._valor_componente(nome))
        digitos = re.sub(r'\D', '', valor)
        novo = valor
        if mascara == 'CPF' and len(digitos) >= 11:
            d = digitos[:11]; novo = f'{d[:3]}.{d[3:6]}.{d[6:9]}-{d[9:]}'
        elif mascara == 'CNPJ' and len(digitos) >= 14:
            d = digitos[:14]; novo = f'{d[:2]}.{d[2:5]}.{d[5:8]}/{d[8:12]}-{d[12:]}'
        elif mascara == 'Telefone' and len(digitos) >= 10:
            d = digitos[:11]; novo = f'({d[:2]}) {d[2:7]}-{d[7:]}' if len(d) == 11 else f'({d[:2]}) {d[2:6]}-{d[6:]}'
        elif mascara == 'CEP' and len(digitos) >= 8:
            d = digitos[:8]; novo = f'{d[:5]}-{d[5:]}'
        elif mascara == 'Data' and len(digitos) >= 8:
            d = digitos[:8]; novo = f'{d[:2]}/{d[2:4]}/{d[4:]}'
        elif mascara == 'Hora' and len(digitos) >= 4:
            d = digitos[:4]; novo = f'{d[:2]}:{d[2:4]}'
        elif mascara == 'Moeda':
            try:
                numero = float(valor.replace('R$', '').replace('.', '').replace(',', '.').strip())
                novo = f'R$ {numero:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
            except ValueError:
                return
        self._definir_valor_componente(nome, novo)

    def validar_login(self):
        messagebox.showinfo('Login', 'Esta tela não está configurada como Login.')

    def salvar_registro(self, selecionados=None):
        if not self.validar_formulario():
            return
        mapa = {'qe46_caminho_excel': 'qe46_caminho_excel', 'qe46_aba': 'qe46_aba', 'qe46_coluna': 'qe46_coluna', 'qe46_pasta_saida': 'qe46_pasta_saida', 'qe46_nome_geral': 'qe46_nome_geral', 'qe46_nome_individual': 'qe46_nome_individual'}
        escolhidos = list(selecionados or ['qe46_caminho_excel', 'qe46_aba', 'qe46_coluna', 'qe46_pasta_saida', 'qe46_nome_geral', 'qe46_nome_individual'])
        escolhidos = [nome for nome in escolhidos if nome in mapa]
        if not escolhidos:
            messagebox.showwarning('SQLite', 'Selecione pelo menos um campo para cadastrar.')
            return
        campos = [mapa[nome] for nome in escolhidos]
        valores = []
        for nome, campo in zip(escolhidos, campos):
            valor = self._valor_componente(nome)
            if campo == 'senha' and str(valor):
                valor = hashlib.sha256(str(valor).encode('utf-8')).hexdigest()
            valores.append(valor)
        placeholders = ','.join('?' for _ in campos)
        sql = 'INSERT INTO quebra_excel_coluna (' + ','.join(campos) + ') VALUES (' + placeholders + ')' 
        try:
            self.app.conexao.execute(sql, valores)
            self.app.conexao.commit()
        except sqlite3.IntegrityError as erro:
            messagebox.showerror('Banco de dados', f'Não foi possível cadastrar: {erro}')
            return
        self.carregar_dados()
        messagebox.showinfo('SQLite', 'Dados cadastrados com sucesso!')

    def carregar_dados(self):
        tabela = self.qe46_resumo
        for item in tabela.get_children():
            tabela.delete(item)
        linhas = self.app.conexao.execute('SELECT id,qe46_caminho_excel,qe46_aba,qe46_coluna,qe46_pasta_saida,qe46_nome_geral,qe46_nome_individual FROM quebra_excel_coluna ORDER BY id DESC').fetchall()
        for linha in linhas:
            tabela.insert('', tk.END, iid=str(linha[0]), values=linha[1:])
        self._atualizar_contadores()

    def aplicar_filtro(self):
        self.carregar_dados()
        self._atualizar_contadores()

    def preencher_formulario(self, event=None):
        selecionado = self.qe46_resumo.selection()
        if not selecionado:
            return
        valores = self.qe46_resumo.item(selecionado[0], 'values')
        if not valores:
            return
        self._id_selecionado = selecionado[0]
        if len(valores) > 0:
            self._definir_valor_componente('qe46_caminho_excel', valores[0])
        if len(valores) > 1:
            self._definir_valor_componente('qe46_aba', valores[1])
        if len(valores) > 2:
            self._definir_valor_componente('qe46_coluna', valores[2])
        if len(valores) > 3:
            self._definir_valor_componente('qe46_pasta_saida', valores[3])
        if len(valores) > 4:
            self._definir_valor_componente('qe46_nome_geral', valores[4])
        if len(valores) > 5:
            self._definir_valor_componente('qe46_nome_individual', valores[5])

    def atualizar_registro(self, selecionados=None):
        if self._id_selecionado is None:
            messagebox.showwarning('Atenção', 'Selecione um registro na tabela da tela antes de atualizar.')
            return
        if not self.validar_formulario():
            return
        mapa = {'qe46_caminho_excel': 'qe46_caminho_excel', 'qe46_aba': 'qe46_aba', 'qe46_coluna': 'qe46_coluna', 'qe46_pasta_saida': 'qe46_pasta_saida', 'qe46_nome_geral': 'qe46_nome_geral', 'qe46_nome_individual': 'qe46_nome_individual'}
        escolhidos = list(selecionados or ['qe46_caminho_excel', 'qe46_aba', 'qe46_coluna', 'qe46_pasta_saida', 'qe46_nome_geral', 'qe46_nome_individual'])
        escolhidos = [nome for nome in escolhidos if nome in mapa]
        if not escolhidos:
            messagebox.showwarning('SQLite', 'Selecione os campos que serão atualizados.')
            return
        campos = [mapa[nome] for nome in escolhidos]
        pares_atualizacao = []
        for nome, campo in zip(escolhidos, campos):
            valor = self._valor_componente(nome)
            if campo == 'senha':
                if not str(valor):
                    continue
                valor = hashlib.sha256(str(valor).encode('utf-8')).hexdigest()
            pares_atualizacao.append((campo, valor))
        if not pares_atualizacao:
            messagebox.showwarning('SQLite', 'Nenhum campo possui um novo valor para atualizar.')
            return
        campos = [campo for campo, _ in pares_atualizacao]
        valores = [valor for _, valor in pares_atualizacao]
        sets = ', '.join(f'{campo} = ?' for campo in campos)
        self.app.conexao.execute('UPDATE quebra_excel_coluna SET ' + sets + ' WHERE id = ?', valores + [self._id_selecionado])
        self.app.conexao.commit()
        self.carregar_dados()
        messagebox.showinfo('SQLite', 'Registro atualizado com sucesso!')

    def excluir_registro(self):
        selecionado = self.qe46_resumo.selection()
        if not selecionado:
            messagebox.showwarning('Atenção', 'Selecione um registro na tabela.')
            return
        valores = self.qe46_resumo.item(selecionado[0], 'values')
        if not valores:
            return
        if not messagebox.askyesno('Excluir', 'Deseja realmente excluir o registro selecionado?'):
            return
        self.app.conexao.execute('DELETE FROM quebra_excel_coluna WHERE id = ?', (selecionado[0],))
        self.app.conexao.commit()
        self.carregar_dados()
        self.limpar_campos()

    def limpar_campos(self, selecionados=None):
        self._id_selecionado = None
        nomes = list(selecionados or ['qe46_caminho_excel', 'qe46_aba', 'qe46_lista_colunas', 'qe46_coluna', 'qe46_pasta_saida', 'qe46_nome_geral', 'qe46_nome_individual'])
        for nome in nomes:
            variavel = getattr(self, f'var_{nome}', None)
            if variavel is not None:
                try:
                    variavel.set(False if isinstance(variavel, tk.BooleanVar) else '')
                except tk.TclError:
                    pass
                continue
            widget = getattr(self, nome, None)
            if isinstance(widget, tk.Text):
                widget.delete('1.0', tk.END)
            elif isinstance(widget, tk.Listbox):
                widget.delete(0, tk.END)

    def _valor_para_formula(self, valor):
        if isinstance(valor, (int, float, bool)):
            return valor
        original = '' if valor is None else str(valor).strip()
        texto = original.replace('R$', '').replace(' ', '')
        try:
            if ',' in texto:
                texto = texto.replace('.', '').replace(',', '.')
            numero = float(texto)
            return int(numero) if numero.is_integer() else numero
        except (ValueError, TypeError):
            return original

    def _formatar_resultado(self, valor):
        if isinstance(valor, float):
            if valor.is_integer():
                return str(int(valor))
            return f'{valor:.10f}'.rstrip('0').rstrip('.').replace('.', ',')
        return str(valor)

    def _avaliar_expressao_segura(self, expressao, valores=None, resultado_anterior=None, n=None):
        valores = list(valores or [])
        def nome_campo_formula(indice):
            numero = indice + 1
            partes = []
            while numero > 0:
                numero, resto = divmod(numero - 1, 26)
                partes.append(chr(65 + resto))
            return ''.join(reversed(partes))
        ambiente = {nome_campo_formula(i): valor for i, valor in enumerate(valores)}
        ambiente.update({f'CAMPO{i + 1}': valor for i, valor in enumerate(valores)})
        if resultado_anterior is not None: ambiente['R'] = resultado_anterior
        if n is not None: ambiente['N'] = n
        funcoes = {
            'round': round, 'abs': abs, 'min': min, 'max': max,
            'int': int, 'float': float, 'str': str,
            'upper': lambda x: str(x).upper(),
            'lower': lambda x: str(x).lower(), 'len': len
        }
        arvore = ast.parse(str(expressao), mode='eval')

        def visitar(no):
            if isinstance(no, ast.Expression):
                return visitar(no.body)
            if isinstance(no, ast.Constant):
                return no.value
            if isinstance(no, ast.Name):
                if no.id in ambiente:
                    return ambiente[no.id]
                raise ValueError(f'Nome não permitido: {no.id}')
            if isinstance(no, ast.BinOp):
                a, b = visitar(no.left), visitar(no.right)
                if isinstance(no.op, ast.Add): return a + b
                if isinstance(no.op, ast.Sub): return a - b
                if isinstance(no.op, ast.Mult): return a * b
                if isinstance(no.op, ast.Div): return a / b
                if isinstance(no.op, ast.FloorDiv): return a // b
                if isinstance(no.op, ast.Mod): return a % b
                if isinstance(no.op, ast.Pow): return a ** b
                raise ValueError('Operador não permitido')
            if isinstance(no, ast.UnaryOp):
                valor = visitar(no.operand)
                if isinstance(no.op, ast.USub): return -valor
                if isinstance(no.op, ast.UAdd): return +valor
                if isinstance(no.op, ast.Not): return not valor
                raise ValueError('Operador unário não permitido')
            if isinstance(no, ast.BoolOp):
                valores_bool = [visitar(x) for x in no.values]
                return all(valores_bool) if isinstance(no.op, ast.And) else any(valores_bool)
            if isinstance(no, ast.Compare):
                esquerda = visitar(no.left)
                for operador, comparador in zip(no.ops, no.comparators):
                    direita = visitar(comparador)
                    if isinstance(operador, ast.Eq): ok = esquerda == direita
                    elif isinstance(operador, ast.NotEq): ok = esquerda != direita
                    elif isinstance(operador, ast.Gt): ok = esquerda > direita
                    elif isinstance(operador, ast.GtE): ok = esquerda >= direita
                    elif isinstance(operador, ast.Lt): ok = esquerda < direita
                    elif isinstance(operador, ast.LtE): ok = esquerda <= direita
                    else: raise ValueError('Comparação não permitida')
                    if not ok: return False
                    esquerda = direita
                return True
            if isinstance(no, ast.IfExp):
                return visitar(no.body) if visitar(no.test) else visitar(no.orelse)
            if isinstance(no, ast.Call):
                if not isinstance(no.func, ast.Name) or no.func.id not in funcoes:
                    raise ValueError('Função não permitida')
                if no.keywords:
                    raise ValueError('Argumentos nomeados não são permitidos')
                return funcoes[no.func.id](*[visitar(x) for x in no.args])
            raise ValueError(f'Elemento não permitido: {type(no).__name__}')

        return visitar(arvore)

    def _operacao_basica(self, valores, operador, expressao=''):
        if operador == 'Expressão personalizada':
            if not str(expressao).strip():
                raise ValueError('Informe a expressão personalizada.')
            return self._avaliar_expressao_segura(expressao, valores)
        if operador == 'Operação definida no Campo 3':
            if len(valores) < 3:
                raise ValueError('Selecione Campo 1, Campo 2 e Campo 3.')
            op = str(valores[2]).strip().lower()
            mapa = {
                'somar': 'Somar', '+': 'Somar',
                'subtrair': 'Subtrair', '-': 'Subtrair',
                'multiplicar': 'Multiplicar', '*': 'Multiplicar', '×': 'Multiplicar',
                'dividir': 'Dividir', '/': 'Dividir', '÷': 'Dividir'
            }
            operador = mapa.get(op, '')
            valores = valores[:2]
        if not valores:
            raise ValueError('Selecione pelo menos um campo.')
        if operador == 'Somar':
            return sum(valores)
        if operador == 'Subtrair':
            resultado = valores[0]
            for valor in valores[1:]: resultado -= valor
            return resultado
        if operador == 'Multiplicar':
            resultado = 1
            for valor in valores: resultado *= valor
            return resultado
        if operador == 'Dividir':
            resultado = valores[0]
            for valor in valores[1:]: resultado /= valor
            return resultado
        if operador == 'Média':
            return sum(valores) / len(valores)
        if operador == 'Porcentagem':
            if len(valores) < 2: raise ValueError('Porcentagem precisa de dois campos.')
            return valores[0] * valores[1] / 100
        if operador == 'Resto da divisão':
            if len(valores) < 2: raise ValueError('Resto precisa de dois campos.')
            return valores[0] % valores[1]
        if operador == 'Potência':
            if len(valores) < 2: raise ValueError('Potência precisa de dois campos.')
            return valores[0] ** valores[1]
        if operador == 'Mínimo':
            return min(valores)
        if operador == 'Máximo':
            return max(valores)
        raise ValueError('Escolha uma operação matemática.')

    def inserir_valor(self, destino, valor, modo='Adicionar'):
        if not destino:
            messagebox.showwarning('Ação', 'Selecione o campo que receberá o valor.')
            return
        atual = str(self._valor_componente(destino))
        novo = str(valor) if modo == 'Substituir' else atual + str(valor)
        if not self._definir_valor_componente(destino, novo):
            messagebox.showwarning('Ação', 'O campo de destino não existe nesta tela.')

    def calcular_campos(self, campos, destino, operador, expressao='', formato='', destino_2='', expressao_2=''):
        if not campos or not destino:
            messagebox.showwarning('Cálculo', 'Selecione os campos da operação e o campo de resultado.')
            return
        try:
            valores = [self._valor_para_formula(self._valor_componente(nome)) for nome in campos]
            resultado = self._operacao_basica(valores, operador, expressao)
            texto = self._formatar_resultado(resultado)
            if formato:
                texto = str(formato).replace('{resultado}', texto)
            if not self._definir_valor_componente(destino, texto):
                raise ValueError('Campo de resultado não encontrado.')
            if destino_2 and expressao_2:
                resultado_2 = self._avaliar_expressao_segura(expressao_2, valores, resultado_anterior=resultado)
                self._definir_valor_componente(destino_2, self._formatar_resultado(resultado_2))
        except ZeroDivisionError:
            messagebox.showwarning('Cálculo', 'Não é possível dividir por zero.')
        except Exception as erro:
            messagebox.showwarning('Cálculo', f'Não foi possível executar a operação: {erro}')

    def calcular_expressao_campo(self, origem, destino, auxiliar=''):
        if not origem or not destino:
            messagebox.showwarning('Cálculo', 'Selecione o campo da expressão e o campo de resultado.')
            return
        original = str(self._valor_componente(origem)).strip()
        expressao = original.replace('×', '*').replace('÷', '/').replace(',', '.')
        if not expressao:
            return
        try:
            resultado = self._avaliar_expressao_segura(expressao)
            if not isinstance(resultado, (int, float)):
                raise ValueError('A expressão deve produzir um número.')
            texto = self._formatar_resultado(resultado)
            self._definir_valor_componente(destino, texto)
            if auxiliar:
                widget = getattr(self, auxiliar, None)
                if isinstance(widget, tk.Listbox):
                    widget.insert(tk.END, f'{original} = {texto}')
                elif isinstance(widget, tk.Text):
                    widget.insert(tk.END, f'{original} = {texto}\n')
        except ZeroDivisionError:
            messagebox.showwarning('Cálculo', 'Não é possível dividir por zero.')
        except Exception as erro:
            messagebox.showwarning('Cálculo', f'Expressão inválida: {erro}')

    def aplicar_condicao(self, campos, destino, comparador, valor_fixo='', verdadeiro='Sim', falso='Não'):
        if not campos or not destino or not comparador:
            messagebox.showwarning('Condição', 'Selecione Campo 1, comparador e campo de resultado.')
            return
        a = self._valor_para_formula(self._valor_componente(campos[0]))
        if len(campos) >= 2:
            b = self._valor_para_formula(self._valor_componente(campos[1]))
        else:
            b = self._valor_para_formula(valor_fixo)
        try:
            if comparador == '==': ok = a == b
            elif comparador == '!=': ok = a != b
            elif comparador == '>': ok = a > b
            elif comparador == '>=': ok = a >= b
            elif comparador == '<': ok = a < b
            elif comparador == '<=': ok = a <= b
            else: raise ValueError('Comparador inválido')
            self._definir_valor_componente(destino, verdadeiro if ok else falso)
        except Exception as erro:
            messagebox.showwarning('Condição', f'Não foi possível comparar os valores: {erro}')

    def gerar_lista_repeticao(self, campos, destino, operador, inicio='1', fim='10', modelo=''):
        if not campos or not destino:
            messagebox.showwarning('Repetição', 'Selecione Campo 1 e o campo de resultado.')
            return
        try:
            a = self._valor_para_formula(self._valor_componente(campos[0]))
            inicio_i, fim_i = int(inicio), int(fim)
            passo = 1 if fim_i >= inicio_i else -1
            linhas_saida = []
            for n in range(inicio_i, fim_i + passo, passo):
                resultado = self._operacao_basica([a, n], operador, '')
                texto_resultado = self._formatar_resultado(resultado)
                linha = modelo or '{A} {operador} {N} = {resultado}'
                linha = str(linha).replace('{A}', self._formatar_resultado(a)).replace('{N}', str(n))
                linha = linha.replace('{operador}', operador).replace('{resultado}', texto_resultado)
                linhas_saida.append(linha)
            self._definir_valor_componente(destino, linhas_saida)
        except Exception as erro:
            messagebox.showwarning('Repetição', f'Não foi possível gerar a lista: {erro}')



if __name__ == '__main__':
    app = AplicacaoGerada()
    app.protocol('WM_DELETE_WINDOW', app.fechar)
    app.mainloop()
