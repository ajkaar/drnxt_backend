# Business logic for authentication
def authenticate_user(username, password):
    return username == "admin" and password == "admin"