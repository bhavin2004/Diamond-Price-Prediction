from src.exception import CustomException
from src.logger import logging
from src.pipelines.prediction_pipeline import PridictionPipeline,InputConverter
import streamlit as st
import sys
import os
from src.pipelines import training_pipeline
import pandas as pd
from sklearn.decomposition import PCA
from streamlit_option_menu import option_menu
import plotly.express as px

st.set_page_config("Diamond Price Prediction",page_icon='💎',layout="wide")
# menu = option_menu()

with st.sidebar:
    selection = option_menu(
    menu_title="Menu",           # Title of the menu
    options=['Home', 'Visualization of Data',"Predict with CSV","About Project"],   # Menu options
    icons=['house', 'bar-chart','filetype-csv'], # Optional icons (from FontAwesome)
    menu_icon="list",            # Main menu icon
    default_index=2,             # Default selected item
    orientation="vertical",    # Options: "horizontal" or "vertical"
    )
df=pd.read_csv('artifacts/test_data.csv')
if selection=='Home':
    st.title("Diamond Price Prediction System")
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
        # st.balloons()
        
    
    #
    with st.container(border=True):
        col1, col2 = st.columns(2,gap='medium')
        with col1:
            carat=float(st.text_input("CARAT",carat))
            depth=float(st.text_input("DEPTH",depth))
            table=float(st.text_input("TABLE",table))
        with col2:
            color=st.selectbox("COLOR",color_list,index=color)
            cut=st.selectbox("CUT",cut_list,index=cut)
            clarity=st.selectbox("CLARITY",clarity_list,index=clarity)
    st.divider()

    if st.button("PREDICT",use_container_width=True):
        # st.write("HI")
        try:
            obj=InputConverter(carat,depth,table,cut,color,clarity)
            predict_obj=PridictionPipeline()
            res = predict_obj.predict(obj.convert_to_Datafram())[0]
            # st.write(type(res))
            # st.write(f"The price of the Gemstone/Diamond is {res}$")
            st.success(f"The price of the Gemstone/Diamond is {res}$")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            raise CustomException(e,sys)
        
        
# """if selection=="Visualization of Data":
#     train_df= pd.read_csv("artifacts/processed_train_data.csv")
#     test_df= pd.read_csv("artifacts/processed_test_data.csv")
#     st.dataframe(test_df.head(5))
#     pca = PCA(n_components=2)
#     df1=pca.fit_transform(train_df[:-1])
#     st.write(px.line(df1))
#    """

if selection=="Predict with CSV":

    st.title("Predict the Diamond Price of a CSV file")
    st.divider()
    st.warning(f"Your CSV should have these columns "+", ".join(list(df.columns)))
    with st.expander("For Example"):
        st.dataframe(df.iloc[:5,:-1])
    st.divider()
  
    sample_csv=pd.read_csv('artifacts/test_data.csv')
    sample_csv.drop("price",axis=1,inplace=True)
    st.download_button(label="Download Sample CSV",file_name='sample.csv',data=sample_csv.to_csv(index=False),mime="text/csv",icon='⬇️')
    
    uploaded_csv=st.file_uploader(label="Upload Your Csv",type="csv",)
    if uploaded_csv:
        upload_df=pd.read_csv(uploaded_csv)
        with st.expander("Your Data in CSV".upper()):
            st.write(upload_df.iloc[:,:-1])

        if st.button("Predict",type='primary',icon='🕵'):
            predict_obj = PridictionPipeline()
            output=predict_obj.predict(upload_df.iloc[:,:-1])
            upload_df['price'] =output
            with st.expander("Your Result",icon='📃'):
                st.dataframe(upload_df)
            csv_file=upload_df.to_csv(index=False)
            st.download_button(label="Download Result",file_name='predicted.csv',data=csv_file,mime="text/csv",icon='⬇️')
        
        
if selection == "About Project":
    st.title("💎 About the Diamond Price Prediction System")
    st.divider()

    st.markdown("""
    ### 🔍 **Project Overview**
    This system predicts the price of a diamond based on various attributes such as:
    - **Carat**: Weight of the diamond.
    - **Cut**: Quality of the cut (Fair, Good, Very Good, Premium, Ideal).
    - **Color**: Diamond color grading (D - best to J - worst).
    - **Clarity**: Measure of the diamond's internal imperfections.
    - **Depth**: Height of the diamond relative to its width.
    - **Table**: Width of the diamond’s top relative to the widest point.

    ### ⚙️ **How It Works**
    - Users can enter individual diamond attributes manually.
    - Upload a CSV file to predict diamond prices for multiple records.
    - PCA is used to visualize the high-dimensional data.

    ### 📊 **Features**
    - Home: Predict diamond price for individual entries.
    - Visualization of Data: PCA visualization of training and test data.
    - Predict with CSV: Predict diamond prices for a batch of records.
    - Downloadable CSV results.

    ### 📧 **Contact**
    If you encounter any issues or have suggestions, feel free to reach out.
    """)

    st.divider()

    # Add developer info or GitHub link
    st.markdown("""
    ### 👨‍💻 **Developed by Bhavin Karangia**
    - 📧 [Email Me](mailto:bhavinkarangia@example.com)
    - 🌐 [GitHub](https://github.com/bhavin2004/Diamond-Price-Prediction)
    """)

    st.success("Thank you for using this system! 💎")