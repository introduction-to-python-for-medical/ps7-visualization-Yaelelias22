import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

features = df.columns
selected_features = [features[1], features[2], features[6], features[7], features[13]]

features = list(df.columns)
print("Available features:", features)
selected_features = [features[1], features[2], features[6], features[7], features[13]]
print("Selected features: ", selected_features)

selected_features
dat = df[selected_features[2]]
plt.hist(data, bins=5, edgecolor= 'black')
plt.xlabel(selected_features[2])
plt.show()

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)

x = df[selected_features[0]]
y = df[selected_features[4]]

plt.scatter(x, y)
plt.xlabel(selected_features[0])
plt.ylabel(selected_features[4])
plt.show

reference_feature = selected_features [4]
reference_feature
reference_feature = selected_features[4]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()


reference_feature = selected_features[0]  # The reference feature
comparison_feature = selected_features[4]  # A feature to compare to


plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6, c='green')
plt.xlabel(reference_feature, fontsize = 20 , c='green')
plt.ylabel(comparison_feature, fontsize= 20, c= 'green')

plt.savefig('correlation_plot.png')

plt.show()

