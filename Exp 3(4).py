import hashlib

packet = input("Enter IP Packet Data: ")

hash_value = hashlib.sha256(packet.encode()).hexdigest()

print("\nAuthentication Header")
print("Packet:", packet)
print("Authentication Value:", hash_value)
