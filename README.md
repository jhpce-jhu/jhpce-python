# jhpce-python

This is a repository to apply and use JHPCE cluster management locally
in python. 

Until it gets put on pypi, you can load with

```
from jhpce.jhpce.module import *
from jhpce.jhpce keygen import *
```

If you don't already have a private key / public key pair. We
require a password on our private key. You can generate a public
private key par with the command:

```
key = keygen("id_jhpce", "****")
```
where `****` is your desired password. 
This will print out a public key text that you need to paste into `~/.ssh/authorized_keys` on jhpce.

Given that you have private key, one can load a key with
```
key = loadkey('filename', 'password')
```
You should execute this command in the interpreter, since it's plain text for the password.
**DO NOT ACCIDENTALLY COMMIT AND PUSH YOUR PRIVATE KEY OR PASSWORD TO A GITHUB REPO**

from the root directory of this repo. One can establish a connection witih

```
## Establish a connection, key is as above
con = jhpce("USERNAME", key)
## It keeps track of a local directory
con.local_set_repo("DIRECTORY ON LOCAL")
## It can execute some remote commands
con.remote_ls(return_as_pd = True)
## It can set a remote directory
con.remote_set_dir("DIRECTORY ON CLUSTER")
## Read the slurm queue
out = con.remote_squeue()['stdout']
```
