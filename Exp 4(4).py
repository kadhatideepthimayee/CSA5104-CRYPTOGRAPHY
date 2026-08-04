import hashlib

message = input("Enter Packet Data: ")

icv = hashlib.sha256(message.encode()).hexdigest()

print("\nIntegrity Check Value (ICV)")
print(icv)
