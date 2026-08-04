sa_database = {
    1001: {"Algorithm": "AES", "Key": "Key123"},
    1002: {"Algorithm": "3DES", "Key": "Secret456"},
    1003: {"Algorithm": "AES256", "Key": "Secure789"}
}

spi = int(input("Enter SPI: "))

if spi in sa_database:
    print("Security Association Found")
    print(sa_database[spi])
else:
    print("Security Association Not Found")
