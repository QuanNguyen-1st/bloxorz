import subprocess

subprocess.call("python tester.py & python tester1.py & python tester2.py", shell=True)