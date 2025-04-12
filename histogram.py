import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/kesin/AIML_project/processed_url.csv')

color_palette = {"benign": "green", "defacement": "yellow", "phishing": "orange", "malware": "red"}

plt.figure(figsize=(20,5))
plt.hist(df['Length of the Url'], bins=50, color='lightblue')
plt.title("URL-Length", fontsize=20)
plt.xlabel("Url-Length", fontsize=18)
plt.ylabel("Number Of Urls", fontsize=18)

plt.figure(figsize=(20,5))
plt.hist(df['Hostname Length'], bins=50, color='lightgreen')
plt.title("Hostname Length", fontsize=20)
plt.xlabel("Length Of Hostname", fontsize=18)
plt.ylabel("Number Of Urls", fontsize=18)

plt.figure(figsize=(20,5))
plt.hist(df['TLD Length'], bins=50, color='lightgreen')
plt.title("TLD-Length", fontsize=20)
plt.xlabel("Length Of TLD", fontsize=18)
plt.ylabel("Number Of Urls", fontsize=18)

plt.show()
