from modelos import Pessoas, Usuarios


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Gabriel', idade=20)
    print(pessoa)
    pessoa.save()


# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Lucas').first()
    print(pessoa.idade)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    pessoa.nome = 'Luan'
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Luan').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('Gabriel', '1234')
    insere_usuario('Luan', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    #consulta_pessoas()
