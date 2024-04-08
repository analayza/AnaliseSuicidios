from flask import *
import plotly.express as px
import dao
import dataanalise as da

app = Flask(__name__)

@app.route('/paginainicial')
def exibir_grafico_continente():
    dados_continente = da.lerdados_continente()

    dados_continente.sort_values(by=['Porcentagem'], ascending=False, inplace=True)
    fig = da.exibir_grafico_continente(dados_continente)
    return render_template('paginainicial.html', fig=fig.to_html())

@app.route('/pais', methods=["POST", "GET"])
def exibir_grafico_pais():
    dados_pais = da.lerdados()

    if request.method == 'POST':
        filtro = int(request.form.get('valor'))
        if filtro > 0:
            dados_pais = dados_pais.sort_values(by=['suicidios'], ascending=False).head(filtro)

    fig = da.exibir_grafico_pais(dados_pais)
    return render_template('pais.html', figpais=fig.to_html())



@app.route('/estado')
def exibir_grafico_linhauf():
    dados_uf = da.lerdados_linha()
    fig=da.exibir_grafico_linhas_uf(dados_uf)
    return render_template('estado.html', figpb=fig.to_html())

@app.route('/correlacao')
def gerarcorrelacao():
    dados = da.lerdados()
    fig = da.exibircorrelacao(dados)
    return render_template('correlacao.html', figmapa=fig.to_html())

@app.route('/salvarcorrelacao', methods=['POST'])
def salvarcorrelacao():
    dados = da.lerdados()
    if 'submitSP' in request.form:
        correlacao = dados['suicidios'].corr(dados['pib'])
        if dao.insert_correlacao(dao.conectardb(), 'pib', correlacao):
            return f"Correlação Suicídio x PIB salva com sucesso! {correlacao} "
        else:
            return "Sem Conexão com o banco de dados"
    elif 'submitSI' in request.form:
        correlacao = dados['suicidios'].corr(dados['idh'])
        if dao.insert_correlacao(dao.conectardb(), 'idh', correlacao):
            return f"Correlação Suicídio x IDH salva com sucesso! {correlacao}"
        else:
            return "Sem Conexão com o banco de dados"
    elif 'submitSID' in request.form:
        correlacao = dados['suicidios'].corr(dados['ideb'])
        if dao.insert_correlacao(dao.conectardb(), 'ideb', correlacao):
            return f"Correlação Suicídio x IDEB salva com sucesso! {correlacao}"
        else:
            return "Sem Conexão com o banco de dados"


@app.route('/prevencao')
def prevencao():
    return render_template('prevencao.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    email = str(request.form.get('email'))
    senha = str(request.form.get('senha'))

    if dao.login(email, senha, dao.conectardb()):
        return redirect(url_for('exibir_grafico_continente'))
    else:
        return render_template('login.html')


@app.route('/cadastrarusuario', methods=['GET', 'POST'])
def redirecionarcadastro():
    if request.method == 'GET':
        return render_template('cadastrarusuario.html')
    elif request.method == 'POST':
        email = str(request.form.get('email'))
        senha = str(request.form.get('senha'))
        if dao.inserirusuer(email, senha, dao.conectardb()):
            return redirect(url_for('exibir_grafico_continente'))
        else:
            texto= 'Email já cadastrado'
            return render_template('cadastrarusuario.html', msg=texto)


@app.route('/')
def suicidio():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

