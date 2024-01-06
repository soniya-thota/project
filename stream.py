import streamlit as st
import pickle

model = pickle.load(open('crop_prediction_model.pkl', 'rb'))  # Replace with your actual model file
st.title('Crop Prediction')

N = st.text_input('Enter Nitrogen amount: ')
P = st.text_input('Enter Phosphorous amount: ')
K = st.text_input('Enter Potassium amount: ')
T = st.text_input('Enter Temperature: ')
H = st.text_input('Enter Humidity level: ')
PH = st.text_input('Enter pH level: ')
R = st.text_input('Enter Rainfall level: ')

if st.button('Predict'):
    # Convert user input to the appropriate data type
    data = [float(N), float(P), float(K), float(T), float(H), float(PH), float(R)]

    # Make predictions
    result = model.predict([data])

    # Display the result
    st.success(f"The predicted crop is: {result[0]}")

'''import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))
st.title('Fraud Detection')

N=st.text_input('Enter Nitrogen amount: ')
P=st.text_input('Enter Phosporous amount: ')
K=st.text_input('Enter potassium amount: ')
T=st.text_input('Enter Temperature: ')
H=st.text_input('Enter humidity level: ')
PH=st.text_input('Enter ph level: ')
R=st.text_input('Enter rainfall level: ')
L=st.text_input('Which Crop ')



if st.button('Predict'):
    a=float(N)
    b=float(P)
    c=float(K)
    d=float(T)
    e=float(H)
    f=float(PH)
    g=float(R)
    i=float(L)
    data=[N,P,K,T,H,PH,R,L]
    result=model.predict(data)
    st.success(result)
    


    if result[0]==0:
        st.write("")

    else:
        st.write("fraud is detected")

'''