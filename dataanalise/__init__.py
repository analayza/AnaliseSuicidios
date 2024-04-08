import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def lerdados_continente():
    dados_continente = pd.read_csv(r'C:\Users\anala\Desktop\Faculdade\5° Período\PythonWeb\analiseSuicidio\dados\continente.csv',delimiter=';')
    return dados_continente

def lerdados_linha():
    dados_linha = pd.read_csv(r'C:\Users\anala\Desktop\Faculdade\5° Período\PythonWeb\analiseSuicidio\dados\dadospb.csv',delimiter=';')
    return dados_linha

def lerdados():
    dados = pd.read_csv(r'C:\Users\anala\Desktop\Faculdade\5° Período\PythonWeb\analiseSuicidio\dados\dataset.csv',delimiter=';')
    return dados

def exibir_grafico_continente(dados):
    fig = px.bar(dados, x='Continente', y='Porcentagem')
    return fig

def exibir_grafico_pais(dados):
    fig = px.pie(dados, values='suicidios', names='estado',title="Suicidios por estado em 2019")
    fig.update_layout(
        width=800,  # Defina a largura desejada
        height=600,  # Defina a altura desejada
    )
    return fig
def exibir_grafico_linhas_uf(dados):
    fig = px.line(dados, x='anos', y='suicidios')
    return fig
def exibircorrelacao(dados):
    dados.drop(columns=['estado'], inplace=True)
    fig = px.imshow(dados.corr())
    return fig