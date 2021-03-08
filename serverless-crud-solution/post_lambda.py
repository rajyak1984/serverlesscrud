import pymysql


rds_host = "<your_rds_instance_endpoint>"
username = "<your_master_user>"
password = "<your_master_password>"
db_name  = "<your_chosen_database_name>"

def save_events(event):
    print("Adding User {")
    print(event["name"])
    print("}")
    result = []
    connection = pymysql.connect(host= rds_host,
                                 user= username,
                                 password= password,
                                 db= db_name,
                                 connect_timeout=5)
    
    with connection.cursor() as cursor:
         cursor.execute("""insert into test (id, name) values(%s, '%s')""" % (event['id'], event['name']))
         cursor.execute("""select * from test""")
         connection.commit()
         cursor.close()
         for row in cursor:
             result.append(list(row))
         print("Data from RDS...")
         print(result)
         

    
def main(event, context):
    save_events(event)

