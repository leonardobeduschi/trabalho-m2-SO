from address_parser import AddressParser

# Teste com página de 4KB
parser = AddressParser(4096)

# Endereço de exemplo
address = 19986
page, offset = parser.parse(address)

print(f"Endereço {address} -> Página {page}, Offset {offset}")

# Testando hexadecimal
address_hex = "0x4E12"
page, offset = parser.parse_string(address_hex)
print(f"Endereço {address_hex} -> Página {page}, Offset {offset}")
