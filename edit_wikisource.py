# -*- coding: utf-8 -*-

"""
    A partir de um arquivos wikisource.xlsx edita ou cria as páginas no Wikisource.
    O arquivo deve conter as colunas:
        title: com os títluos das páginas, incluindo o domínio
        text: com o wikitext a ser inserido na página

    Para configurações de login edite user_config.py
"""

import random
import pandas as pd
from time import sleep
from edit_wikimedia import edit

df = pd.read_excel('wikisource.xlsx')
n = len(df)
i = 0
for line in range(n):
    title = df['title'].iloc[i]
    text = df['text'].iloc[i]
    data = edit(title, text, project='wikisource')
    time = round(random.uniform(27, 143), 2)
    i += 1
    print(f'{i} de {n}: Aguarde {time/60:.2} minutos')
    sleep(time)
