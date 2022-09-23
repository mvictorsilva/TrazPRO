import PySide6.QtSql

con = PQconnectdb("host=server user=bart password=simpson dbname=springfield")
drv = QPSQLDriver(con)
db = QSqlDatabase.addDatabase(drv) # becomes the default connection()
query = QSqlQuery()
query.exec("SELECT NAME, ID FROM STAFF")
