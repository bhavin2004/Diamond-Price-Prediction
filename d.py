import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load and prepare data
df = pd.read_csv('artifacts/processed_test_data.csv')
df = df.drop('price', axis=1)  # Drop price column if it's present

# Standardize data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Apply PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_scaled)

# Create line graph for PCA
fig, ax = plt.subplots()
ax.plot(pca_result[:, 0], label='PCA Component 1', marker='o')
ax.plot(pca_result[:, 1], label='PCA Component 2', marker='x')
ax.set_xlabel('Index')
ax.set_ylabel('PCA Components')
ax.legend()
st.pyplot(fig)
