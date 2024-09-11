import classes as cl

if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome de usúario: ')
    email = input('Informe o E-mail do usúario: ')
    cpf = input('Informe o CPF do usúario: ')
    profissao = input('Informe a Profissão do usúario: ')
    endereco = input('Informe o Endereço do usúario: ')
    telefone = input('Informe o Telefone do usúario: ')

    # instancia a classe pessoa fisica
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone)

    # Entrada de dados
    nome = input('Informe o nome da Empresa: ')
    email = input('Informe o E-mail da Empresa: ')
    cnpj = input('Informe o CNPJ da Empresa: ')
    razao_social = input('Informe a Razão social da Empresa: ')
    endereco = input('Informe o Endereço da Empresa: ')
    telefone = input('Informe o Telefone da Empresa: ')

    # instancia a classe pessoa juridica
    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    # Saida de dados
    usuario.mostrar_cartao_visitas()
    print('-'*30)
    empresa.mostrar_cartao_visitas()
    