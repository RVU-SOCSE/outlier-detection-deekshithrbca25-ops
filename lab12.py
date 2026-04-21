import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:\\Users\\Deekshith\\Downloads\\12laptops - 12laptops.csv")
print("Dataset:")
print(df)

# Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Deekshith\\Downloads\\12laptops - 12laptops.csv")

plt.boxplot(df["Screen"], notch=True, vert=False, showmeans=True)  # notch(curve) around the median
plt.xlabel("Screen")
plt.show()

plt.boxplot(df["Weight"])
plt.ylabel("Weight")
plt.show()

