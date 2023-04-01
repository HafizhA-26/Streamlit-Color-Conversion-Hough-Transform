import streamlit as st

def colorInputSection(key):
    colorOption = st.selectbox(label="Pilih Jenis Input Warna", options=("Color Picker", "Nilai RGB Manual"), key=key)
    color = None
    if colorOption == "Color Picker":
        hexColor = st.color_picker(label="Pilih Warna", value="#000000", key=key+"_picker")
        st.write("Hex code : "+ hexColor)
        hexColor = hexColor.lstrip('#') 
        color = tuple(int(hexColor[i:i+2], 16) for i in (0, 2, 4))
    else:
        st.write("Masukkan Nilai RGB Manual : ")
        r_value = st.number_input(label='Red', step=1, format="%d", max_value=255, min_value=0)
        g_value = st.number_input(label='Green', step=1, format="%d", max_value=255, min_value=0)
        b_value = st.number_input(label='Blue', step=1, format="%d", max_value=255, min_value=0)
        color = (int(r_value), int(g_value), int(b_value))
    st.write("RGB : "+ str(color))
    return color

st.set_page_config(
    page_title="Color Conversion"
)
st.title("Color Conversion")
st.markdown("***")
st.subheader("RGB to Other Color")
color = colorInputSection("rgb")
st.markdown("***")
st.subheader("XYZ to Other Color")
color = colorInputSection("xyz")
