import streamlit as st


Study_on_the_election_dataset = st.Page('Pages/1_📚Project_page.py',title="Study_on_the_election_dataset")

side_bar  = st.navigation({" ":[st.Page('Pages/1_Welcome_page.py', title='Dashboard',icon=":material/home:"),
                                st.Page('Pages/2_🙋About_me_pages.py',title='ABOUT ME')],
                          
                            "Projects": [Study_on_the_election_dataset]
                           })
side_bar.run()

