
import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt 


#######################
# Configurações gerais da página
st.set_page_config(
    page_title="Marvel",
    page_icon=":superhero:",
    layout="wide",
    initial_sidebar_state="expanded")

#######################
# Estilização CSS 
# Crie o seu arquivo .css
with open('style.css', 'r') as fp:
    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

#######################
# Carregamento de dados com Pandas
df_marvel_full = pd.read_csv('Data/Marvel Movies.csv')
df_valores = pd.read_csv('Data/Custo_Lucro.csv')
# Filtragem de dados
df_marvel_filme_lucro = df_marvel_full[['Filmes','Ganho de bilheteria','Lucro']]
df_selected_lucro_sorted = df_marvel_filme_lucro.sort_values(by="Ganho de bilheteria", ascending=False)     
#######################
# Sidebar (barra lateral)
with st.sidebar:
    st.title(':superhero: Filmes da marvel')
    series_list = list(df_valores.Filmes.unique())[::-1]

    selected_series = st.selectbox('Selecione um Filme', series_list)
    df_selected_series = df_valores[df_valores.Filmes == selected_series]
    df_marvel_full_selected = df_marvel_full[df_marvel_full.Filmes == selected_series]
    


    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

#Filtragem de dados pos select box
crit=int(df_selected_series["critics score"].dropna(how=all))
aud=int(df_selected_series["audience score"].dropna(how=all))
Delta_semana=(df_marvel_full_selected['1st vs 2nd weekend drop off'].dropna(how=all))



#######################
# Criando Plots
# crie uma função para cada gráfico
# a função deve retornar o objeto do gráfico.
# Use e abuse do Plotly!

def Format_Milion(num):
    return f'{num} M'

def graph_bar(df_input,input_x,input_y,input_color):
    graph_comparaçao = px.bar(df_input, x=input_x, y=input_y, color= input_color ,barmode='group' )
    return graph_comparaçao 


def make_donut(input_response, input_text, input_color):
  int(input_response)
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text


#######################
# Apresentando plots no painel 
# principal do dashboard 

# criando colunas e suas larguras
col = st.columns((3, 2.5 ,3), gap='large')

with col[0]:
    
    # Metric
    st.markdown("#### 1ª vs 2ª Semana")
    st.metric(label="Semana de abertura", value=Format_Milion(df_marvel_full_selected['opening weekend'].iloc[0]))
    
    st.metric(label="Segunda Semana", value=Format_Milion(df_marvel_full_selected["second weekend"].iloc[0]), 
              delta=df_marvel_full_selected['1st vs 2nd weekend drop off'].iloc[0])
    
    # Grafico de Barras
    st.markdown('#### Lucro/Custo')
    p1 = graph_bar(df_selected_series,"Filmes","Valor em (m$)","Lucro/Custo")
    st.plotly_chart(p1, use_container_width=True)

with col[1]:

    # Imagem Banner
    st.markdown("#### Filme")
    st.image(df_selected_series['Imagens'].values[0], use_column_width=True, output_format='JPEG',)
    
    # Grafico de donut
    st.markdown('#### Notas')
    aud = make_donut(aud,"críticos","blue")
    crit = make_donut(crit,"audiência","orange")
    notas_col = st.columns((5, 5))
    with notas_col[0]:
        st.write('Audiência')
        st.altair_chart(aud)
    with notas_col[1]:   
        st.write('Críticos')
        st.altair_chart(crit)

with col[2]:
    # Data frame de Lucro Geral
    st.markdown('#### Lucro Geral')
    st.dataframe (df_selected_lucro_sorted, 
                  column_order=("Filmes", "Ganho de bilheteria","Lucro"),
                  hide_index=True,
                  width=None,
                  column_config={
                    "Ganho de bilheteria": st.column_config.TextColumn(
                        "Bilheteria (M)",
                    )})
    # Sobre
    with st.expander('Sobre', expanded=True):
        st.write('''
            - Data: [MARVEL Movies - Box Office Data]( https://www.kaggle.com/datasets/jainaru/marvel-movies-box-office-data).
            - :orange[**Lucro/Custo**]: O grafico Mostra o Valor que foi gasto para realizar o filme e quando arrecadou de volta .
            - :orange[**Notas**]: A porcentagem em media da nota da audiencia e dos criticos .
            - :orange[**1ª vs 2ª Semana**]: O delta nesse topico representa a porcentagem de ganho que foi perdido entre a primeira e a segunda semana.
            ''')