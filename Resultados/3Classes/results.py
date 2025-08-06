import json
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, classification_report


#o certo é o Llama3_13ClassesResults.json e o 3ClassesResults pro Llama3.2
with open('Llama3_13ClassesResults.json', 'r') as f:
    results = json.load(f)
    
y_true = [result['class_label'] for result in results]
y_pred = [int(result['prediction']) for result in results]

print(classification_report(y_true, y_pred))

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)


# Ambos os modelos tiveram resultados promissores nos conjuntos de testes, com o modelo \gls{llm} se saindo melhor que a \gls{rnn}. Dos 80 casos que foram usados como teste para os modelos, o modelo Llama3.1-8B-\textit{Instruct} ajustado, identificou e classificou corretamente 77 casos, ou seja, uma acurácia de 96,25\%. Em termos de comparação, a \gls{rnn} treinada teve sua maior acurácia nos dados de teste após ser treinada por 7 épocas, seguindo a metodologia proposta, acertando certa de 83,75\% dos casos.

#         Ademais, uma análise qualitativa das classificações, demonstra que, apesar de, em geral, textos feitos por humanos serem maiores que os artificiais, essa diferença não foi o único fator considerado pelo modelo durante a classificação. Como a inferência do modelo classificador \gls{llm} foi feita manualmente, foi possível perceber que o modelo identificou tanto textos pequenos como humanos, quanto os textos maiores como artificiais, demonstrando que outras características, além do tamanho das entradas, foram consideradas. O modelo Llama 3.1 errou apenas casos de textos humanos, classificando-os como artificiais (três no total). Porém, os textos errados não diferem muito de tamanho quando comparados a outros casos acertados pelo modelo. Ao se fazer uma análise similar em relação ao modelo de \gls{rnn}, é possível notar que ele possui 80\% de acurácia na classificação das 5 menores frases de teste, das quais três são textos humanos. Desta forma, é possível afirmar que, apesar de influenciados pelos tamanhos dos textos, ambos os modelos utilizam características além desta para classificar corretamente cada exemplo de teste.