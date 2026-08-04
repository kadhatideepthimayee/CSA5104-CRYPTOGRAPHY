packet = input("Enter IP Packet: ")

print("\nTransport Mode")
print("Original Header + ESP + Payload")

transport = "[IP Header] + [ESP] + [" + packet + "]"

print(transport)

print("\nTunnel Mode")

tunnel = "[New IP Header] + [ESP] + [Old IP Header + " + packet + "]"

print(tunnel)
