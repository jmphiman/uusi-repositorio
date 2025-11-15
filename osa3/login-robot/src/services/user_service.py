from entities.user import User
import re
import sys, pdb


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("The minimum username length is three characters")

        if len(password) < 8:
            raise UserInputError("The minimum password length is 8 characters")

        if not re.match("^[a-z]+$", username):
            raise UserInputError("The username can only contain characters a-z")

        if re.match("^[A-Za-z]+$", password):
            raise UserInputError("The password must contain other characters besides alphabets")

        user = self._user_repository.find_by_username(username)
        if user:
            raise UserInputError("The username is already in use")
