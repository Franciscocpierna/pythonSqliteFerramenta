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
        self.title('Criador de E-mails em Rascunho no Outlook')
        self.geometry('1000x1240')
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
        self._metadados_tabelas = {'Tela Principal': {'tabela': 'rascunhos_outlook', 'pk': 'id', 'colunas': ['caminho_excel', 'planilha_excel', 'email_to', 'email_cc', 'email_bcc', 'assunto_email', 'pasta_anexos', 'regra_anexo', 'exigir_anexo', 'tamanho_texto_email', 'corpo_email'], 'titulos': {'caminho_excel': 'Planilha do Excel', 'planilha_excel': 'Planilha/aba', 'email_to': 'Para', 'email_cc': 'CC', 'email_bcc': 'CCO', 'assunto_email': 'Assunto', 'pasta_anexos': 'Pasta dos anexos', 'regra_anexo': 'Regra do anexo', 'exigir_anexo': 'Exigir Anexo', 'tamanho_texto_email': 'Tamanho', 'corpo_email': 'Corpo do e-mail'}}}
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
        self.app.conexao.execute('CREATE TABLE IF NOT EXISTS rascunhos_outlook (id INTEGER PRIMARY KEY AUTOINCREMENT, caminho_excel TEXT, planilha_excel TEXT, email_to TEXT, email_cc TEXT, email_bcc TEXT, assunto_email TEXT, pasta_anexos TEXT, regra_anexo TEXT, exigir_anexo INTEGER, tamanho_texto_email TEXT, corpo_email TEXT)')
        colunas_existentes = {linha[1] for linha in self.app.conexao.execute('PRAGMA table_info(rascunhos_outlook)').fetchall()}
        if 'caminho_excel' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN caminho_excel TEXT')
        if 'planilha_excel' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN planilha_excel TEXT')
        if 'email_to' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN email_to TEXT')
        if 'email_cc' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN email_cc TEXT')
        if 'email_bcc' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN email_bcc TEXT')
        if 'assunto_email' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN assunto_email TEXT')
        if 'pasta_anexos' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN pasta_anexos TEXT')
        if 'regra_anexo' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN regra_anexo TEXT')
        if 'exigir_anexo' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN exigir_anexo INTEGER')
        if 'tamanho_texto_email' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN tamanho_texto_email TEXT')
        if 'corpo_email' not in colunas_existentes:
            self.app.conexao.execute('ALTER TABLE rascunhos_outlook ADD COLUMN corpo_email TEXT')
        self.app.conexao.commit()

    def _criar_interface(self):
        self._criar_area_rolavel(1000, 1160)
        self.titulo = ttk.Label(self.area, text='Criador de E-mails em Rascunho no Outlook', style='Title.TLabel')
        self.titulo.place(x=175, y=20, width=650, height=44)
        self.lbl_excel = ttk.Label(self.area, text='Planilha do Excel', style='TLabel')
        self.lbl_excel.place(x=45, y=88, width=145, height=28)
        self.var_caminho_excel = tk.StringVar(value='')
        self.caminho_excel = ttk.Entry(self.area, textvariable=self.var_caminho_excel)
        self.caminho_excel.place(x=190, y=81, width=560, height=34)
        self.btn_selecionar_excel = ttk.Button(self.area, text='Selecionar Excel', command=lambda: None)
        self.btn_selecionar_excel.place(x=765, y=78, width=190, height=40)
        self.lbl_planilha = ttk.Label(self.area, text='Planilha/aba', style='TLabel')
        self.lbl_planilha.place(x=45, y=138, width=145, height=28)
        self.var_planilha_excel = tk.StringVar()
        self.planilha_excel = ttk.Combobox(self.area, textvariable=self.var_planilha_excel, values=[], state='readonly')
        self.planilha_excel.place(x=190, y=131, width=300, height=34)
        self.lbl_colunas = ttk.Label(self.area, text='Colunas do Excel', style='TLabel')
        self.lbl_colunas.place(x=45, y=187, width=180, height=28)
        self.lista_colunas_excel = tk.Listbox(self.area, font=('Segoe UI', 10), relief='solid', bd=1, bg=self.app.cor_cartao, fg=self.app.cor_texto)
        self.lista_colunas_excel.place(x=45, y=220, width=280, height=270)
        self.lbl_arrastar = ttk.Label(self.area, text='Arraste uma coluna para Para, CC, CCO, Assunto, Corpo ou regra do anexo.', style='TLabel')
        self.lbl_arrastar.place(x=45, y=500, width=910, height=28)
        self.lbl_to = ttk.Label(self.area, text='Para (.To)', style='TLabel')
        self.lbl_to.place(x=355, y=138, width=115, height=28)
        self.var_email_to = tk.StringVar(value='')
        self.email_to = ttk.Entry(self.area, textvariable=self.var_email_to)
        self.email_to.place(x=470, y=131, width=485, height=34)
        self.lbl_cc = ttk.Label(self.area, text='CC (.CC)', style='TLabel')
        self.lbl_cc.place(x=355, y=188, width=115, height=28)
        self.var_email_cc = tk.StringVar(value='')
        self.email_cc = ttk.Entry(self.area, textvariable=self.var_email_cc)
        self.email_cc.place(x=470, y=181, width=485, height=34)
        self.lbl_bcc = ttk.Label(self.area, text='CCO (.BCC)', style='TLabel')
        self.lbl_bcc.place(x=355, y=238, width=115, height=28)
        self.var_email_bcc = tk.StringVar(value='')
        self.email_bcc = ttk.Entry(self.area, textvariable=self.var_email_bcc)
        self.email_bcc.place(x=470, y=231, width=485, height=34)
        self.lbl_assunto = ttk.Label(self.area, text='Assunto', style='TLabel')
        self.lbl_assunto.place(x=355, y=288, width=115, height=28)
        self.var_assunto_email = tk.StringVar(value='')
        self.assunto_email = ttk.Entry(self.area, textvariable=self.var_assunto_email)
        self.assunto_email.place(x=470, y=281, width=485, height=34)
        self.lbl_pasta_anexos = ttk.Label(self.area, text='Pasta dos anexos', style='TLabel')
        self.lbl_pasta_anexos.place(x=355, y=338, width=150, height=28)
        self.var_pasta_anexos = tk.StringVar(value='')
        self.pasta_anexos = ttk.Entry(self.area, textvariable=self.var_pasta_anexos)
        self.pasta_anexos.place(x=505, y=331, width=280, height=34)
        self.btn_pasta_anexos = ttk.Button(self.area, text='Escolher pasta', command=lambda: None)
        self.btn_pasta_anexos.place(x=800, y=328, width=155, height=40)
        self.lbl_regra_anexo = ttk.Label(self.area, text='Regra do anexo', style='TLabel')
        self.lbl_regra_anexo.place(x=355, y=388, width=150, height=28)
        self.var_regra_anexo = tk.StringVar(value='')
        self.regra_anexo = ttk.Entry(self.area, textvariable=self.var_regra_anexo)
        self.regra_anexo.place(x=505, y=381, width=450, height=34)
        self.lbl_exemplo_anexo = ttk.Label(self.area, text='Ex.: {Codigo}_boleto.pdf  ou  Contratos\\{Cliente}_contrato.pdf. Separe vários por ;', style='TLabel')
        self.lbl_exemplo_anexo.place(x=355, y=425, width=600, height=28)
        self.var_exigir_anexo = tk.BooleanVar(value=False)
        self.exigir_anexo = ttk.Checkbutton(self.area, text='Só criar se o anexo for encontrado', variable=self.var_exigir_anexo)
        self.exigir_anexo.place(x=355, y=462, width=310, height=34)
        self.lbl_corpo = ttk.Label(self.area, text='Corpo do e-mail', style='TLabel')
        self.lbl_corpo.place(x=45, y=552, width=180, height=28)
        self.btn_negrito_email = ttk.Button(self.area, text='Negrito', command=lambda: None)
        self.btn_negrito_email.place(x=200, y=545, width=85, height=40)
        self.btn_italico_email = ttk.Button(self.area, text='Itálico', command=lambda: None)
        self.btn_italico_email.place(x=290, y=545, width=85, height=40)
        self.btn_sublinhado_email = ttk.Button(self.area, text='Sublinhar', command=lambda: None)
        self.btn_sublinhado_email.place(x=380, y=545, width=100, height=40)
        self.btn_cor_email = ttk.Button(self.area, text='Cor', command=lambda: None)
        self.btn_cor_email.place(x=485, y=545, width=70, height=40)
        self.var_tamanho_texto_email = tk.StringVar()
        self.tamanho_texto_email = ttk.Combobox(self.area, textvariable=self.var_tamanho_texto_email, values=['8', '9', '10', '11', '12', '14', '16', '18', '20', '24', '28', '32'], state='readonly')
        self.tamanho_texto_email.place(x=560, y=548, width=70, height=34)
        self.btn_tamanho_email = ttk.Button(self.area, text='Aplicar tamanho', command=lambda: None)
        self.btn_tamanho_email.place(x=635, y=545, width=120, height=40)
        self.btn_link_email = ttk.Button(self.area, text='Link', command=lambda: None)
        self.btn_link_email.place(x=760, y=545, width=75, height=40)
        self.btn_imagem_email = ttk.Button(self.area, text='Imagem', command=lambda: None)
        self.btn_imagem_email.place(x=840, y=545, width=100, height=40)
        self.corpo_email = scrolledtext.ScrolledText(self.area, relief='solid', bd=1, font=('Segoe UI', 10), bg=self.app.cor_cartao, fg=self.app.cor_texto, insertbackground=self.app.cor_texto)
        self.corpo_email.place(x=45, y=595, width=910, height=240)
        self.lbl_anexos_fixos = ttk.Label(self.area, text='Anexos fixos adicionais', style='TLabel')
        self.lbl_anexos_fixos.place(x=45, y=852, width=200, height=28)
        self.lista_anexos_fixos = tk.Listbox(self.area, font=('Segoe UI', 10), relief='solid', bd=1, bg=self.app.cor_cartao, fg=self.app.cor_texto)
        self.lista_anexos_fixos.place(x=45, y=885, width=610, height=120)
        self.btn_adicionar_anexo = ttk.Button(self.area, text='Adicionar arquivo', command=lambda: None)
        self.btn_adicionar_anexo.place(x=675, y=885, width=190, height=40)
        self.btn_remover_anexo = ttk.Button(self.area, text='Remover selecionado', command=lambda: None)
        self.btn_remover_anexo.place(x=675, y=935, width=190, height=40)
        self.btn_criar_rascunhos = ttk.Button(self.area, text='Criar rascunhos no Outlook', command=lambda: None)
        self.btn_criar_rascunhos.place(x=45, y=1030, width=390, height=40)
        self.status_outlook = ttk.Label(self.area, text='Status: pronto para selecionar uma planilha.', style='TLabel')
        self.status_outlook.place(x=460, y=1038, width=495, height=28)
        self.lbl_seguranca = ttk.Label(self.area, text='Cada linha do Excel pode gerar um rascunho. Nenhum e-mail é enviado automaticamente.', style='TLabel')
        self.lbl_seguranca.place(x=45, y=1090, width=910, height=28)

        self._configurar_outlook_excel()

    def _configurar_outlook_excel(self):
        self._dados_excel_outlook = []
        self._cabecalhos_excel_outlook = []
        self._coluna_arrastada_outlook = ""
        self._links_outlook = {}
        self._cores_outlook = {}
        self._tamanhos_outlook = {}
        self._imagens_outlook = {}
        self._fontes_outlook = []

        getattr(self, 'btn_selecionar_excel').configure(command=self._selecionar_excel_outlook)
        getattr(self, 'btn_pasta_anexos').configure(command=self._selecionar_pasta_anexos_outlook)
        getattr(self, 'btn_negrito_email').configure(command=lambda: self._alternar_tag_outlook('outlook_negrito'))
        getattr(self, 'btn_italico_email').configure(command=lambda: self._alternar_tag_outlook('outlook_italico'))
        getattr(self, 'btn_sublinhado_email').configure(command=lambda: self._alternar_tag_outlook('outlook_sublinhado'))
        getattr(self, 'btn_cor_email').configure(command=self._aplicar_cor_outlook)
        getattr(self, 'btn_tamanho_email').configure(command=self._aplicar_tamanho_outlook)
        getattr(self, 'btn_link_email').configure(command=self._aplicar_link_outlook)
        getattr(self, 'btn_imagem_email').configure(command=self._inserir_imagem_outlook)
        getattr(self, 'btn_adicionar_anexo').configure(command=self._adicionar_anexo_fixo_outlook)
        getattr(self, 'btn_remover_anexo').configure(command=self._remover_anexo_fixo_outlook)
        getattr(self, 'btn_criar_rascunhos').configure(command=self._criar_rascunhos_outlook)

        combo_planilha = getattr(self, 'planilha_excel')
        combo_planilha.bind('<<ComboboxSelected>>', lambda e: self._carregar_aba_excel_outlook())

        lista_colunas = getattr(self, 'lista_colunas_excel')
        lista_colunas.bind('<ButtonPress-1>', self._iniciar_arraste_coluna_outlook)
        lista_colunas.bind('<ButtonRelease-1>', self._finalizar_arraste_coluna_outlook)

        corpo = getattr(self, 'corpo_email')
        corpo.tag_configure('outlook_negrito', font=self._fonte_email_outlook(weight='bold'))
        corpo.tag_configure('outlook_italico', font=self._fonte_email_outlook(slant='italic'))
        corpo.tag_configure('outlook_sublinhado', underline=1)

        if not str(self._valor_componente('tamanho_texto_email')).strip():
            self._definir_valor_componente('tamanho_texto_email', '11')
        if not str(self._valor_componente('assunto_email')).strip():
            self._definir_valor_componente('assunto_email', 'Documento de {Nome}')
        if not str(self._valor_componente('regra_anexo')).strip():
            self._definir_valor_componente('regra_anexo', '{Codigo}_documento.pdf')
        var_exigir = getattr(self, 'var_exigir_anexo', None)
        if var_exigir is not None:
            var_exigir.set(True)
        if not corpo.get('1.0', 'end-1c').strip():
            corpo.insert('1.0', 'Olá {Nome},\n\nSegue o documento referente ao seu cadastro.\n\nAtenciosamente,\nEquipe')
        self._status_outlook('pronto para selecionar uma planilha.')

    def _fonte_email_outlook(self, **alteracoes):
        import tkinter.font as tkfont
        corpo = getattr(self, 'corpo_email')
        fonte = tkfont.Font(font=corpo.cget('font'))
        fonte.configure(**alteracoes)
        self._fontes_outlook.append(fonte)
        return fonte

    def _status_outlook(self, texto):
        widget = getattr(self, 'status_outlook', None)
        if widget is not None:
            try:
                widget.configure(text='Status: ' + str(texto))
            except tk.TclError:
                pass

    def _selecionar_excel_outlook(self):
        try:
            from openpyxl import load_workbook
        except ImportError:
            messagebox.showerror(
                'Excel',
                'Para usar planilhas do Excel, instale a biblioteca openpyxl com:\n\npip install openpyxl',
            )
            return
        caminho = filedialog.askopenfilename(
            title='Selecionar planilha do Excel',
            filetypes=[('Planilhas do Excel', '*.xlsx *.xlsm'), ('Arquivo .xlsx', '*.xlsx'), ('Todos os arquivos', '*.*')],
        )
        if not caminho:
            return
        self._definir_valor_componente('caminho_excel', caminho)
        try:
            wb = load_workbook(caminho, read_only=True, data_only=True)
            nomes_abas = list(wb.sheetnames)
            wb.close()
        except Exception as erro:
            messagebox.showerror('Excel', f'Não foi possível abrir a planilha.\n\n{erro}')
            return
        combo = getattr(self, 'planilha_excel')
        combo.configure(values=nomes_abas)
        if nomes_abas:
            self._definir_valor_componente('planilha_excel', nomes_abas[0])
            self._carregar_aba_excel_outlook()
        else:
            self._status_outlook('a planilha não possui abas disponíveis.')

    def _carregar_aba_excel_outlook(self):
        try:
            from openpyxl import load_workbook
        except ImportError:
            return
        caminho = str(self._valor_componente('caminho_excel')).strip()
        aba = str(self._valor_componente('planilha_excel')).strip()
        if not caminho or not aba:
            return
        try:
            wb = load_workbook(caminho, read_only=True, data_only=True)
            if aba not in wb.sheetnames:
                wb.close()
                messagebox.showwarning('Excel', 'A aba selecionada não existe mais na planilha.')
                return
            ws = wb[aba]
            linhas = ws.iter_rows(values_only=True)
            primeira = next(linhas, None)
            if primeira is None:
                wb.close()
                self._cabecalhos_excel_outlook = []
                self._dados_excel_outlook = []
                self._preencher_lista_colunas_outlook([])
                self._status_outlook('a aba selecionada está vazia.')
                return

            cabecalhos = []
            usados = {}
            for indice, valor in enumerate(primeira, 1):
                nome = str(valor).strip() if valor is not None else ''
                if not nome:
                    nome = f'Coluna{indice}'
                quantidade = usados.get(nome.casefold(), 0) + 1
                usados[nome.casefold()] = quantidade
                if quantidade > 1:
                    nome = f'{nome}_{quantidade}'
                cabecalhos.append(nome)

            dados = []
            for valores in linhas:
                valores = list(valores[:len(cabecalhos)])
                if len(valores) < len(cabecalhos):
                    valores.extend([None] * (len(cabecalhos) - len(valores)))
                if not any(valor not in (None, '') for valor in valores):
                    continue
                dados.append(dict(zip(cabecalhos, valores)))
            wb.close()
        except Exception as erro:
            messagebox.showerror('Excel', f'Não foi possível ler os dados da planilha.\n\n{erro}')
            return

        self._cabecalhos_excel_outlook = cabecalhos
        self._dados_excel_outlook = dados
        self._preencher_lista_colunas_outlook(cabecalhos)

        if not str(self._valor_componente('email_to')).strip():
            coluna_email = next(
                (c for c in cabecalhos if 'email' in c.casefold().replace('-', '').replace('_', '')),
                '',
            )
            if coluna_email:
                self._definir_valor_componente('email_to', '{' + coluna_email + '}')
        self._status_outlook(f'{len(dados)} linha(s) carregada(s) da aba {aba}.')

    def _preencher_lista_colunas_outlook(self, cabecalhos):
        lista = getattr(self, 'lista_colunas_excel')
        lista.delete(0, tk.END)
        for cabecalho in cabecalhos:
            lista.insert(tk.END, cabecalho)

    def _iniciar_arraste_coluna_outlook(self, evento):
        lista = evento.widget
        if lista.size() <= 0:
            self._coluna_arrastada_outlook = ''
            return
        indice = lista.nearest(evento.y)
        if indice < 0 or indice >= lista.size():
            self._coluna_arrastada_outlook = ''
            return
        lista.selection_clear(0, tk.END)
        lista.selection_set(indice)
        self._coluna_arrastada_outlook = str(lista.get(indice))
        self._status_outlook(f'arrastando a coluna {self._coluna_arrastada_outlook}.')

    def _finalizar_arraste_coluna_outlook(self, evento):
        coluna = str(getattr(self, '_coluna_arrastada_outlook', '') or '').strip()
        self._coluna_arrastada_outlook = ''
        if not coluna:
            return
        alvo = self.winfo_containing(evento.x_root, evento.y_root)
        widgets = {
            getattr(self, 'email_to'): 'destinatario',
            getattr(self, 'email_cc'): 'destinatario',
            getattr(self, 'email_bcc'): 'destinatario',
            getattr(self, 'assunto_email'): 'texto',
            getattr(self, 'regra_anexo'): 'texto',
            getattr(self, 'pasta_anexos'): 'texto',
            getattr(self, 'corpo_email'): 'corpo',
        }
        while alvo is not None and alvo not in widgets:
            alvo = getattr(alvo, 'master', None)
        if alvo not in widgets:
            self._status_outlook('solte a coluna sobre Para, CC, CCO, Assunto, Corpo ou regra do anexo.')
            return
        marcador = '{' + coluna + '}'
        tipo = widgets[alvo]
        if tipo == 'corpo':
            alvo.insert(tk.INSERT, marcador)
            alvo.focus_set()
        elif tipo == 'destinatario':
            atual = alvo.get().strip()
            if atual:
                alvo.insert(tk.END, ';' + marcador)
            else:
                alvo.insert(0, marcador)
            alvo.focus_set()
        else:
            try:
                posicao = alvo.index(tk.INSERT)
            except tk.TclError:
                posicao = tk.END
            alvo.insert(posicao, marcador)
            alvo.focus_set()
        self._status_outlook(f'coluna {coluna} adicionada ao campo escolhido.')

    def _intervalo_selecionado_outlook(self):
        corpo = getattr(self, 'corpo_email')
        try:
            return corpo.index('sel.first'), corpo.index('sel.last')
        except tk.TclError:
            messagebox.showinfo('Formatação', 'Selecione primeiro o trecho do corpo do e-mail que deseja formatar.')
            return None

    def _alternar_tag_outlook(self, tag):
        intervalo = self._intervalo_selecionado_outlook()
        if not intervalo:
            return
        corpo = getattr(self, 'corpo_email')
        inicio, fim = intervalo
        if tag in corpo.tag_names(inicio):
            corpo.tag_remove(tag, inicio, fim)
        else:
            corpo.tag_add(tag, inicio, fim)
        corpo.focus_set()

    def _aplicar_cor_outlook(self):
        intervalo = self._intervalo_selecionado_outlook()
        if not intervalo:
            return
        from tkinter import colorchooser
        _rgb, cor = colorchooser.askcolor(title='Cor do texto do e-mail', parent=self)
        if not cor:
            return
        corpo = getattr(self, 'corpo_email')
        tag = f'outlook_cor_{len(self._cores_outlook) + 1}'
        self._cores_outlook[tag] = cor
        corpo.tag_configure(tag, foreground=cor)
        corpo.tag_add(tag, *intervalo)
        corpo.focus_set()

    def _aplicar_tamanho_outlook(self):
        intervalo = self._intervalo_selecionado_outlook()
        if not intervalo:
            return
        try:
            tamanho = int(str(self._valor_componente('tamanho_texto_email')).strip())
        except (TypeError, ValueError):
            messagebox.showwarning('Tamanho', 'Escolha um tamanho de fonte válido.')
            return
        if tamanho < 6 or tamanho > 72:
            messagebox.showwarning('Tamanho', 'Use um tamanho de fonte entre 6 e 72.')
            return
        corpo = getattr(self, 'corpo_email')
        tag = f'outlook_tamanho_{len(self._tamanhos_outlook) + 1}'
        self._tamanhos_outlook[tag] = tamanho
        corpo.tag_configure(tag, font=self._fonte_email_outlook(size=tamanho))
        corpo.tag_add(tag, *intervalo)
        corpo.focus_set()

    def _aplicar_link_outlook(self):
        intervalo = self._intervalo_selecionado_outlook()
        if not intervalo:
            return
        from tkinter import simpledialog
        url = simpledialog.askstring(
            'Inserir link',
            'Informe o endereço do link. Pode usar uma coluna, por exemplo:\nhttps://site.com/cliente/{Codigo}',
            parent=self,
        )
        if not url:
            return
        corpo = getattr(self, 'corpo_email')
        tag = f'outlook_link_{len(self._links_outlook) + 1}'
        self._links_outlook[tag] = url.strip()
        corpo.tag_configure(tag, foreground='#0563C1', underline=1)
        corpo.tag_add(tag, *intervalo)
        corpo.focus_set()

    def _inserir_imagem_outlook(self):
        caminho = filedialog.askopenfilename(
            title='Selecionar imagem para o corpo do e-mail',
            filetypes=[('Imagens', '*.png *.jpg *.jpeg *.gif *.bmp'), ('Todos os arquivos', '*.*')],
        )
        if not caminho:
            return
        corpo = getattr(self, 'corpo_email')
        tag = f'outlook_imagem_{len(self._imagens_outlook) + 1}'
        self._imagens_outlook[tag] = caminho
        marcador = f'[Imagem: {os.path.basename(caminho)}]'
        corpo.insert(tk.INSERT, marcador, (tag,))
        corpo.tag_configure(tag, background='#E8F0FE', foreground='#174EA6')
        corpo.focus_set()

    def _selecionar_pasta_anexos_outlook(self):
        caminho = filedialog.askdirectory(title='Selecionar pasta dos anexos')
        if caminho:
            self._definir_valor_componente('pasta_anexos', caminho)

    def _adicionar_anexo_fixo_outlook(self):
        caminhos = filedialog.askopenfilenames(title='Selecionar anexos fixos')
        if not caminhos:
            return
        lista = getattr(self, 'lista_anexos_fixos')
        atuais = set(lista.get(0, tk.END))
        for caminho in caminhos:
            if caminho not in atuais:
                lista.insert(tk.END, caminho)
                atuais.add(caminho)

    def _remover_anexo_fixo_outlook(self):
        lista = getattr(self, 'lista_anexos_fixos')
        selecao = list(lista.curselection())
        for indice in reversed(selecao):
            lista.delete(indice)

    def _valor_excel_outlook(self, valor):
        if valor is None:
            return ''
        if isinstance(valor, datetime):
            return valor.strftime('%d/%m/%Y %H:%M:%S')
        if isinstance(valor, date):
            return valor.strftime('%d/%m/%Y')
        if isinstance(valor, float) and valor.is_integer():
            return str(int(valor))
        return str(valor)

    def _preencher_modelo_outlook(self, modelo, linha):
        modelo = '' if modelo is None else str(modelo)
        def substituir(casamento):
            chave = casamento.group(1).strip()
            if chave in linha:
                return self._valor_excel_outlook(linha.get(chave))
            chave_cf = chave.casefold()
            for nome, valor in linha.items():
                if str(nome).casefold() == chave_cf:
                    return self._valor_excel_outlook(valor)
            return casamento.group(0)
        return re.sub(r'\{([^{}]+)\}', substituir, modelo)

    def _texto_html_outlook(self, texto, linha):
        import html
        texto = '' if texto is None else str(texto)
        partes = []
        posicao = 0
        for casamento in re.finditer(r'\{([^{}]+)\}', texto):
            partes.append(html.escape(texto[posicao:casamento.start()]))
            chave = casamento.group(1).strip()
            valor = casamento.group(0)
            if chave in linha:
                valor = self._valor_excel_outlook(linha.get(chave))
            else:
                chave_cf = chave.casefold()
                for nome, conteudo in linha.items():
                    if str(nome).casefold() == chave_cf:
                        valor = self._valor_excel_outlook(conteudo)
                        break
            partes.append(html.escape(str(valor)))
            posicao = casamento.end()
        partes.append(html.escape(texto[posicao:]))
        return ''.join(partes).replace('\r\n', '\n').replace('\r', '\n').replace('\n', '<br>')

    def _corpo_html_outlook(self, linha):
        import html
        corpo = getattr(self, 'corpo_email')
        eventos = corpo.dump('1.0', 'end-1c', text=True, tag=True)
        ativos = []
        saida = []
        imagens = []
        imagens_emitidas = set()
        for tipo, valor, _indice in eventos:
            if tipo == 'tagon':
                if valor not in ativos:
                    ativos.append(valor)
                continue
            if tipo == 'tagoff':
                if valor in ativos:
                    ativos.remove(valor)
                continue
            if tipo != 'text':
                continue

            tag_imagem = next((tag for tag in ativos if tag in self._imagens_outlook), None)
            if tag_imagem:
                if tag_imagem not in imagens_emitidas:
                    caminho = self._imagens_outlook[tag_imagem]
                    cid = f'gerador_outlook_{len(imagens) + 1}@imagem'
                    imagens.append((caminho, cid))
                    imagens_emitidas.add(tag_imagem)
                    saida.append(f'<br><img src="cid:{html.escape(cid, quote=True)}" style="max-width:100%;height:auto;"><br>')
                continue

            trecho = self._texto_html_outlook(valor, linha)
            estilos = []
            for tag in ativos:
                if tag in self._cores_outlook:
                    estilos.append('color:' + self._cores_outlook[tag])
                if tag in self._tamanhos_outlook:
                    estilos.append('font-size:' + str(self._tamanhos_outlook[tag]) + 'pt')
            if estilos:
                trecho = '<span style="' + ';'.join(estilos) + '">' + trecho + '</span>'
            if 'outlook_sublinhado' in ativos:
                trecho = '<u>' + trecho + '</u>'
            if 'outlook_italico' in ativos:
                trecho = '<em>' + trecho + '</em>'
            if 'outlook_negrito' in ativos:
                trecho = '<strong>' + trecho + '</strong>'
            tag_link = next((tag for tag in ativos if tag in self._links_outlook), None)
            if tag_link:
                url = self._preencher_modelo_outlook(self._links_outlook[tag_link], linha)
                trecho = '<a href="' + html.escape(url, quote=True) + '">' + trecho + '</a>'
            saida.append(trecho)

        html_corpo = '<html><body style="font-family:Segoe UI,Arial,sans-serif;font-size:11pt;">' + ''.join(saida) + '</body></html>'
        return html_corpo, imagens

    def _caminhos_anexos_outlook(self, linha):
        pasta_modelo = str(self._valor_componente('pasta_anexos')).strip()
        pasta = self._preencher_modelo_outlook(pasta_modelo, linha).strip()
        regra = str(self._valor_componente('regra_anexo')).strip()
        regras = [item.strip() for item in re.split(r'[;\n]+', regra) if item.strip()]
        caminhos = []
        ausentes = []

        for modelo in regras:
            relativo = self._preencher_modelo_outlook(modelo, linha).strip()
            if not relativo:
                continue
            caminho = relativo if os.path.isabs(relativo) else os.path.join(pasta, relativo) if pasta else relativo
            caminho = os.path.abspath(os.path.expandvars(os.path.expanduser(caminho)))
            if os.path.isfile(caminho):
                caminhos.append(caminho)
            else:
                ausentes.append(caminho)

        lista = getattr(self, 'lista_anexos_fixos')
        for caminho in lista.get(0, tk.END):
            caminho = os.path.abspath(os.path.expandvars(os.path.expanduser(str(caminho))))
            if os.path.isfile(caminho):
                caminhos.append(caminho)
            else:
                ausentes.append(caminho)

        unicos = []
        vistos = set()
        for caminho in caminhos:
            chave = os.path.normcase(os.path.normpath(caminho))
            if chave not in vistos:
                vistos.add(chave)
                unicos.append(caminho)
        return unicos, ausentes

    def _criar_rascunhos_outlook(self):
        if os.name != 'nt':
            messagebox.showwarning(
                'Outlook',
                'A criação de rascunhos pelo Outlook requer o Windows e o Outlook clássico instalado no computador.',
            )
            return
        if not self._dados_excel_outlook:
            messagebox.showwarning('Outlook', 'Selecione uma planilha do Excel com pelo menos uma linha de dados.')
            return
        modelo_para = str(self._valor_componente('email_to')).strip()
        if not modelo_para:
            messagebox.showwarning('Outlook', 'Informe o campo Para (.To). Você pode arrastar uma coluna do Excel para ele.')
            return
        try:
            import win32com.client as win32
        except ImportError:
            messagebox.showerror(
                'Outlook',
                'Para criar rascunhos no Outlook, instale a biblioteca pywin32 com:\n\npip install pywin32',
            )
            return
        try:
            outlook = win32.Dispatch('Outlook.Application')
        except Exception as erro:
            messagebox.showerror(
                'Outlook',
                'Não foi possível acessar o Outlook. Verifique se o Outlook clássico para Windows está instalado e configurado.\n\n' + str(erro),
            )
            return

        modelo_cc = str(self._valor_componente('email_cc')).strip()
        modelo_bcc = str(self._valor_componente('email_bcc')).strip()
        modelo_assunto = str(self._valor_componente('assunto_email')).strip()
        var_exigir = getattr(self, 'var_exigir_anexo', None)
        exigir_anexo = bool(var_exigir.get()) if var_exigir is not None else False

        criados = 0
        ignorados = 0
        problemas = []
        total = len(self._dados_excel_outlook)
        for indice, linha in enumerate(self._dados_excel_outlook, 1):
            self._status_outlook(f'criando rascunho {indice} de {total}...')
            self.update_idletasks()
            para = self._preencher_modelo_outlook(modelo_para, linha).strip()
            cc = self._preencher_modelo_outlook(modelo_cc, linha).strip()
            bcc = self._preencher_modelo_outlook(modelo_bcc, linha).strip()
            assunto = self._preencher_modelo_outlook(modelo_assunto, linha).strip()
            if not para:
                ignorados += 1
                problemas.append(f'Linha {indice}: destinatário Para vazio.')
                continue

            anexos, ausentes = self._caminhos_anexos_outlook(linha)
            corpo_html, imagens = self._corpo_html_outlook(linha)
            imagens_validas = []
            for caminho_imagem, cid in imagens:
                if os.path.isfile(caminho_imagem):
                    imagens_validas.append((caminho_imagem, cid))
                else:
                    ausentes.append(caminho_imagem)

            if ausentes and exigir_anexo:
                ignorados += 1
                problemas.append(
                    f'Linha {indice}: anexo não encontrado: ' + ', '.join(os.path.basename(x) or x for x in ausentes[:3])
                )
                continue

            mail = None
            try:
                mail = outlook.CreateItem(0)
                mail.To = para
                mail.CC = cc
                mail.BCC = bcc
                mail.Subject = assunto
                mail.BodyFormat = 2
                mail.HTMLBody = corpo_html
                mail.Save()

                for caminho in anexos:
                    mail.Attachments.Add(caminho)
                for caminho_imagem, cid in imagens_validas:
                    anexo = mail.Attachments.Add(caminho_imagem)
                    anexo.PropertyAccessor.SetProperty(
                        'http://schemas.microsoft.com/mapi/proptag/0x3712001F',
                        cid,
                    )
                mail.Save()
                criados += 1
                if ausentes:
                    problemas.append(
                        f'Linha {indice}: rascunho criado, mas arquivo não encontrado: ' + ', '.join(os.path.basename(x) or x for x in ausentes[:3])
                    )
            except Exception as erro:
                ignorados += 1
                problemas.append(f'Linha {indice}: {erro}')
                if mail is not None:
                    try:
                        mail.Delete()
                    except Exception:
                        pass

        self._status_outlook(f'{criados} rascunho(s) criado(s); {ignorados} linha(s) não concluída(s).')
        resumo = f'Rascunhos criados: {criados}\nLinhas não concluídas: {ignorados}'
        if problemas:
            resumo += '\n\nOcorrências:\n' + '\n'.join(problemas[:10])
            if len(problemas) > 10:
                resumo += f'\n... e mais {len(problemas) - 10} ocorrência(s).'
        messagebox.showinfo('Rascunhos do Outlook', resumo)

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
        caminho = filedialog.asksaveasfilename(title='Exportar para Excel', defaultextension='.xlsx', filetypes=[('Arquivo do Excel', '*.xlsx')])
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
        caminho = filedialog.askopenfilename(title='Abrir arquivo TXT', filetypes=[('Arquivo de texto', '*.txt'), ('Todos os arquivos', '*.*')])
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
            caminho = filedialog.asksaveasfilename(title='Salvar arquivo TXT', initialfile=caminho_atual.split('/')[-1].split('\\')[-1], defaultextension='.txt', filetypes=[('Arquivo de texto', '*.txt'), ('Todos os arquivos', '*.*')])
        else:
            caminho = filedialog.asksaveasfilename(title='Salvar arquivo TXT', defaultextension='.txt', filetypes=[('Arquivo de texto', '*.txt'), ('Todos os arquivos', '*.*')])
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
        caminho = filedialog.askopenfilename(title='Selecionar arquivo CSV', filetypes=[('Arquivo CSV', '*.csv'), ('Todos os arquivos', '*.*')])
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
        mapa = {'caminho_excel': 'caminho_excel', 'planilha_excel': 'planilha_excel', 'email_to': 'email_to', 'email_cc': 'email_cc', 'email_bcc': 'email_bcc', 'assunto_email': 'assunto_email', 'pasta_anexos': 'pasta_anexos', 'regra_anexo': 'regra_anexo', 'exigir_anexo': 'exigir_anexo', 'tamanho_texto_email': 'tamanho_texto_email', 'corpo_email': 'corpo_email'}
        escolhidos = list(selecionados or ['caminho_excel', 'planilha_excel', 'email_to', 'email_cc', 'email_bcc', 'assunto_email', 'pasta_anexos', 'regra_anexo', 'exigir_anexo', 'tamanho_texto_email', 'corpo_email'])
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
        sql = 'INSERT INTO rascunhos_outlook (' + ','.join(campos) + ') VALUES (' + placeholders + ')' 
        try:
            self.app.conexao.execute(sql, valores)
            self.app.conexao.commit()
        except sqlite3.IntegrityError as erro:
            messagebox.showerror('Banco de dados', f'Não foi possível cadastrar: {erro}')
            return
        messagebox.showinfo('SQLite', 'Dados cadastrados com sucesso!')

    def carregar_dados(self):
        pass
        self._atualizar_contadores()

    def aplicar_filtro(self):
        pass
        self._atualizar_contadores()

    def preencher_formulario(self, event=None):
        pass

    def atualizar_registro(self, selecionados=None):
        messagebox.showinfo('Configuração', 'Para atualizar pela tela, inclua uma Treeview e selecione o registro.')

    def excluir_registro(self):
        messagebox.showinfo('Excluir', 'Adicione uma Treeview à tela para selecionar o registro que será excluído.')

    def limpar_campos(self, selecionados=None):
        self._id_selecionado = None
        nomes = list(selecionados or ['caminho_excel', 'planilha_excel', 'lista_colunas_excel', 'email_to', 'email_cc', 'email_bcc', 'assunto_email', 'pasta_anexos', 'regra_anexo', 'exigir_anexo', 'tamanho_texto_email', 'lista_anexos_fixos'])
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
