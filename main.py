#!pip install streamlit joblib scikit-learn seaborn matplotlib

import streamlit as st
import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import LabelEncoder

# st.markdown(,unsafe_allow_html=True)



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



# st.markdown("""<div class="stars"></div><div class="centered"><span class="cyberspace" data-text="CYBERSPACE">PROMPTORA</span><span class="cyberspace" data-text="RACEWAY">.AI</span></div><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><filter id="extrude"><feMorphology operator="erode" radius="0" in="SourceGraphic" result="erode" /><feMorphology operator="erode" radius="2" in="SourceGraphic" result="erode1" /><feMorphology operator="erode" radius="3" in="SourceGraphic" result="erode2" /><feMorphology operator="erode" radius="4" in="SourceGraphic" result="erode3" /><feMorphology operator="erode" radius="6" in="SourceGraphic" result="erode4" /><feComposite in="erode" in2="erode1" operator="out" result="main"/> <feComposite in="erode1" in2="erode2" operator="out" result="stroke1"/><feComposite in="erode2" in2="erode3" operator="out" result="stroke2"/><feComposite in="erode3" in2="erode4" operator="out" result="stroke3"/><feGaussianBlur in="stroke1" stdDeviation="0 10" result="stroke1-blur" /><feBlend in="stroke1-blur" mode="screen" result="stroke1-blur-blend"></feBlend><feGaussianBlur in="stroke2" stdDeviation="0 10"  /><feOffset dx="0" dy="10" result="stroke2-blur"/><feBlend in="stroke2-blur" mode="screen" result="stroke2-blur-blend"></feBlend><feGaussianBlur in="stroke3" stdDeviation="0 25"  /><feOffset dx="0" dy="20" result="stroke3-blur"/>      <feBlend in="stroke3-blur" mode="screen" result="stroke3-blur-blend"></feBlend><feFlood result="floodFill" flood-color="rgba(0,0,0,0.7)" flood-opacity="1"/><feComposite in="floodFill" in2="erode2" operator="in" result="black"/> <feBlend in="black" mode="screen" result="letterInside"></feBlend><feMerge><feMergeNode in="stroke1-blur-blend"></feMergeNode><feMergeNode in="stroke2-blur-blend"></feMergeNode><feMergeNode in="stroke3-blur-blend"></feMergeNode><feMergeNode in="main"></feMergeNode><feMergeNode in="letterInside"></feMergeNode></feMerge></filter><filter id="extrude1"><feOffset dx="1" dy="3" in="SourceGraphic" result="L1"/><feMorphology operator="erode" radius="1" in="L1" result="L2" /><feOffset dx="1" dy="10" in="L2" result="L3"/><feMerge result="trail"><feMergeNode in="L1" /><feMergeNode in="L3" /></feMerge><feGaussianBlur in="trail" stdDeviation="3 0" result="trail-blur" /><feMerge><feMergeNode in="trail-blur" /><feMergeNode in="SourceGraphic" /></feMerge></filter>  </defs></svg>         <style>.reportview-container {background: radial-gradient(#050526 0%,black 90%) -200vw 10vh no-repeat black;margin:0;padding:10;width:100vw;height:100vh;position:center;  perspective: 340px;height: 100%;overflow: hidden;}.centered{position:center;left:500px;top:1000px;transform:translateX(-50%) translateY(-50%) rotateX(15deg);text-align:center;}.cyberspace{position:relative;font-family:'Cyberspace-Raceway-Back',sans-serif;font-size:4rem;color:black;-webkit-clip:background;-webkit-background-clip:text;-webkit-text-fill-color:rgba(135,209,228,1);-webkit-text-stroke-width: 0.1rem;-webkit-text-stroke-color: rgba(135,209,228,1); filter:url(#extrude);}$stars: 350;         // Number of start per layer$depth: 300;         // Depth between star layers$speed: 10s;          // Number of seconds to transition between layers$width: 3000;        // Width of the starfield$height: 960;        // Height of the starfield.stars {position: absolute;top: 50%;left: 50%;width: 2px;height: 2px;$box-shadow: ();@for $i from 0 through $stars {$box-shadow: $box-shadow, (random($width)-$width/2 + px) (random($height)-$height/2 + px) hsl(90,0,75+random(25));}box-shadow: $box-shadow;animation: fly $speed linear infinite;transform-style: preserve-3d;&:before, &:after {content: "";position: absolute;width: inherit;height: inherit;box-shadow: inherit;}&:before {transform: translateZ(-$depth + px);animation: fade1 $speed linear infinite;}&:after {transform: translateZ(-$depth * 2 + px);animation: fade2 $speed linear infinite;}}@keyframes fly {from {transform: translateZ(0px);}to {transform: translateZ($depth + px);}}@keyframes fade1 {from {opacity: .5;  }  to {opacity: 1;}  }@keyframes fade2 {from {opacity: 0;}to {opacity: .5;  }  }}</>""",unsafe_allow_html=True)
# st.markdown(f''' 
#             <style>
#             .body {{position: fixed;inset: -20px;background:repeating-radial-gradient(#000 0 0.001%,#fff 0 0.002%)20% 20%/300px 300px,repeating-conic-gradient(#000 0 0.001%,#fff 0 0.002%)10% 10%/400px 300px;background-blend-mode: normal;filter: blur(0.5px) contrast(21) brightness(40);mix-blend-mode: normal;}} 
#             .st-emotion-cache-uf99v8 {{background: black;margin: 0;min-height: 100vh;}}
#             html {{background: black;}}     </style>''',unsafe_allow_html=True)
# st.markdown(f'''
#             <style>
#             .st-emotion-cache-1dtefog eqpbllx3{{
#                 background:
#                     repeating-radial-gradient(#66d11f 0 0.00001%,#000000 0 0.002%)
#                     20% 20%/200px 200px,
#                     repeating-conic-gradient(#e32020 0 0.0001%,#fff 0 0.002%)
#                     10% 10%/100px 100px;
#             }}
#             </style>
#             ''',unsafe_allow_html=True)
# st.markdown(f'''
#             <style>
#             .st-emotion-cache-uf99v8 {{
#                 background:
#                     repeating-radial-gradient(#66d11f 0 0.001%,#b183d6 0 0.005%)
#                     30% 60%/500px 4000px,
#                     repeating-conic-gradient(#e32020 0 0.001%,#fff 0 0.0002%)
#                     20% 20%/1000px 1000px;
#                 background-blend-mode: normal;
#                 mix-blend-mode: normal;
#             }}
#             .st-emotion-cache-1y4p8pa ea3mdgi5{{
#                 background-color:#000000
#             }}
#             </style>
#             ''',unsafe_allow_html=True)



###---------------------------------------------------------------------
## Working

st.markdown(f'''
    <div class="perspective-text">
      <div class="perspective-line">
        <p class="para"></p>
        <p class="para">FRAUD</p>
      </div>
      <div class="perspective-line">
        <p class="para">Fraud</p>
        <p class="para">Detection by</p>
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
###---------------------------------------------------------------------




# st.markdown(f'''<style> 
#     .main {{
#     background: white;
#     background-image: linear-gradient(90deg, #c6a5d1 20%, transparent 0),
#                       linear-gradient(#948d8b 20%, transparent 0);
#     background-size: 10px 10px;
# }}</style>''',unsafe_allow_html=True)




# st.markdown(f'''<style>
#     .main {{
#     background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
#     background-size: 400% 400%;
#     animation: gradient 15s ease infinite;
#     height: 100vh;
# }}
# @keyframes gradient {{
#     0% {{
#         background-position: 0% 50%;
#     }}
 
#     50% {{
#         background-position: 100% 50%;
#     }}
 
#     100% {{
#         background-position: 0% 50%;
#     }}
# }}</style>''',unsafe_allow_html=True)





# st.title("Fraud Detection, :blue[Promptora]")
# st.markdown("""<h2 style='text-align: center'><span class='big'>Fraud Detection</span> <span class='small'>Promptora</span></h2><style>.big{font-size: 40px;}.small{font-family: 'georgia'; font-weight: bold;font-size: 34px;color: blue;}</style>""",unsafe_allow_html=True)
# st.markdown("""<div class="overlay"></div><div class="text"><div class="wrapper"><div id="P" class="letter">P</div><div class="shadow">P</div></div><div class="wrapper"><div id="R" class="letter">R</div><div class="shadow">R</div></div><div class="wrapper"><div id="O" class="letter">O</div><div class="shadow">O</div></div><div class="wrapper"><div id="M" class="letter">M</div><div class="shadow">M</div></div><div class="wrapper"><div id="P" class="letter">P</div><div class="shadow">P</div></div><div class="wrapper"><div id="T" class="letter">T</div><div class="shadow">T</div></div><div class="wrapper"><div id="O" class="letter">O</div><div class="shadow">O</div></div><div class="wrapper"><div id="R" class="letter">R</div><div class="shadow">R</div></div><div class="wrapper"><div id="Stwo" class="letter">A</div><div class="shadow">A</div></div></div>  <style>.overlay{position:absolute;bottom:0;left:0;width:100%;height:30vh;z-index:100;} .text{font-family:"Yanone Kaffeesatz";font-size: 100px;	display: flex;position: absolute;	bottom: 20vh;left: 50%;transform: translateX(-50%);user-select: none;.wrapper {padding-left: 20px;padding-right: 20px;padding-top: 20px;.letter {transition: ease-out 1s;transform: translateY(40%);}.shadow {transform: scale(1, -1);color: #999;transition: ease-in 5s, ease-out 5s;} &:hover{.letter {transform: translateY(-200%);}.shadow {opacity: 0;transform: translateY(200%);}}}}</style>""",unsafe_allow_html=True)



###---------------------------------------------------------------------
## Working
# st.markdown(f"""
#             <section class="wrapper">
#             <div class="top">Promptora</div>
#             <div class="bottom" aria-hidden="true">Promptora</div>
#             </section>
#             <style>
#             * {{box-sizing: border-box;}}
#             :root {{--background-color: black;--text-color: hsl(0, 0%, 100%);}}
#             body {{margin: 0;}}
#             .wrapper {{display: grid;place-content: center;min-height: 150px;font-family: "Oswald", sans-serif;font-size: 5rem;font-weight: 750;text-transform: uppercase;color: var(--text-color);}}
#             .wrapper > div {{grid-area: 1/1/-1/-1;}}
#             .top {{clip-path: polygon(0% 0%, 100% 0%, 100% 48%, 0% 58%);color: #68e7fc;}}
#             .bottom {{clip-path: polygon(0% 60%, 100% 50%, 100% 100%, 0% 100%);color: transparent;background: -webkit-linear-gradient(177deg, black 53%, var(--text-color) 65%);background: linear-gradient(177deg, black 53%, var(--text-color) 65%);background-clip: text;-webkit-background-clip: text;transform: translateX(-0.02em);}}</style>""",unsafe_allow_html=True)
###---------------------------------------------------------------------


# st.markdown("""<span>Promptora</span><style>@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@1,900&display=swap');body {padding: 0;margin: 0;font-family: 'Poppins', sans-serif;background: black;height: 100vh;width: 100vw;}span {position: absolute;left: 50%;top: 50%;  transform: translate(-50%, -50%);display: block;color: #cf1b1b;font-size: 124px;letter-spacing: 8px;cursor: pointer;}span::before {content: "Promptora";  position: absolute;  color: transparent;background-image: repeating-linear-gradient(45deg,transparent 0,transparent 2px,white 2px,white 4px);-webkit-background-clip: text;top: 0px;left: 0;z-index: -1;transition: 1s;}span::after {content: "Promptora";position: absolute;color: transparent;background-image: repeating-linear-gradient(135deg,transparent 0,transparent 2px,white 2px,white 4px);-webkit-background-clip: text;top: 0px;left: 0px;transition: 1s;}span:hover:before {top: 10px;left: 10px;}span:hover:after {top: -10px;left: -10px;}</style>""",unsafe_allow_html=True)

choice=st.sidebar.selectbox('Select a Model:',('', "RANDOM FOREST",'LOGISTIC REGRESSION',"ISO FOREST"))#, "ISOLATION FOREST"))#, "CAT BOOST"))#, "CAT MODEL", "LOGISTIC REGRESSION"))


if choice=='':
    st.info("Select any model from the sidebar to continue prediction")



elif choice=='ISO FOREST':
 
    IsoForest = load(r'.\Models\IsoForest012.joblib')
    
    if st.button("Sample1"):
        currency,amount,purse,cpf,master,description,sys,time=1,1254.00,122.00,122.00,125.00,4,8327439212,1
        if (description=='ATM Cash Withdrawal'or'Merchant Purchase'or'Over The Counter'):online=0
        else:online=1
        result=IsoForest.predict([[amount,purse,cpf,master,int(sys),int(time),online,currency]])
        if result[0]==-1:st.subheader('Not Fraud')
        else:st.subheader('Fraud')
    
    currency=st.sidebar.selectbox('Posted Purse Currency',('OTHER','AED','USD','EUR','GBP'))
    amount=st.sidebar.number_input('Transaction Amount')
    purse=st.sidebar.number_input('Posted Transaction Purse Amount')
    cpf=st.sidebar.number_input('CPF Purse Transaction Amount')
    master=st.sidebar.number_input('Mastercard Amount')
    description=st.sidebar.selectbox('Transaction Description',('','ATM CASH WITHDRAWAL','BALANCE INQUIRY','CASH ADVANCE REVERSAL','ECOM TRANSACTION','MERCHANT PURCHASE', 'OVER THE COUNTER'))
    sys=st.sidebar.text_input('System Generated Reference Number')
    time=st.sidebar.text_input('Transaction Timestamp')
    if st.sidebar.button("Compute"):
        if description=='':st.warning("Please pick a transaction type")
        else: 
            if (description=='ATM Cash Withdrawal'or'Merchant Purchase'or'Over The Counter'):
                online=0
            else:
                online=1
        # if(description=='Ecom Transaction'or'Cash Advance Reversal'or'Balance Inquiry')
        if currency=='Other':curr=0
        else:curr=1
        if type=='':st.warning('Enter transaction type')
        else:
            if(type=='Debit'):db=1
            else:db=0
        result=IsoForest.predict([[amount,purse,cpf,master,int(sys),int(time),online,curr]])
        if result[0]==-1:st.subheader('Not Fraud')
        else:st.subheader('Fraud')
        # st.write(result[0])


# elif choice=='ISOLATION FOREST':
 
#     IsoForest = load(r'.\Models\IsoForest.joblib')
#     bin=st.sidebar.text_input('Bank Identification Number(BIN)')
#     mer=st.sidebar.text_input('MER_CODE')
#     type=st.sidebar.selectbox('Type Debit or Credit',('','Debit','Credit'))
#     amount=st.sidebar.number_input('Transaction Amount')
#     currency=st.sidebar.selectbox('Posted Purse Currency',('OTHER','AED','USD','EUR','GBP'))
#     cpf=st.sidebar.number_input('CPF Purse Transaction Amount')
#     purse=st.sidebar.number_input('Posted Transaction Purse Amount')
#     master=st.sidebar.number_input('Mastercard Amount')
#     description=st.sidebar.selectbox('Transaction Description',('','ATM CASH WITHDRAWAL','BALANCE INQUIRY','CASH ADVANCE REVERSAL','ECOM TRANSACTION','MERCHANT PURCHASE', 'OVER THE COUNTER'))
#     sys=st.sidebar.text_input('System Generated Reference Number')
#     time=st.sidebar.text_input('Transaction Timestamp')
#     if st.sidebar.button("Compute"):
#         if description=='':st.warning("Please pick a transaction type")
#         else: 
#             if (description=='ATM Cash Withdrawal'or'Merchant Purchase'or'Over The Counter'):
#                 offline=1
#                 online=0
#             else:
#                 offline=0
#                 online=1
#         # if(description=='Ecom Transaction'or'Cash Advance Reversal'or'Balance Inquiry')
#         if currency=='Other':curr=0
#         else:curr=1
#         if type=='':st.warning('Enter transaction type')
#         else:
#             if(type=='Debit'):db=1
#             else:db=0
#         result=IsoForest.predict([[int(bin),int(mer),amount,purse,cpf,master,int(sys),int(time),offline,online,db,curr]])
#         if result[0]==-1:st.subheader('Not Fraud')
#         else:st.subheader('Fraud')
#         # st.write(result[0])
    


# elif choice=='CAT BOOST':
#     from catboost import CatBoostClassifier
#     cat=CatBoostClassifier().load_model(r".\Models\CatModel1")
#     TRANSACTION_AMOUNT= st.sidebar.number_input('Transaction Amount')
#     POSTED_TRANSACTION_PURSE_AMOUNT= st.sidebar.number_input('Purse Transaction Amount')
#     CPF_PURSE_TRANSACTION_AMOUNT= st.sidebar.number_input('CPF Transaction Amount')
#     MASTERCARD_AMOUNT= st.sidebar.number_input('MasterCard Amount')
#     TRANSACTION_TIMESTAMP= st.sidebar.text_input("Transaction Timestamp")
#     PRODUCT_DESCRIPTION= st.sidebar.selectbox('Product Description',('','New Borderless Prepaid','PARTNER BORDERLESS PREPAID','MASTER STUDENT','Partner One Currency','New One Currency','VISA BPC','VISA STUDENT','NEW RBL BPC'))
#     CARDHOLDER_TYPE= st.sidebar.selectbox('Card Holder Type',('','Corporate','Retail'))
#     TRANSACTION_DESCRIPTION= st.sidebar.selectbox('Transaction Description',('','ATM CASH WITHDRAWAL','BALANCE INQUIRY','CASH ADVANCE REVERSAL','ECOM TRANSACTION','MERCHANT PURCHASE','OVER THE COUNTER'))
#     POSTED_PURSE_CURRENCY= st.sidebar.selectbox('Purse Currency',('','AED','EUR','CAD','USD','GBP','CHF','SGD','THB','AUD','JPY'))
#     if st.sidebar.button("Compute"):
#         # if 40001 <= int(TRANSACTION_TIMESTAMP) <= 225959:TRANSACTION_TIMESTAMP=0
#         # else:TRANSACTION_TIMESTAMP=1
#         result=cat.predict([[TRANSACTION_AMOUNT,POSTED_TRANSACTION_PURSE_AMOUNT,CPF_PURSE_TRANSACTION_AMOUNT,MASTERCARD_AMOUNT,TRANSACTION_TIMESTAMP,PRODUCT_DESCRIPTION,POSTED_PURSE_CURRENCY]])
#         result_proba=cat.predict_proba([[TRANSACTION_AMOUNT,POSTED_TRANSACTION_PURSE_AMOUNT,CPF_PURSE_TRANSACTION_AMOUNT,MASTERCARD_AMOUNT,TRANSACTION_TIMESTAMP,PRODUCT_DESCRIPTION,POSTED_PURSE_CURRENCY]])
#         if result==1:st.warning('Fraud')
#         else:st.success("Not Fraud")
#         per=format(result_proba[0][1]*100, '.3f')
#         # per=format(per, '.3f')
#         st.subheader(f'Probability of fraud: {per}%')


elif choice=='RANDOM FOREST':
    RandFor = load(r'.\Models\NewRandFor.joblib')
    if st.button('Sample1'):
        mer,card_type,desc,transaction_type,amount,purse_amount,cpf,master_amount,time=7011,1,1,2,0.00,0.00,0.00,0.00,124506
        if 40001 <= int(time) <= 225959:timezone=0
        else:timezone=1
        result=RandFor.predict([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        result1=RandFor.predict_proba([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        if result==1:st.warning('Fraud')
        else:st.success("Not Fraud")
        per=format(result1[0][1]*100, '.3f')
        # per=format(per, '.3f')
        st.header(f'Probability of fraud: {per}%')
        
        if card_type==1:card_type="Corporate"
        else: card_type="Retail"
        
        if desc==1:desc="MASTER STUDENT"
        elif desc==2:desc="NEW BORDERLESS PREPAID"
        elif desc==3:desc="NEW ONE CURRENCY"
        elif desc==4:desc="NEW RBL BPC"
        elif desc==5:desc="PARTNER BORDERLESS PREPAID"
        elif desc==6:desc="PARTNER ONE CURRENCY"
        elif desc==7:desc="VISA BPC"
        else:desc="VISA STUDENT"
            
        if transaction_type==1:transaction_type="ATM CASH WITHDRAWAL"
        elif transaction_type==2:transaction_type='BALANCE INQUIRY'
        elif transaction_type==3:transaction_type='CASH ADVANCE REVERSAL'
        elif transaction_type==4:transaction_type='ECOM TRANSACTION'
        elif transaction_type==5:transaction_type='MERCHANT PURCHASE'
        else: transaction_type='OVER THE COUNTER'
        
        st.info(f"""
                Our Inputs:\n\n
                MER_CODE: {mer}\n
                CARDHOLDER_TYPE: {card_type}\n
                PRODUCT_DESCRIPTION: {desc}\n
                TRANSACTION_DESCRIPTION: {transaction_type}\n
                TRANSACTION_AMOUNT: {amount}\n
                POSTED_TRANSACTION_PURSE_AMOUNT: {purse_amount}\n
                CPF_Purse_Transaction_Amount: {cpf}\n
                MASTERCARD_AMOUNT: {master_amount}\n
                TRANSACTION_TIMESTAMP: {time}
                """)
        
        
    if st.button('Sample2'):
        mer,card_type,desc,transaction_type,amount,purse_amount,cpf,master_amount,time=1232,1,1,1,200.00,2343.00,1324.00,3243.00,234506
        if 40001 <= int(time) <= 225959:timezone=0
        else:timezone=1
        result=RandFor.predict([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        result1=RandFor.predict_proba([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        if result==1:st.warning('Fraud')
        else:st.success("Not Fraud")
        per=format(result1[0][1]*100, '.3f')
        # per=format(per, '.3f')
        st.header(f'Probability of fraud: {per}%')
        
        if card_type==1:card_type="Corporate"
        else: card_type="Retail"
        
        if desc==1:desc="MASTER STUDENT"
        elif desc==2:desc="NEW BORDERLESS PREPAID"
        elif desc==3:desc="NEW ONE CURRENCY"
        elif desc==4:desc="NEW RBL BPC"
        elif desc==5:desc="PARTNER BORDERLESS PREPAID"
        elif desc==6:desc="PARTNER ONE CURRENCY"
        elif desc==7:desc="VISA BPC"
        else:desc="VISA STUDENT"
            
        if transaction_type==1:transaction_type="ATM CASH WITHDRAWAL"
        elif transaction_type==2:transaction_type='BALANCE INQUIRY'
        elif transaction_type==3:transaction_type='CASH ADVANCE REVERSAL'
        elif transaction_type==4:transaction_type='ECOM TRANSACTION'
        elif transaction_type==5:transaction_type='MERCHANT PURCHASE'
        else: transaction_type='OVER THE COUNTER'
        
        st.info(f"""
                Our Inputs:\n\n
                MER_CODE: {mer}\n
                CARDHOLDER_TYPE: {card_type}\n
                PRODUCT_DESCRIPTION: {desc}\n
                TRANSACTION_DESCRIPTION: {transaction_type}\n
                TRANSACTION_AMOUNT: {amount}\n
                POSTED_TRANSACTION_PURSE_AMOUNT: {purse_amount}\n
                CPF_Purse_Transaction_Amount: {cpf}\n
                MASTERCARD_AMOUNT: {master_amount}\n
                TRANSACTION_TIMESTAMP: {time}
                """)
    
    # col1, col2, col3 = st.columns(3)
    # st.markdown("""  """,unsafe_allow_html=True)
    mer=st.sidebar.text_input("MER Code")
    desc=st.sidebar.selectbox('Product Description',('','MASTER STUDENT','NEW BORDERLESS PREPAID','NEW ONE CURRENCY','NEW RBL BPC','PARTNER BORDERLESS PREPAID','PARTNER ONE CURRENCY','VISA BPC','VISA STUDENT'))
    card_type=st.sidebar.selectbox('Card Holder Type',('','CORPORATE','RETAIL'))
    transaction_type=st.sidebar.selectbox('Transaction Description',('','ATM CASH WITHDRAWAL','BALANCE INQUIRY','CASH ADVANCE REVERSAL','ECOM TRANSACTION','MERCHANT PURCHASE','OVER THE COUNTER'))
    amount=st.sidebar.number_input("Transaction Amount")
    purse_amount=st.sidebar.number_input("POSTED TRANSACTION PURSE AMOUNT")
    cpf=st.sidebar.number_input('CPF Purse Transaction Amount')
    master_amount=st.sidebar.number_input("MASTERCARD AMOUNT")
    time=st.sidebar.text_input("Transaction Timestamp")
    if st.sidebar.button("Compute"):
        if desc=='MASTER STUDENT':desc=1
        elif desc=='NEW BORDERLESS PREPAID':desc=2
        elif desc=='NEW ONE CURRENCY':desc=3
        elif desc=='NEW RBL BPC':desc=4
        elif desc=='PARTNER BORDERLESS PREPAID':desc=5
        elif desc=='PARTNER ONE CURRENCY':desc=6
        elif desc=='VISA BPC':desc=7
        elif desc=='VISA STUDENT':desc=8
        else:st.warning("Select a Product Description")
        if card_type=='CORPORATE':card_type=1
        else:card_type=2
        if transaction_type=='ATM CASH WITHDRAWAL':transaction_type=1
        elif transaction_type=='BALANCE INQUIRY':transaction_type=2
        elif transaction_type=='CASH ADVANCE REVERSAL':transaction_type=3
        elif transaction_type=='ECOM TRANSACTION':transaction_type=4
        elif transaction_type=='MERCHANT PURCHASE':transaction_type=5
        elif transaction_type=='OVER THE COUNTER':transaction_type=6
        if 40001 <= int(time) <= 225959:time=0
        else:time=1
        result=RandFor.predict([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,time]])
        result1=RandFor.predict_proba([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,time]])
        if result==1:st.warning('Fraud')
        else:st.success("Not Fraud")
        per=format(result1[0][1]*100, '.2f')
        # per=format(per, '.3f')
        st.subheader(f'Probability of fraud: {per}%')
        





elif choice=='LOGISTIC REGRESSION':
    RandFor = load(r'.\Models\NewRandFor.joblib')
    if st.button('Sample1'):
        mer,card_type,desc,transaction_type,amount,purse_amount,cpf,master_amount,time=7011,1,6,6,233.00,232.00,232.00,234.00,124506
        if 40001 <= int(time) <= 225959:timezone=0
        else:timezone=1
        result=RandFor.predict([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        result1=RandFor.predict_proba([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        if result==1:st.warning('Fraud')
        else:st.success("Not Fraud")
        per=format(result1[0][1]*100, '.3f')
        # per=format(per, '.3f')
        st.header(f'Probability of fraud: {per}%')
        
        if card_type==1:card_type="Corporate"
        else: card_type="Retail"
        
        if desc==1:desc="MASTER STUDENT"
        elif desc==2:desc="NEW BORDERLESS PREPAID"
        elif desc==3:desc="NEW ONE CURRENCY"
        elif desc==4:desc="NEW RBL BPC"
        elif desc==5:desc="PARTNER BORDERLESS PREPAID"
        elif desc==6:desc="PARTNER ONE CURRENCY"
        elif desc==7:desc="VISA BPC"
        else:desc="VISA STUDENT"
            
        if transaction_type==1:transaction_type="ATM CASH WITHDRAWAL"
        elif transaction_type==2:transaction_type='BALANCE INQUIRY'
        elif transaction_type==3:transaction_type='CASH ADVANCE REVERSAL'
        elif transaction_type==4:transaction_type='ECOM TRANSACTION'
        elif transaction_type==5:transaction_type='MERCHANT PURCHASE'
        else: transaction_type='OVER THE COUNTER'
        
        st.info(f"""
                Our Inputs:\n\n
                MER_CODE: {mer}\n
                CARDHOLDER_TYPE: {card_type}\n
                PRODUCT_DESCRIPTION: {desc}\n
                TRANSACTION_DESCRIPTION: {transaction_type}\n
                TRANSACTION_AMOUNT: {amount}\n
                POSTED_TRANSACTION_PURSE_AMOUNT: {purse_amount}\n
                CPF_Purse_Transaction_Amount: {cpf}\n
                MASTERCARD_AMOUNT: {master_amount}\n
                TRANSACTION_TIMESTAMP: {time}
                """)
        
        
    if st.button('Sample2'):
        mer,card_type,desc,transaction_type,amount,purse_amount,cpf,master_amount,time=7011,1,1,4,1234.00,2343.00,1324.00,3243.00,234506
        if 40001 <= int(time) <= 225959:timezone=0
        else:timezone=1
        result=RandFor.predict([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        result1=RandFor.predict_proba([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,timezone]])
        if result==1:st.warning('Fraud')
        else:st.success("Not Fraud")
        per=format(result1[0][1]*100, '.3f')
        # per=format(per, '.3f')
        st.header(f'Probability of fraud: {per}%')
        
        if card_type==1:card_type="Corporate"
        else: card_type="Retail"
        
        if desc==1:desc="MASTER STUDENT"
        elif desc==2:desc="NEW BORDERLESS PREPAID"
        elif desc==3:desc="NEW ONE CURRENCY"
        elif desc==4:desc="NEW RBL BPC"
        elif desc==5:desc="PARTNER BORDERLESS PREPAID"
        elif desc==6:desc="PARTNER ONE CURRENCY"
        elif desc==7:desc="VISA BPC"
        else:desc="VISA STUDENT"
            
        if transaction_type==1:transaction_type="ATM CASH WITHDRAWAL"
        elif transaction_type==2:transaction_type='BALANCE INQUIRY'
        elif transaction_type==3:transaction_type='CASH ADVANCE REVERSAL'
        elif transaction_type==4:transaction_type='ECOM TRANSACTION'
        elif transaction_type==5:transaction_type='MERCHANT PURCHASE'
        else: transaction_type='OVER THE COUNTER'
        
        st.info(f"""
                Our Inputs:\n\n
                MER_CODE: {mer}\n
                CARDHOLDER_TYPE: {card_type}\n
                PRODUCT_DESCRIPTION: {desc}\n
                TRANSACTION_DESCRIPTION: {transaction_type}\n
                TRANSACTION_AMOUNT: {amount}\n
                POSTED_TRANSACTION_PURSE_AMOUNT: {purse_amount}\n
                CPF_Purse_Transaction_Amount: {cpf}\n
                MASTERCARD_AMOUNT: {master_amount}\n
                TRANSACTION_TIMESTAMP: {time}
                """)
        
    # col1, col2, col3 = st.columns(3)
    # st.markdown("""  """,unsafe_allow_html=True)
    mer=st.sidebar.text_input("MER Code")
    card_type=st.sidebar.selectbox('Card Holder Type',('','CORPORATE','RETAIL'))
    desc=st.sidebar.selectbox('Product Description',('','MASTER STUDENT','NEW BORDERLESS PREPAID','NEW ONE CURRENCY','NEW RBL BPC','PARTNER BORDERLESS PREPAID','PARTNER ONE CURRENCY','VISA BPC','VISA STUDENT'))
    transaction_type=st.sidebar.selectbox('Transaction Description',('','ATM CASH WITHDRAWAL','BALANCE INQUIRY','CASH ADVANCE REVERSAL','ECOM TRANSACTION','MERCHANT PURCHASE','OVER THE COUNTER'))
    amount=st.sidebar.number_input("Transaction Amount")
    purse_amount=st.sidebar.number_input("POSTED TRANSACTION PURSE AMOUNT")
    cpf=st.sidebar.number_input('CPF Purse Transaction Amount')
    master_amount=st.sidebar.number_input("MASTERCARD AMOUNT")
    time=st.sidebar.text_input("Transaction Timestamp")
    if st.sidebar.button("Compute"):
        if desc=='MASTER STUDENT':desc=1
        elif desc=='NEW BORDERLESS PREPAID':desc=2
        elif desc=='NEW ONE CURRENCY':desc=3
        elif desc=='NEW RBL BPC':desc=4
        elif desc=='PARTNER BORDERLESS PREPAID':desc=5
        elif desc=='PARTNER ONE CURRENCY':desc=6
        elif desc=='VISA BPC':desc=7
        elif desc=='VISA STUDENT':desc=8
        else:st.warning("Select a Product Description")
        if card_type=='CORPORATE':card_type=1
        else:card_type=2
        if transaction_type=='ATM CASH WITHDRAWAL':transaction_type=1
        elif transaction_type=='BALANCE INQUIRY':transaction_type=2
        elif transaction_type=='CASH ADVANCE REVERSAL':transaction_type=3
        elif transaction_type=='ECOM TRANSACTION':transaction_type=4
        elif transaction_type=='MERCHANT PURCHASE':transaction_type=5
        elif transaction_type=='OVER THE COUNTER':transaction_type=6
        if 40001 <= int(time) <= 225959:time=0
        else:time=1
        result=RandFor.predict([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,time]])
        result1=RandFor.predict_proba([[desc,card_type,mer,amount,purse_amount,cpf,master_amount,transaction_type,time]])
        if result==1:st.warning('Fraud')
        else:st.success("Not Fraud")
        per=format(result1[0][1]*100, '.3f')
        # per=format(per, '.3f')
        st.header(f'Probability of fraud: {per}%')
        
    
    
    
    # Logi = load(r'.\Models\LogReg.joblib')
    # desc=st.sidebar.selectbox('Product Description',('','New Borderless Prepaid','PARTNER BORDERLESS PREPAID','MASTER STUDENT','Partner One Currency','New One Currency','VISA BPC','VISA STUDENT','NEW RBL BPC'))
    # amount=st.sidebar.number_input("Transaction Amount")
    # mer=st.sidebar.text_input("MER Code")
    # card_type=st.sidebar.selectbox('Card Holder Type',('','Corporate','Retail'))
    # currency=st.sidebar.selectbox('Purse Currency',('','AED','EUR','CAD','USD','GBP','CHF','SGD','THB','AUD','JPY'))
    # # purse_amount=st.sidebar.number_input("POSTED TRANSACTION PURSE AMOUNT")
    # master_amount=st.sidebar.number_input("MASTERCARD AMOUNT")
    # transaction_type=st.sidebar.selectbox('Transaction Description',('','ATM CASH WITHDRAWAL','BALANCE INQUIRY','CASH ADVANCE REVERSAL','ECOM TRANSACTION','MERCHANT PURCHASE','OVER THE COUNTER'))
    # # cpf=st.sidebar.number_input('CPF Purse Transaction Amount')
    # time=st.sidebar.text_input("Transaction Timestamp")
    # if st.sidebar.button("Compute"):
    #     # if desc=='MASTER STUDENT':desc=1
    #     # elif desc=='NEW BORDERLESS PREPAID':desc=2
    #     # elif desc=='NEW ONE CURRENCY':desc=3
    #     # elif desc=='NEW RBL BPC':desc=4
    #     # elif desc=='PARTNER BORDERLESS PREPAID':desc=5
    #     # elif desc=='PARTNER ONE CURRENCY':desc=6
    #     # elif desc=='VISA BPC':desc=7
    #     # elif desc=='VISA STUDENT':desc=8
    #     # else:st.warning("Select a Product Description")
    #     # if card_type=='CORPORATE':card_type=1
    #     # else:card_type=2
    #     # if transaction_type=='ATM CASH WITHDRAWAL':transaction_type=1
    #     # elif transaction_type=='BALANCE INQUIRY':transaction_type=2
    #     # elif transaction_type=='CASH ADVANCE REVERSAL':transaction_type=3
    #     # elif transaction_type=='ECOM TRANSACTION':transaction_type=4
    #     # elif transaction_type=='MERCHANT PURCHASE':transaction_type=5
    #     # elif transaction_type=='OVER THE COUNTER':transaction_type=6
        
    #     le=LabelEncoder()
        
    #     le.fit(['New Borderless Prepaid','PARTNER BORDERLESS PREPAID','MASTER STUDENT','Partner One Currency','New One Currency','VISA BPC','VISA STUDENT','NEW RBL BPC'])
    #     desc=int(le.transform([desc]))
    #     le.fit(['Corporate','Retail'])
    #     card_type=int(le.transform([card_type]))
    #     le.fit(['AED','EUR','CAD','USD','GBP','CHF','SGD','THB','AUD','JPY'])
    #     currency=int(le.transform([currency]))
    #     le.fit(['ATM CASH WITHDRAWAL','ECOM TRANSACTION','BALANCE INQUIRY','MERCHANT PURCHASE','OVER THE COUNTER','CASH ADVANCE REVERSAL'])
    #     transaction_type=int(le.transform([transaction_type]))
        
        
    #     if 40001 <= int(time) <= 225959:time=0
    #     else:time=1
    #     result=Logi.predict([[desc,card_type,int(mer),amount,master_amount,transaction_type,time]])
    #     result1=Logi.predict_proba([[desc,card_type,int(mer),amount,master_amount,transaction_type,time]])
    #     if result==1:st.warning('Fraud')
    #     else:st.success("Not Fraud")
    #     per=format(result1[0][1]*100, '.3f')
    #     # per=format(per, '.3f')
    #     st.subheader(f'Probability of fraud: {per}%')        
st.divider()
        
with st.expander('Show Dataset'):
    df=pd.read_csv('CSVdataset.csv')
    st.write("Not Fraud:")
    st.dataframe(df[df['IsFraud'] == 0].head(2))
    st.write("Fraud:")
    st.dataframe(df[df['IsFraud'] == 1].head(2))
    
    if st.button('Details'):
                st.write("""Dataset info:\n
                Data columns (total 28 columns):\n
        Column                             Non-Null Count  Dtype  \n
    ---  ------                             --------------  -----  \n
    0   BUSINESS_DATE                      21704 non-null  int64  \n
    1   ICA_NUMBER                         13491 non-null  float64\n
    2   BIN                                21704 non-null  int64  \n
    3   PRODUCT_DESCRIPTION                21704 non-null  object \n
    4   ACCOUNT_NUMBER                     21704 non-null  object \n
    5   CARDHOLDER_NAME                    21704 non-null  object \n
    6   CARDHOLDER_TYPE                    21704 non-null  object \n
    7   CORPORATE_NAME                     21704 non-null  object \n
    8   CARD_NUMBER                        21704 non-null  object \n
    9   PASSPORT_NUMBER                    21704 non-null  object \n
    10  MER_CODE                           21704 non-null  int64  \n
    11  TRANSACTION_AMOUNT                 21532 non-null  float64\n
    12  TRANSACTION_CURRENCY               21704 non-null  object \n
    13  DB_CR                              21704 non-null  object \n
    14  POSTED_PURSE_CURRENCY              21704 non-null  object \n
    15  POSTED_TRANSACTION_PURSE_AMOUNT    21532 non-null  float64\n
    16  POSTED_FEE_AMOUNT                  988 non-null    float64\n
    17  GST                                988 non-null    float64\n
    18  POSTED_MARK_UP_FEE                 1600 non-null   float64\n
    19  MARKUP_GST                         1581 non-null   float64\n
    20  CPF_PURSE_TRANSACTION_AMOUNT       21688 non-null  float64\n
    21  MASTERCARD_AMOUNT                  21514 non-null  float64\n
    22  TRANSACTION_DESCRIPTION            21704 non-null  object \n
    23  LONG_ADJUSTMENT_DESCRIPTION        21704 non-null  object \n
    24  SYSTEM_GENERATED_REFERENCE_NUMBER  21704 non-null  int64  \n
    25  TRANSACTION_DATE                   21704 non-null  int64  \n
    26  TRANSACTION_TIMESTAMP              21704 non-null  int64  \n
    27  IsFraud                            21704 non-null  int64  \n
dtypes: float64(9), int64(7), object(12)\n
memory usage: 4.6+ MB\n
                """)
                
                
with st.expander("Rules"):
    st.write("""
    The transactions have been marked as Fraud when they satisfies all the below conditions: \n
    1.  If transaction is in offline format, from timestamp 23:00:00 to 04:00:00
    2.  If transaction amount is greater than 500(USD/EUR/GBP)\n
    3.  More than 5 transactions a day.
                """)
with st.expander("Analysis"):
    
    st.write('Correlation Matrix: ')
    st.image('./images/Correlation_Matrix.png')
    st.divider()
    st.info("We can see from the below plots that transactions of CARDHOLDER_TYPE=Corporate has higher spending power but in less frequency. Similarly transactions of CARDHOLDER_TYPE=Retail has higher frequency but lesser spending power")
    st.write('Bar Chart:')
    st.image('./images/bar_card.png')
    st.divider()
    st.write('Distribution in TRANSACTION_AMOUNT of each category of CARDHOLDER_TYPE:')
    st.image('./images/dist_holder.png')
    st.divider()
    st.write('Distribution among CARDHOLDER_TYPE and TRANSACTION_AMOUNT:')
    st.image('./images/prodesc2.png')
    st.divider()
    st.write('Distribution in TRANSACTION_AMOUNT:')
    st.image('./images/compa.png')

