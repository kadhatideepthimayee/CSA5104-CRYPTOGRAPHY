import hashlib
import base64

packet = input("Enter Packet: ")

encrypted = base64.b64encode(packet.encode()).decode()

authentication = hashlib.sha256(encrypted.encode()).hexdigest()

print("\nPacket Sent")

print("Encrypted Data:", encrypted)
print("Authentication:", authentication)

print("\nReceiver Side")

verify = hashlib.sha256(encrypted.encode()).hexdigest()

if verify == authentication:
    print("Authentication Successful")
    decrypted = base64.b64decode(encrypted).decode()
    print("Decrypted Packet:", decrypted)
else:
    print("Packet Authentication Failed")
