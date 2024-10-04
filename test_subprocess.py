import subprocess

result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)

print(result.stdout)
