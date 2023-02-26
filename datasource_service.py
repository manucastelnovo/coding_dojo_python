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
        


# def registerPypie( name:str,filling:str ,crust:str, user_id:str,votes:str ):
#     
#         with connection.cursor() as cursor:
#             sql = "INSERT INTO `users`(`name`,`filling`,`crust`,`votes`) VALUES (%s,%s,%s,%s)"
#             cursor.execute(sql, (name, filling, crust, votes))
#             connection.commit()
    
