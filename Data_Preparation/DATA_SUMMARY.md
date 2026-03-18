### **Dataset Documentation: Training \& Testing Sets**


**Overview**
---



This directory contains the split and preprocessed datasets for the Advanced Telecommunications Solutions Customer Churn project. The data has been partitioned to facilitate robust model training and unbiased evaluation.



###### 

###### **File Descriptions**

preprocessed_train_data.csv: The primary dataset used for model training.



preprocessed_test_data.csv: The "hold-out" dataset used to validate model performance on unseen data.





###### **Composition & Split Strategy**



Split Ratio: 80% Training / 20% Testing.



Total Records: 7,043



Training Set: 5,634 rows



Testing Set: 1,409 rows



Target Variable: Churn (Binary: 0 = No, 1 = Yes)



###### 

###### **Preprocessing Applied**



All files have undergone:



Missing Value Mitigation: Null values were validated and handled during the ingestion phase.



Categorical Encoding: Label Encoding for binary features and One-Hot Encoding for multi-class features (e.g., Contracts).



Feature Scaling: Standardized numerical inputs to ensure model convergence.

