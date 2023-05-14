import os
import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "ACcfdf1e08b1dcb2c97092aa28792f2dc1"
# Your Auth Token from twilio.com/console
auth_token  = "562902d01c3c143c3ba14ed92effa595"
client = Client(account_sid, auth_token)

# passo a passo para solução

# abrir os 6 arquivos em Excel

aquivos = os.listdir(plan)

                     
listas_meses = (plan);
for mes in listas_meses:
    tabela_vendas =pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 ,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, alguem bateu a meta. Vendedor: {vendedor}, Valor: {vendas}')
        message = client.messages.create(
            to="+5511913184417", 
            from_="+16802198562",
            body=f'No mês de {mes}, alguem bateu a meta. Vendedor: {vendedor}, Valor: {vendas}')

        print(message.sid)
# verificar se algum valor na coluna Vendas daquile arquivo é maior que 55.000
# se for maior do que 55.000 -> envia um SMS com o nome, o mês e as vendas do vendedor
# Caso nao seja maior do que 55.000 não fazer nada 