import random
import socket
import struct
import pythonping
print("""
░██████╗██████╗░██╗░░░░░░█████╗░░██████╗██╗░░██╗░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔════╝██║░░██║██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
╚█████╗░██████╔╝██║░░░░░███████║╚█████╗░███████║╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░╚═══██╗██╔═══╝░██║░░░░░██╔══██║░╚═══██╗██╔══██║░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██████╔╝██║░░░░░███████╗██║░░██║██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝""")
print("")
print("")
print("")
print("Scanning the Internet for Minecraft servers... ")
while True:
    ip = str(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))
    port = str(25565)
    ipadd = f"{ip}:{port}"
    msg = f"ip:{ip}, port:{port}, online:true"
    try:
        if (bool(pythonping.ping(ipadd, verbose=False)))==True:
            print(f"{ipadd}")
            with open(f"{ipadd}.txt", 'w') as f:
                f.write(msg)
    except RuntimeError:
        pass