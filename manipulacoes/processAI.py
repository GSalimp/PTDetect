from peewee import *

db = PostgresqlDatabase(
    'postgres',
    user='postgres',
    password='changeme',
    host='localhost',
    port=5432
)

class Article(Model):
    id = AutoField()
    title = CharField(null=False)
    human_article = CharField(null=False)
    AI_article = CharField(column_name='AI_article', null=True)
    Rewritten_article = CharField(column_name='Rewritten_article', null=True)

    class Meta:
        database = db
        table_name = 'article'
        
db.connect()

ai_articles = Article.select().where(Article.human_article != '' and Article.AI_article.is_null(False))

print(len(ai_articles))