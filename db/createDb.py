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

if __name__ == "__main__":
    db.connect()
    db.create_tables([Article])
    print("Table created successfully.")
