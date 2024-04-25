from models import *

# Plov.create(name='Adik', email='adikabdulhayev@hotmail.com', parol='1991')
# Plov.create(name='Aygerim', email='aigerim@gmail.com', parol='1998')
# Plov.create(name='Abuzar', email='abuzar@hotmail.com', parol='2023')


# users = Plov.select()
# for user in users:
#     print(user.name, user.email, user.parol)

# query = Plov.update(name='Dantes').where(Plov.id == 1)
# query.execute()

# Plov.delete().where(Plov.email == 'adikabdulhayev@hotmail.com').execute()


# eda = Plov.select().where(Plov.name **'A%')
# for user in eda:
#     print(user.name, user.email, user.parol)


# eda = Plov.select().where(Plov.email**'%@gmail.com')
# for user in eda:
#     print(user.name, user.email, user.parol)