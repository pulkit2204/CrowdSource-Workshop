import streamlit as st
import fastai.vision.all import *

@st.cache
def load_learner_(path):
    return load_learner(path)

@st.cache
def load_img(path):
    image = Image.open(path)
    w, h = image.size
    dim = (500, int((h*500)/w))
    return image.resize(dim)

learn = load_learner_('export.pkl')

st.markdown("#Animal Classifier")
st.markdown("Upload an image and the classifier will tell you whether its a horse, dog or bear.")

file_bytes = st.file_uploader("Upload a file", type=("png", "jpg", "jpeg"))
if file_bytes:
    img = load_img(file_bytes)
    st.image(img)
    
    submit = st.button('Predict!')
    if submit:
        pred, pred_idx, probs = learn.predict(img)
        st.markdown(f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}')
