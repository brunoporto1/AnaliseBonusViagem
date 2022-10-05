import pandas as pd
import openpyxl
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa0ea1962936f2e78a42010c2bc09e6b1"
# Your Auth Token from twilio.com/console
auth_token  = "91555c1a50f10c605b36433f0ac2de18"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas:{vendas}')
        message = client.messages.create(
            to="+5524998543878",
            from_="+16302167988",
            body=f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas:{vendas}')
        print(message.sid)


# Para cada arquivo:
 #Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000;
 #Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor;
 #Caso não seja maior que 55.000 não quero fazer nada.