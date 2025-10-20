Esse é um desafio de CRUD com banco de dados no sqlite e Python, onde estou aplicando o que estou estudando com o Python e SQLite.

• Atualmente o banco de dados é unico tanto para os dois tipos de clientes (PF, PJ) e está com uma conexão global.

O código possui diversas funções que compoem o CRUD:

• create_table(): função de uso único apenas para criar a tabela do banco de dados.

• register_cpf(): Responsável por processar os dados de entrada para criação de PF(Pessoa fisica) e registrar na tabela clientes.

• register_cnpj(): Formulada na mesma estrutura da register_cpf(), porém ela diferencia a entrada e o registro para PJ(Pessoa juridica) na tabela clientes.

• update_client_cpf(): Essa função atualiza os dados de um cliente PF(Pessoa Fisica), ele pode alterar o Nome e o CPF do cliente na tabela.

• update_client_cnpj(): Novamente, segue a estrutura da update_client_cpf(), diferenciado apenas as entradas dos dados.

• show_physical_person() e show_juridical_person(): Retornam uma verificação da tabela do banco de dados, para validar se o dado requisito(CPF ou CNPJ)
é existente ou não no id da tabela, assim diferenciando os clientes fisicos dos juridicos.

• for_physical_person() e for_juridical_person(): Essas funções rodam a estrutura "for" com uma variavel atribuindo as funções show_physical_person() e show_juridical_person()
respectivamente para cada função semelhante ao dado, com o intuito de fazer a separação dos clientes PF e PJ e realizar a listagem dos clientes.

• delete_data_client(): Função de DELETE comum, que solicita apenas o id do cliente na tabela e realiza o DELETE dos dados desse id.

• menu(): Aqui é onde toda a interação com o CRUD acontece, com uma estrutura while True para rodar o loop, e a estrutura if, elif e else para poder intaragir selecionando
cada ação do menu, e estar operando o CRUD com a tabela do SQLite.

Por fim é chamado a função menu() e o CRUD passa a ser interativo no terminal.
