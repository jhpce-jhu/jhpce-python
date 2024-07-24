# jhpce-tools

This repository contains tools for working with the JHPCE cluster while still working in your local environment. The tools are designed to be used within python.
If you want to see a working example of the software, look [here](https://colab.research.google.com/drive/1SUyhRhfvLps1Zkv-iAkyJVXNIRtcDbYf?usp=sharing)

## Installation (recommended)

The package is called `jhpce` on pypi. To install, 
```
pip install jhpce
```

## Installing from source
Alternatively, if you want to install from source, clone the repository.  In the root directory of the software is the requirements. You 
can install them with
```
pip install -r requirements.txt
```
(put an `!` in a jupyter notebook cell). Then load the software; this assumes that you're in the directory containing the github repo.

```
from jhpce.module import *
from jhpce.keygen import *
```

## Creating a key 
To use this package, you need a public/private key pair for JHPCE. This package helps do this for you. You can generaate a key with

```
key = keygen()
## Print out your public key to paste in your authorized_keys file on JHPCE
print("ssh-rsa " + key.get_base64())
```
This command generages two files, `id_jhpce` and `id_jhpce.pub` which are your public and private key pair. You need
to store your private key somewhere secure and paste your public key onto your `authorized_keys` files on JHPCE.

Alternatively, [this](https://colab.research.google.com/drive/1I8VjmDDO86Qj0jJYMmDlZWrAoZwVLrpj?usp=sharing) jupyter notebook walks you through the process.

One needs to have ssh paswordless access to the JHPCE cluster. For example, my username is `bcaffo` and I have a file `~/.ssh/id_rsa` that is my private key. You can set this up with

```
from jhpce.jhpce.keygen import *
keygen()
```

This will prompt you for a password for the private key then your username, password and OTP (verification code). Then it will paste your public key onto your `authorized_keys` file on jhpce. Make sure to save your public and private key, which by default are in 
`id_jhpce` and `id_jhpce.pub` in the current working directory.


## Establishing a connection

Given that this is set up, to establish a connections do the following. First,
load your key into python with the command

```
key = loadkey("FILENAME OR FULLPATHTOFILE")
```

This will load the private key. You can then establish a connection with:

```
con = jhpce("USERNAME", key)
```
or just
```
con = jhpce("USERNAME")
```
if your ssh key is in the default location. For example my path would be `~/.ssh/id_rsa`.

## Running remote commands
Commands that opperate on the remote cluster are prefixed with `remote_`. For example, to list the files in the current directory, one would use the following command:

```
con.remote_ls()
```
Lists out the files in the current remote directory. To change directories one would use the following command:

```
con.remote_set_dir("RELATIVE_OR_ABSOLUTE_PATH_TO_NEW_DIRECTORY")
```

## Running local commands

Commands that opperate on the local machine are prefixed with `local_`. For example, to list the files in the current directory, one would use the following command:

```
con.local_set_dirI('RELATIVE_OR_ABSOLUTE_PATH_TO_NEW_DIRECTORY')
```

## Slurm commands

