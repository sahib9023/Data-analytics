import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
file_path = "Sample_Data_for_Activity.csv"  # Update if needed
df = pd.read_csv(file_path)

# Set Seaborn style
sns.set(style="whitegrid")

# Rugplot: Adds small ticks along the x-axis to visualize distribution
sns.rugplot(df["Normal_Distribution"], height=0.1)
plt.title("Rugplot of Normal_Distribution")
plt.savefig("rugplot.png")
