from twitter import app, database
from twitter.models import User


# No contexto de bancos de dados e ORM (Object-Relational Mapping), "filtrar" significa selecionar registros que atendem a certos critérios específicos. Quando você filtra, você está procurando apenas por aqueles dados que correspondem a determinadas condições, em vez de obter todos os registros da tabela.

# Exemplo Simples
# Vamos imaginar que você tem uma tabela de usuários e quer encontrar todos os usuários com o nome "João". Filtrar significa buscar na tabela apenas os registros onde o nome do usuário é "João".

# Como Filtrar Usando SQLAlchemy
# Filtrar por Atributo Específico
# Se você quer encontrar todos os usuários com um determinado nome de usuário, você pode usar filter_by:
    # filter_by: Permite filtrar registros pela igualdade de um ou mais atributos.
usuarios_com_username_joao = User.query.filter_by(username="joao123").all()


# Filtrar Usando Condições Personalizadas
# Se você precisa de uma condição mais complexa, você pode usar filter:
# filter: Permite usar expressões mais complexas, como comparações e combinações de condições.
usuarios_com_nome_joao = User.query.filter(User.name == "João").all()


# Exemplos de Filtros Comuns
# Filtrar por Nome

usuarios_com_nome_joao = User.query.filter(User.name == "João").all()

# Filtrar por Parte do Nome (Usando like)
# like: Busca por uma substring dentro de um campo. % é um caractere coringa que representa qualquer sequência de caracteres.
usuarios_com_nome_joao = User.query.filter(User.name.like("%João%")).all()


# Filtrar por Múltiplas Condições
usuarios_com_nome_joao_e_email = User.query.filter(User.name == "João", User.email == "joao@example.com").all()


# Resumo
# Filtrar: Selecionar registros que atendem a certas condições específicas.
# Métodos para filtrar:
# filter_by: Para condições simples de igualdade.
# filter: Para condições mais complexas e expressões.
# Usos comuns:
# Encontrar registros com valores específicos (==, !=).
# Buscar por padrões em strings (like).
# Combinar múltiplas condições (and, or).
# Filtrar é uma operação essencial para trabalhar eficientemente com dados, permitindo que você obtenha apenas as informações relevantes de um grande conjunto de registros.