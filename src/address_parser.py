class AddressParser:
    def __init__(self, page_size):
        self.page_size = page_size
        self.offset_bits = self._calculate_offset_bits(page_size)

    def _calculate_offset_bits(self, page_size):
        bits = 0
        while (1 << bits) < page_size:
            bits += 1
        return bits

    def parse(self, address):
        """
        Recebe um endereço (int) e retorna (page_number, offset)
        """
        page_number = address >> self.offset_bits
        offset_mask = (1 << self.offset_bits) - 1
        offset = address & offset_mask
        return page_number, offset

    def parse_string(self, address_str):
        """
        Recebe string decimal ou hexadecimal ('0x...') e retorna (page_number, offset)
        """
        if address_str.startswith("0x") or address_str.startswith("0X"):
            address = int(address_str, 16)
        else:
            address = int(address_str)
        return self.parse(address)
