from peewee import *

db = SqliteDatabase('Polzovateli.db')


class Plov(Model):
    name = CharField()
    email = IntegerField()
    parol = IntegerField()

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Plov])
