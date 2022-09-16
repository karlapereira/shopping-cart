from passlib.context import CryptContext


class Hash:
    def __init__(self) -> None:
        self.pwd_encrypted = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt(self, password):
        return self.pwd_encrypted.hash(password)

    def verify(self, password, password_encrypted):
        return self.pwd_encrypted.verify(password, password_encrypted)
