import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt

df = pd.read_csv('/home/kesin/AIML_project/processed_url.csv')

x = df[['Hostname Length', 'Path Length', 'First Directory Length', 'TLD Length', 'No. of -', 'No. of @', 'No. of ?',
       'No. of %', 'No. of .', 'No. of =', 'No. of http','No. of https', 'No. of www', 'No. of Numerical Values',
       'No. of Letters', 'No. of Directories', 'IP address or not']]

df['result'] = df['Type'].map({'benign': 0, 'malware': 1, 'phishing': 2, 'defacement': 3})
y = df['result']

# Splitting dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.3, random_state=42)

y_test.fillna(0, inplace=True)
y_train.fillna(0, inplace=True)

dt_model = DecisionTreeClassifier(criterion='gini', max_depth=10, min_samples_split=5, random_state=42)
dt_model.fit(x_train, y_train)

dt_predictions = dt_model.predict(x_test)

accuracy = accuracy_score(y_test, dt_predictions)
report = classification_report(y_test, dt_predictions)

print(f"Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", report)

'''y_test_bin = label_binarize(y_test, classes=[0, 1, 2, 3])
class_labels = ['benign', 'malware', 'phishing', 'defacement']

plt.figure()
for i, label in enumerate(class_labels):  
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], dt_model.predict_proba(x_test)[:, i])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'{label} (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], color="gray", linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Multiclass Classification (One-vs-Rest)")
plt.legend()
plt.show()'''
