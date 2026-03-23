# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("dataset_with_clusters.csv")

# Separate features (X) and target (y)
X = df.drop(columns=["Churn"])   # all columns except target
y = df["Churn"]                 # target variable

# Perform Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y   # IMPORTANT: keeps churn distribution balanced
)

# Check shapes
print("Training set:", X_train.shape)
print("Testing set:", X_test.shape)

# Check distribution
print("\nChurn distribution in training set:")
print(y_train.value_counts(normalize=True))

print("\nChurn distribution in testing set:")
print(y_test.value_counts(normalize=True))

# Combine X and y back together for saving
train_data = X_train.copy()
train_data["Churn"] = y_train

test_data = X_test.copy()
test_data["Churn"] = y_test

# Save to CSV files
train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

print("Train and Test datasets saved successfully!")

# Feature Scaling

# Create scaler object
scaler = StandardScaler()

# Columns to scale
num_cols = ["tenure", "MonthlyCharges"]

# Fit ONLY on training data, transform both
X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

#Scaling numerical values
print(X_train[["tenure", "MonthlyCharges"]].head())
print()
print("Means:")
print(X_train[["tenure", "MonthlyCharges"]].mean())
print()
print("Standard deviations:")
print(X_train[["tenure", "MonthlyCharges"]].std())

# Check result
print(X_train.head())