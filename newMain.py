import pandas as pd
import seaborn as sns
import streamlit as st
from joblib import dump, load
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


st.markdown(f''' 
<style>
.st-emotion-cache-1avcm0n{{
    visibility: hidden
}}
.st-emotion-cache-10y5sf6{{
    color: white;
}}
.st-emotion-cache-1dx1gwv{{
    
    background-color: #262730
}}
.st-emotion-cache-1clstc5{{
    color-scheme: dark;
    background-color: #262730
}}
.st-emotion-cache-p5msec{{
    
    background-color: #262730
}}
.st-emotion-cache-sh2krr{{
    color: white
}}
.st-emotion-cache-1dtefog{{
    
    background-color: #262730   
}}
</style>
''',unsafe_allow_html=True)


st.markdown(f'''
    <div class="perspective-text">
      <div class="perspective-line">
        <p class="para"></p>
        <p class="para">FRAUD</p>
      </div>
      <div class="perspective-line">
        <p class="para">Fraud</p>
        <p>Detection by</p>
      </div>
      <div class="perspective-line">
        <p class="para">Detection by</p>
        <p class="para">Promptora &</p>
      </div>
      <div class="perspective-line">
        <p class="para">Promptora &</p>
        <p class="para">Thomas Cook</p>
      </div>
      <div class="perspective-line">
        <p class="para">Thomas Cook</p>
        <p class="para"></p>
      </div>
    </div>
    <style>
        .perspective-text {{
            color: white;
            font-family: Arial;
            font-size: 58px;
            font-weight: bold;
            letter-spacing: -1px;
            text-transform: uppercase;
            padding-left:140px;
            padding-right:80px;
            height: 350px;
            width: 380px;
        }}
        .perspective-line {{
            height: 50px;
            overflow: hidden;
            position: relative;
        }}
        .para {{
            margin: 0;
            height: 50px;
            line-height: 50px;
            transition: all 0.5s ease-in-out;
        }}
        .perspective-line:nth-child(odd) {{
            transform: skew(60deg, -30deg) scaleY(0.667);
        }}
        .perspective-line:nth-child(even) {{
            transform: skew(0deg, -30deg) scaleY(1.337);
        }}
        .perspective-text:hover p {{
            transform: translate(0, -50px);
        }}
        .perspective-line:nth-child(1) {{
            left: 29px;
        }}
        .perspective-line:nth-child(2) {{
            left: 58px;
            background: #f07e6e;
        }}
        .perspective-line:nth-child(3) {{
            left: 87px;
            background: #84cdfa;
        }}
        .perspective-line:nth-child(4) {{
            left: 116px;
            background: #5ad1cd;
        }}
        .perspective-line:nth-child(5) {{
            left: 145px;
        }}
    </style>''',unsafe_allow_html=True)


    
df=pd.read_csv('CSVdataset.csv')
if st.button("Show Dataset"):
    st.write("Not Fraud:")
    st.dataframe(df[df['IsFraud'] == 0].head(2))
    st.write("Fraud:")
    st.dataframe(df[df['IsFraud'] == 1].head(2))


def categorize_time(timestamp):
    if 40001 <= timestamp <= 225959:
        return 0
    else:
        return 1

model_name=st.sidebar.radio("***Choose a model:***",('Logistic Regression','Random Forest', 'CatBoost', 'Isolation Forest'),index=None)
# st.sidebar.divider()
st.sidebar.write('')
if model_name==None:
    st.info('select a model from the sidebar to continue')
    
elif model_name=='Logistic Regression':
    # graph(df)
    with st.expander('Initial Correlation Matrix'):
        st.image("./images/CorrMat1.png")
    with st.expander('Final Correlation Matrix'):
        st.image("./images/CorrMat2.png")
        
    logistic = load(r'.\Models\NewLogi.joblib')
    prod_desc=st.sidebar.selectbox('Product Description',('New Borderless Prepaid','PARTNER BORDERLESS PREPAID','MASTER STUDENT','Partner One Currency','New One Currency','VISA BPC','VISA STUDENT','NEW RBL BPC'))
    cardholder=st.sidebar.selectbox('Cardholder Type',('Corporate','Retail'))
    Mer=st.sidebar.text_input('Merchant Code')
    amount=st.sidebar.number_input('Transaction Amount')
    currency=st.sidebar.selectbox('Purse Currency',('','AED','EUR','CAD','USD','GBP','CHF','SGD','THB','AUD','JPY'))
    master=st.sidebar.number_input('Mastercard Amount')
    tran_desc=st.sidebar.selectbox('Transaction Description',('ATM CASH WITHDRAWAL','ECOM TRANSACTION','BALANCE INQUIRY','MERCHANT PURCHASE','OVER THE COUNTER','CASH ADVANCE REVERSAL'))
    timestamp=st.sidebar.slider('Select Timestamp',0,235959)
    if st.sidebar.button('Compute'):
        timestamp=categorize_time(timestamp)
        if Mer=='':
            st.warning('Enter a valid merchant number')
        else:Mer=int(Mer)
        le=LabelEncoder()
        
        le.fit(['New Borderless Prepaid','PARTNER BORDERLESS PREPAID','MASTER STUDENT','Partner One Currency','New One Currency','VISA BPC','VISA STUDENT','NEW RBL BPC'])
        prod_desc=int(le.transform([prod_desc]))
        le.fit(['Corporate','Retail'])
        cardholder=int(le.transform([cardholder]))
        le.fit(['AED','EUR','CAD','USD','GBP','CHF','SGD','THB','AUD','JPY'])
        currency=int(le.transform([currency]))
        le.fit(['ATM CASH WITHDRAWAL','ECOM TRANSACTION','BALANCE INQUIRY','MERCHANT PURCHASE','OVER THE COUNTER','CASH ADVANCE REVERSAL'])
        tran_desc=int(le.transform([tran_desc]))
        
        result=logistic.predict([[prod_desc,cardholder,Mer,amount,currency,master,tran_desc,timestamp]])
        st.write(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
with st.expander("Rules"):
    st.write("""
    Transaction Wise: \n
       1.  If transaction is in offline format, from timestamp 23:00:00 to 04:00:00
       2.  If transaction amount is greater than 500(USD/EUR/GBP)s
    Customer wise: More than 5 transactions a day(Incase of customer profiling)
                 """)