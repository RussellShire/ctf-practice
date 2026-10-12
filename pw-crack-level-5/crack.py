import subprocess
import sys

passwords=['one', 'two']
attempts=0
correctPassword=''

for password in passwords:
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

    if stderr:
        print("Error:", stderr)
    
    attempts += 1

print("Process completed, passwords attempted: ", attempts)