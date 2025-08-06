import json

with open('3ClassesResults.json', 'r') as f:
    results = json.load(f)

missedQuestions = []

for result in results:
    if result['class_label'] != int(result['prediction']):
        missedQuestions.append(result)
        
with open('missedQuestions.json', 'w') as f:
    json.dump(missedQuestions, f, indent=4, ensure_ascii=False)
    
print(len(missedQuestions))
    