import paramiko
from getpass import getpass

#writes a private key to a file in the formate JHPCE wants
#filename is the file and path, typically ~/.ssh/keyname
#password is the password for the key and is required
def keygen(filename, save_to_file = True) :
    key = paramiko.RSAKey.generate(4096)
    password = getpass("Enter a password")
    if save_to_file:
        key.write_private_key_file(filename, password = password)
        f = open(filename+".pub", "w")
        f.write("ssh-rsa " + key.get_base64())
        f.close()
        print("Private key written to " + filename)    
        print("Public key written to " + filename + ".pub")    
    print("Copy the following the public key to the authorized_keys file on JHPCE")
    print("ssh-rsa " + key.get_base64())
    return key

## Recommended way to load the password is using getpass
def loadkey(filename):
    from getpass import getpass
    password = getpass()
    return paramiko.RSAKey.from_private_key_file(filename, password)


def colabgetkey(secret_id):
    from getpass import getpass
    import io
    ## Note this is not included in requirements since it
    ## only is useful on colab
    from google.colab import userdata
    keyfile = io.StringIO()
    keyfile.write(userdata.get(secret_id))
    keyfile.seek(0)
    return paramiko.RSAKey.from_private_key(keyfile, getpass())

