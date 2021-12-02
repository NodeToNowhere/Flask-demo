
from db.run_sql import run_sql
from models.location import Location
from models.user import User
from models.visit import Visit

def save(user):
    sql = "INSERT INTO users( name ) VALUES ( %s ) RETURNING id"
    values = [user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['id'] )
    return user


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def users(location):
    users = []
    sql = "SELECT users.* FROM users INNER JOIN locations ON users.location.name = locations.name WHERE location.name = %s"
    values = [location.name]
    results = run_sql(sql, values)
    
    for row in results:
        users = User(row['name'],row['id'])
        users.append(users)
    return users