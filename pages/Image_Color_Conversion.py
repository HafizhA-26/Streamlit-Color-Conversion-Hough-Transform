import streamlit as st
import numpy as np
import conversion_color as cc
import cv2


def loadImageJPG(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
def showResultImage(img, img_name="Gambar"):
  st.markdown(img_name+" Ukuran asli ("+str(img.shape[1])+"x"+str(img.shape[0]) +")")
  st.image(img, clamp=True)
  image_5x = cv2.resize(img, (img.shape[1]*5, img.shape[0]*5))
  st.markdown(img_name+" 5x Ukuran ("+str(img.shape[1]*5)+"x"+str(img.shape[0]*5)+")")
  st.image(image_5x, clamp=True)

st.set_page_config(
    page_title="Image Color Conversion"
)
st.title("Image Color Conversion")
st.markdown("***")
foto_default = loadImageJPG('images/foto.jpg')
showResultImage(foto_default, "Foto :")
st.markdown("***")
st.subheader("Matriks Original Gambar")
st.code(foto_default)
fotoSource = np.array(foto_default, dtype=np.float32)
resultHSV = cc.RGB2HSV(fotoSource)
st.subheader("Matriks Konversi ke HSV")
st.code(resultHSV)
resultXYZ = cc.RGB2XYZ(fotoSource)
st.subheader("Matriks Konversi ke XYZ")
st.code(resultXYZ)
resultCMY = cc.RGB2CMY(fotoSource)
st.subheader("Matriks Konversi ke CMY")
st.code(resultCMY)
resultYCbCr = cc.RGB2YCBCR(fotoSource)
st.subheader("Matriks Konversi ke YCbCr")
st.code(resultYCbCr)
resultCieLab = cc.RGB2LAB(fotoSource)
st.subheader("Matriks Konversi ke CIE LAB")
st.code(resultCieLab)