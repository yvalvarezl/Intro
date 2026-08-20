import streamlit as st
from PIL import Image

st.title("La app de Yoselin")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Fácilmente puedo realizar backend y frontend")
image = Image.open('Interfaces multimodales.png')
st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribe algo','Este es mi texto')
st.write ('El texto escrito es',texto)

st.subheader("Ahora usemos 2 columnas")

col1,col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("¿Qué modalidad es la principal interfaz?",('Visual','Auditiva','Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de botones")
if st.button('Presiona el botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')
