# src/memory_manager.py

from pathlib import Path
from tlb import TLB
from page_table import PageTable
from address_parser import AddressParser


class MemoryManager:
    def __init__(self, page_size=4096, tlb_size=16, memory_file_path="data/data_memory.txt"):
        self.page_size = page_size
        self.parser = AddressParser(page_size)
        self.tlb = TLB(tlb_size)
        self.page_table = PageTable(size=32)  # Inicializa com 32 entradas como especificado
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
        # Verifica se é string (hexa ou decimal) ou número
        if isinstance(virtual_address, str):
            page_number, offset = self.parser.parse_string(virtual_address)
        else:
            page_number, offset = self.parser.parse(virtual_address)

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
            frame_number = self.page_table.lookup(page_number)
            
            if frame_number is None:
                # Page Fault
                result["page_fault"] = True
                frame_number = self.page_table.handle_page_fault(page_number)

            # Atualiza TLB
            self.tlb.insert(page_number, frame_number)

        # Marca a página como acessada (já feito no lookup da PageTable)
        # Se precisar marcar como dirty em operações de escrita, adicionar método

        # Calcula o endereço físico
        physical_address = (frame_number * self.page_size) + offset

        # Busca o valor na memória física
        try:
            value = self.memory[physical_address]
        except IndexError:
            raise ValueError(f"Endereço físico inválido: {physical_address}")

        result["value"] = value
        return result