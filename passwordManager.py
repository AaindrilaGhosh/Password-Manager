from cryptography.fernet import Fernet         #module which allows us to encrypt

# key + password + text to encrypt = random text
# random test + key + password = text to encrypt

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "\nPassword:", fer.decrypt(passw.encode()).decode())

# b'hello' is a byte str
# 'hello' is a normal str

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")  #encoding it reverts it inot bytes


while True:
    mode = input("Would you like to add a new password or view the existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue