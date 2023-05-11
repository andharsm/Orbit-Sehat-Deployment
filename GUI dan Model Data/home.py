import streamlit as st
# import pickle
import numpy as np
import os


# def load_model():
#     with open('model_IMT.pkl', 'rb') as file:
#         data = pickle.load(file)
#     return data

# data = load_model()

def show_home():
    
    st.title("ORBIT SEHAT")
    
    st.write("""
        Selamat datang di ORBIT SEHAT! Kami menyediakan berbagai fitur untuk membantu menganalisis kesehatan anda dengan bantuan model machine learning.
        """)
    
    st.header("Fitur")
    st.write("""
        Berikut adalah beberapa fitur yang kami sediakan:
        - Pengecekan Indeks Massa Tubuh
        - Pengecekan Stroke
        - Pengecekan Jantung
        - Pengecekan Diabetes
        """)
    
    st.header("Anggota Kelompok")
    
    # Menggunakan layout grid untuk menampilkan nama-nama kelompok secara horizontal
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        image_path = os.path.join("..", "Media", "andhar.png")
        st.image(image_path, caption="Andhar Siraj Munir")
    
    with col2:
        image_path = os.path.join("..", "Media", "adrians.jpg")
        st.image(image_path, caption="Adrians Galih AG")
    
    with col3:
        image_path = os.path.join("..", "Media", "annisa.jpg")
        st.image(image_path, caption="Annisa Fauziah")
    
    with col4:
        image_path = os.path.join("..", "Media", "nabil.jpg")
        st.image(image_path, caption="Nabil Muhyidin")

    st.header("Support by")
    col1, col2, col3 = st.columns(3)

    with col1:
        image_path = os.path.join("..", "Media", "logo amikom.png")
        st.image(image_path, caption="Universitas Amikom Purwokerto")
    
    with col2:
        image_path = os.path.join("..", "Media", "logo telkom.png")
        st.image(image_path, caption="ITT Telkom Purwokerto")
    
    with col3:
        image_path = os.path.join("..", "Media", "logo ugm.png")
        st.image(image_path, caption="Universitas Gajah Mada")