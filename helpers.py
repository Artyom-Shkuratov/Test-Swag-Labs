import random
from data.users import UsersLogin, UsersPassword


class GeneratorData:
    @staticmethod
    def get_random_login() -> str:
        logins = [
            UsersLogin.STANDARD,
            UsersLogin.PROBLEM,
            UsersLogin.PERFORMANCE_GLITCH,
            UsersLogin.ERROR,
            UsersLogin.VISUAL,
        ]
        return random.choice(logins)
    
    @staticmethod
    def get_password():
        return UsersPassword.PASSWORD

