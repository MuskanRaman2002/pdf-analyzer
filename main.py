import streamlit as st
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from sqlalchemy.orm import sessionmaker
from files import FILE
from sqlalchemy import create_engine

engine=create_engine('sqlite:///file_db.sqlite3')
Session=sessionmaker(bind=engine)
sess=Session()



st.set_page_config(
    page_title="PDF Analyzer",
    layout='wide',
    initial_sidebar_state='collapsed'
)

def extract_text(doc):

    output_string = StringIO()
    with open(doc, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return output_string

st.sidebar.title("PDF Analyser")
menu_options=['Upload PDF files','View Uploaded file']
menu_choice = st.sidebar.radio("select an option",menu_options)

if menu_choice == menu_options[0]:
    
    st.header("📄 Upload PDF files")
    data = st.file_uploader("upload a pdf")
    
    submit=st.button("UPLOAD")


    if data and submit:
        try:
            # data=FILE(file_name=data)
            # sess.add(data)
            # sess.commit()
            st.write("We got the File")
            

        except:
            st.write("There was an error")
        
        out=extract_text(data)
        val= data.getvalue()
        st.write(val)

if menu_choice == menu_options[1]:

    st.header("👁 View PDF files")
    

