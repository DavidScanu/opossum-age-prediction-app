import pickle
import streamlit as st
import time

# venv 
# Install streamlit, scikit-learn

# Import pickle data 
pickle_in = open("model.pkl","rb")
export = pickle.load(pickle_in)
pickle_in.close()

# Variables
model_best = export['model']
scaler = export['scaler']


def prediction(hdlngth, skullw, totlngth, footlgth, chest, belly):

    if hdlngth and skullw and totlngth and footlgth and chest and belly:

        X = [[float(hdlngth), float(skullw), float(totlngth), float(footlgth), float(chest), float(belly)]]
        # Mise à l'échelle
        X_scaled = scaler.transform(X)
        # Prédiction
        prediction = round(float(model_best.predict(X_scaled)), 1)

        if prediction:
            message = f"This opossum is {prediction} years old."

    else : 
        message = "Please enter Opossum parameters."

    # print("Prédiction : ", message)
    return message


# Streamlit
st.set_page_config(
    page_title="Opossum Age Prediction",
    page_icon=":mouse:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# if 'iteration' not in st.session_state:
#     st.session_state.iteration = 0

with st.container():
    st.title(':mouse: Opossum Prediction')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Enter Opossum parameters :')
    hdlngth = st.slider("Head length in mm", 83, 105, 90)
    skullw = st.slider("Skull width in mm", 50, 65, 55)
    totlngth = st.slider("Total length in cm", 78, 100, 87)
    footlgth = st.slider("Foot length in mm", 58, 80, 68)
    chest = st.slider("Chest girth in cm", 21, 33, 26)
    belly = st.slider("Belly girth in cm", 25, 42, 32)

with col2:
    # Check if session variable is set
    if 'my_button' in st.session_state:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.header(prediction(hdlngth, skullw, totlngth, footlgth, chest, belly))


# st.write(st.session_state) 
if 'my_button' not in st.session_state:
    st.session_state.my_button = True

# st.write(st.session_state.iteration)
# st.session_state.iteration += 1