import os
import streamlit as st
from sqlalchemy.orm import sessionmaker
from files import UserInput
from sqlalchemy import create_engine

#new
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

#new
def text_extract(docName):
    out= StringIO()

    with open (f'D:\Tasks\PDF_Analyzer\static\{docName}','rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rmanager=PDFResourceManager()
        device = TextConverter(rmanager, out, laparams=LAParams())
        interperter= PDFPageInterpreter(rmanager, device)
        for page in PDFPage.create_pages(doc):
            interperter.process_page(page)

    return out.getvalue()

#connecting database
engine=create_engine('sqlite:///file_db.sqlite3')
Session=sessionmaker(bind=engine)
sess=Session()

#save the files given by user at 'UploadedFiles' folder
def save_uploaded_doc(uploadedDoc):
    with open (os.path.join('UploadedFiles',uploadedDoc.name),'wb')as f:
        f.write(uploadedDoc.getbuffer())
    return True 

st.set_page_config(
    page_title="PDF Analyzer",
    layout='wide',
    initial_sidebar_state='collapsed'
)


st.sidebar.title("PDF Analyser")
menu_options=['Upload PDF files','View Uploaded file']
menu_choice = st.sidebar.radio("select an option",menu_options)

if menu_choice == menu_options[0]:
    st.header("📄 Upload PDF files")
    doc=st.file_uploader("upload a pdf", type=['pdf'])
    submit=st.button("UPLOAD")


    if submit and doc is not None:
        doc_name=doc.name
        doc_size=doc.size
        if save_uploaded_doc(doc):
            path = f'C:\\Users\\AICT\\Documents\\pdf analyzer\\UploadedFiles\\{doc_name}' 
        try:
            upload=UserInput(name=doc_name, size=doc_size, location=path)
            sess.add(upload)
            sess.commit()
            st.success("We got the File")
            

        except Exception as e:
            st.error(f"Error has occured : {e}")

if menu_choice == menu_options[1]:

    st.header("👁 View PDF files")
    #new    
    if view:
        results=sess.query(UserInput).all()
        last_name= str(results[-1].name )
        output= text_extract(last_name)
        st.write(output)

