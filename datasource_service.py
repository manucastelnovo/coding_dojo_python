import pymysql.cursors



# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='holamundo',
                             cursorclass=pymysql.cursors.DictCursor)

# connection.ping(reconnect=True)

# with connection:
#     print('Base de datos conectada')
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `user` (`name`, `edad`, `email`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)



    # SELECT


def registerUser( email:str,firstname:str ,lastname:str ,password:str ):
    
    with connection.cursor() as cursor:
        sql = "INSERT INTO `users`(`email`,`firstname`,`lastname`,`password`) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (email, firstname, lastname, password))
        connection.commit()
        



def getUser( email:str ):
    
    with connection.cursor() as cursor:
    # Read a single record
        sql = "SELECT `id`, `firstname`,`lastname`, `email`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, (email))
        result = cursor.fetchone()
        connection.commit()
        
        return result
        
    

def getUserById( id:int ):
    
    with connection.cursor() as cursor:
    # Read a single record
        sql = "SELECT `id`, `firstname`,`lastname`, `email`, `password` FROM `users` WHERE `id`=%s"
        cursor.execute(sql, (id))
        result = cursor.fetchone()
        connection.commit()
        print(result)
        return result
        


def registerPypie( name:str,filling:str ,crust:str, user_id:int,votes:str ):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `pie`(`name`,`filling`,`crust`,`votes`,`user_id`) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (name, filling, crust, votes,user_id))
        connection.commit()
    
def getAllUserPie(user_id:int):
    with connection.cursor() as cursor:
        sql = "SELECT `id`, `name`, `filling`, `crust`, `votes` FROM `pie` WHERE `user_id`=%s"
        cursor.execute(sql, (user_id,))
        result = cursor.fetchall()
        return result
 
def editPie(pie_id:int, name:str, filling:str, crust:str):
    with connection.cursor() as cursor:
        sql = "UPDATE `pie` SET `name`=%s, `filling`=%s, `crust`=%s WHERE `id`=%s"
        cursor.execute(sql, (name, filling, crust, pie_id))
        connection.commit()
 
def deletePie(pie_id:int):
    with connection.cursor() as cursor:
        sql = "DELETE FROM `pie` WHERE `id`=%s"
        cursor.execute(sql, (pie_id,))
        connection.commit()
 
def votePie(pie_id:int):
    with connection.cursor() as cursor:
        sql = "UPDATE `pie` SET `votes`=`votes`+1 WHERE `id`=%s"
        cursor.execute(sql, (pie_id,))
        connection.commit()

def getPieById( id:int ):
    
    with connection.cursor() as cursor:
    # Read a single record
        sql = "SELECT `id`, `name`,`filling`, `crust` FROM `pie` WHERE `id`=%s"
        cursor.execute(sql, (id))
        result = cursor.fetchone()
        connection.commit()
        print(result)
        return result
