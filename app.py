from pathlib import Path
import streamlit as st
from PIL import Image

# --- usful functions ---
def table2(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def table3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
      col3, col4 = st.columns([1, 1])
      for i in b :
          c = i[0]
          d = i[1]
          with col3:
              st.text(c)
          with col4:
              st.markdown(d)

def txt(a, b):
  col1, col2 = st.columns([1,1])
  with col1:
    st.markdown(a)
  with col2:
    st.text(b)

def stage_edu(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.image(a, width=80)
  with col2:
      st.text(b[0])
      st.write(b[1])

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


INH_pic = "assets/FHC.png"
Enageo_pic = "assets/E.Na.Geo.jpg"
Crnd_pic = "assets/CRND.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Mokrani A. E."
PAGE_ICON = "assets/omar_logo.ico"
NAME = "Mokrani Amor Elmokhtar"
DESCRIPTION = """
`Geophysicist with a strong passion for leveraging Python and machine learning to enhance efficiency and effectiveness in geoscience applications.`
"""
EMAIL = "amomokelm@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/a-e-mokrani/",
    "GitHub": "https://github.com/omarmokrani97",
}
PROJECTS = {
    "🏆 SeisInsight-Synthetic 2D Seismic Section Generator": "https://github.com/omarmokrani97/SeisInsight-Synthetic-2D-Seismic-Section-Generator",
}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write("---")
table2(a='Geophysical methods',b='Master the research and exploration procedures (`Acquisition`, `Processing` and `Interpretation`) of different Geophysical methods (`Seismic`, `Gravimetric`, `Radiometric`, `Geomagnetic`, `Electrical`, and `Well Logging`).')
table2(a='Geology',b='Master the essential bases of (`General and Structural Geology`, `Geodynamics`, `Geodesy`).')
table2(a='Geophysical Software',b='`Geosoft Oasis Montaj`,`Global Mapper`,`Golden Software Surfer`,`ArcGIS`')
table3(a='Hard Skills',b=[['Programming:','`Python`'],
                          ['Data visualization:','`matplotlib`,`seaborn`'],
                          ['Machine Learning:','`scikit-learn`']])
table2(a='Soft Skills',b='`Ability to adapt`, `Teamwork`, `Sense of communication`, `Decision-making ability`, `Sense of organization`, `Rigor`, `Perseverance`, `Reactivity`.')


# --- EDUCATION HISTORY ---
st.write('\n')
st.subheader("EDUCATION")
st.write("---")

# --- Master
txt("Master’s degree in Petroleum Geophysics","Sep. 2019 – Sept. 2021")
stage_edu(a=INH_pic , b= ["University of M'hamed Bougara | Boumerdes, Algeria","Faculty of Hydrocarbons and Chemistry (FHC | ex : INH)"])

st.write('\n')

# --- Bachelor
txt("Bachelor’s degree in Geophysics","Sep. 2016 – juil. 2019")
stage_edu(a=INH_pic , b= ["University of M'hamed Bougara | Boumerdes, Algeria","Faculty of Hydrocarbons and Chemistry (FHC | ex : INH)"])


# --- INTERNSHIPS HISTORY ---
st.write('\n')
st.subheader("INTERNSHIPS")
st.write("---")

# --- INTERNSHIP 1
txt("C.R.N.D | Draria, Algiers, Algeria","Juin. 2021 – Sept. 2021 (4 Months)")
stage_edu(a=Crnd_pic , b= ["Draria Nuclear Research Center","Thesis title: `Analysis of the Aero-geophysical Information Acquired above the Tin Seririne Sedimentary Basin for the Delimitation of Potentially Favorable Perimeters for Uranium Research.`"])

st.write('\n')

# --- INTERNSHIP 2
txt("E.NA.GEO | Hassi Messaoud, Algeria","Jan. 2019 (1 Month)")
stage_edu(a=Enageo_pic , b= ["National Geophysical Company","`The purpose of this internship is to follow the different acquisition techniques used by E.NA.GEO, and to understand the structure of a seismic mission and these different teams, as well as the relationship between them.`"])
st.write('\n')

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
