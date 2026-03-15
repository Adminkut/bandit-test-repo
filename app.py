import subprocess
# This WILL fail the Bandit scan
subprocess.call("ls", shell=True) 
