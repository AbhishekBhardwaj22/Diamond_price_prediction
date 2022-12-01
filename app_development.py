#                                   -------- Importing libraries-----------
import streamlit as st
import requests
import pickle
import numpy as np
from PIL import Image
from sklearn.preprocessing import StandardScaler,LabelEncoder


#                       ------------------------Unpacking Models-------------
xg = pickle.load(open('xg_model.pkl','rb'))
ada = pickle.load(open('ada.pkl','rb'))


#                                       ------ Page Configuration --------
im = Image.open("viz.jpg")
st.set_page_config(page_title="Diamond Price Web App",page_icon= im,layout='wide')


#                                   ---------- Setting App Layout ----------
with st.container():
    left_columns, right_columns = st.columns(2)
    with left_columns:
        st.title("Diamond Price Prediction")
    with right_columns:
        img = Image.open("bla.jpeg")
        st.image(img,width=200)
html_temp = """
    <div style="background-color:#9400D3 ;padding:10px">
    <h2 style="color:#00FFFF;text-align:center;">Price Prediction</h2>
    </div>
"""
st.markdown(html_temp, unsafe_allow_html=True)


#                         -------------------Feature Value Description-----------------------------
if st.button("How to fill"):
    with st.container():
        cut,color,clarity  = st.columns(3,gap = 'small')
        with color:
            st.write("""In Color Choose:\n
            0 for 'D',
            1 for 'E',
            2 for 'F',
            3 for 'G',
            4 for 'H',
            5 for 'I' ,
            6 for 'J'
            where j(worst) to D(Best)\n """
            )
        with cut:
            st.write("""In Cut choose:\n
                        0 for 'Fair',
                        1 for 'Good', 
                        2 for 'Ideal',
                        3 for 'Premium',
                        4 for 'Very Good'
                        \n """
                    )
        with clarity:
            st.write("""In Clarity Choose:\n
            0 for 'I1',
            1 for 'IF',
            2 for 'SI1',
            3 for 'SI2',
            4 for 'VS1',
            5 for 'VS2',
            6 for 'VVS1',
            7 for 'VVS2'\n""")


#                       -----------------------Input value Section---------------------------
carat = st.slider("Select Size of Carat:", min_value=0.2, max_value=5.01)
cut = st.selectbox("Select type of cut diamond has:",(0,1,4,3,2))
color =st.selectbox("Select color of diamond:",(6,5,4,3,2,1,0))
clarity = st.selectbox("Select Clarity Of diamond:",(0,3,2,5,4,6,7,1))
depth = st.slider("Select depth of diamond:",min_value=57.0,max_value=64.2)
table = st.slider("Select the size of table of diamond:",53.0,62.0)
x = st.slider("Select Length of diamond:",min_value=4.02,max_value=8.07)
y = st.slider("Select Width of diamond:",min_value=4.04,max_value=8.05)
z = st.slider("Select depth of diamond:",min_value=2.48,max_value=4.98)


#                               ------------------Standard Scaling-------------

#carat transformation
ca = (carat-0.792973)/0.457918

#depth transformation
de = (depth - 61.737286)/1.238462

#table transformation
t = (table - 57.412676)/2.090089

# dimensions transformation
l = (x - 5.724653)/1.100267
w = (y - 5.726571)/1.092441
d = (z - 3.534747)/0.679324	


#                                   ------------ Model Prediction code----------------

inputs = [[cut,color,clarity,ca,de,t,l,w,d]]
i2 = np.array(inputs)
if st.button("predict price"):
        st.success(xg.predict(i2))

st.write("Click on button to make prediction!")

#                               -------------------------Code Ends Here-----------------