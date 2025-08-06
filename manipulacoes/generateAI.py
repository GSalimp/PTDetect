import logging
from peewee import fn, Model, CharField, AutoField, PostgresqlDatabase, IntegrityError
import openai
import argparse

parser = argparse.ArgumentParser(description="Script para gerar e reescrever textos de IA.")

parser.add_argument('-q', '--qtd', type=int, required=True, help="Numero de textos a serem processados.")
args = parser.parse_args()

client = openai.OpenAI(
  api_key="YOUR_API_KEY_HERE",
  base_url="https://chat.maritaca.ai/api",
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("article_processing.log"),
        logging.StreamHandler()
    ]
)

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

def generate_ai(article):
    messages = [
        {"role": "user", "content": "Crie uma notícia jornalística com exatamente" + str(len(article.human_article)) + " caracteres, incluindo espaços, com o título: " + article.title + ". Assegure que o conteúdo seja informativo e esteja dentro do limite de caracteres especificado."},
    ]
    try:
      response = client.chat.completions.create(
        model="sabia-3",
        messages=messages,
        temperature=0.7,
        max_tokens=10000,
      )
      answer = response.choices[0].message.content
    except Exception as e:
      logging.error(f"Error generating AI article for {article.id}: {e}", exc_info=True)
    return answer

def rewrite(article):
    messages = [
        {"role": "user", "content": "Reescreva a notícia jornalística abaixo, mantendo o mesmo contexto e informações, mas utilizando suas próprias palavras: " + article.human_article},
    ]
    try:
      response = client.chat.completions.create(
        model="sabia-3",
        messages=messages,
        temperature=0.7,
        max_tokens=10000,
      )
      answer = response.choices[0].message.content
    except Exception as e:
      logging.error(f"Error rewriting article for {article.id}: {e}", exc_info=True)
    return answer

db.connect()

def process_articles(batch_size):
    try:
        logging.info("Starting article processing...")
        
        articles = (
            Article.select()
            .where((Article.AI_article.is_null()) | (Article.Rewritten_article.is_null()))
            .order_by(Article.id)
            .limit(batch_size)
        )

        if not articles:
            logging.info("No articles to process.")
            return
        
        for article in articles:
            try:
                logging.info(f"Processing Article ID: {article.id}, Title: {article.title}")
                    
                ai_article = generate_ai(article)
                rewritten_article = rewrite(article)

                rows_updated = (
                    Article.update(
                        AI_article=ai_article,
                        Rewritten_article=rewritten_article
                    ).where(Article.id == article.id).execute()
                )
                if rows_updated == 1:
                    logging.info(f"Article ID {article.id} updated successfully.")
                else:
                    logging.warning(f"Article ID {article.id} not updated. Check constraints.")
                
            except Exception as e:
                logging.error(f"Error processing Article ID {article.id}: {e}", exc_info=True)

    except Exception as e:
        logging.critical(f"Critical error during article processing: {e}", exc_info=True)

    finally:
        logging.info("Article processing completed.")

process_articles(args.qtd)

db.close()