import pandas as pd 
import streamlit as st 
from datetime import datetime

st.set_page_config(layout="wide")



with st.container():
    col1, col2, col3 = st.columns(3)

    with col2:
            date= datetime.now().strftime("%d/%m/%Y")
            st.title(f"STOCK {date}")

def selectColumns(data):
    
    try:
       
        df=pd.read_excel(data)
    
        df = df.dropna(axis=1, how="all")

        df = df.dropna(how="all")
                        
        porcentaje = len(df) * 0.90

        df = df [df.columns[df.isnull().sum() < porcentaje]]

        #NULOS POR COLUMNAS-----------!!!!!!!!!!!!!!!

        lenn = len(df.columns) * 0.80

        df = df[df.isnull().sum(axis=1) < lenn]

        df = df.reset_index(drop = True)
        
        df.columns= df.iloc[0]
        
        df = df.drop(0)

        df = df.fillna("-")
        
        tabColumns, tabData=st.tabs(["Seleccion de Columnas", "Data"])    
            
        with tabColumns:   
                    
            st.markdown("#### Descarta columnas que no deseas visualizar")
            
            listaDescarte=[]
            
            for x in df.columns:  #RECORRIENDO LOS NOMBRES DE LAS COLUMNAS DEL DF
                
                check = st.checkbox(x, value = True, key = str(x))
                
                if check == False:
                        
                    listaDescarte.append(x)
                    
        with tabData:
            
            listaDf=[]
            
            botonData= st.button("Cargar Data")
            
            if botonData ==True:
            
                for a in df.columns:
                    
                    if a not in listaDescarte :
                    
                        listaDf.append(a)
                
            st.dataframe(df[listaDf])

            
            
    except Exception as error:
        
        st.write(error)


selectColumns("stock 14.xlsx")
