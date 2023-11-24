...
def logon(username,password):
    global usu
    comando="select * from usu where logon='" + username \
        + "' and password = '" + password + "'"
    cursor = db.cursor()
    cursor.execute(comando)
    achou=False
    regs=cursor.fetchOne()
    for reg in regs:
        achou=True
        usu=reg
        if usu[5]:
            log.info(f"adm logado:{usu}")
        break
    if achou:
        return True
    return False

def alterar_prioridade(username,nova):
    if usu[5]:
        log.info(f"alterando prioridade:{usu[0]},username:{username} nova: {nova}")
        comando="update usu set prioridade=" + nova \
            + " where username='" + username + "'"
        cursor = db.cursor()
        cursor.execute(comando)
...