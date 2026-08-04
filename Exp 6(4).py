import base64

packet = input("Enter Packet: ")

encrypted = base64.b64encode(packet.encode()).decode()

print("\nEncrypted Packet")
print(encrypted)

decrypted = base64.b64decode(encrypted).decode()

print("\nDecrypted Packet")
print(decrypted)
