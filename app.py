# Import librairie
import streamlit as st 
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go


# Page configuration
st.set_page_config(
    page_title='Dashboard Getaround', 
    page_icon=None, 
    layout="wide", 
    initial_sidebar_state="collapsed", 
    menu_items=None)


# Custom style
st.write(
    """
    <style>
    [data-testid="stMetricDelta"] svg {
        display: none;
    }

    .st-emotion-cache-ocqkz7 {
        align-items: center;
    }

    [data-testid="stMetricDelta"], .st-emotion-cache-wnm74r, .e1i5pmia0 {
        color: darksalmon !important;
        font-size: .9rem !important;
    }

    h1 {
        font-size: 2.2rem;
        padding-bottom: 0;
    }

    h2 {
        font-size: 1.8rem;
    }

    h3 {
        position: relative;
        top: 50px;
        z-index: 1000;
        text-align: center;
        display: block;
        width: 100%;
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 600;
        font-size: .9rem;
    }

    div > div > .st-emotion-cache-183lzff, .exotz4b0 {
        position: relative;
        top: 80px;
        z-index: 1000;
        text-align: center;
        display: block;
        width: 100%;
        font-family: "Source Sans Pro", sans-serif;
        font-size: .85rem;
        color: rgba(250, 250, 250, 0.9);
    }

    .st-emotion-cache-z5fcl4 {
        padding-top: 1rem;
        padding-bottom: 6.5rem;
    }

    .st-emotion-cache-pe5sya > p, .e1nzilvr5 > p,
    .st-emotion-cache-pe5sya > ul > li > p, .e1nzilvr5 > ul > li > p {
        color: rgba(250, 250, 250, 0.8)
    }

    .st-emotion-cache-pe5sya > p > em, .e1nzilvr5 > p > em {
        color: rgba(250, 250, 250, 0.6);
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)


# Header banner
st.title('Tableau de bord')
st.markdown('---')


# PART 1 : 
# Introduction to general data

st.header('Données générales')
st.caption('*Toutes les locations*')

col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    st.metric("réservations", value=21309, delta='locations', delta_color='normal')
    st.metric("parc", value=8142, delta='voitures uniques', delta_color='normal')
    
with col2:
    st.metric("retards", value=9404, delta='soit 44%', delta_color='inverse')
    st.metric("annulations", value=3264, delta='soit 15%', delta_color='inverse')

with col3:
    st.metric("temps de retour", value=-46, delta='minutes', delta_color='inverse')
    st.metric("retard moyen", value=202, delta='minutes', delta_color='inverse')

with col4:
    st.metric("check-in mobile", value=17002, delta='soit 80%', delta_color='normal')
    st.metric("check-in connect", value=4307, delta='soit 20%', delta_color='normal')


# PART 2 : 
# Visualization & comparison

col1, col2, col3, col, col4, col5, col6 = st.columns([1.6, .2, 1.1, .2, 1.6, .2, 1.1])

with col1:
    st.subheader('Toutes les locations')
    y = [21309, 9404, 3264]
    x = ['nombre locations', 'rendues en retard', 'annulées']
    y_percent = [21309, '44%','15%']
    fig = go.Figure()
    fig.add_trace(go.Bar(
            x = x,
            y = y,
            name = 'toutes les locations',
            text = y_percent,
            textposition='auto',
            orientation = 'v',
            offsetgroup = 0,
            marker = dict(
                color = 'lightsalmon')
            ))
    fig.update_layout(height=400)
    fig.update_traces(textfont_size=15)
    st.plotly_chart(fig, use_container_width=True)

with col3:
    colors = ['lightskyblue', 'dodgerblue']
    labels = ['mobile','connect']
    values = [17002, 4307]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.1])])
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=15, title='Méthode ckeck-in',
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader('Locations avec un délai serré')
    y = [1841, 873, 229]
    x = ['nombre locations', 'rendues en retard', 'annulées']
    y_percent = [1841, '47%', '12%']
    fig = go.Figure()
    fig.add_trace(go.Bar(
            x = x,
            y = y,
            text = y_percent,
            textposition='auto',
            name = 'locations serrées',
            offsetgroup = 0,
            base = 0,
            orientation = 'v',
            marker = dict(
                color = 'salmon')
            ))
    fig.update_traces(textfont_size=15)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col6:
    labels = ['mobile','connect']
    values = [1028, 813] 
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.1])])
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=15, title='Méthode ckeck-in',
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    st.plotly_chart(fig, use_container_width=True)


# PARTIE 3 : 
# Tight rentals data

st.markdown('---')
st.header('Locations avec un délai serré')
st.caption('*Le délai accordé entre deux locations est inférieur à 12 heures*')

col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    st.metric("locations", value=1841, delta='9% du total', delta_color='normal')
    st.metric("voitures uniques", value=1087, delta='13% du total', delta_color='normal')
    
with col2:
    st.metric("retards", value=873, delta='soit 48%', delta_color='inverse')
    st.metric("annulations", value=229, delta='soit 12%', delta_color='inverse')

with col3:
    st.metric("temps de retour", value=23, delta='minutes', delta_color='normal')
    st.metric("retard moyen", value=1, delta='minute', delta_color='inverse')

with col4:
    st.metric("check-in mobile", value=1028, delta='soit 56%', delta_color='normal')
    st.metric("check-in connect", value=813, delta='soit 44%', delta_color='normal')


# PART 4 : 
# Tight rentals revenue

col0, col1, col2, col3, col4, col5, col6 = st.columns([.5,.1,.5,.1,.5,.1,.5])

with col0:
    st.subheader(':moneybag: Revenus générés')
    labels = ['tous','délai serré']
    values = [21309-7255, 7255]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.05])])
    fig.update_layout(height=310)
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=15,
                  marker=dict(colors=['pink', 'salmon'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader(':oncoming_automobile: Parc de voitures')
    labels = ['tous','délai serré']
    values = [8142-1087, 1087]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.05])])
    fig.update_layout(height=310)
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=12.5,
                  marker=dict(colors=['pink', 'salmon'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader(':birthday: Part des revenus')
    labels = ['tous','délai serré']
    values = [72, 28]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.05])])
    fig.update_layout(height=310)
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=15,
                  marker=dict(colors=['pink', 'salmon'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader(':key: Méthode check-in')
    labels = ['mobile','connect']
    values = [1028, 813]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.05])])
    fig.update_layout(height=310)
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=15,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    st.plotly_chart(fig, use_container_width=True)


col0, col1, col2, col3, col4, col5, col6 = st.columns([.5,.2,.5,.2,.5,.2,.5])
with col0:
    st.caption('Les loueurs ayant des locations serrées comptabilisent un total de 7255 locations tous types confondus, dont 1841 locations serrées.')
with col2:
    st.caption('Avec une flotte de 1087 voitures soit 13.35% de la flotte totale, ils réalisent 34% des locations soit plus du tiers.')
with col4:
    st.caption("En moyenne les locations serrées représentent 28% de leurs revenus. Pour certains loueurs cette part dépasse les 50% et peut atteindre jusqu'à 80%.")
with col6:
    st.caption("Comparativement au groupe total les locations serrées se font davantage sur des voiture Connect : 44% contre seulement 20% dans le groupe total.")


# PART 5 : 
# Threshold optimization

st.markdown('---')
st.header('Délai entre deux locations')

@st.cache_data
def load_data():
    data = pd.read_csv('src/data.csv')
    return data
data = load_data()

@st.cache_data
def load_impacting_delay():
    data = pd.read_csv('src/impacting_delay.csv')
    return data
df = load_impacting_delay()
impacting_delay = df[df['previous_delay_hours'] <= 12]

col0, col1 = st.columns([5,3])

with col0:
    st.subheader('Diminution des réservations suivant le délai')
    fig = px.bar(data, x='seuil_en_heure', y=['reservations','annulations'], barmode='group')
    fig.update_layout(bargap=0,
                 xaxis_title="délai en heure", 
                 yaxis_title="nombre",
                 height=600)
    fig.update_xaxes(tickangle=0,
                 tickmode = 'array',
                 tickvals = [i for i in range(0,13,1)],
                 ticktext = [i for i in range(0,13,1)])
    st.plotly_chart(fig, use_container_width=True)
    st.caption("""
        - Le nombre de réservations diminue rapidement au départ, puis à partir d'un délai de 5 heures il diminue moins vite. 
        
        - Définir un seuil à 5 heures permettrait de conserver 735 réservations et de descendre à moins de 100 annulations. Les revenus des loueurs concernés descendraient à 28.8% des revenus totaux.
        
        - Si l'on désire minimiser les pertes, définir un seuil à 2,5 heures permettrait de conserver 1000 réservations et d'avoir 140 annulations au lieu de 230. Les revenus des loueurs concernés seraient maintenus à 30% des revenus totaux.

        - Cependant on observe que la majorité des retards impactants se situent dans un délai de 0 à 4 heures. Par conséquent le seuil devrait être de **4 heures minimum**. Dans ce cas on conserverait 840 réservations (perte de 1000 réservations) et le nombre d'annulations descendrait à 110 contre 230. Les revenus des loueurs concernés seraient de 29.3% des revenus totaux.

        - Au-delà de 12 heures il n'y aurait plus de réservations à délai court. Les loueurs concernés ne représenteraient plus qu'un quart des revenus totaux alors qu'ils représentaient plus du tiers au départ.

        - Les réservations avec un délai court s'effectuant principalement avec des **voitures Connect**, il serait judicieux de tester la fonctionnalité sur ce type de véhicule en particulier.
    """)

with col1:
    st.subheader('Diminution des annulations suivant le délai')
    fig = px.area(data, x='seuil_en_heure', y=['annulations'])
    fig.update_layout(bargap=0,
                    xaxis_title="délai en heure", 
                    yaxis_title="nombre",
                    height=300)
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [i for i in range(0,13,1)],
                    ticktext = [i for i in range(0,13,1)])
    st.plotly_chart(fig, use_container_width=True)

with col1:
    reservations = ['1840', '1000', '840', '735', '0']
    annulations = ['230', '140', '110', '< 100', '0']
    part_revenus = ['34 %', '30,3 %', '29,3 %', '28,8 %', '25,4 %']
    delai = ['0 heure','2,5 heures', '4 heures', '5 heures', '12 heures']
    columns = ['délai', 'réservations', 'annulations', 'part revenus']
    threshold_df = pd.DataFrame(list(zip(delai, reservations, annulations, part_revenus)), columns=columns)
    st.table(threshold_df)

with col1:
    st.subheader('Distribution des retards impactants')
    fig = px.histogram(impacting_delay, x="previous_delay_hours", nbins=9, color_discrete_sequence=['indianred'])
    fig.update_layout(
            bargap=0,
            xaxis_title="retard en heure",
            yaxis_title="nombre", 
            height=360,
            xaxis = dict(
                tickmode = 'linear',
                tick0 = 0,
                dtick = 1
            )
    )
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [i for i in range(0,13,1)],
                    ticktext = [i for i in range(0,13,1)])
    st.plotly_chart(fig, use_container_width=True)
    

# Footer
st.text("""
   Application créée avec Streamlit ⭐ et déployée avec Heroku 💜 2024
""")