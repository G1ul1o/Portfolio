
from tool_functions.imports_ import *

st.set_page_config(
    page_title="Giulio_Garnier_portfolio",
    page_icon="👋",
)


st.title("About me")
st.write("Hey ! My name is Giulio Garnier I am actually 21 years old and I am in my fourth year at Efrei Paris, in the major Data Engeneering.")
st.write("As you can tell at my name I'm italian. One of my biggest passion isdoing sport and more particularly running, biking and swimming. I am actually prepraring the Marathon of Paris !")
st.write("I also finished the 20km of Paris and the half marathon of Montreal during my semester abroad, where I could study at Concordia University.")
st.write("Here is my Curiculum that resume a lot of my career so far. If my profil draws your attention feel free to contact me with the links at the end of this page.")


cv_path = r"..\CV_validé_30-08-2024.pdf"

with open(cv_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name="Resume.pdf",
        mime="application/octet-stream",
    )



pdf_viewer(cv_path)

Contact = {
    "LinkedIn": "https://www.linkedin.com/in/giulio-garnier-66ab03221/",
    "GitHub": "https://github.com/G1ul1o",
    
}

cols = st.columns(len(Contact))
for index, (platform, link) in enumerate(Contact.items()):
    cols[index].write(f"[{platform}]({link})")
