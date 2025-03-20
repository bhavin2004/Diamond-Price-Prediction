from src.exception import CustomException
from src.logger import logging
from src.pipelines import prediction_pipeline
import streamlit as st
import sys
from src.pipelines import training_pipeline
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config("Diamond Price Prediction",page_icon='istockphoto-1152003770-612x612.jpg')
# menu = option_menu()


st.title("Diamond Price Prediction System")
df=pd.read_csv('artifacts/test_data.csv')
df=df.sample(6)


st.divider()

#Giving Defualt Values
carat=0
depth=0
table=0
cut_list=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
cut=0
color_list=['D', 'E', 'F', 'G', 'H', 'I', 'J']
color=0
clarity_list=['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
clarity=0

sample=st.selectbox(label="Select The Sample Data",placeholder="Choose An Option",options=["Choose an option"] +[f"Sample Data {i}" for i in range(1,6)],index=0)
i=sample[-1]
sample_btn = st.button("Select")
if sample_btn and i.isdigit():
    i=int(i)
    sample_data=df.iloc[i]
    carat=sample_data['carat']
    depth=sample_data['depth']
    table=sample_data['table']
    cut=cut_list.index(sample_data['cut'])
    color=color_list.index(sample_data['color'])
    clarity=clarity_list.index(sample_data['clarity'])
    st.balloons()
  
carat=float(st.text_input("CARAT",carat))
depth=float(st.text_input("DEPTH",depth))
table=float(st.text_input("TABLE",table))
cut=st.selectbox("CUT",cut_list,index=cut)
color=st.selectbox("COLOR",color_list,index=color)
clarity=st.selectbox("CLARITY",clarity_list,index=clarity)
st.divider()

if st.button("PREDICT"):
    # st.write("HI")
    try:
        obj=prediction_pipeline.InputConverter(carat,depth,table,cut,color,clarity)
        predict_obj=prediction_pipeline.PridictionPipeline()
        res = predict_obj.predict(obj.convert_to_Datafram())[0]
        # st.write(type(res))
        st.write(f"The price of the Gemstone/Diamond is {res}$")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise CustomException(e,sys)
    