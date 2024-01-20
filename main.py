import secrets
import string
def generPassword(length):
  charac = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(secrets.choice(charac) for _ in range(length))
  return password

length = int(input("Entrez la taille du mot de passe souhaiter: "))
password = generPassword(length)
print(password)
