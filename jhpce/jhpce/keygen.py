import paramiko
from getpass import getpass

#writes a private key to a file in the formate JHPCE wants
#filename is the file and path, typically ~/.ssh/keyname
#password is the password for the key and is required
def keygen(filename, password) :
    key = paramiko.RSAKey.generate(4096)
    key.write_private_key_file(filename, password = password)
    print(f"Private key written to {filename}")    
    print("Copy the following to the JHPCE authorized_keys file")
    print("ssh-rsa " + key.get_base64())
    return key

## Recommended way to load the password
def loadkey(filename):
    from getpass import getpass
    #password = getpass()
    return paramiko.RSAKey.from_private_key_file(filename, getpass())