from twitter import app, database
from twitter.models import User, Post, Follow


# with app.app_context():
#     database.drop_all()
#     database.create_all()


# Criação de um novo usuário
# with app.app_context():
#     novo_usuario = User(username='Joao Lira', password='123456', name='João', email='joao@mail.com')
#     database.session.add(novo_usuario)
#     database.session.commit()

# # Criação de um novo post associado ao usuário
# with app.app_context():
#     novo_usuario = User.query.filter_by(email='joao@mail.com').first()
#     for post in novo_usuario.posts:
#         print(post.content)
    # novo_post = Post(content='Meu primeiro post!', user_id=novo_usuario.id)
    # database.session.add(novo_post)
    # database.session.commit()

# # Consulta de posts de um usuário
# usuario = User.query.filter_by(name='João').first()
# for post in usuario.posts:
#     print(post.content)


# with app.app_context():
#     posts = Post.query.all()
#     for post in posts:
#         print(post.author)

with app.app_context():
    # Obtém um post
    post = Post.query.first()


    # Acessa o autor do post
    autor_do_post = post.author

    print(autor_do_post)