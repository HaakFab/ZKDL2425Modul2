#learn more about streamlit: https://docs.streamlit.io/

import streamlit as st
#import pyterrier as pt
import pickle
import os

#if not pt.java.started():
#    pt.java.init()

#INDEX_PATH = os.getcwd() + "/ai_index_mult/data.properties"
DATA_PATH =  os.getcwd() + "/ai_index_mult/ai_publications.pkl"

def init():
    #index = pt.IndexFactory.of(INDEX_PATH)
    #st.session_state["engine"] = pt.terrier.Retriever(index, wmodel="TF_IDF")
    st.session_state["data"] = pickle.load(open(DATA_PATH, "rb"))

def search(query):

    #res = st.session_state["engine"].search(query)
    res = pickle.load(open("./search_result.pkl", "rb"))
    fields_to_show = ['text', 'tags', 'url', 'author', 'description']

    for _, row in res.iterrows():

       
        score = round(row['score'], 2)

        sel_entry = st.session_state["data"][st.session_state["data"]['docno'] == row['docno']]
        if sel_entry.empty:
            continue 
        entry = sel_entry.iloc[0]

        for field in fields_to_show:
            if field == "text":
                st.title(entry[field])
            else:
                st.write(f"{field.capitalize()}: \t {entry[field]}")

        st.write(f"Score: {score}")
        st.divider()


if not "engine" in st.session_state:
    init()

query = st.sidebar.text_input("Query")
st.sidebar.button("Search", on_click=search, args=(query,))