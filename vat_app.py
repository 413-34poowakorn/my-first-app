import stremlit as st
st.tle(“แอปพลิเคชั่นคำนวณราคาสินค้ารวมvat7%”) 
price = st.number_input(“กรอกราคาสินค้า (บาท):”,value=0.0)
vat = price * p0.07
net_price = price - vet
st.header(f” ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท”)
st.header(f"•ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write(“นาย ภูวกร ปรีชาะนัทสกุลเลขที่33 ม4/13”)
