import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('/home/kesin/AIML_project/processed_url.csv')

x = df[['Hostname Length', 'Path Length', 'First Directory Length', 'TLD Length', 'No. of -', 'No. of @', 'No. of ?',
       'No. of %', 'No. of .', 'No. of =', 'No. of http','No. of https', 'No. of www', 'No. of Numerical Values',
       'No. of Letters', 'No. of Directories', 'IP address or not']]

df['result'] = df['Type'].map({'benign': 0, 'malware': 1, 'phishing': 2, 'defacement': 3})
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.3, random_state=42)

y_test.fillna(0, inplace=True)
y_train.fillna(0, inplace=True)

rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)

rfc_predictions = rfc.predict(x_test)

accuracy = accuracy_score(y_test, rfc_predictions)
report = classification_report(y_test, rfc_predictions)

print(confusion_matrix(y_test, rfc_predictions))

print(f"Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", report)

#with open('Random_forest.pkl','wb') as file:
    #pickle.dump(rfc, file)