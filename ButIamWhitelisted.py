from mcstatus import JavaServer

server = JavaServer("<address>", 25565)
server.ping()

# Info about players on the server

print(server.status())