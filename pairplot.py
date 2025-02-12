import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
file_path = "Sample_Data_for_Activity.csv"  # Update if needed
df = pd.read_csv(file_path)

# Set Seaborn style
sns.set(style="whitegrid")

# Pairplot: Visualize relationships among all numerical columns
sns.pairplot(df)
plt.savefig("pairplot.png")
