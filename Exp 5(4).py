import hashlib

packet = input("Enter Packet: ")

print("\nWithout AH")
print(packet)

print("\nWith AH")

ah = hashlib.sha256(packet.encode()).hexdigest()

print("Packet:", packet)
print("AH:", ah)

print("\nReceiver Verification")

received_hash = hashlib.sha256(packet.encode()).hexdigest()

if ah == received_hash:
    print("Integrity Verified")
else:
    print("Packet Modified")
