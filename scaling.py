import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# --------------------------
# LOAD IRIS DATASET
# --------------------------
iris = load_iris()
data = pd.DataFrame(
    data=np.c_[iris['data'], iris['target']],
    columns=iris['feature_names'] + ['target']
)

numerical_features = iris['feature_names']
X = data[numerical_features]
y = data['target']

# --------------------------
# FEATURE SCALING
# --------------------------
# Standardization
scaler_standard = StandardScaler()
X_standardized = scaler_standard.fit_transform(X)

# Normalization (Min-Max)
scaler_minmax = MinMaxScaler()
X_normalized = scaler_minmax.fit_transform(X)

# --------------------------
# PRINT NORMALIZED DATA
# --------------------------
print("Normalized Features:\n", X_normalized)

# --------------------------
# PLOTTING
# --------------------------
plt.figure(figsize=(18,5))

# Original Features
plt.subplot(1,3,1)
plt.scatter(X.iloc[:,0], X.iloc[:,1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title('Original Features')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Standardized Features
plt.subplot(1,3,2)
plt.scatter(X_standardized[:,0], X_standardized[:,1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title('Standardized Features')
plt.xlabel('Feature 1 (Standardized)')
plt.ylabel('Feature 2 (Standardized)')

# Normalized Features
plt.subplot(1,3,3)
plt.scatter(X_normalized[:,0], X_normalized[:,1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title('Normalized Features')
plt.xlabel('Feature 1 (Normalized)')
plt.ylabel('Feature 2 (Normalized)')

plt.tight_layout()
plt.show()
