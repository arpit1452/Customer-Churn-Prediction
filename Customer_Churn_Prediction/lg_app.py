import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler

#load model and data
lg, scaler = pickle.load(open('logistic_Churn.pkl','rb'))


#create a web app
st.title("Churn Prediction using Logistic Regression")
gender=st.selectbox('Select Gender:',options=['Male','Female'])
SeniorCitizen=st.selectbox("Are you a Senior Citizen:", options=['Yes','No'])
Partner = st.selectbox("Do you have partner?", options=['Yes','No'])
Dependents	 = st.selectbox("Are you dependents on other?", options=['Yes','No'])
tenure = st.text_input("Enter Your tenure?")
PhoneService = st.selectbox("Do have phone service?",options=['Yes','No'])
MultipleLines = st.selectbox("Do you have mutlilines servics?", options=['Yes','No','No Phone Service'])
TechSupport = st.selectbox("Do you have any tech support?", options=['Yes','No','No Internet Service'])
Contract = st.selectbox("Your Contracts?",options=['One year','Two year','Month-to_month'])
MonthlyCharges= st.text_input("Enter your Monthly charges")
TotalCharges = st.text_input("Enter your Total charges")

#helper functions
def prediction(gender, SeniorCitizen, Partner, Dependents, tenure,
               PhoneService, MultipleLines, TechSupport, Contract,
               MonthlyCharges, TotalCharges):

    df1 = pd.DataFrame([[
        gender, SeniorCitizen, Partner, Dependents, tenure,
        PhoneService, MultipleLines, TechSupport, Contract,
        MonthlyCharges, TotalCharges
    ]], columns=[
        'gender','SeniorCitizen','Partner','Dependents','tenure',
        'PhoneService','MultipleLines','TechSupport','Contract',
        'MonthlyCharges','TotalCharges'
    ])

    # Encode categorical columns ONLY (same as training)
    categorical_cols = [
        'gender','SeniorCitizen','Partner','Dependents',
        'PhoneService','MultipleLines','TechSupport','Contract'
    ]

    for col in categorical_cols:
        df1[col] = LabelEncoder().fit_transform(df1[col])

    # Convert numeric columns
    df1['tenure'] = pd.to_numeric(df1['tenure'])
    df1['MonthlyCharges'] = pd.to_numeric(df1['MonthlyCharges'])
    df1['TotalCharges'] = pd.to_numeric(df1['TotalCharges'])

    # Scale using TRAINED scaler (NO FIT)
    df1 = scaler.transform(df1)

    result = lg.predict(df1)
    return result[0]


# Tips for Churn Prevention
churn_tips_data = {
    "Tips for Churn Prevention": [
        "Identify the Reasons: Understand why customers or employees are leaving. Conduct surveys, interviews, or exit interviews to gather feedback and identify common issues or pain points.",
        "Improve Communication: Maintain open and transparent communication channels. Address concerns promptly and proactively. Make sure customers or employees feel heard and valued.",
        "Enhance Customer/Employee Experience: Focus on improving the overall experience. This could involve improving product/service quality or creating a more positive work environment for employees.",
        "Offer Incentives: Provide incentives or loyalty programs to retain customers. For employees, consider benefits, bonuses, or career development opportunities.",
        "Personalize Interactions: Tailor interactions and offers to individual needs and preferences. Personalization can make customers or employees feel more connected and valued.",
        "Monitor Engagement: Continuously track customer or employee engagement. For customers, this might involve monitoring product usage or website/app activity. For employees, assess job satisfaction and engagement levels.",
        "Predictive Analytics: Use data and predictive analytics to anticipate churn. Machine learning models can help identify patterns and predict which customers or employees are most likely to churn.",
        "Feedback Loop: Create a feedback loop for ongoing improvement. Regularly seek feedback, analyze it, and use it to make informed decisions and changes.",
        "Employee Training and Development: Invest in training and development programs for employees. Opportunities for growth and skill development can improve job satisfaction and loyalty.",
        "Competitive Analysis: Stay aware of what competitors are offering. Ensure your products, services, and workplace environment remain competitive in the market."
    ]
}

# Tips for Customer Retention (Not Churning)
retention_tips_data = {
    "Tips for Customer Retention": [
        "Provide Exceptional Customer Service: Ensure that customers receive excellent customer service and support.",
        "Create Loyalty Programs: Reward loyal customers with discounts, special offers, or exclusive access to products/services.",
        "Regularly Communicate with Customers: Keep customers informed about updates, new features, and promotions.",
        "Offer High-Quality Products/Services: Consistently deliver high-quality products or services that meet customer needs.",
        "Resolve Issues Quickly: Address customer concerns and issues promptly to maintain their satisfaction.",
        "Build Strong Customer Relationships: Develop strong relationships with customers by understanding their needs and preferences.",
        "Provide Value: Offer value-added services or content that keeps customers engaged and interested.",
        "Simplify Processes: Make it easy for customers to do business with you. Simplify processes and reduce friction.",
        "Stay Responsive: Be responsive to customer inquiries and feedback, even on social media and review platforms.",
        "Show Appreciation: Express gratitude to loyal customers and acknowledge their continued support."
    ]
}

# Create DataFrames
churn_tips_df = pd.DataFrame(churn_tips_data)
retention_tips_df = pd.DataFrame(retention_tips_data)

if st.button("Predict churn or not"):
    result = prediction(gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, TechSupport, Contract, MonthlyCharges, TotalCharges)
    if result == 1:
        st.title("Churn")
        st.write("Here are 10 tips for Churn Prevention:")
        st.dataframe(churn_tips_df, height=400,width=1200)
    else:
        st.title('Not Churn')
        st.write("Here are 10 tips for Customer Retention (Not Churning):")
        st.dataframe(retention_tips_df, height=400,width=1200)