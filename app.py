import subprocess
# This WILL fail the Bandit scan test
subprocess.call("ls", shell=True) 
