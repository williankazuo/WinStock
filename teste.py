import mechanicalsoup
import pandas as pd

browser = mechanicalsoup.StatefulBrowser()

# Login
browser.open('https://cei.b3.com.br/CEI_Responsivo/', verify=False)
browser.select_form('form[action="./"]')
browser['ctl00$ContentPlaceHolder1$txtLogin'] = '44605047824'
browser['ctl00$ContentPlaceHolder1$txtSenha'] = '7747979@Wk'
browser.submit_selected()

# Carteira de ativos
browser.open('https://cei.b3.com.br/CEI_Responsivo/ConsultarCarteiraAtivos.aspx', verify=False)
browser.select_form('form[action="./ConsultarCarteiraAtivos.aspx"]')
browser.submit_selected()
teste = pd.read_html(str(browser.get_current_page()), thousands='.', decimal=',')


# Não esquecer de varrer as instituições.
# Negociações de ativos.
# Aqui tem um bug no site, que tem que apertar "Consultar" duas vezes
browser.open('https://cei.b3.com.br/CEI_Responsivo/negociacao-de-ativos.aspx', verify=False)
browser.select_form('form[action="./negociacao-de-ativos.aspx"]')
browser.submit_selected()
browser.select_form('form[action="./negociacao-de-ativos.aspx"]')
browser.submit_selected()
teste2 = pd.read_html(str(browser.get_current_page()), thousands='.', decimal=',')
teste2[0].columns = teste2[0].columns.str.replace('ó', 'o')
teste2[0].columns = teste2[0].columns.str.replace('ã', 'a')
teste2[0].columns = teste2[0].columns.str.replace('á', 'a')
teste2[0].columns = teste2[0].columns.str.replace('ç', 'c')
teste2[0].columns = teste2[0].columns.str.replace('/', '_')
teste2[0].columns = teste2[0].columns.str.replace('\(R\$\)', '')
teste2[0].columns = teste2[0].columns.str.strip()
teste2[0].columns = teste2[0].columns.str.replace(' ', '_')

teste2[0].columns = teste2[0].columns.str.lower()


print(teste2[0].to_json(orient='records'))

# def format_columns(values):
#     values.columns = values.columns.str.replace('ó', 'o')
#     values.columns = values.columns.str.replace('ã', 'a')
#     values.columns = values.columns.str.replace('á', 'a')
#     values.columns = values.columns.str.replace('ç', 'c')
#     values.columns = values.columns.str.replace('/', '_')
#     values.columns = values.columns.str.replace('\(R\$\)', '')
#     values.columns = values.columns.str.strip()
#     values.columns = values.columns.str.replace(' ', '_')

#     values.columns = values.columns.str.lower()
#     return values
