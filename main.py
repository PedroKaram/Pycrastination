import time

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

blocked_websites = [
    "www.instagram.com",
    "instagram.com",
    "www.youtube.com",
    "youtube.com"
]

try:
    print("Bloqueando sites enquanto o programa estiver rodando")

    while True:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in blocked_websites:
                if site not in content:
                    file.write(f"{redirect} {site}\n")
        time.sleep(10)
except KeyboardInterrupt:
    print("Encerrando e removendo bloqueios")

    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in blocked_websites):
                file.write(line)
        file.truncate()

    print("Sites desbloqueados.")
