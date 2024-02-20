# jhpce-tools

This is a repository to apply and use JHPCE cluster management locally
in python. 

Until it gets put on pypi, you can load with

```
from jhpce.jhpce.module import *
```

from the root directory of this repo. One can establish a connection witih

```
## Establish a connection
con = jhpce("USERNAME", "LOCATION OF PRIVATE KEY")
## It keeps track of a local directory
con.local_set_repo("DIRECTORY ON LOCAL")
## It can execute some remote commands
con.remote_ls(return_as_pd = True)
## It can set a remote directory
con.remote_set_dir("DIRECTORY ON CLUSTER")
## Read the slurm queue
out = con.remote_squeue()['stdout']
```