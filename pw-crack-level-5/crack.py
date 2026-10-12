import subprocess
import sys

with open('dictionary.txt', 'r') as file:
    passwords = file.read().splitlines()

attempts=0
flag=''

for password in passwords:
    print(attempts)

    process = subprocess.Popen(
        [sys.executable, 'level5.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(f"{password}\n")
    
    if "That password is incorrect" not in stdout:
        print(f"Trying: {password}")
        print("Output:", stdout)
        flag = stdout
        break

    if stderr:
        print("Error:", stderr)
    
    attempts += 1

print("Process completed, passwords attempted: ", attempts)
print("flag: ", flag)
