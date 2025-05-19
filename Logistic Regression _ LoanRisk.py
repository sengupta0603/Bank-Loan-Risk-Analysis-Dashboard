import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# step 1 : Load Data
df = pd.read_csv('C:/Users/Priya/OneDrive/Desktop/Bank_loan_info (Bank Loan DB)_Bank_loan_info.csv')
#print(df['Loan Status'].unique())

#Step 2: Label Encode Categorical columns
categorical_cols = ['Grade', 'Purpose', 'Home Ownership', 'Term']
for col in categorical_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

# Step 3: create target Variable
df['Loan Status'] = df['Loan Status'].apply(lambda x: 1 if x == 'Charged Off' else 0)

# print(df['Loan Status'].value_counts())


#Step 4 : Train/Test split
x = df[['Dti', 'Int Rate', 'Loan Amount', 'Grade', 'Purpose', 'Home Ownership', 'Term']]
y = df['Loan Status']
x_train, x_test,  y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# Step 5 Train Model
model = LogisticRegression(solver='liblinear')
model.fit(x_train,y_train)

# Step 6 : Predict Probabilities

df['default_probability'] = model.predict_proba(x)[:,1]

# step 7: Create Risk Buckets

def classify_risk(prob):
    if prob >= 0.40:
        return 'High'
    elif prob >= 0.25:
        return 'Medium'
    else:
        return 'Low'

df['default_risk'] = df['default_probability'].apply(classify_risk)

# step 8: Save to CSV
df.to_csv("loan_data_risk2_.csv", index=False)

print(df[['Dti', 'Int Rate', 'Loan Amount', 'default_probability', 'default_risk']].head(10))

print(df['default_risk'].value_counts())

