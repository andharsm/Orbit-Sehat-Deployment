import streamlit as st
import pickle
import numpy as np

def show_bmi():
    st.title("Pemeriksaan Indeks Massa Tubuh")
    gender_choice = (
        "Pria","Wanita",
    )

    gender = st.selectbox("Jenis Kelamin", gender_choice)
    height = st.number_input('Masukan Tinggi Badan (cm)',0)
    weight = st.number_input('Masukan Berat Badan (kg)',0)
    bt_predict = st.button('Prediksi')

    if gender == 'Pria':
        gender = 0
    else:
        gender = 1

    if bt_predict:
        model = pickle.load(open('model_BMI.pkl', 'rb'))
        imt = weight/((height/100)*(height/100))

        #input(Gender, Tinggi, Berat)
        input_data = (gender,height,weight)

        #mennganti input data menjadi numpy array
        input_data_array = np.array(input_data)

        #
        input_data_reshape = input_data_array.reshape(1,-1)

        prediksi = model.predict(input_data_reshape)
        print(prediksi)

        if (prediksi[0]==0):
            st.write('Indeks Massa Tubuh Anda Sangat Kurus')
        elif (prediksi[0]==1):
            st.write('Indeks Massa Tubuh Anda Kurus')
        elif (prediksi[0]==2):
            st.write('Indeks Massa Tubuh Anda Normal')
        elif (prediksi[0]==3):
            st.write('Indeks Massa Tubuh Anda Kegemukan')
        elif (prediksi[0]==4):
            st.write('Indeks Massa Tubuh Anda Obesitas')
            
        else:
            st.write('Indeks Massa Tubuh Anda Obesitas Ekstrim')
        
        st.write('Dengan Indeks Masa Tubuh : ',imt)
