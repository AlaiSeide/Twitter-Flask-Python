from twitter import app, database
from twitter.models import User


with app.app_context():
    database.drop_all()
    database.create_all()


# with app.app_context():
#     usuario1 = User(username='Alai Seide', password='1234', name='Alai', email='tenw313@gmail.com')
#     database.session.add(usuario1)
#     database.session.commit()

# with app.app_context():
#     usuario2 = User(username='Maicon Scofield', password='1234', name='Maicon', email='alaiseide2006@gmail.com')
#     database.session.add(usuario2)
#     database.session.commit()

with app.app_context():
    user = User.query.all()
    print(user)

# 1. Criar um usuário (Inserir)
# Para criar um novo usuário, você instancia a classe User e adiciona a sessão do banco de dados.

novo_usuario = User(username="joao123", password="senha_secreta", name="João", email="joao@example.com")
database.session.add(novo_usuario)
database.session.commit()



# 2. Ler (Consultar)
# Para ler os dados dos usuários, você pode usar a função query.
# Ler todos os usuários:

usuarios = User.query.all()
for user in usuarios:
    print(user)

# Ler um usuário específico (por ID):

user = User.query.get(1)
print(user)

# Filtrar usuários:

joao = User.query.filter_by(username="joao123").first()
print(joao)


# 3. Atualizar um usuário
# Para atualizar um registro, você primeiro consulta o usuário, altera os atributos desejados e, em seguida, faz o commit.

user = User.query.filter_by(username="joao123").first()
user.email = "novoemail@example.com"
database.session.commit()


# . Deletar um usuário
# Para deletar um registro, você consulta o usuário, remove-o da sessão e faz o commit.

user = User.query.filter_by(username="joao123").first()
database.session.delete(user)
database.session.commit()


# 5. Filtrar e Ordenar
# Filtrar usuários por uma condição:

usuarios_joao = User.query.filter(User.name.like("%João%")).all()
for user in usuarios_joao:
    print(user)


# Ordenar usuários:
usuarios_ordenados = User.query.order_by(User.username).all()
for user in usuarios_ordenados:
    print(user)


# Resumo
# Criar: session.add e session.commit
# Ler: query.all, query.get, query.filter_by
# Atualizar: Consultar, modificar atributos, session.commit
# Deletar: Consultar, session.delete, session.commit
# Filtrar: query.filter
# Ordenar: query.order_by
