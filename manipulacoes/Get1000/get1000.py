import json
import csv

def get1000(csv_file):
    articles = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            title = row[0]
            text = row[1]
            articles.append({'title': title, 'human_article': text})
    return articles

def shuffle1000(articles):
    import random
    random.shuffle(articles)
    random.shuffle(articles)
    return articles[1000:]

def save1000(articles, json_file):
    with open(json_file, 'w') as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)
        
def main():
    articles = get1000('../Articles/articles.csv')
    articles_shuffled = shuffle1000(articles)
    save1000(articles_shuffled, 'titles.json')

if __name__ == '__main__':
    main()
            