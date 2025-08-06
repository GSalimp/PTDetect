import json
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

with open('2ClassesResults.json', 'r') as f:
    results = json.load(f)
    
y_true = [result['class_label'] if result['class_label'] == 0 else 1 for result in results]
y_pred = [0 if result['prediction'] == 'sim' else 1 for result in results]

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')

# # Calculate accuracy
# accuracy = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp) / len(y_true)

# # Calculate precision
# true_positive = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp == 1)
# false_positive = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
# precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0

# # Calculate recall
# false_negative = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)
# recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0

# # Calculate F1 score
# f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)