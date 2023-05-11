import streamlit as st
import pickle
import numpy as np

def show_diabetes():
    st.title("Pemeriksaan Diabetes")

    yes_no = ['Ya','Tidak']

    
    gender_choice = (
        "Pria","Wanita",
    )


    gender = st.selectbox("Jenis Kelamin", gender_choice)
    age = st.number_input('Berapa Usia Anda?',0)
    question_1 = st.radio('Apakah Anda Memiliki Tekanan Darah Tinggi?',yes_no)
    question_2 = st.radio('Apakah Anda Memiliki Kadar Kolestrol Tinggi?',yes_no)
    bmi = st.number_input('Masukan Indeks Massa Tubuh (Berat badan(kg)/TInggi Badan(m)xTInggi Badan(m))',0)
    question_3 = st.radio('Apakah Anda Seorang Perokok?',yes_no)
    question_4 = st.radio('Apakah Anda Memiliki Gejala Stroke?',yes_no)
    question_5 = st.radio('Apakah Anda Memiliki Gejala Serangan Jantung?',yes_no)
    question_6 = st.radio('Apakah Anda Sering Beraktivitas Berat?',yes_no)
    question_7 = st.radio('Apakah Anda Mengkonsumsi Buah Minimal 1x Perhari?',yes_no)
    question_8 = st.radio('Apakah Anda Mengkonsumsi Sayur Minimal 1x Perhari?',yes_no)
    bt_predict = st.button('Prediksi')

    if gender == 'Pria':
        gender = 1
    else:
        gender = 0

    if question_1 == 'Ya':
        question_1 = 1
    else:
        question_1 = 0

    if question_2 == 'Ya':
        question_2 = 1
    else:
        question_2 = 0

    if question_3 == 'Ya':
        question_3 = 1
    else:
        question_3 = 0

    if question_4 == 'Ya':
        question_4 = 1
    else:
        question_4 = 0

    if question_5 == 'Ya':
        question_5 = 1
    else:
        question_5 = 0

    if question_6 == 'Ya':
        question_6 = 1
    else:
        question_6 = 0

    if question_7 == 'Ya':
        question_7 = 1
    else:
        question_7 = 0
    
    if question_8 == 'Ya':
        question_8 = 1
    else:
        question_8 = 0

    if bt_predict:

        model = pickle.load(open('model_Diabetes.pkl', 'rb'))

        #input(Gender, Tinggi, Berat)
        input_data = (gender,age,question_1,question_2,bmi,question_3,question_4,question_5,question_6,question_7,question_8)

        #mennganti input data menjadi numpy array
        input_data_array = np.array(input_data)

        #
        input_data_reshape = input_data_array.reshape(1,-1)

        prediksi = model.predict(input_data_reshape)
        print(prediksi)

        if (prediksi[0]==0):
            st.write('Anda Tidak Terindikasi Diabetes')
        elif (prediksi[0]==1):
            st.write('Anda Terindikasi Prediabetes')
        else:
            st.write('Anda Terindikasi Diabetes')
        
