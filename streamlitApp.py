import streamlit as st
import pickle

with open('churn_model.bin', 'rb') as f:
    dv, model = pickle.load(f)

def predict_churn(user):
    user = dv.transform([user])
    probabilty_churning = model.predict_proba(user)[0,1]
    y_pred = probabilty_churning >= 0.5

    if y_pred == True:
        return f'Send a promotion to this user because the probabilty of churning is {probabilty_churning}'
    
    return f'Do not Send a promotion to this user because the probabilty of churning is {probabilty_churning}'

def main():
    st.title("Churn Service")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Churn Service ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    gender = st.text_input("gender","male or female")
    seniorcitizen = st.text_input("seniorcitizen","0 or 1")
    partner = st.text_input("partner","yes or no")
    dependents = st.text_input("dependents","yes or no")
    phoneservice = st.text_input("phoneservice","yes or no")

    multiplelines = st.text_input("multiplelines","no_phone_service or yes or no")
    internetservice = st.text_input("internetservice","dsl or fiber_optic or no")

    onlinesecurity = st.text_input("onlinesecurity","yes or no or no_internet_service")
    onlinebackup = st.text_input("onlinebackup","yes or no or no_internet_service")
    deviceprotection = st.text_input("deviceprotection","yes or no")
    techsupport = st.text_input("techsupport","yes or no or no_internet_service")
    streamingtv = st.text_input("streamingtv","yes or no or no_internet_service")
    streamingmovies = st.text_input("streamingmovies","yes or no or no_internet_service")

    contract = st.text_input("contract","month-to-month or one_year or two_years")
    paperlessbilling = st.text_input("paperlessbilling","yes or no")
    paymentmethod = st.text_input("paymentmethod","bank_transfer_(automatic) or credit_card_(automatic)	or electronic_check or mailed_check")
    tenure = st.text_input("tenure",1 )
    monthlycharges = st.text_input("monthlycharges",29.85)
    totalcharges = st.text_input("totalcharges",29.85)

    customer = {
        "gender": gender.strip().lower(),
        "seniorcitizen": seniorcitizen.strip().lower(),
        "partner": partner.strip().lower(),
        "dependents": dependents.strip().lower(),
        "phoneservice": phoneservice.strip().lower(),
        "multiplelines": multiplelines.strip().lower(),
        "internetservice": internetservice.strip().lower(),
        "onlinesecurity": onlinesecurity.strip().lower(),
        "onlinebackup": onlinebackup.strip().lower(),
        "deviceprotection": deviceprotection.strip().lower(),
        "techsupport": techsupport.strip().lower(),
        "streamingtv": streamingtv.strip().lower(),
        "streamingmovies": streamingmovies.strip().lower(),
        "contract": contract.strip().lower(),
        "paperlessbilling": paperlessbilling.strip().lower(),
        "paymentmethod": paymentmethod.strip().lower(),
        "tenure": int(tenure),
        "monthlycharges": float(monthlycharges),
        "totalcharges": float(totalcharges)
    }
    result = ''
    if st.button('Predict'):
        result = predict_churn(customer)
    
    st.success(result)

    if st.button("About"):
        st.text("My name is Mohamed Algebai Almoazin AI and ML engineer , have solid foundations in NLP, CV and RL fields ")
        st.text("nemo45627@gmail.com")
        st.text("(+20)1555859441")


if __name__=='__main__':
    main()