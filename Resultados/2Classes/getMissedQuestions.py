import json

with open('Llama3_12ClassesResults.json', 'r') as f:
    results = json.load(f)

missedQuestions = []

for result in results:
    if result['class_label'] == 0 and result['prediction'] != 'sim':
        missedQuestions.append(result)
    elif (result['class_label'] == 1 or result['class_label'] == 2) and result['prediction'] != 'não':
        missedQuestions.append(result)
        
with open('missedQuestions.json', 'w') as f:
    json.dump(missedQuestions, f, indent=4, ensure_ascii=False)
    
print(len(missedQuestions))
        