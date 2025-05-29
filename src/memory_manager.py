# src/memory_manager.py

from pathlib import Path
from .tlb import TLB
from .page_table import PageTable
from .address_parser import AddressParser


class MemoryManager:
    def __init__(self, page_size=4096, tlb_size=16, memory_file_path="data/data_memory.txt"):
        self.page_size = page_size
        self.offset_bits = page_size.bit_length() - 1
        self.tlb = TLB(tlb_size)
        self.page_table = PageTable()
        self.memory = self._load_memory(memory_file_path)

    def _load_memory(self, file_path):
        """Carrega o arquivo data_memory.txt como uma lista de inteiros."""
        memory = []
        with open(file_path, "r") as file:
            for line in file:
                memory.append(int(line.strip()))
        return memory

    def translate_address(self, virtual_address):
        """Traduz o endereço virtual, considerando TLB e Page Table."""
        parser = AddressParser(self.page_size)
        page_number, offset = parser.parse_address(virtual_address)

        result = {
            "virtual_address": virtual_address,
            "page_number": page_number,
            "offset": offset,
            "tlb_hit": False,
            "page_fault": False,
            "value": None
        }

        # 1. TLB lookup
        frame_number = self.tlb.lookup(page_number)
        if frame_number is not None:
            result["tlb_hit"] = True
        else:
            # 2. Page Table lookup
            page_entry = self.page_table.get_entry(page_number)
            if not page_entry.valid:
                # Page Fault
                result["page_fault"] = True
                self.page_table.load_page(page_number)  # Simula o carregamento
            frame_number = page_entry.frame_number

            # Atualiza TLB
            self.tlb.insert(page_number, frame_number)

        # Atualiza bits da Page Table
        self.page_table.update_access(page_number)

        # Calcula o endereço físico
        physical_address = (frame_number * self.page_size) + offset

        # Busca o valor na memória física
        try:
            value = self.memory[physical_address]
        except IndexError:
            raise ValueError(f"Endereço físico inválido: {physical_address}")

        result["value"] = value
        return result
