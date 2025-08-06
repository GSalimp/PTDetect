from peewee import *
import random

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

if __name__ == "__main__":
    db.connect()
    db.create_tables([Train, Test])
    print("Train and Test tables created successfully.")

    # Fetch all articles
    articles = Article.select().where(
        (Article.human_article != '') &
        (Article.AI_article.is_null(False)) &
        (Article.Rewritten_article.is_null(False))
    )

    # Prepare data for train and test tables
    data = []
    for article in articles:
        if article.human_article:
            data.append((article.id, article.human_article, 0))  # Class 0 for human_article
        if article.AI_article:
            data.append((article.id, article.AI_article, 1))  # Class 1 for AI_article
        if article.Rewritten_article:
            data.append((article.id, article.Rewritten_article, 2))  # Class 2 for Rewritten_article

    # Shuffle the data
    random.shuffle(data)

    # Split the data into train (80%) and test (20%)
    split_index = int(len(data) * 0.8)
    train_data = data[:split_index]
    test_data = data[split_index:]

    # Insert data into Train table
    with db.atomic():
        for article_id, text, class_label in train_data:
            Train.create(article_id=article_id, text=text, class_label=class_label)

    # Insert data into Test table
    with db.atomic():
        for article_id, text, class_label in test_data:
            Test.create(article_id=article_id, text=text, class_label=class_label)

    print("Data successfully inserted into Train and Test tables.")