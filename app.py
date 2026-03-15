import subprocess

def insecure_func(user_input):
    # This is a High Severity vulnerability (B602)
    subprocess.call("echo " + user_input, shell=True)

insecure_func("test")
