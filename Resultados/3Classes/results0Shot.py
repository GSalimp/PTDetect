import json
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, classification_report


with open('0Shot_Llama3_23ClassesResults.json', 'r') as f:
    results = json.load(f)
    
y_true = []
y_pred = []

for result in results:
    try:
        y_pred.append(int(result['prediction'][0]))
        y_true.append(result['class_label'])
    except:
        print(result)
        continue
    
print(len(y_true), len(y_pred))

print(classification_report(y_true, y_pred))

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)