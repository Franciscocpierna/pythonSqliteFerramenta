GERADOR VISUAL INTELIGENTE DE SISTEMAS PYTHON + SQLITE

Este projeto permite criar programas visualmente com Python, Tkinter e SQLite.

COMO FUNCIONA

1. Arraste componentes para o Designer Visual.
2. Dê os nomes que quiser aos campos.
3. Configure textos, máscaras e validações.
4. Nos botões, escolha uma ação genérica.
5. Se a ação usar dados, selecione visualmente os campos que participarão.
6. Indique o campo que receberá o resultado.
7. Gere e execute o código Python.

AÇÕES GENÉRICAS

O Gerador não depende de ações específicas como "Calcular IMC" ou
"Calcular desconto". Os projetos usam blocos reutilizáveis:

- Cadastrar no SQLite
- Atualizar registro
- Excluir registro
- Pesquisar / aplicar filtro
- Limpar campos selecionados
- Inserir valor em campo
- Calcular com campos
- Calcular expressão de um campo
- Aplicar condição
- Gerar lista por repetição
- Abrir outra tela
- Entrar / validar login
- Sair da conta
- Voltar para tela anterior
- Mostrar mensagem
- Fechar sistema

CÁLCULOS

Na ação "Calcular com campos", o usuário pode selecionar quantos campos precisar.
Os seis primeiros aparecem inicialmente e o botão "+ Adicionar mais um campo à ação"
cria novos seletores sem um limite fixo. Depois disso, escolha a operação desejada:

- Somar
- Subtrair
- Multiplicar
- Dividir
- Média
- Porcentagem
- Resto da divisão
- Potência
- Mínimo
- Máximo
- Operação definida pelo conteúdo de outro campo
- Expressão personalizada

Nas expressões personalizadas:
A = Campo 1
B = Campo 2
C = Campo 3
...
Z = Campo 26
AA = Campo 27
AB = Campo 28, e assim por diante
CAMPO1, CAMPO2, CAMPO3... também podem ser usados de acordo com a ordem dos campos
Para ações com muitos campos, CAMPO1, CAMPO2... é a forma mais explícita de referência.
R = resultado anterior, quando utilizado na segunda expressão
N = contador da repetição

Exemplo:
round(A * B * (1 - C / 100), 2)

Assim, o usuário pode criar regras próprias sem depender dos exemplos do curso.

SQLITE

Os componentes de entrada podem ser associados a campos do banco. Quando o
campo do banco estiver vazio, o Gerador consegue usar o nome do próprio
componente como coluna SQLite.

Os exemplos prontos possuem botão "Cadastrar no SQLite".

Um projeto criado do zero começa somente com uma tela simples e o título configurado.
Nenhum campo SQLite ou aba adicional é criado automaticamente nesse momento.

Quando um botão recebe a ação "Cadastrar no SQLite", a tela automática "Dados cadastrados" passa a fazer parte do projeto e aparece também no seletor de telas do Designer.

A tela "Dados cadastrados" permite:
- escolher a tabela;
- visualizar os registros;
- atualizar a lista;
- selecionar um registro;
- excluir o registro do SQLite.

No Designer, essa tela pode ser selecionada para visualizar sua estrutura e pode ser removida manualmente pelo botão "Remover". Ao removê-la, os campos e os registros do SQLite são mantidos; somente a tela automática de consulta deixa de ser incluída no programa gerado.

O código gerado também verifica colunas novas e consegue acrescentá-las em
tabelas SQLite já existentes.

MODELOS

Os modelos prontos também usam a mesma estrutura de ações e SQLite.

62 PROJETOS

O menu "62 Projetos" cria o exemplo escolhido diretamente no Designer Visual. Cada projeto pode ser editado, ter componentes movidos, copiados, renomeados ou excluídos e continua usando o mesmo gerador de código em tempo real.

1. Cadastro de Alunos
2. Cadastro de Produtos
3. Calculadora Básica com Teclado
4. Calculadora de Média Escolar
5. Calculadora de IMC
6. Calculadora de Desconto
7. Calculadora de Comissão de Vendas
8. Conversor de Temperatura
9. Conversor de Quilômetros para Milhas
10. Gerador de Tabuada
11. Verificador de Número Par ou Ímpar
12. Verificador de Maioridade
13. Classificador de Nota
14. Calculadora de Salário Líquido
15. Calculadora de Horas Trabalhadas
16. Calculadora de Consumo de Combustível
17. Simulador de Troco
18. Simulador de Parcelamento
19. Gerador de Orçamento Simples
20. Controle de Notas Acadêmicas
21. Lista de Tarefas
22. Agenda de Compromissos
23. Controle de Empréstimos de Livros
24. Alerta de Estoque Mínimo
25. Pesquisa de Satisfação
26. Questionário de Múltipla Escolha
27. Formulário de Inscrição em Evento
28. Sistema de Login Simples
29. Menu com Várias Telas
30. Calculadora com Histórico
31. Cronômetro
32. Temporizador
33. Gerador de Senhas Seguras
34. Calculadora de Idade Completa
35. Sorteador de Nomes
36. Gerador de Números para Sorteio
37. Quiz Interativo
38. Preferências com RadioButton, Spinbox, Scale, Separador e Frame
39. Formulário com Senha, E-mail, Data e Horário
40. Editor com ScrolledText, Menubutton e ToggleButton
41. Painel com Progressbar, Separador Vertical e Canvas
42. Lista com Filtro, Contador e Exportação para Excel
43. Exportar Listbox para Excel
44. Exportar Dados da Treeview para Excel
45. Criador de E-mails em Rascunho no Outlook
46. Quebrar Planilha do Excel por Coluna
47. Quebrar Arquivo com Várias Abas por Coluna
48. Gerenciador de Itens na Listbox
49. Lista de Compras Interativa
50. Gerador de Sequência Numérica em Lista
51. Treeview Personalizada
52. Campos Obrigatórios e Campos Bloqueados
53. Contador de Palavras e Caracteres
54. Localizar e Substituir em um Texto
55. Editor de Arquivo TXT
56. Calculadora de Intervalo entre Datas
57. Organizador de Lista
58. Importador de CSV para Treeview
59. Estatísticas de uma Lista Numérica
60. Conversor de Texto
61. Gerador de Calendário Mensal
62. Analisador de Força de Senha

RECURSOS DOS PROJETOS 48 A 52

Os projetos 48 e 49 demonstram inclusão, exclusão e limpeza de itens em Listbox. As ações podem ser escolhidas manualmente na configuração dos botões e reutilizadas em outras listas.

O projeto 50 gera uma sequência numérica de 1 até a quantidade informada pelo usuário. O exemplo começa com 600, mas aceita outras quantidades positivas sem o limite artificial de 60.

O projeto 51 demonstra a personalização visual da Treeview por meio das propriedades de fonte, tamanho, negrito, cor do texto e cor do fundo.

O projeto 52 demonstra campos obrigatórios e campos bloqueados. Campos marcados como obrigatórios precisam ser preenchidos antes do cadastro. Campos marcados como bloqueados ficam somente para leitura durante a execução do programa.

RECURSOS DOS PROJETOS 53 A 62

Os projetos 53 e 54 trabalham análise, busca e substituição de texto. O projeto 55 abre e salva arquivos TXT utilizando caixas de diálogo do Windows.

O projeto 56 calcula a diferença entre duas datas. O projeto 57 demonstra ordenação e remoção de duplicados em Listbox. O projeto 58 importa arquivos CSV diretamente para uma Treeview, criando as colunas a partir do cabeçalho do arquivo.

O projeto 59 calcula quantidade, soma, média, mediana, menor e maior valor de uma lista numérica. O projeto 60 transforma textos em maiúsculas, minúsculas e formato de título. O projeto 61 monta um calendário mensal e o projeto 62 analisa critérios de força de uma senha.

As ações usadas nesses exemplos também aparecem na lista de ações dos botões, permitindo reutilizá-las em projetos criados manualmente.

CALCULADORA COM TECLADO

A calculadora utiliza componentes comuns:
- os botões numéricos usam "Inserir valor em campo";
- o usuário escolhe qual campo funciona como visor;
- o botão "=" usa "Calcular expressão de um campo";
- o botão de limpeza usa "Limpar campos selecionados".

Portanto, o nome do visor pode ser qualquer um.

EXECUÇÃO

No Windows, execute:

INICIAR.bat

ou:

python main.py

O projeto utiliza Python, Tkinter e SQLite.

Para usar recursos com arquivos .xlsx nos programas gerados, instale também o openpyxl com:

pip install openpyxl

O exemplo de criação de rascunhos no Outlook utiliza o Outlook clássico para Windows e a biblioteca pywin32:

pip install pywin32

Esse exemplo cria mensagens na pasta de rascunhos e não executa envio automático.

Os projetos 46 e 47 utilizam openpyxl para ler e criar arquivos do Excel. O projeto 46 permite quebrar uma aba por uma coluna, gerando um único arquivo com várias abas ou vários arquivos separados. O projeto 47 lê várias abas do mesmo arquivo e gera um arquivo separado para cada valor da coluna escolhida, mantendo as abas originais filtradas por esse valor.

ARQUIVOS DE TESTE DOS PROJETOS 46 E 47

Na pasta arquivos_teste existem dois arquivos prontos:

- Projeto_46_Teste_Quebra_Por_Coluna.xlsx: use a aba Dados e escolha a coluna Departamento. Financeiro e Vendas possuem 5 registros cada, RH possui 4 e TI possui 6.
- Projeto_47_Teste_Quebra_Varias_Abas.xlsx: possui Janeiro, Fevereiro, Março e Abril. Escolha a coluna Filial para gerar um arquivo por filial mantendo as quatro abas filtradas.

ARQUIVOS DE TESTE DOS PROJETOS 55 E 58

Na mesma pasta também existem exemplos simples para testar os novos recursos:

- Projeto_55_Exemplo_Texto.txt: arquivo de texto pronto para abrir, editar e salvar no Editor de Arquivo TXT.
- Projeto_58_Exemplo_Alunos.csv: arquivo CSV com Nome, Curso, Nota e Cidade para importar diretamente na Treeview.

EDIÇÃO VISUAL EM TEMPO REAL

O Designer trabalha com sincronização automática. Não é necessário clicar em um botão para atualizar o código depois de mover, redimensionar, renomear, copiar, colar, adicionar ou excluir um componente.

- As réguas horizontal e vertical mostram as coordenadas em pixels.
- Ao aproximar um componente de outro, linhas-guia ajudam a alinhar bordas e centros.
- O componente selecionado possui alças nas laterais e nos cantos para aumentar ou diminuir largura e altura livremente.
- Ctrl + clique ou Shift + clique seleciona vários componentes.
- Ctrl + C copia um ou vários componentes selecionados.
- Ctrl + V cola novas cópias independentes.
- Ctrl + D duplica a seleção.
- As setas movem a seleção em 1 pixel.
- Shift + setas movem a seleção em 10 pixels.

Cada componente colado recebe um novo identificador e um novo nome. Quando o componente representa um campo de dados, ele também recebe sua própria coluna SQLite. Por isso, renomear a cópia não altera o componente original.

PERSONALIZAÇÃO VISUAL DOS COMPONENTES

Ao selecionar um componente, o painel de propriedades possui a área "Personalização visual". As mudanças são refletidas no Designer e no código Python em tempo real.

É possível configurar:
- fonte;
- tamanho da fonte;
- negrito;
- itálico;
- sublinhado;
- alinhamento do conteúdo: esquerda, centro ou direita;
- cor do texto;
- cor de fundo.

As cores podem ser digitadas pelo nome aceito pelo Tkinter ou por valor hexadecimal, como #1f4e78. Os botões "Escolher cor do texto" e "Escolher cor de fundo" abrem um seletor visual. O botão "Restaurar aparência padrão" remove a personalização do item selecionado e volta a usar as definições do tema.

Cada componente mantém sua própria aparência. Ao copiar e colar um item, a cópia recebe a mesma aparência inicial, mas pode ser personalizada depois sem alterar o componente original. As propriedades também são gravadas junto com o projeto e reaparecem quando ele é aberto novamente.

Nos componentes que não possuem conteúdo textual, somente as propriedades visualmente aplicáveis são utilizadas.

CAMPOS E TREEVIEWS

As colunas do SQLite acompanham os campos existentes no Designer. Se existir apenas um campo chamado "nome", as Treeviews e a tela "Dados cadastrados" exibem somente "nome". Se o campo for renomeado para "cliente", o código e as Treeviews passam a usar "cliente". Se o campo for excluído, ele deixa de fazer parte da estrutura gerada.

O identificador interno do SQLite continua existindo para localizar registros durante alterações e exclusões, mas não aparece como uma coluna criada pelo usuário.

MODELOS PRONTOS COMPLETOS

Os modelos da janela "Modelos prontos" foram estruturados para funcionar como sistemas utilizáveis e editáveis no Designer, e não apenas como telas demonstrativas.

Os dois modelos finais possuem um fluxo de acesso completo:
- tela de Login;
- botão "Cadastrar usuário" disponível na própria tela de Login;
- cadastro de usuário com Nome, Usuário e Senha;
- Menu Principal após a autenticação;
- tela "Usuários" para gerenciar contas cadastradas;
- módulo principal correspondente ao modelo escolhido;
- aba "Dados cadastrados" para consultar, editar e excluir registros.

O usuário inicial para testes continua sendo:
- Usuário: admin
- Senha: admin

CADASTRO E GERENCIAMENTO DE USUÁRIOS

A tela "Cadastrar Usuário" permite criar uma conta antes de entrar no sistema. O nome de usuário não pode ficar vazio e não é permitido cadastrar dois usuários com o mesmo nome.

Na tela "Usuários" é possível cadastrar, pesquisar, selecionar, alterar e excluir usuários. A conta possui Nome, Usuário, Senha, Perfil e Status.

Ao alterar um usuário, o campo de senha fica vazio propositalmente. Se ele continuar vazio ao salvar, a senha existente é mantida. Se uma nova senha for digitada, ela substitui a anterior e é armazenada de forma protegida pelo sistema.

A senha não é exibida como texto nem como código de hash nas Treeviews. Ela aparece mascarada.

EDIÇÃO NA ABA DADOS CADASTRADOS

A aba "Dados cadastrados" possui as ações:
- Atualizar lista;
- Editar selecionado;
- Excluir selecionado.

Um duplo clique sobre um registro também abre a edição.

Ao escolher "Editar selecionado", o programa abre uma janela com os campos daquele registro. A edição é montada dinamicamente de acordo com as colunas reais do projeto, portanto também acompanha os campos criados ou renomeados no Designer.

Quando o registro possuir senha, o campo de edição começa vazio. Deixá-lo vazio preserva a senha atual; preencher uma nova senha grava a nova credencial protegida.

Os dados de usuários são exibidos uma única vez na lista de fontes da aba "Dados cadastrados", mesmo que várias telas do sistema utilizem a mesma tabela SQLite.

ESTRUTURA DOS MODELOS

Os modelos de cadastro e controle mantêm o CRUD do módulo principal e acrescentam o fluxo completo de usuários e autenticação. O Sistema Comercial mantém seus vários módulos de negócio. A Calculadora também utiliza o mesmo fluxo de Login, cadastro de usuário, Menu Principal e gerenciamento de usuários antes da funcionalidade principal.

Tudo continua editável no Designer Visual. Telas, campos, botões, ações, nomes, posições, tamanhos, cores, fontes, colunas SQLite e títulos de Treeview podem ser modificados e o código gerado acompanha as mudanças automaticamente. A personalização visual de fonte, tamanho, negrito, itálico, sublinhado, cor do texto, cor de fundo e alinhamento é aplicada aos componentes compatíveis, incluindo Entry, Text, ScrolledText, Combobox, Listbox, Treeview, botões, seletores, Spinbox, Scale e outros controles temáticos.

## Componentes disponíveis no Designer

O Designer possui 24 tipos de componentes: Texto / Rótulo, Campo de texto, Texto multilinha, Lista suspensa, Lista, Tabela / Treeview, Botão, Caixa de seleção, Botão de opção, Campo numérico, Controle deslizante, Separador, Painel / Grupo, Filtro de tabela, Campo de senha, Campo de e-mail, Campo de data, Campo de horário, Texto com rolagem, Menu de opções, Botão liga/desliga, Barra de progresso, Separador vertical e Área de desenho.

A janela de edição dos registros mantém os botões Salvar alterações e Cancelar fixos no rodapé. Quando existirem muitos campos, a área do formulário possui rolagem vertical e também aceita a roda do mouse.

EXPORTAÇÃO PARA ARQUIVO EXECUTÁVEL

Na aba "Código", ao lado do botão "Exportar .py", existe o botão "Exportar .exe".

Ao utilizar essa opção:
- o Gerador utiliza o código Python correspondente ao projeto que está atualmente no Designer Visual;
- o usuário escolhe o nome e a pasta do arquivo executável;
- o PyInstaller cria um único arquivo .exe em modo gráfico, sem abrir uma janela de console junto com o programa Tkinter;
- os arquivos temporários utilizados durante a criação são removidos automaticamente;
- se o projeto utiliza leitura ou exportação de Excel, o openpyxl também é verificado para manter esse recurso no executável;
- se o projeto utiliza automação do Outlook, o pywin32 e os módulos COM necessários também são incluídos no empacotamento;
- se alguma biblioteca necessária não estiver instalada, o Gerador oferece a instalação automática.

A criação de arquivos .exe deve ser executada no Windows. O arquivo final pode ser aberto diretamente pelo Windows sem precisar abrir manualmente o arquivo .py correspondente.
