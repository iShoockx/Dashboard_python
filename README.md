# :superhero: Dashboard de Filmes da Marvel
Este repositório contém um dashboard sobre Filmes da Marvel. Seu desenvolvimento é para fins didáticos, preechendo os recursos exigidos pelo Desafio Python do [Projeto Desenvolve](http://projetodesenvolve.com.br).

### Instruções de uso
Este projeto foi desenvolvido usando a versão 3.12.3 do Python. Para execução do script, além da instalação do Python, se certifique que as dependências (em `requerimentos.txt`) foram devidamente instaladas. <br>
O dashboard pode ser executado através do seguinte comando no terminal:
```
streamlit run dash.py
```
A execução iniciará o servidor local do Streamlit e abrirá o dashboard no seu navegador padrão.

### Estrutura do Projeto
| Arquivo   | Descrição |
| :-------- | :------- |
| `dash.py`  | Este é o arquivo principal do projeto. Ele contém as funcionalidades do dashboard, entre elas a manipulação de dados com Pandas, criação das visualizações com Plotly, e manipulação de widgets do Streamlit.    |
| `style.css` | A estilização de elementos com CSS. Note que o nome das classes está associada aos nomes de widgets do Streamlit |
| `Marvel Movies.csv e Custo_Lucro.csv`   | Base de dados utilizada no projeto. Maiores detalhes a seguir.   |

### Dados
O arquivo `Marvel Movies.csv` é uma base de dados de informaçoes sobre filme da Marvel, onde cada linha é a informaçao sobre um filme em especifico. Descreveremos a seguir apenas as colunas relevantes para o nosso painel.
* Categorias: Categoria de filme em que se encontra EX: (Thor:love in thunder e da categoria de filmes) do (Thor)
* Filmes: Os Filmes mostrados no dashboard .
* Ganho de bilheteria: O valor bruto ganho com a bilheteria do filme
* Lucro: A porcentagem de Lucro do filme .
* critics score: A porcentagem de nota que a critica deu para o filme.
* audience score: A porcentagem de nota que a audiencia deu para o filme.
* opening weekend: O valor de Bilheteria da primeira semana.
* second weekend: O valor de Bilheteria da segunda semana.
* 1st vs 2nd weekend drop off : A diferença do valor de Bilheteria da primeira pela segunda semana.

### Joao Vitor Moreira Silva 
Caso deseje saber mais sobre os meus Projetos <br>
🌐 [Visite Meu Github](https://github.com/iShoockx) <br>
>

### Referências
Este painel foi criado seguindo o tutorial do Asimov Academy: [É o fim do Power BI? Criando Dashboard com Python em 15 minutos](https://youtu.be/P6E_Kts9pxE?si=6ZU2ilvVCR-Af_mW)
[Documentaçao do Strealit](https://docs.streamlit.io/)
[Documentaçao de Grafico do Plotly](https://plotly.com/python/)
[Documentaçao do Pandas](https://pandas.pydata.org/docs/)
[Introdução ao Pandas no Python - [SAIA DO ZERO EM 1 AULA]](https://www.youtube.com/watch?v=C0aj3FjN5e0&t=1396s)
