import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# 🧭 Load the dataset
df = pd.read_csv("../Data/amazon_reviews_dataset (1).csv")

# ✅ Confirm the data loaded successfully
print("✅ Dataset loaded successfully!")
print("🔹 Shape of dataset:", df.shape)

print("\n🔹 First 5 rows:")
print(df.head())

# 🧩 Check column info
print("\n📊 Dataset Info:")
print(df.info())

# 🔍 Check for missing values
print("\n🔍 Missing values per column:")
print(df.isnull().sum())

# 📈 Summary statistics for numerical columns
print("\n📈 Summary Statistics:")
print(df.describe())

# 🔢 Check unique values for potential categorical columns
print("\n🔢 Unique values in each column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# 🧼 Visualize missing data
plt.figure(figsize=(12, 8))
sns.heatmap(df.isnull(), cbar=False, cmap="coolwarm")
plt.title("Missing Values Heatmap")
plt.savefig("missing_values_heatmap.png")
plt.close()


# 📊 Visualize distributions of numerical data
fig, axes = plt.subplots(figsize=(14, 8))  # create a figure and axes
df.hist(figsize=(14, 8), bins=25, color='skyblue', edgecolor='black')
plt.suptitle("Distribution of Numerical Columns", fontsize=18)

# ✅ Save high-quality plot
plt.savefig("numerical_distribution.png", dpi=300, bbox_inches="tight")
print("✅ Saved: numerical_distribution.png")
plt.close()  # close to prevent conflicts for next plots
