import streamlit as st
import pickle as pk



html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Heart Disease Prediction</h2>
</div>
"""

def main():
    st.markdown(html_temp,unsafe_allow_html=True)
    #st.markdown(html_temp, unsafe_allow_html=True)
    # load the model
    model = pk.load(open("Heart Disease ML Mode", "rb"))

    
    f1 = st.number_input("Enter BMI")

    p1 = st.selectbox("Smoking", ("No", "Yes"))
    if p1 == "No":
        f2 = 0
    else:
        f2 = 1

    p2 = st.selectbox("AlcoholDrinking", ("No", "Yes"))
    if p2 == "No":
        f3 = 0
    else:
        f3 = 1

    p3 = st.selectbox("Stroke", ("No", "Yes"))
    if p3 == "No":
        f4 = 0
    else:
        f4 = 1

    f5 = st.slider("Enter PhysicalHealth", 0, 30)

    f6 = st.slider("Enter MentalHealth", 0, 30)

    p4 = st.selectbox("DiffWalking", ("No", "Yes"))
    if p4 == "No":
        f7 = 0
    else:
        f7 = 1

    p5 = st.selectbox("Sex", ("Female", "Male"))
    if p5 == "Female":
        f8 = 0
    else:
        f8 = 1

    p6 = st.selectbox("AgeCategory", (
    "18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79",
    "80 - Older"))
    if p6 == "18-24":
        f9 = 0
    elif p6 == "25-29":
        f9 = 1
    elif p6 == "30-34":
        f9 = 2
    elif p6 == "35-39":
        f9 = 3
    elif p6 == "40-44":
        f9 = 4
    elif p6 == "45-49":
        f9 = 5
    elif p6 == "50-54":
        f9 = 6
    elif p6 == "55-59":
        f9 = 7
    elif p6 == "60-64":
        f9 = 8
    elif p6 == "65-69":
        f9 = 9
    elif p6 == "70-74":
        f9 = 10
    elif p6 == "75-79":
        f9 = 11
    else:
        f9 = 12

    p7 = st.selectbox("Race", ("American Indian/Alaskan Native", "Asian", "Other", "Black", "Hispanic", "White"))
    if p7 == "American Indian/Alaskan Native":
        f10 = 0
    elif p7 == "Asian":
        f10 = 1
    elif p7 == "Other":
        f10 = 2
    elif p7 == "Black":
        f10 = 3
    elif p7 == "Hispanic":
        f10 = 4
    else:
        f10 = 5

    p8 = st.selectbox("Diabetic", ("No", "No, borderline diabetes", "Yes", "Yes ,during pregnancy"))
    if p8 == "No":
        f11 = 0
    elif p8 == "No, borderline diabetes":
        f11 = 1
    elif p8 == "Yes":
        f11 = 2
    else:
        f11 = 3

    p9 = st.selectbox("PhysicalActivity", ("No", "Yes"))
    if p9 == "No":
        f12 = 0
    else:
        f12 = 1

    p10 = st.selectbox("GenHealth", ("Excellent", "Fair", "Good", "Poor", "Very Good"))
    if p10 == "Excellent":
        f13 = 0
    elif p10 == "Fair":
        f13 = 1
    elif p10 == "Good":
        f13 = 2
    elif p10 == "Poor":
        f13 = 3
    else:
        f13 = 4

    f14 = st.slider("Enter SleepTime", 0, 30)

    p11 = st.selectbox("Asthma", ("No", "Yes"))
    if p11 == "No":
        f15 = 0
    else:
        f15 = 1

    p12 = st.selectbox("KidneyDisease", ("No", "Yes"))
    if p12 == "No":
        f16 = 0
    else:
        f16 = 1

    p13 = st.selectbox("SkinCancer", ("No", "Yes"))
    if p13 == "No":
        f17 = 0
    else:
        f17 = 1

    if st.button("  Predict  "):
        pre = model.predict([[f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17]])
        st.balloons()
        prediction_text = "Yes" if pre == 1 else "No"
        st.success(f"Heart Disease = {prediction_text}")
        #st.success("Heart Disease = {}".format(round(("No" if pre == 0 else "Yes")[0], 2)))



main()

