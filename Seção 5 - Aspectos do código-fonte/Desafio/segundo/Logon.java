...
class Logon {
	boolean logon(String username, String password) throws SQLException {
		Statement stmt=this.db.createStatement();
		String comando = "select * from usu where logon='" + username 
		        + "' and password = '" + password + "'";
		ResultSet rs = stmt.executeQuery(comando);
		boolean achou = false;
		while (rs.next()) {
			this.usu = new Usu(rs);
			achou = true;
			if (this.usu.isAdmin()) {
				log.info("adm logado:" + usu);
			}
			break;
		}
		if (achou)
			return true;
		return false;
	}
	
	void alterarPrioridade(String username, int nova) throws SQLException {
		if (this.usu.isAdmin()) {
			log.info("alterando prioridade: " + usu + ", " + username + ", " + nova);
			Statement stmt=this.db.createStatement();
			String comando = "update usu set prioridade=" + nova 
		            + " where username='" + username + "'";
			stmt.executeUpdate(comando);
		}
	}
}
...

