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

## Recommended way to load the password is using getpass
## If filename_is_key is set to true, then the user has supplied
## the actual keyfile as text rather than a link to a filename
def loadkey(filename, filename_is_key = False):
    from getpass import getpass
    password = getpass()
    if filename_is_key :
        import io
        keyfile = io.StringIO()
        keyfile.write(filename)
        keyfile.seek(0)
        return paramiko.RSAKey.from_private_key_file(keyfile, password)
    else :
        return paramiko.RSAKey.from_private_key_file(filename, password)
        