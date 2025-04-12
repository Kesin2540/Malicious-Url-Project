import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/kesin/AIML_project/processed_url.csv')

color_palette = {"benign": "green", "defacement": "yellow", "phishing": "orange", "malware": "red"}

plt.figure(figsize=(15, 5))
sns.countplot(x='Type', data=df)
plt.title("Count Of URLs",fontsize=20)
plt.xlabel("Type Of URLs",fontsize=18)
plt.ylabel("Number Of URLs",fontsize=18)

plt.figure(figsize=(15,5))
plt.title("Use Of WWW In URL", fontsize=20)
sns.countplot(x='No. of www', hue='Type', data=df, palette=color_palette)
plt.xlabel("Count Of WWW", fontsize=18)
plt.ylabel("Number Of URLs", fontsize=18)


plt.figure(figsize=(15,5))
plt.title("Number Of Directories In Url", fontsize=20)
sns.countplot(x='No. of Directories', data=df, hue='Type', palette=color_palette)
plt.xlabel("Number Of Directories", fontsize=18)
plt.ylabel("Number Of URLs", fontsize=18)

plt.figure(figsize=(15,5))
plt.title("Use Of IP In Url", fontsize=20)
sns.countplot(x='IP address or not', data=df)
plt.xlabel("Use Of IP", fontsize=18)
plt.ylabel("Number of URLs", fontsize=18)

plt.figure(figsize=(15,5))
plt.title("Use Of HTTP In Url", fontsize=20)
sns.countplot(x='No. of https', hue='Type', data=df, palette=color_palette)
plt.xlabel("Count Of HTTP", fontsize=18)
plt.ylabel("Number of URLs", fontsize=18)

plt.show()