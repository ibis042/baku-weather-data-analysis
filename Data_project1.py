import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\Javad\Desktop\for vs code\Data analys\Data_Projects\baki_2025.csv");
df["tarix"] = pd.to_datetime(df["tarix"])

print(f"Ən yüksək tempratur: {df["maks_temp"].max()}")
print(f"Ən aşağı tempratur: {df["min_temp"].min()}")
print(f"Cədvəldəki Boş xanalarin sayı : {df.isnull().sum()}")
print(f"Orta tempratur max: {df["maks_temp"].mean()}")
print(f"Orta tempratur min: {df["min_temp"].mean()}")
print(f"Bakıya yağan yağışların cəmi: {df["yagis"].sum()}")
print(f"Bakıya bir gündə ən çox  yağan yağış: {df['yagis'].max()}")
print(f"Bakıya neçə gün yağış yağıb: {(df['yagis']>0).sum()}")

# tempratur qrafik
plt.figure(figsize=(10,5))
plt.plot(df["tarix"], df["maks_temp"], label="Maksimum temp")
plt.plot(df["tarix"], df["min_temp"], label="Minimum temp")
plt.title("Bakı 2025 Günlük Max-Min Tempratur Analiz Nəticələri ")
plt.xlabel("Tarix")
plt.ylabel("Tempratur (C)")

plt.legend()
plt.tight_layout()
plt.show()
#yagis qrafik
plt.figure(figsize=(10, 4))
plt.bar(df["tarix"], df["yagis"])
plt.title("Bakı 2025 - Günlük Yağıntı Miqdarı")
plt.xlabel("Tarix")
plt.ylabel("Yağış (mm)")

plt.tight_layout()
plt.show()