# src/main.py

import sys
from pathlib import Path
from memory_manager import MemoryManager


def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def process_address(address_str, memory_manager):
    try:
        # Detecta se é hexadecimal ou decimal
        if address_str.startswith("0x") or is_hex(address_str):
            virtual_address = int(address_str, 16)
        else:
            virtual_address = int(address_str)
    except ValueError:
        print(f"Endereço inválido: {address_str}")
        return

    try:
        result = memory_manager.translate_address(virtual_address)
        print(f"\nEndereço virtual: {result['virtual_address']}")
        print(f"Número da página: {result['page_number']}")
        print(f"Deslocamento: {result['offset']}")

        if result["tlb_hit"]:
            print("TLB hit")
        else:
            print("TLB miss")

        if result["page_fault"]:
            print("Page Fault - Carregado da backing store")
        else:
            print("Page Hit")

        print(f"Valor lido da memória: {result['value']}")
    except Exception as e:
        print(f"Erro ao processar {address_str}: {e}")


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <endereço ou arquivo>")
        sys.exit(1)

    input_arg = sys.argv[1]
    memory_manager = MemoryManager(page_size=4096)  # Ajustável

    if Path(input_arg).is_file():
        with open(input_arg, "r") as file:
            for line in file:
                address = line.strip()
                if address:
                    process_address(address, memory_manager)
    else:
        process_address(input_arg, memory_manager)


if __name__ == "__main__":
    main()
