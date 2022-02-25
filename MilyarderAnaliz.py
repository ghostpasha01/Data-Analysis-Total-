import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Billionaire.csv")
print(data.head()) 
print(data.isnull().sum())
#Yani bu veri kümesinde Yaş sütununda 79 eksik değer var, hadi şu satırları kaldıralım
data = data.dropna()

#Bu veri kümesindeki NetWorth sütununda Milyarderlerin Net değerinin başında $ işareti ve sonunda B vardır.
#Bu yüzden bu işaretleri kaldırmamız ve NetWorth sütununu float'a dönüştürmemiz gerekiyor
data["NetWorth"] = data["NetWorth"].str.strip("$")
data["NetWorth"] = data["NetWorth"].str.strip("B")
data["NetWorth"] = data["NetWorth"].astype(float)

#Şimdi NetWorth'lerine göre en iyi 10 milyardere bir göz atalım
df = data.sort_values(by = ["NetWorth"], ascending=False).head(10)
plt.figure(figsize=(20, 10))
sns.histplot(x="Name", hue="NetWorth", data=df)
plt.show()

#Şimdi en çok milyardere sahip ilk 5 alana bir göz atalım
a = data["Source"].value_counts().head()
index = a.index
sources = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(sources, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Milyarder Olmak İçin En İyi 5 Alan Adı", fontsize=20)
plt.show()

#Şimdi en çok milyardere sahip ilk 5 sektöre bir göz atalım
a = data["Industry"].value_counts().head()
index = a.index
industries = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(industries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("En Çok Milyardere Sahip İlk 5 Sektör", fontsize=20)
plt.show()

#Şimdi en çok milyardere sahip ilk 5 ülkeye bir göz atalım
a = data["Country"].value_counts().head()
index = a.index
Countries = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(Countries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("En Çok Milyarder Olan İlk 5 Ülke", fontsize=20)
plt.show()