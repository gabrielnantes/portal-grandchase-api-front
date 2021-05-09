from src.Model.openSql import retornar_conexao_sql
from flask import jsonify, request


def select_all_tabela_teste():
    cursor = retornar_conexao_sql()
    cursor.execute("SELECT * FROM TABELA_TESTE")

    row = cursor.fetchone()
    mesasge = ""
    if row:
        print(list(row))
        mesasge = jsonify("Deu Certo\n", list(row))
    else:
        mesasge = jsonify("Deu Certo\n", list(row))
    return mesasge


def add_teste():
    playload = request.form
    dict_playload = dict(playload)
    if not dict_playload.get("TEST1"):
        return jsonify({"error": "Parametro TEST1 é obrigatorio"})
    if dict_playload.get("TEST1") and not dict_playload.get("TEST1").isnumeric():
        return jsonify({"error": "Parametro TEST1 não é inteiro"})
    test1 = int(request.form["TEST1"])
    test2 = request.form["TEST2"]

    cursor = retornar_conexao_sql()
    ttt = cursor.execute(
        f"INSERT INTO TABELA_TESTE (TEST1,TEST2) values({test1}, '{test2}')")
    cursor.commit()
    return jsonify(True)
