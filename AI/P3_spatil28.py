# %%
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error

# %%
col_names = ['Type','Alcohol','MalicAcid','Ash','Alcalinity','Magnesium','Phenols','Flavanoids','Nonflavanoid','Proanthocyanins','ColorIntensity','Hue','DilutedWines','Proline']
df = pd.read_csv('wines.csv', skiprows=1, header=None, names=col_names)

# %%
# Clean data
df.dropna() 
df.drop_duplicates()
print(df.head())

# %%
X = df.drop('Type', 1)
y = df.Type

# %%
# Create a correlation matrix
corr_matrix = df.corr()
plt.subplots(figsize=(15,10))
# Plot a heatmap of the correlation matrix
sns.heatmap(corr_matrix, xticklabels=corr_matrix.columns, yticklabels=corr_matrix.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

# %%
# Get the absolute correlation of each column with the target variable 'Type'
correlations = abs(corr_matrix['Type'])

# Sort the correlations in descending order
sorted_correlations = correlations.sort_values(ascending=False)

# Print the sorted correlations
print(sorted_correlations)

# %%
featured_col = ['Flavanoids','DilutedWines','Phenols','Hue','ColorIntensity']
X = df[featured_col]
y = df.Type

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0) # 80% training and 20% test
print('#Training data points: %d' % X_train.shape[0])
print('#Testing data points: %d' % X_test.shape[0])
print('Class labels:', np.unique(y))

# %%
clf = DecisionTreeClassifier(criterion="entropy",min_samples_split=3,splitter='best',max_depth=3,random_state = 0)
#clf = DecisionTreeClassifier(criterion="entropy",splitter='random',max_depth=3,random_state = 0)
# If splitter is random then training accuracy is 0.9
# Train Decision Tree Classifer
# assume X_test is your testing data features and y_test is the corresponding labels/targets
test_df = pd.DataFrame(X_test, columns=['Flavanoids','DilutedWines','Phenols','Hue','ColorIntensity'])
test_df['Type'] = y_test
# save the testing data to a CSV file
test_df.to_csv('testing_data.csv', index=False)

clf = clf.fit(X_train,y_train)
y_train_pred = clf.predict(X_train)
#Predict the response for test dataset
y_test_pred = clf.predict(X_test)
#Mean Squared Error
print(mean_squared_error(y_test, y_test_pred))

# %%
# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_train, y_train_pred))
print("Accuracy:", metrics.accuracy_score(y_test, y_test_pred))

# %%
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = featured_col,class_names=['1','2','3'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('Classifier.png')
Image(graph.create_png())


