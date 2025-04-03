
# Heart Disease Prediction using Python and SQL

## Project Overview
This project aims to analyze heart disease data using Python, performing data cleaning, exploratory data analysis (EDA), and machine learning modeling. The primary objective is to predict the presence or absence of heart disease based on patient data.

## Dataset
The dataset used in this project is a heart disease dataset containing numerical attributes related to patient health.
The dataset contains the following key columns:
- **age**: Age of the patient
- **sex**: Gender (1 = male, 0 = female)
- **cp**: Chest pain type
- **trestbps**: Resting blood pressure
- **chol**: Serum cholesterol level
- **fbs**: Fasting blood sugar (1 = > 120 mg/dl, 0 = normal)
- **restecg**: Resting electrocardiographic results
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina (1 = yes, 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment
- **ca**: Number of major vessels colored by fluoroscopy
- **thal**: Thalassemia (blood disorder)
- **target**: Heart disease presence (1 = disease, 0 = no disease)

## Analysis and Methodology
### 1. Data Exploration & Cleaning
- Loaded the dataset and checked its structure using `shape`, `describe()`, and `info()`.
- Verified that all columns were in numerical format, eliminating the need for data type conversions.
- Checked for missing values and found none, ensuring data completeness.

### 2. Exploratory Data Analysis (EDA)
- Created histograms for all dataset variables to visualize distributions.
- Generated a correlation matrix heatmap to identify relationships between features.

### 3. Machine Learning Model
- Used a **Random Forest Classifier** to predict heart disease presence.
- Split the dataset into training (80%) and testing (20%) sets.
- Trained the model with `RandomForestClassifier(n_estimators=100)`.
- Evaluated model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix
  - ROC Curve & AUC Score

## Results
- **Accuracy:** The model achieved **98% accuracy** in classifying patients with and without heart disease.
- **Confusion Matrix:** Displayed classification performance, showing the number of correctly and incorrectly classified instances.
- **ROC Curve & AUC Score:** Demonstrated the model’s ability to distinguish between classes, with a high area under the curve indicating strong classification performance.
- **Feature Importance Analysis:** Identified key factors contributing to heart disease prediction, with the most influential features being age, cholesterol levels, blood pressure, and maximum heart rate.
- **Correlations:** Strong correlations were observed between features such as cholesterol and heart disease risk, as well as blood pressure and age.
- **Data Distribution:** The dataset showed a balanced distribution of target labels, ensuring fair model training.

## Visualizations
The project includes the following visualizations:
1. Histograms of dataset variables.
2. Correlation matrix heatmap.
3. Confusion matrix plot.
4. Receiver Operating Characteristic (ROC) curve.
5. Feature importance bar chart.

## SQL Analysis Performed
The following SQL queries were used to derive insights:

### 1️⃣ Data Overview
- Count the total number of patients in the dataset.
- Find the number of patients with and without heart disease.

### 2️⃣ Age and Heart Disease Trends
- Compute the average age of patients with and without heart disease.
- Analyze age group distribution for patients with heart disease.

### 3️⃣ Cholesterol and Blood Pressure Analysis
- Calculate the average cholesterol levels for patients with and without heart disease.
- Identify patients with dangerously high cholesterol (>250 mg/dl) and heart disease.

### 4️⃣ Gender-Based Analysis
- Determine heart disease cases among males vs. females.
- Compute the average maximum heart rate achieved (thalach) based on gender.

### 5️⃣ Impact of Chest Pain Type
- Analyze the distribution of chest pain types (cp) among heart disease patients.

## Results and Key Findings
- **Patients with heart disease tend to have higher cholesterol and blood pressure levels.**
- **Age is a significant risk factor, with most heart disease cases found in patients over 40 years old.**
- **Males have a higher prevalence of heart disease than females in this dataset.**
- **Chest pain type and maximum heart rate are strong indicators of heart disease.**
  
## Disclaimer
This project is an individual work. **No one is allowed to edit, modify, or reuse this project in any form.** Unauthorized use or replication is strictly prohibited.

## Author
Neha Altaf
linkedin:www.linkedin.com/in/neha-altaf-44952726a


