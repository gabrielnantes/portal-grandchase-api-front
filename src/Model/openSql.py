import pyodbc


def retornar_conexao_sql():
    server = "A5679"
    database = "TESTE"
    username = "adm_xisde"
    password = "92357955"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server=' + \
        server+';Database='+database+';UID='+username+';PWD=' + password
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()