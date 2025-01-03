from src.exception import CustomException
from src.logger import logging
from src.pipelines import prediction_pipeline
import streamlit as st
import sys


st.title("Diamond Price Prediction")

carat=float(st.text_input("CARAT",0))
depth=float(st.text_input("DEPTH",0))
table=float(st.text_input("TABLE",0))
cut=st.selectbox("CUT",['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color=st.selectbox("COLOR",['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity=st.selectbox("CLARITY",['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

if st.button("PREDICT"):
    st.write("HI")
    try:
        obj=prediction_pipeline.InputConverter(carat,depth,table,cut,color,clarity)
        predict_obj=prediction_pipeline.PridictionPipeline()
        res = predict_obj.predict(obj.convert_to_Datafram())
        st.write(res)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise CustomException(e,sys)