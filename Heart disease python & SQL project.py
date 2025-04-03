import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,roc_curve,auc
from sklearn.metrics import precision_score,recall_score,f1_score


#load dataset
dataset=pd.read_csv(r'C:\Users\DELL\Desktop\Heart project using python and sql\archive (1)\heart.csv')
print(dataset)

        #EXPLORE & CLEAN DATASET
print(dataset.shape)
print(dataset.describe())
print(dataset.info())
#dataset columns are already in numerical type so there is no  need to convert
#datatypes of columns

#check for missing values
print(dataset.isnull().sum())

       #EXPLORATORY DATA ANALYSIS
#Histogram & correlation between dataset variables
plt.style.use('dark_background')
dataset.hist(figsize=(12,12),zorder=2,color='red')
plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.suptitle('Heart Disease Dataset Histogram')
plt.show()

corr_matrix=dataset.corr()
plt.figure(figsize=(9,8))
plt.imshow(corr_matrix,cmap='coolwarm',interpolation='nearest')
plt.title('Correlation Matrix')
plt.xticks(range(len(dataset.columns)),dataset.columns,rotation=90)
plt.yticks(range(len(dataset.columns)),dataset.columns)
plt.colorbar()
plt.show()


#Predict the presence or abscence of heart diseasse

X_train,X_test,y_train,y_test=train_test_split(dataset.drop('target',axis=1),dataset['target'],test_size=0.2,random_state=42)

rfc=RandomForestClassifier(n_estimators=100)
rfc.fit(X_train,y_train)

y_pred=rfc.predict(X_test)

print('Accuracy:',accuracy_score(y_test,y_pred))
print('Precision:',precision_score(y_test,y_pred))
print('Recell:',recall_score(y_test,y_pred))
print('F1 Score:',f1_score(y_test,y_pred))
print('confusion matrix:',confusion_matrix(y_test,y_pred))

cm=confusion_matrix(y_test,y_pred)
plt.imshow(cm,interpolation='nearest',cmap='coolwarm')
plt.title('Classificatiion performance: Heart Disease Presence/Absence',pad=20)
for i in range(len(cm)):
    for j in range(len(cm[i])):
        plt.text(j,i,cm[i][j],ha='center',va='center',color='k')
plt.colorbar()
plt.show()


fpr,tpr,thresholds=roc_curve(y_test,rfc.predict_proba(X_test)[:,1])
roc_auc=auc(fpr,tpr)
plt.plot(fpr,tpr,color='darkorange',lw=2,label='ROC curve (area=%0.2f)' % roc_auc)
plt.plot([0,1],[0,1],color='navy',lw=2,linestyle='--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristics example')
plt.legend(loc='lower right')
plt.show()


# Feature Importance

X = dataset.drop(columns=['target'])
y = dataset['target']

importances = rfc.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(9, 8))
plt.title('Feature Importance')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
plt.show()
