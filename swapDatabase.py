import psycopg2

class swapDatabase():
    def __init__(self):
        # Creates a Connection to the database
        try:
            self.connection = psycopg2.connect(
                    database = "postgres",
                    user = "postgres",
                    password = "ZZiCHA321!#",
                    host = "alphalibertee1.ccwxvu5q3faa.us-east-1.rds.amazonaws.com",
                    port = "5432",
                    connect_timeout = 5,
                    )
            self.connection.autocommit = True           # Auto commits any data updated/removed/added to the database
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(str(e))

    def getTransaction(self, hash, fromAddress, fromBlockchain):
        cmd = f'select to_address, to_blockchain, to_amount from "swapTransactions" where transhash1=\'{hash}\' and from_address=\'{fromAddress}\' and from_blockchain=\'{fromBlockchain}\''
        self.cursor.execute(cmd)
        try:
            return self.cursor.fetchone()
        except Exception as e:
            print(e)

    def newTransaction(self, username, from_blockchain, transhash1, to_blockchain, from_amount, to_amount, from_address, to_address):
        cmd = f'INSERT INTO public."swapTransactions"(username, from_blockchain, transhash1, to_blockchain, from_amount, to_amount, from_address, to_address) VALUES (\'{username}\', \'{from_blockchain}\', \'{transhash1}\', \'{to_blockchain}\', \'{from_amount}\', \'{to_amount}\', \'{from_address}\', \'{to_address}\');'
        self.cursor.execute(cmd)
        return True
    
    def updateTransaction(self, to_address, to_blockchain, to_amount, transhash2):
        cmd = f'UPDATE public."swapTransactions" SET transhash2=\'{transhash2}\' WHERE to_address=\'{to_address}\' and to_blockchain =\'{to_blockchain}\' and to_amount = \'{to_amount}\';'
        self.cursor.execute(cmd)


