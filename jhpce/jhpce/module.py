from io import StringIO
import os
import pandas as pd
import paramiko 
## pip install GitPython to install this
import git

class jhpce():
    # Class for connecting to jhpce
    # Currently only connects to jhpce01
    def __init__(self,  username, pkey):
        self.address01 = "jhpce01.jhsph.edu"
        self.address02 = "jhpce02.jhsph.edu"
        self.address03 = "jhpce03.jhsph.edu"
        self.username = username
        self.pkey = pkey
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.address02, username = self.username, pkey = self.pkey)
        self.local_dir = os.getcwd()
        self.remote_dir = "$HOME"
        self.local_remote_mappings = {}        

    ##############################################################
    ## Connection commands
    ##############################################################
    def close(self):
        self.ssh.close()

    ## if the connection gets closed
    def reconnect(self):
        self.ssh.connect(self.address03, username = self.username, pkey = self.pkey)                      

    ##############################################################
    ## Local commands
    ##############################################################
    def local_ls(self, opts = "-alh", pandas = True, print_results = True):
        if pandas:
            cmd = "ls -alh "
        else :
            cmd = "ls " 


    def local_set_dir(self, path):
        if os.path.isdir(path):
            self.local_dir = path
        else :
            print("Path does not exist " + path)

    ##############################################################
    ## Remote commands
    ##############################################################
    def remote_set_dir(self, path):
        if self.remote_dircheck(path, print_results = False):
            print("Success")
            self.remote_dir = path
        else :
            print("Remote path does not exist " + path)
                    
    def remote_ls(self, opts = "-alh", return_as_pd = False, print_results = True):
        ## Force alh if returning as pd
        if return_as_pd:
            cmd = "ls -alh "
        else :
            cmd = "ls " 

        stdin, stdout, stderr = self.ssh.exec_command(cmd + opts + " " + self.remote_dir)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        
        if print_results: print(stdout)

        if return_as_pd :
            return pd.read_csv(StringIO(stdout), sep = "\s+",  skiprows = 1,  header = None)    
        
    ### checks if a remote directory is present
    def remote_dircheck(self, path, print_results = True):
        cmd = "test -d " + path + " && echo 1"
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        
        if stdout.readline() == "1\n":
            if print_results: print("Directory exists on jhpce")
            rval = True
        else :
            if print_results: print("Directory does not exist on jhpce")
            rval = False
        return rval
    
    ##############################################################
    ## Git commands
    ##############################################################
    ### Allows you to change the director of the get repo
    def local_set_repo(self, path):
        if os.path.isdir(path):
            self.local_repo = git.Repo(path)
        else :
            print("Path does not exist " + path)
    def local_git_pull(self, ):
        ## Assumes you're in the correct local directory
        os.system("git pull")    
    def local_git_push(self, branch = "main"):
        os.system("git push origin " + branch)
    def local_git_origin(self):        
        return [r.url for r in self.local_repo.remotes][0]
    def remote_git_pull(self):
        cmd = "cd " + self.remote_dir + "; git pull"
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        print(stdout)
        print(stderr)

    ##############################################################
    ## Slurm commands            
    ##############################################################
    def remote_squeue(self, opts = "", print_results = False, pandas = True):
        cmd = "squeue " + opts
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if print_results:
            print(stdout)
        if pandas :
            rval = pd.read_table(StringIO(stdout), delim_whitespace=True)
        else :
            rval = {"stdout" : stdout, "stderr" : stderr}

        return rval
    
    def remote_sinfo(self, opts = "", print_results = False, pandas = True):
        cmd = "sinfo " + opts
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if print_results:
            print(stdout)
        if pandas :
            rval = {"stdout" : pd.read_table(StringIO(stdout), delim_whitespace=True)}
        else :
            rval = {"stdout" : stdout, "stderr" : stderr}

        return rval

    def remote_sstat(self, jobid, opts = "", print_results = False, pandas = True):
        cmd = "sstat " + opts + " " + jobid
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if print_results:
            print(stdout)
        if pandas :
            rval = pd.read_table(StringIO(stdout), delim_whitespace=True)
        else :
            rval = {"stdout" : stdout, "stderr" : stderr}

        return rval
    
    def remote_sbatch(self, script, opts = "", print_results = False):
        cmd = "sbatch " + opts + " " + script
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if print_results:
            print(stdout)
        rval = {"stdout" : stdout, "stderr" : stderr}
        return rval
    
    def remote_scancel(self, jobid, opts = "", print_results = False):
        cmd = "scancel " + opts + " " + jobid
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if print_results:
            print(stdout)
        rval = {"stdout" : stdout, "stderr" : stderr}
        return rval
    
    def remote_sacct(self, opts = "", print_results = False, pandas = True):
        cmd = "sacct " + opts + " " 
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = stdout.read().decode()
        stderr = stderr.read().decode()
        if print_results:
            print(stdout)
        if pandas :
            rval = pd.read_table(StringIO(stdout), delim_whitespace=True)
        else :
            rval = {"stdout" : stdout, "stderr" : stderr}

        return rval
