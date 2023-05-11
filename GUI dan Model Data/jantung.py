import streamlit as st
import pickle
import numpy as np

def show_jantung():
    st.title("Pemeriksaan Jantung")

    yes_no = ['Ya','Tidak']

    gender_choice = (
        "Pria","Wanita",
    )
    ecg_result = (
        "Rendah","Normal", "Tinggi",
    )

    thal_choice = (
        'Normal','Fixed Defect','Reversible Defect'
    )


    gender = st.selectbox("Jenis Kelamin", gender_choice)
    age = st.number_input('Berapa Usia Anda?',0)
    blood_press = st.number_input('Tekanan Darah (mmHg)',0)
    chol = st.number_input('Kolestrol (mg/dl)',0)
    question_1 = st.radio('Apakah Anda Gula Darah Anda 120 mg/dl?',yes_no)
    ecg = st.selectbox("Hasil Pemeriksaan EKG", ecg_result)
    hearth_beat = st.number_input('Detak Jantung Maksimum (70-200bpm)',0)
    question_2 = st.radio('Apakah Sering Nyeri Dada Saat Beraktivitas?',yes_no)
    thal = st.selectbox('Kelainan Darah / Thalasemia',thal_choice)
    bt_predict = st.button('Prediksi')

    if gender == 'Pria':
        gender = 1
    else:
        gender = 0

    if ecg == "Rendah":
        ecg = 0
    elif ecg == "Normal":
        ecg = 1
    else:
        ecg = 3

    if thal == 'Normal':
        thal = 0
    elif thal == 'Fixed Defect':
        thal = 1
    else:
        thal = 3

    if question_1 == 'Ya':
        question_1 = 1
    else:
        question_1 = 0

    if question_2 == 'Ya':
        question_2 = 1
    else:
        question_2 = 0

    if bt_predict:

        model = pickle.load(open('model_PJ.pkl', 'rb'))

        #input(Gender, Tinggi, Berat)
        input_data = (gender,age,blood_press,chol,question_1,ecg,hearth_beat,question_2,thal)

        #mennganti input data menjadi numpy array
        input_data_array = np.array(input_data)

        #
        input_data_reshape = input_data_array.reshape(1,-1)

        prediksi = model.predict(input_data_reshape)
        print(prediksi)

        if (prediksi[0]==0):
            st.write('Anda Tidak Terindikasi Penyakit Jantung')
        else:
            st.write('Anda Terindikasi Penyakit Jantung')