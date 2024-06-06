
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
alt.themes.enable("dark")

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
df_sort_lucro = df_marvel_full[['Filmes','Lucro','Ano']].sort_values(by="Lucro", ascending=True)
#######################
# Sidebar (barra lateral)
with st.sidebar:
    st.title(':superhero: Filmes da marvel')
    series_list = list(df_valores.Filmes.unique())[::-1]

    selected_series = st.selectbox('Selecione um Filme', series_list)
    df_selected_series = df_valores[df_valores.Filmes == selected_series]
    df_marvel_full_selected = df_marvel_full[df_marvel_full.Filmes == selected_series]
    
    
    category_list = list(df_valores.category.unique())[::-1]
    
    selected_color_theme = st.selectbox('Selecione o Tema',category_list )
    st.write("Joao Vitor Moreira Silva/PDITA:079")
    

#######################
# Criando Plots
# crie uma função para cada gráfico
# a função deve retornar o objeto do gráfico.
# Use e abuse do Plotly!

def Format_Milion(num):# Funçao para formatar valor para milhao
    return f'{num} M'

def graph_bar(df_input,input_x,input_y,input_color,Color_select,input_barmode):# Grafico de Barra
    chart_color = escolha_cor(Color_select)
   
    fig = px.bar(df_input, x=input_x, y=input_y, color= input_color ,barmode=input_barmode,height=500,color_discrete_sequence=chart_color )
    return fig

def escolha_cor(Cor):#Funçao de definiçao de Cor da Select theme
    if Cor == 'Deadpool':
      chart_color = ['#A32633','#60262C']
    elif Cor == 'Deadpool 2':
      chart_color = ['#962333','#343339']

    if Cor == 'The Marvels':
      chart_color = ['#3969CD','#1E376B']
    elif Cor == 'The Marvels 2':
      chart_color = ['#FFFC50','#B3B138']    
    
    if Cor == 'Thor':
      chart_color = ['#537DA3','#A0B4BD']
    elif Cor == "Thor 2" :
      chart_color = ['#B11F06','#415C5E']
    
    if Cor == 'Spider-Man':
      chart_color = ['#447BBE','#2B3784']
    elif Cor == 'Spider-Man 2':
      chart_color = ['#DF1F2D','#B11313']
    
    if Cor == 'Iron Man':
      chart_color = ['#AA0505','#FBCA03']
    elif Cor == 'Iron Man 2':
      chart_color = ['#4B0908','#B97D10']
    
    if Cor == 'Incredible Hulk':
      chart_color = ['#A2CD48','#875094']
    elif Cor == "Incredible Hulk 2":
       chart_color = ['#875094','#A2CD48']
    
    if Cor == 'Guardians':
      chart_color = ['#FDFAC3','#AB7D41']
    elif Cor == 'Guardians 2':
      chart_color = ['#529EE9','#13286B']
    
    if Cor == "Shang-Chi":
      chart_color = ['#FF7A36','#05B1C5']
    elif Cor == "Shang-Chi 2":
       chart_color = ["#05B1C5","#FF7A36"]
    
    if Cor == 'Eternals':
      chart_color = ['#035AA6','#211159']
    elif Cor == 'Eternals 2':
      chart_color = ['#98A632','#BF871F']
      
    if Cor == 'Dr Strange':
      chart_color = ['#2FD93B','#03223F']
    elif Cor == 'Dr Strange 2':
      chart_color = ['#FF6312','#691821']
      
    if Cor == 'Captain Marvel':
      chart_color = ['#1C2351','#9E1C21']
    elif Cor == 'Captain Marvel 2':
      chart_color = ['#EACF40','#E9AE2C']
    
    if Cor == 'Black Widow':
      chart_color = ['#1C1C1C','#ff0000']
    elif Cor == 'Black Widow 2':
      chart_color = ['#ff0000','#1C1C1C']
      
    if Cor == 'Black Panther':
      chart_color = ['#1A0554','#C4A8FF']
    elif Cor == 'Black Panther 2':
      chart_color = ['#C4A8FF','#664EAE']
      
    if Cor == 'Avengers':
      chart_color = ['#a50000','#3268bd']
    elif Cor == 'Avengers 2':
      chart_color = ['#3268bd','#999999']
    
    if Cor == 'Avengers: Age of Ultron':
      chart_color = ['#C72523','#4D1518']
    elif Cor == 'Avengers: Age of Ultron 2':
      chart_color = ['#4D8AB5','#1E2639']
      
    if Cor == 'Avengers: Infinity War':
      chart_color = ['#924F9E','#626EDA']
    elif Cor == 'Avengers: Infinity War 2':
      chart_color = ['#D93D27','#361A29']

    if Cor == 'Avengers: End Game':
      chart_color = ['#7B6FDE','#453AA4']
    elif Cor == 'Avengers: End Game 2':
      chart_color = ['#1A1A64','#0B0930']

    if Cor == 'Captain America':
      chart_color = ['#1849CA','#EC2004']
    elif Cor == 'Captain America 2':
      chart_color = ['#C31D10','#162CA2']

    if Cor == 'Ant-Man':
      chart_color = ['#D30026','#9D152C']
    if Cor == 'Ant-Man 2':
      chart_color = ['#868A93','#5E6674']
    
    return chart_color


def make_donut(input_response, input_text, input_color):#Grafico de donut
  # Escolha de cores
  chart_color = escolha_cor(input_color)
    # Criaçao da lista utilizada para o grafico
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode( #Criação do Grafico de donut
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    # Formataçao do Texto do Grafico
  text = plot.mark_text(align='center', color="#29b5e8", font="sans serif", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # select color theme
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text


#######################
# Apresentando plots no painel 
# principal do dashboard 

# criando colunas e suas larguras
col = st.columns((2.5, 2.5 ,3), gap='medium')
cols1 = st.columns((5, 5))
cols2 = st.columns((1,8,1))
# Primeira coluna
if selected_series == "Marvel":
  cols3 = st.columns((1,1))
   #Criando Colunas
  with cols3[0]:
      chart_color = escolha_cor(selected_color_theme)#Secect Color
      #Organizaçao de Dados
      media_open = round(df_marvel_full['opening weekend'].mean())
      media_sec = round(df_marvel_full['second weekend'].mean())
      media_diference = round((media_sec/media_open)*100)-100
      st.markdown("#### Media 1ª :crossed_swords: 2ª Semana")
      # Metrics
      st.metric(label="Semana de abertura", value=Format_Milion(media_open))
      st.metric(label="Semana de abertura", value=Format_Milion(media_sec), delta=f'{media_diference} %')
      
      #
      st.markdown('#### Audiencia e Critica dos filmes')
      #Dicionario para organizaçao de dados
      scatter = {
        "x":[df_marvel_full["critics score"],df_marvel_full["Filmes"]],
        "y":[df_marvel_full["audience score"],df_marvel_full["Filmes"]]
      }
      #Grafico Scatter
      fig = px.scatter(df_marvel_full, x=df_marvel_full["critics score"],y=df_marvel_full["audience score"],color=df_marvel_full["Filmes"] ,color_discrete_sequence=chart_color)
      st.plotly_chart(fig, use_container_width=True)
  with cols3[1]:
      #Data Frame
      st.markdown('#### Lucro Geral')
      st.dataframe (df_selected_lucro_sorted, 
                  column_order=("Filmes", "Ganho de bilheteria","Lucro"),
                  hide_index=True,
                  width=None,
                  column_config={
                    "Ganho de bilheteria": st.column_config.TextColumn(
                        "Bilheteria (M)",
                    )})
        
      
      #Grafico Donut
      st.markdown("Media")
      aud2 = make_donut(int(df_valores["critics score"].mean()),"críticos",selected_color_theme)
      crit2 = make_donut(int(df_valores["audience score"].mean()),"audiência",f'{selected_color_theme} 2')
      cols4= st.columns((2,4,4))
      with cols4[1]:
          st.write('Audiência')
          st.altair_chart(aud2)
      with cols4[2]:   
          st.write('Críticos')
          st.altair_chart(crit2)
    
else:
  with col[0]:

    # Metricas
    st.markdown("#### 1ª :crossed_swords: 2ª Semana")
    st.metric(label="Semana de abertura", value=Format_Milion(df_marvel_full_selected['opening weekend'].iloc[0]))
    st.metric(label="Segunda Semana", value=Format_Milion(df_marvel_full_selected["second weekend"].iloc[0]), 
        delta=df_marvel_full_selected['1st vs 2nd weekend drop off'].iloc[0])
    
    # Grafico de Barras
    st.markdown('#### Lucro/Custo')
    Graph = graph_bar(df_selected_series,"Filmes","Valor em (m$)","Lucro/Custo",selected_color_theme,"group")# Chamada do plot de Grafico de Barra
    st.plotly_chart(Graph, use_container_width=True)
  

# Segunda Coluna 

  with col[1]:
      st.markdown("#### Filme")
      cols2 = st.columns((1,8,1))
      with cols2[1]:
        # Imagem Banner
          st.image(df_selected_series['Imagens'].values[0], width=200, output_format='JPEG')

    # Grafico de donut
      st.markdown('#### Notas')
      aud = make_donut(int(df_selected_series["critics score"].iloc[0]),"críticos",selected_color_theme)
    
      crit = make_donut(int(df_selected_series["audience score"].iloc[0]),"audiência",f'{selected_color_theme} 2')
      cols1 = st.columns((5, 5))
      with cols1[0]:
          st.write('Audiência')
          st.altair_chart(aud)
      with cols1[1]:   
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
            - Data: [MARVEL Movies - Box Office Data](https://github.com/iShoockx/Dashboard_python/tree/main/Data).
            - :orange[**Lucro/Custo**]: O grafico Mostra o Valor que foi gasto para realizar o filme e quando arrecadou de volta .
            - :orange[**Notas**]: A porcentagem em media da nota da audiencia e dos criticos .
            - :orange[**1ª vs 2ª Semana**]: O delta nesse topico representa a porcentagem de ganho que foi perdido entre a primeira e a segunda semana.
            ''')