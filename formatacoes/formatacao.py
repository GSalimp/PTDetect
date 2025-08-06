import json
from peewee import *

# Connect to the PostgreSQL database
db = PostgresqlDatabase(
    'postgres',  # Replace with your database name
    user='postgres',  # Replace with your username
    password='changeme',  # Replace with your password
    host='localhost',  # Replace with your database host if not local
    port=5432           # Replace with your database port if not default
)

class BaseModel(Model):
    class Meta:
        database = db

class Article(BaseModel):
    id = AutoField(primary_key=True)  # Auto-incrementing primary key
    title = CharField(max_length=255, null=False)  # Article title, not nullable
    human_article = TextField(null=True)  # Human-written article
    AI_article = TextField(null=True)  # AI-generated article
    Rewritten_article = TextField(null=True)  # Rewritten article

class Train(BaseModel):
    id = AutoField(primary_key=True)
    article_id = ForeignKeyField(Article, backref='train')
    text = TextField(null=False)
    class_label = IntegerField(null=False)

class Test(BaseModel):
    id = AutoField(primary_key=True)
    article_id = ForeignKeyField(Article, backref='test')
    text = TextField(null=False)
    class_label = IntegerField(null=False)
    
def process_articles(title, text, class_label):
    text = text.replace(title, '')
    text = text.replace('*', '')
    text = text.replace('#', '')
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    text = text.replace('\"', '"')
    if text.startswith(' '):
        text = text[1:]
    return {
        'title': title,
        'text': text,
        'class_label': class_label
    }
    
if __name__ == "__main__":
    db.connect()
    
    train_articles = []
    test_articles = []
    # Fetch and process data from Train table
    train_entries = Train.select(Train, Article.title).join(Article)
    for entry in train_entries:
        train_articles.append(process_articles(entry.article_id.title, entry.text, entry.class_label))

    # Fetch and process data from Test table
    test_entries = Test.select(Test, Article.title).join(Article)
    for entry in test_entries:
        test_articles.append(process_articles(entry.article_id.title, entry.text, entry.class_label))
        
    with open('Articles/trainArticles.json', 'w') as f:
        json.dump(train_articles, f, ensure_ascii=False, indent=4)
        
    with open('Articles/testArticles.json', 'w') as f2:
        json.dump(test_articles, f2, ensure_ascii=False, indent=4)
