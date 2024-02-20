# jhpce-tools

This repository contains tools for working with the JHPCE cluster. The tools are designed to be used within python and have been tested within unix environments.

## Installation

Currently `jhpce-tools` is not on pypi. To install, clone the repository and run the following command from the root directory of the repository. Until it is on pypi, you will need to install it from the git repository, from which you should pull often.

```
from jhpce.jhpce.module import *
```

## Establishing a connection
One needs to have ssh paswordless access to the JHPCE cluster. For example, my username is `bcaffo` and I have a file `~/.ssh/id_rsa` that is my private key.
Given that this is set up, to establish a connections do the following:

```
con = jhpce("USERNAME", "PATH_TO_YOUR_SSH_KEY/id_rsa")
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

