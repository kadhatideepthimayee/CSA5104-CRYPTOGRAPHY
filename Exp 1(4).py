class AH:
    def process(self):
        print("Authentication Header (AH): Integrity + Authentication")

class ESP:
    def process(self):
        print("Encapsulating Security Payload (ESP): Encryption + Authentication")

class SA:
    def process(self):
        print("Security Association (SA): Security Parameters")

print("===== IPSec Architecture Simulation =====")

packet = "Original IP Packet"

print("Sender:")
print(packet)

sa = SA()
ah = AH()
esp = ESP()

sa.process()
ah.process()
esp.process()

print("\nPacket transmitted securely...\n")

print("Receiver:")
print("ESP verifies and decrypts")
print("AH verifies integrity")
print("Original packet received")
