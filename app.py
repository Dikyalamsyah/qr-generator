import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Pembuat QR Code Undangan", page_icon="📍")

st.title("📍 Pembuat QR Code Google Maps")
st.write("Masukkan link Google Maps di bawah untuk membuat QR Code lokasi secara otomatis.")

link_maps = st.text_input("Link Google Maps:", placeholder="https://maps.app.goo.gl/...")

if link_maps:
    # Buat QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link_maps)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Simpan gambar ke memory buffer
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption="QR Code Berhasil Dibuat", use_column_width=True)

    st.download_button(
        label="⬇️ Download QR Code (PNG)",
        data=byte_im,
        file_name="qr_location.png",
        mime="image/png"
    )
