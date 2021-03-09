import subprocess

# Exemplo ping

process = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

out: str = process.stdout()
print(out)