import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
file_path = "Sample_Data_for_Activity.csv"  # Update if needed
df = pd.read_csv(file_path)

# Set Seaborn style
sns.set(style="whitegrid")

# Rugplot: Adds small ticks along the x-axis to visualize distribution
sns.kdeplot(df["Normal_Distribution"], fill=True)
plt.title("KDE Plot of Normal_Distribution")
plt.savefig("kdeplot.png")
