import streamlit as st
import pickle
import numpy as np

def show_stroke():
    st.title("Pemeriksaan Stroke")

    yes_no = ['Ya','Tidak']

    
    gender_choice = (
        "Pria","Wanita",
    )

    residence_choice = (
        "Desa","Kota",
    )


    gender = st.selectbox("Jenis Kelamin", gender_choice)
    age = st.number_input('Berapa Usia Anda?',0)
    question_1 = st.radio('Apakah Anda Memiliki Tekanan Darah Tinggi?',yes_no)
    question_2 = st.radio('Apakah Anda Memiliki Penyakit Jantung?',yes_no)
    question_3 = st.radio('Apakah Anda Sudah Menikah?',yes_no)
    residence = st.selectbox("Tempat Tinggal", residence_choice)
    glukosa = st.number_input('Berapa Rata-rata Level Glukosa?',0)
    bmi = st.number_input('Berapa Nilai Index Massa Tubuh?',0)
    bt_predict = st.button('Prediksi')

    if gender == 'Pria':
         gender = 1
    else:
        gender = 0

    if residence == 'Kota':
        residence = 1
    else:
        residence = 0

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

    if bt_predict:
        model = pickle.load(open('model_stroke.pkl', 'rb'))


        #input(Gender, Tinggi, Berat)
        input_data = (gender,age,question_1,question_2,question_3,residence,glukosa,bmi)

        #mennganti input data menjadi numpy array
        input_data_array = np.array(input_data)

        #
        input_data_reshape = input_data_array.reshape(1,-1)

        prediksi = model.predict(input_data_reshape)
        print(prediksi)

        if (prediksi[0]==0):
            st.write('Anda Tidak Terindikasi Penyakit Stroke')
        else:
            st.write('Anda Terindikasi Penyakit Stroke')
