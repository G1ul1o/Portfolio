
from tool_functions.imports_ import *

# librairie utilisé voir import + missingno + io (for the data.info the output is printed to sys.stdout)

@st.cache_data
def load_data():
    data = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/b8703c69-a18f-46ab-9e7f-3a8368dcb891",delimiter =';',low_memory=False,header=0)
    data_election = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/52a11762-45b4-414f-b6a2-eaa290217dc6",delimiter =';',low_memory=False,header=0)
    data_copy = data.copy()
    data_election_copy = data_election.copy()
    return data_copy,data_election_copy

@st.cache_data
def preprocessing(data_copy):
   
    st.write("Let's see have a quick look of our dataset")
    
    st.write(data_copy.head(10))
    
    st.write("Before choosing wich column we want to keep let's etablish how much data is missing from our dataset and wich columns are not good to keep")
    f=msno.bar(data_copy)
        
    st.pyplot(f.figure)
    
    
    st.write("""Here a small description of all the columns.
1. **Nuls**: Number of invalid (null) votes.
2. **Blancs**: Number of blank votes.
3. **Votants**: Total number of voters who participated.
4. **Inscrits**: Total number of registered voters.
5. **% Abs/Ins**: Percentage of abstentions relative to registered voters.
6. **% Exp/Ins**: Percentage of valid votes relative to registered voters.
7. **% Exp/Vot**: Percentage of valid votes relative to voters.
8. **% Vot/Ins**: Percentage of voters relative to registered voters.
9. **Exprimés**: Number of valid votes.
10. **% Nuls/Ins**: Percentage of null votes relative to registered voters.
11. **% Nuls/Vot**: Percentage of null votes relative to voters.
12. **Abstentions**: Number of abstentions.
13. **id_election**: Unique identifier for the election.
14. **% Blancs/Ins**: Percentage of blank votes relative to registered voters.
15. **% Blancs/Vot**: Percentage of blank votes relative to voters.
16. **id_brut_miom**: Unique identifier for the raw data entry.
17. **Code du b.vote**: Code for the type of voting ballot.
18. **Code du canton**: Code for the canton (district) where the vote took place.
19. **Code de la commune**: Code for the municipality.
20. **Libellé du canton**: Name of the canton (district).
21. **Code du département**: Code for the department (administrative region).
22. **Libellé de la commune**: Name of the municipality.
23. **Libellé du département**: Name of the department.
24. **Code de la circonscription**: Code for the electoral constituency.
25. **Libellé de la circonscription**: Name of the electoral constituency.
""")

    st.write("Let's see the differents types of the columns to see if they are errors")
    
    buffer = io.StringIO()
    data_copy.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.markdown("Let's convert the Blancs vote in int because you can't have a half vote but before that we need to fill it of 0 when there isn't any value")

    data_copy['Blancs']=data_copy['Blancs'].fillna(0.0)
    data_copy['Blancs']=data_copy['Blancs'].astype(int)

    st.write("The result:")    
    buffer = io.StringIO()
    data_copy.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)


    st.markdown("Let's see a a overview of the different numerical columns (Inscrits,Abstentions,Nuls,Exprimés)")

    data_numerical = data_copy[["Inscrits","Abstentions","Nuls","Exprimés"]]
    st.write(data_numerical.describe())

    st.markdown("Let's drop some of the columns that we will not use because they miss to much value or they don't have any important information")
    
    data_copy = data_copy.drop(columns=["Libellé du département","Code de la circonscription","Code du canton","% Abs/Ins","% Blancs/Ins","% Blancs/Vot","% Vot/Ins","% Nuls/Ins","% Nuls/Vot","% Exp/Ins","% Exp/Vot","Libellé de la circonscription","Libellé du canton"])
    
    st.markdown("We will drop **Libellé du département**, **Code de la circonscription** ,**Code du canton**,**% Abs/Ins**,**% Blancs/Ins**,**% Blancs/Vot**,**% Vot/Ins**,**% Nuls/Ins**,**% Nuls/Vot**,**% Exp/Ins**,**% Exp/Vot**,**Libellé de la circonscription**,**Libellé du canton**")
    st.markdown("Here a little recap of the dataset that we have")
    st.write(data_copy.head(10))

    st.markdown("Let's see what we have as different values in the column Id")
    st.write(data_copy['id_election'].unique())

    st.markdown("As we can see the ID contains a lot of info in fact we can see legi euro and pres, if it's a t1 or t2 and for the last the year let's regroup this information into columns to adapt our study")
    
    data_copy[['année', 'occasion', 'tours']] = data_copy['id_election'].str.split('_', expand=True)
    
    st.write('Again a little recap')
    st.write(data_copy.head(10))

    st.markdown("Let's now see a pie of the votant and abstentions in all the France, for that you need to choose the year and the occasion of the vote")

    return data_copy

@st.cache_data
def preprocessing_elections(data_copy_election):
    

    st.write("Here is a new dataset with wich will work with")
    st.write(data_copy_election.head(10))
    
    st.write("Again here his a short explanation of the different columns")
    st.write("""
1. **id_election**: Unique identifier for the election.
2. **id_brut_miom**: Unique identifier for the raw data entry.
3. **code du département**: Code for the department (administrative region).
4. **code de la commune**: Code for the municipality.
5. **code du b.vote**: Code for the type of voting ballot.
6. **N°Panneau**: Number of the panel where the list or candidate is displayed.
7. **Libellé Abrégé Liste**: Abbreviated name of the political list or party.
8. **Libellé Etendu Liste**: Full name of the political list or party.
9. **Nom Tête de Liste**: Name of the lead candidate (head of the list).
10. **Voix**: Number of votes received.
11. **% Voix/Ins**: Percentage of votes received relative to registered voters.
12. **% Voix/Exp**: Percentage of votes received relative to valid (expressed) votes.
13. **Sexe**: Gender of the candidate.
14. **Nom**: Last name of the candidate.
15. **Prénom**: First name of the candidate.
16. **Nuance**: Political shade or affiliation (party lean).
17. **Binôme**: Indicates if the candidate is part of a pair (used in certain elections).
18. **Liste**: The political list or group to which the candidate belongs.
""")
    
    st.write("Let's try to see how much data is missing from our dataset")
    f=msno.bar(data_copy_election)
    
    f.legend().set_visible(False) #taken off the legend
    
    st.pyplot(f.figure)
    
    #to show the info of the dataset
    buffer = io.StringIO()
    data_copy_election.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    
    st.write("Again the id is a real good source of information")
    st.write("As you can see some errors are in dataset so we need to correct them")
    data_copy_election[['année', 'occasion', 'tours']] = data_copy_election['id_election'].str.split('_', expand=True)
    
    data_copy_election = data_copy_election[data_copy_election["Nuance"]!="M"]
    
    data_copy_election = data_copy_election[data_copy_election["Nuance"]!="nan"]
    
    data_copy_election.loc[data_copy_election['Nuance'] == "2", 'Nuance'] = data_copy_election['Sexe']
    
    data_copy_election.dropna(subset=['Nuance'], inplace=True)
    
    
    return data_copy_election

    
def plot_tab(char):
    fig_7, ax_7 = plt.subplots(figsize=(10, 6))

    
    df_tab = data_copy[data_copy["occasion"] == char]

    
    df_tab = df_tab.groupby('année')[['Votants', 'Abstentions', 'Blancs', 'Nuls']].sum().reset_index()

    
    df_tab.set_index('année', inplace=True)

  
    df_tab.plot(kind='bar', stacked=True, ax=ax_7, color=['royalblue', 'orange', 'lightgreen', 'red'])

    
    ax_7.set_title("Comparison of the number of votes for {char} votes")
    ax_7.set_xlabel("Année")
    ax_7.set_ylabel("Nombre de votes")
    ax_7.set_xticks(range(len(df_tab.index)))
    ax_7.set_xticklabels(df_tab.index, rotation=0)

    
    st.pyplot(fig_7)

def plot_tab_parties(char):
    
    
    df_tab_election = data_election_copy[data_election_copy["occasion"] == char]
    years_pos = df_tab_election["année"].unique()
    
    year = st.select_slider(
         'Select a year',
         options=  years_pos
         )
    
    
    
    df_tab_election = df_tab_election[data_election_copy["année"] == year]
    
    if not df_tab_election.empty:
        
        data_election_grouped_copy = df_tab_election.groupby('Nuance')["Voix"].sum().reset_index()
    
        # Préparer les données pour le plot
        data_election_group_plot = data_election_grouped_copy[["Nuance", "Voix"]]
    
        # Créer le plot
        fig, ax = plt.subplots(figsize=(10, 6))
    
        # Utiliser une palette de couleurs automatiquement générée par matplotlib
        data_election_group_plot.plot(
            kind='bar',
            x='Nuance', 
            y='Voix',
            ax=ax, 
            colormap='tab10'  # Palette de couleurs automatique
        )
    
        # Titre et labels
        plt.title('Number of Votes by Political Nuance in 2019 Euro Elections')
        plt.xlabel('Political Nuance')
        plt.ylabel('Number of Votes')
    
        # Rotation des étiquettes sur l'axe X pour lisibilité
        plt.xticks(rotation=45)  # Rotation si nécessaire
        plt.tight_layout()  # Ajuster le layout pour éviter les chevauchements
        
        # Afficher le plot dans Streamlit
        st.pyplot(fig)
    else:
        st.write("No data available for the euro 2019 election.")


def plot_dept(code_dep):
    
    data_sorted = data_copy[data_copy["Code du département"] == code_dep]
    data_sorted = data_sorted.groupby('année')[['Votants', 'Abstentions']].sum().reset_index() #to keep the year
   

    fig = px.scatter(data_sorted,x='année',y=['Votants', 'Abstentions'],labels={'value': 'Nombre', 'variable': 'Type'},title='Votants et Abstentions par Année')
    fig.update_traces(mode='lines+markers')
    st.plotly_chart(fig,use_container_width=True,on_select="rerun",key="line_compare")

    


st.title("Study on elections datasets")
st.subheader("by Giulio Garnier")

st.write("If you followed the 2024 legislative elections, you also worried by the abstention rate and also the changes in the French political sphere.")
st.write("Many people accuse growth of abstention rate saying that he was never greater that before. For other the rise of the \"extrême droite\" was a surprise. Here we will propose to see what are the real state of this two hypothesis.")
st.markdown("First hypothesis : __The abstention are higher than the last times__")
st.markdown("Second hypothesis : __This changes just begins in the recent years__")
st.write("Thanks to this interactive graph we will see wich of this statement are true")
#data_copy,data_election_copy = load_data()


data_copy=preprocessing(data_copy)

st.write("Those pie are interractive so you need to select the occasion, the date and the event to saw those")
occasions = data_copy['occasion'].unique()
chose_occasion = st.selectbox('Wich occasions do you want ?',occasions)

years = data_copy[data_copy["occasion"]==chose_occasion]['année'].unique() #chose de year in the data where there is this occasion


chose_years = st.selectbox('Wich year do you want ?',years)

tour = st.radio('Select tour:', data_copy[data_copy["occasion"]==chose_occasion]['tours'].unique())

data_filtered = data_copy[(data_copy["année"]==chose_years) & (data_copy["occasion"]==chose_occasion) & (data_copy["tours"]==tour)]

overall_vote = data_filtered[['Votants', 'Abstentions']].sum()

fig, ax = plt.subplots()
ax.pie(overall_vote, labels=overall_vote.index, autopct='%1.1f%%', startangle=90) #autopct to show the pourcentage
plt.title(f"Distribution of votes ({chose_occasion}, {chose_years},{tour})")
plt.axis('equal')

st.pyplot(fig)

overall_view_vote = data_filtered[['Exprimés', 'Blancs',"Nuls"]].sum()
fig_3, ax_3 = plt.subplots()
ax_3.pie(overall_view_vote, startangle=90) #autopct to show the pourcentage
ax_3.legend(overall_view_vote.index, title="Vote Categories", loc="best", fontsize='small')
plt.title("Distribution in the votes")


st.pyplot(fig_3)


st.markdown("As we can see there is a large proportion of the population does not vote. Going from at least 30% up to 60% depending on the occasion. But let's confirm it with a other graph")


euro_tab, legislative_tab,department_tab,presidential_tab,municipal_tab,regional_tab,canton_tab = st.tabs(["Europe Vote",
                                                                                   "Legislative Vote",
                                                                                   "Department Vote",
                                                                                   "Presidential Vote",
                                                                                   "Municipal Vote",
                                                                                   "Regional Vote",
                                                                                   "Canton Vote"])

with euro_tab:
    plot_tab("euro")

with legislative_tab:
    plot_tab("legi")
    

with department_tab:
    plot_tab("dpmt")

    
with presidential_tab:
    plot_tab("pres")


with municipal_tab:
    plot_tab("muni")
    

with regional_tab:
    plot_tab("regi")

with canton_tab:
    plot_tab("cant")

st.markdown("Thanks to this bar graph we can clearly see that in the majority of the events we have less and less votes, people who goes to vote. But is it in the totality of France ? Let's try to see how many votes dept by dept")


code_dept = data_copy['Code du département'].unique()
code_dept_choose = st.selectbox('Wich dept do you want ?',code_dept)

plot_dept(code_dept_choose)

st.write("As we can see this movement of non-voters his not in all France but begin to spread little by little")
st.write("Sadly the first hypothesis his true. Let's to etablished if the second one is too")

data_election_copy = preprocessing_elections(data_election_copy)

st.dataframe(data_election_copy[data_election_copy["Voix"].isna()])

data_election_copy["Voix"].fillna(data_election_copy["% Voix/Ins"], inplace=True)

data_election_copy = data_election_copy.drop(columns=["id_brut_miom","% Voix/Ins","% Voix/Exp"])


euro_vote_tab, legislative_vote_tab,department_vote_tab,presidential_vote_tab,municipal_vote_tab,regional_vote_tab,canton_vote_tab = st.tabs(["Europe Vote",
                                                                                   "Legislative Vote",
                                                                                   "Department Vote",
                                                                                   "Presidential Vote",
                                                                                   "Municipal Vote",
                                                                                   "Regional Vote",
                                                                                   "Canton Vote"])

with euro_vote_tab:
    plot_tab_parties("euro")

with legislative_vote_tab:
    plot_tab_parties("legi")

with department_vote_tab:
    plot_tab_parties("dpmt")

with presidential_vote_tab:
    plot_tab_parties("pres")
    
with municipal_vote_tab:
    plot_tab_parties("muni")

with regional_vote_tab:
    plot_tab_parties("regi")

with canton_vote_tab:
    plot_tab_parties("cant")

st.write("If we analyse a little bit we can see that the \"droit\" mouvement have always had a certain power in France but nowadays they gain a lot of it.")
st.write("That conclude my Study on those dataset thank you very much for reading until now !")

