import streamlit as st
import pickle
import tensorflow as tf
import numpy as np
from home import show_home
from bmi import show_bmi
from diabetes import show_diabetes
from jantung import show_jantung
from stroke import show_stroke


page_dataset = st.sidebar.selectbox(
    'Pilih Pemeriksaan',
    ('Beranda', 'Cek Indeks Massa Tubuh', 'Cek Stroke', 'Cek Jantung', 'Cek Diabetes')
)

if page_dataset == 'Beranda':
    show_home()
elif page_dataset == 'Cek Indeks Massa Tubuh':
    show_bmi()
elif page_dataset == 'Cek Diabetes':
    show_diabetes()
elif page_dataset == 'Cek Jantung':
    show_jantung()
else:
    show_stroke()



