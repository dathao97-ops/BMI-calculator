import streamlit as st
st.title("Công cụ tính BMI")
st.write("Nhập chiều cao và cân nặng để tính chỉ số BMI của bạn.")
weight = st.number_input("Cân nặng (kg)", min_value=0.0)
height = st.number_input("Chiều cao (m)", min_value=0.0)

# Tính BMI
if height > 0:
    bmi = weight / (height ** 2)

    st.subheader(f"BMI của bạn là: {bmi:.2f}")

    # Phân loại BMI
    if bmi < 18.5:
        st.info("Bạn đang thiếu cân")
    elif 18.5 <= bmi < 24.9:
        st.success("Bạn có cân nặng bình thường")
    elif 25 <= bmi < 29.9:
        st.warning("Bạn đang thừa cân")
    else:
        st.error("Bạn đang béo phì")

# Disclaimer 
st.caption("Công cụ chỉ mang tính tham khảo, không thay thế tư vấn y khoa.")
