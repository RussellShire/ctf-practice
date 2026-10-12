import subprocess
import sys

process = subprocess.Popen(
    [sys.executable, 'level5.py'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(input="password1\npassword2\n")

print(stdout)
print('error', stderr)
