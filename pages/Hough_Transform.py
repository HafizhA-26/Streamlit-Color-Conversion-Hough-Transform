import streamlit as st
import cv2
import numpy as np

def loadImageJPG(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def loadImagePNG(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    return img

st.set_page_config(
    page_title="Boundary Detection"
)
st.title("Boundary Detection")
st.markdown("***")
foto_upload = st.file_uploader("Custom upload foto", 
    ['png', 'jpg', 'jpeg'], 
    help="Foto bisa bebas"
    )
foto_default = loadImageJPG('images/wgs.png')
if foto_upload is not None:
    foto_upload_np = np.asarray(bytearray(foto_upload.read()), dtype=np.uint8)
    if foto_upload.name[-3:] == 'png':
        foto_upload_np = cv2.cvtColor(cv2.imdecode(foto_upload_np, 1), cv2.COLOR_BGRA2RGB)
    else:
        foto_upload_np = cv2.cvtColor(cv2.imdecode(foto_upload_np, 1), cv2.COLOR_BGR2RGB)
    foto = foto_upload_np
else:
    foto = foto_default

st.image(foto)