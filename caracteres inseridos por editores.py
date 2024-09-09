# -*- coding: utf-8 -*-
import requests


def obter_contribuidores(artigo):
    # URL da API da Wikipedia para obter informações sobre um artigo, incluindo contribuidores
    url = f"https://pt.wikipedia.org/w/api.php?action=query&format=json&titles={artigo}&prop=revisions&rvprop=ids|user&rvlimit=500"

    resposta = requests.get(url)
    dados = resposta.json()

    # Extrai informações sobre os contribuidores
    contribuidores = {}
    paginas = dados.get('query', {}).get('pages', {})
    for pagina_id, pagina_info in paginas.items():
        revisions = pagina_info.get('revisions', [])
        for revision in revisions:
            user = revision.get('user')
            user_id = revision.get('userid', 0)
            contribuidores[user_id] = user

    return contribuidores


def obter_quantidade_caracteres(artigo):
    # URL da API da Wikipedia para obter o conteúdo de uma revisão específica de um artigo
    url = f"https://pt.wikipedia.org/w/api.php?action=query&format=json&titles={artigo}&prop=revisions&rvprop=content"

    resposta = requests.get(url)
    dados = resposta.json()

    # Extrai o conteúdo da revisão
    paginas = dados.get('query', {}).get('pages', {})
    for pagina_id, pagina_info in paginas.items():
        revisions = pagina_info.get('revisions', [])
        for revision in revisions:
            conteudo = revision.get('*')

    quantidade_caracteres = len(conteudo)
    return quantidade_caracteres

# Exemplo de uso
artigo_wikipedia = "Dores do Rio Preto"
contribuidores = obter_contribuidores(artigo_wikipedia)

for user_id, user in contribuidores.items():
    quantidade_caracteres = obter_quantidade_caracteres(artigo_wikipedia)
    print(f"O contribuidor {user} (ID: {user_id}) inseriu {quantidade_caracteres} caracteres.")
