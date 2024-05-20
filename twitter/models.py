from twitter import database


class User(database.Model):
    __tablename__ = 'usuarios'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), unique=True)
    password = database.Column(database.String)
    name = database.Column(database.String(50))
    email = database.Column(database.String(120), unique=True)
    #posts:
    # Cria um relacionamento de um-para-muitos entre User e Post. O parâmetro backref='user' cria um atributo user nos objetos Post, permitindo acessar o usuário dono do post. O parâmetro lazy=True indica que os posts do usuário serão carregados sob demanda.
    posts = database.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    # A função __repr__ que você mostrou serve para retornar o nome de usuário (username) quando você tenta obter uma representação do objeto. Isso pode ajudar a ver rapidamente informações úteis sobre o objeto ao imprimir ou depurar.
    def __repr__(self):
        return self.username


class Post(database.Model):
    # Define o nome da tabela no banco de dados: 'posts'.
    __tablename__ = 'posts'
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.Text)
    user_id = database.Column(database.Integer, database.ForeignKey('usuarios.id'))
    

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'{self.id} - {self.user.username}'
    

class Follow(database.Model):
    __tablename__ = 'follow'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('usuarios.id'))
    follower_id = database.Column(database.Integer, database.ForeignKey('usuarios.id'))

    user = database.relationship('User', foreign_keys=user_id)
    follower = database.relationship('User', foreign_keys=follower_id)
    