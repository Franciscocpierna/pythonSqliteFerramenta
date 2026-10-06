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

Para usar a ação de exportação para arquivo .xlsx nos programas gerados, instale também o openpyxl com:

pip install openpyxl

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

Tudo continua editável no Designer Visual. Telas, campos, botões, ações, nomes, posições, tamanhos, cores, fontes, colunas SQLite e títulos de Treeview podem ser modificados e o código gerado acompanha as mudanças automaticamente.

## Componentes disponíveis no Designer

O Designer possui 24 tipos de componentes: Texto / Rótulo, Campo de texto, Texto multilinha, Lista suspensa, Lista, Tabela / Treeview, Botão, Caixa de seleção, Botão de opção, Campo numérico, Controle deslizante, Separador, Painel / Grupo, Filtro de tabela, Campo de senha, Campo de e-mail, Campo de data, Campo de horário, Texto com rolagem, Menu de opções, Botão liga/desliga, Barra de progresso, Separador vertical e Área de desenho.

A janela de edição dos registros mantém os botões Salvar alterações e Cancelar fixos no rodapé. Quando existirem muitos campos, a área do formulário possui rolagem vertical e também aceita a roda do mouse.
