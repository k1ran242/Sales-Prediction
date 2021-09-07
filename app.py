import numpy as np
import pickle
import pandas as pd
import streamlit as st

model=pickle.load(open('Sales.pkl','rb'))

def welcome():
    return "Welcome"




def main():
    st.title('Sales Prediction')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Sales Prediction App</h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
   
    Item_Weight=st.text_input('Item_Weight') 
    Item_Fat_Content=st.text_input('Item_Fat_Content')
    Item_Visibility=st.text_input('Item_Visibility')
    Item_Type=st.text_input('Item_Type')
    Item_MRP=st.text_input('Item_MRP')
    Outlet_Size=st.text_input('Outlet_Size')
    Outlet_Location_Type=st.text_input('Outlet_Location_Type')
    Outlet_Type=st.text_input('Outlet_Type')
    New_Item_Type=st.text_input('New_Item_Type')
    Outlet_years=st.text_input('Outlet_years')
    Outlet=st.text_input('Outlet')
    

    

    st.title('The Sales for the Product will be....!')
    html_temp = """
    <div style="background-color:tomato;padding:5px">
    <h3 style="color:white;text-align:center;"></h3>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    if st.button(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Click Here . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . "):
        features=[[Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Item_MRP,Outlet_Size,Outlet_Location_Type,Outlet_Type,New_Item_Type,Outlet_years,Outlet]]
        print(features)
        prediction = model.predict(features)
        back = np.expm1(prediction)

        print(back)
        st.success(f'The Sales for the product in the perticular store is : {np.expm1(prediction)}')
        

            
    if st.button("About"):
        st.write("This is Machine Learning Project to predict the future sales of the product.")
    if st.button("Credits"):
        st.write("Kiran Bhongal")

    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h3 style="color:white;text-align:center;"> Thank You..!</h3>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)        
if __name__=='__main__':
    main()