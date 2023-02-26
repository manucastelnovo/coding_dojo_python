import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='holamundo',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    print('Base de datos conectada')
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


    def registerUser( email,firstname ,lastname ,password ):
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `holamundo`.`user` (`email`,`firstname` `lastname`,`password`) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql, (email, firstname, lastname, password))
            connection.commit()

    # CREATE

