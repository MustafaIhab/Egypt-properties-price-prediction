import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing

model = joblib.load('DTmodel.h5')
scaler = joblib.load('scaler.h5')
encoders = list()
input = list()

for i in range(1, 5):
    encoders.append(joblib.load('label_encoder{}.joblib'.format(i)))

st.title("PROPERTIES PRICE PREDICTION IN EGYPT")
with st.form(key='mu_form'):

    p_types = open("property_type.txt", "r")
    property_type = st.selectbox('Property type', options=p_types.read().splitlines())

    bedrooms = st.slider('Bedrooms', min_value = 0, max_value = 10)
    bathrooms = st.slider('Bathrooms', min_value = 0, max_value = 10)
    area = st.number_input('Area', step = 1)

    compound = st.selectbox('Compound', options=(open('compounds.txt', 'r').read().splitlines()))

    district = st.selectbox('District', options=(open('district.txt', 'r').read().splitlines()))

    city = st.selectbox('City', options=(open('city.txt', 'r').read().splitlines()))

    sumbit_button = st.form_submit_button(label='Predict')

if sumbit_button:

    input.append(encoders[0].transform([property_type]))
    input.append(bedrooms)
    input.append(bathrooms)
    input.append(area)
    input.append(encoders[1].transform([compound]))
    input.append(encoders[2].transform([district]))
    input.append(encoders[3].transform([city]))

    profit = int(model.predict(scaler.transform([input])))
    st.header('We predict the price to be about {}'.format(profit))