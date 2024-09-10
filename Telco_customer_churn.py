import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline




df = pd.read_csv('data.csv')
df




df.drop('customerID', axis = 1, inplace=True)
df




df.columns = df.columns.str.lower()
df




cat_var = [var for var in df.columns if df[var].dtype == 'object']
cat_var




for cols in cat_var:
    df[cols] = df[cols].str.lower().str.replace(' ', '_')
df



missing_values = [var for var in df.columns if df[var].isnull().sum()]
missing_values




cat_var.remove('churn')
#for var in cat_var:
   # print(var)
    #print(df[var].nunique())




X = df.drop('churn', axis=1)
y = df['churn']



class ValueCountTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, cat_var):
        self.cat_var = cat_var
        self.value_count_mapping = {}

    def fit(self, X, y = None):
        for cols in self.cat_var:
            self.value_count_mapping[cols] = X[cols].value_counts().to_dict()
        return self

    def transform(self, X, y = None):
        X_transformed = X.copy()
        for cols in self.cat_var:
            X_transformed[cols] = X_transformed[cols].map(self.value_count_mapping[cols]).fillna(0)
        return X_transformed




cat_columns = X.select_dtypes(include=['object']).columns.tolist()



value_count_transformer = ValueCountTransformer(cat_columns)



pipeline = Pipeline([
    ('value_counts', value_count_transformer),
    ('logistic_regression', LogisticRegression(max_iter=200))
])




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



pipeline.fit(X_train, y_train)




prediction = pipeline.predict(X_test)




comparing = pd.DataFrame({'Actual vaue': y_test, 'Predicted Value': prediction})
comparing



ac = accuracy_score(y_test, prediction)
ac


cm = confusion_matrix(y_test, prediction)





import pickle



with open('pipeline.pkl', 'wb') as f:
    pickle.dump(pipeline, f)


# In[ ]:


#pickle.dump(pipeline, open(r'C:\Users\ajana\OneDrive\ML\ML Zoom camp\Section 5\model_saved', 'wb'))


# In[ ]:


#model_load = pickle.load(open('model_saved', 'rb'))


# In[ ]:


#model_load.predict(X_test)

