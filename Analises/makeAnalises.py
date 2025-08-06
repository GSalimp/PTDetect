from peewee import *

db = PostgresqlDatabase(
    'postgres',  # Replace with your database name
    user='postgres',
    password='changeme',
    host='localhost',
    port=5432
)

class BaseModel(Model):
    class Meta:
        database = db
        
class Article(BaseModel):
    id = AutoField(primary_key=True)
    title = CharField(max_length=255, null=False)
    human_article = TextField(null=True)
    AI_article = TextField(null=True)
    Rewritten_article = TextField(null=True)
    
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
    
def getClassArticles():
    db.connect()
    
    #Get train articles
    human_train = Train.select().where(Train.class_label == 0)
    AI_train = Train.select().where(Train.class_label == 1)
    rewritten_train = Train.select().where(Train.class_label == 2)
    
    #Get test articles
    human_test = Test.select().where(Test.class_label == 0)
    AI_test = Test.select().where(Test.class_label == 1)
    rewritten_test = Test.select().where(Test.class_label == 2)
    
    db.close()
    
    print("Human Train Articles:", len(human_train))
    print("AI Train Articles:", len(AI_train))
    print("Rewritten Train Articles:", len(rewritten_train))
    print("Human Test Articles:", len(human_test))
    print("AI Test Articles:", len(AI_test))
    print("Rewritten Test Articles:", len(rewritten_test))
    
    return human_train, AI_train, rewritten_train, human_test, AI_test, rewritten_test
  
def makeAnalises():
    human_train, AI_train, rewritten_train, human_test, AI_test, rewritten_test = getClassArticles()
    
    average_human_train = 0
    average_AI_train = 0
    average_rewritten_train = 0
    average_human_test = 0
    average_AI_test = 0
    average_rewritten_test = 0
    average_human = 0
    average_AI = 0
    average_rewritten = 0
    minimal_human_train = 1000000
    minimal_AI_train = 1000000
    minimal_rewritten_train = 1000000
    minimal_human_test = 1000000
    minimal_AI_test = 1000000
    minimal_rewritten_test = 1000000
    maximal_human_train = 0
    maximal_AI_train = 0
    maximal_rewritten_train = 0
    maximal_human_test = 0
    maximal_AI_test = 0
    maximal_rewritten_test = 0
    
    for article in human_train:
        average_human_train += len(article.text)
        if len(article.text) < minimal_human_train:
            minimal_human_train = len(article.text)
        if len(article.text) > maximal_human_train:
            maximal_human_train = len(article.text)
    average_human_train /= len(human_train)
    
    for article in AI_train:
        average_AI_train += len(article.text)
        if len(article.text) < minimal_AI_train:
            minimal_AI_train = len(article.text)
        if len(article.text) > maximal_AI_train:
            maximal_AI_train = len(article.text)
    average_AI_train /= len(AI_train)
    
    for article in rewritten_train:
        average_rewritten_train += len(article.text)
        if len(article.text) < minimal_rewritten_train:
            minimal_rewritten_train = len(article.text)
        if len(article.text) > maximal_rewritten_train:
            maximal_rewritten_train = len(article.text)
    average_rewritten_train /= len(rewritten_train)
    
    for article in human_test:
      if(len(article.text) != 1):
        average_human_test += len(article.text)
        if len(article.text) < minimal_human_test:
            minimal_human_test = len(article.text)
        if len(article.text) > maximal_human_test:
            maximal_human_test = len(article.text)
      average_human_test /= len(human_test)
    
    for article in AI_test:
        average_AI_test += len(article.text)
        if len(article.text) < minimal_AI_test:
            minimal_AI_test = len(article.text)
        if len(article.text) > maximal_AI_test:
            maximal_AI_test = len(article.text)
    average_AI_test /= len(AI_test)
    
    for article in rewritten_test:
        average_rewritten_test += len(article.text)
        if len(article.text) < minimal_rewritten_test:
            minimal_rewritten_test = len(article.text)
        if len(article.text) > maximal_rewritten_test:
            maximal_rewritten_test = len(article.text)
    average_rewritten_test /= len(rewritten_test)
    
    average_human = (average_human_train + average_human_test) / 2
    average_AI = (average_AI_train + average_AI_test) / 2
    average_rewritten = (average_rewritten_train + average_rewritten_test) / 2
    
    print("Average Human Train Article Length:", average_human_train)
    print("Average AI Train Article Length:", average_AI_train)
    print("Average Rewritten Train Article Length:", average_rewritten_train)
    print("Average Human Test Article Length:", average_human_test)
    print("Average AI Test Article Length:", average_AI_test)
    print("Average Rewritten Test Article Length:", average_rewritten_test)
    print("Average Human Article Length:", average_human)
    print("Average AI Article Length:", average_AI)
    print("Average Rewritten Article Length:", average_rewritten)
    print("Minimal Human Train Article Length:", minimal_human_train)
    print("Minimal AI Train Article Length:", minimal_AI_train)
    print("Minimal Rewritten Train Article Length:", minimal_rewritten_train)
    print("Maximal Human Train Article Length:", maximal_human_train)
    print("Maximal AI Train Article Length:", maximal_AI_train)
    print("Maximal Rewritten Train Article Length:", maximal_rewritten_train)
    print("Minimal Human Test Article Length:", minimal_human_test)
    print("Minimal AI Test Article Length:", minimal_AI_test)
    print("Minimal Rewritten Test Article Length:", minimal_rewritten_test)
    print("Maximal Human Test Article Length:", maximal_human_test)
    print("Maximal AI Test Article Length:", maximal_AI_test)
    print("Maximal Rewritten Test Article Length:", maximal_rewritten_test)
    print("Minimal Human Article Length:", min(minimal_human_train, minimal_human_test))
    print("Minimal AI Article Length:", min(minimal_AI_train, minimal_AI_test))
    print("Minimal Rewritten Article Length:", min(minimal_rewritten_train, minimal_rewritten_test))
    print("Maximal Human Article Length:", max(maximal_human_train, maximal_human_test))
    print("Maximal AI Article Length:", max(maximal_AI_train, maximal_AI_test))
    print("Maximal Rewritten Article Length:", max(maximal_rewritten_train, maximal_rewritten_test))
    
  
if __name__ == "__main__":
  makeAnalises()
        
        