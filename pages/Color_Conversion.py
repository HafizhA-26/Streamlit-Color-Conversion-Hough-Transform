import streamlit as st
import numpy as np
import conversion_color as cc

st.set_page_config(
    page_title="Color Conversion"
)
st.title("Color Conversion")
st.markdown("***")
st.subheader("RGB to Other Color")
colorRGB = None
colorOption = st.selectbox(label="Pilih Jenis Input Warna", options=("Color Picker", "Nilai RGB Manual"))
if colorOption == "Color Picker":
    hexColor = st.color_picker(label="Pilih Warna", value="#000000", key="rgb_hex_picker")
    st.write("Hex code : "+ hexColor)
    hexColor = hexColor.lstrip('#') 
    colorRGB = list(int(hexColor[i:i+2], 16) for i in (0, 2, 4))
else:
    st.write("Masukkan Nilai RGB Manual : ")
    r_value = st.number_input(label='Red', step=1, format="%d", max_value=255, min_value=0)
    g_value = st.number_input(label='Green', step=1, format="%d", max_value=255, min_value=0)
    b_value = st.number_input(label='Blue', step=1, format="%d", max_value=255, min_value=0)
    colorRGB = [int(r_value), int(g_value), int(b_value)]
st.write("RGB : "+ str(colorRGB))
rgbSource = np.array(colorRGB, dtype=np.float32)
st.code("HSV : "+ str(cc.RGB2HSV(np.float32([[rgbSource]]))[0, 0, :]))
st.code("XYZ : "+ str(cc.RGB2XYZ(np.float32([[rgbSource]]))[0, 0, :]))
st.code("CMY : "+ str(cc.RGB2CMY(np.float32([[rgbSource]]))[0, 0, :]))
st.code("YCbCr : "+ str(cc.RGB2YCBCR(np.float32([[rgbSource]]))[0, 0, :]))
st.code("CieLab : "+ str(cc.RGB2LAB(np.float32([[rgbSource]]))[0, 0, :]))
st.markdown("***")
st.subheader("XYZ to Other Color")
colorXYZ = None
st.write("Masukkan Nilai XYZ Manual : ")
x_value = st.number_input(label='X Value', step=1, format="%d", min_value=0)
y_value = st.number_input(label='Y Value', step=1, format="%d", min_value=0)
z_value = st.number_input(label='Z Value', step=1, format="%d", min_value=0)
colorXYZ = (int(x_value), int(y_value), int(z_value))
xyzSource = np.array(colorXYZ, dtype=np.float32)
st.write("XYZ : "+ str(colorXYZ))
st.code("RGB : "+ str(cc.XYZ2RGB(np.float32([[xyzSource]]))[0, 0, :]))
st.code("HSV : "+ str(cc.XYZ2HSV(xyzSource)[0, 0, :]))
st.code("CMY : "+ str(cc.XYZ2CMY(xyzSource)[0, 0, :]))
st.code("CIE Lab : "+ str(cc.XYZ2LAB(xyzSource)[0, 0, :]))
