# import streamlit as st

# st.title("Aplikasi Streamlit Pertama")
# st.write("Selamat datang di Streamlit")
# st.write("made in FTSL")

# with st.form("form_data_diri"):
#     nama = st.text_input("Masukkan Nama Anda")
#     alamat = st.text_area("Masukkan Alamat Anda")
#     usia = st.number_input("Usia")
#     submit = st.form_submit_button("Submit")


import streamlit as st

st.title("Aplikasi Streamlit Pertama")
st.write("Selamat datang di Streamlit")
st.write("made in FTSL")

with st.form("form_data_diri"):
    nama = st.text_input("Masukkan Nama Anda")
    alamat = st.text_area("Masukkan Alamat Anda")
    umur = st.number_input("Masukkan Umur Anda", min_value=0, max_value=120, step=1)
    submit_button = st.form_submit_button("submit")

    if submit_button:
        st.success(f"Terimakasih {nama} telah mengisi data diri ")
        st.write(f"Nama : {nama}")
        st.write(f"Alamat : {alamat}")
        st.write(f"Usia : {umur}")
