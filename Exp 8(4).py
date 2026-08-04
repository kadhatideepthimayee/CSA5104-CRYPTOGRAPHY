import base64

packet = input("Enter Packet: ")

print("\nEncapsulation")

encrypted = base64.b64encode(packet.encode()).decode()

esp_packet = {
    "ESP Header": "SPI=1001",
    "Encrypted Payload": encrypted,
    "ESP Trailer": "Padding"
}

print(esp_packet)

print("\nDecapsulation")

decrypted = base64.b64decode(esp_packet["Encrypted Payload"]).decode()

print("Recovered Packet:", decrypted)
