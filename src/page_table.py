class PageTableEntry:
    def __init__(self):
        self.valid = False       # Está na memória?
        self.accessed = False    # Foi acessada?
        self.dirty = False       # Foi modificada?
        self.frame_number = None # Qual quadro na RAM


class PageTable:
    def __init__(self, size=32):
        # Inicializa a tabela com 'size' entradas
        self.entries = {i: PageTableEntry() for i in range(size)}
        self.frame_counter = 0   # Conta os quadros alocados

    def lookup(self, page_number):
        """
        Verifica se a página está na memória.
        Retorna:
            - frame_number se estiver (page hit)
            - None se não estiver (page fault)
        """
        entry = self.entries.get(page_number)
        if entry and entry.valid:
            entry.accessed = True
            return entry.frame_number
        else:
            return None

    def handle_page_fault(self, page_number):
        """
        Simula um page fault. Carrega a página no próximo quadro livre.
        """
        entry = self.entries[page_number]

        # Atribui um novo quadro
        frame_number = self.frame_counter
        self.frame_counter += 1

        entry.valid = True
        entry.accessed = True
        entry.dirty = False
        entry.frame_number = frame_number

        print(f"Page fault: carregando página {page_number} no quadro {frame_number}")

        return frame_number

    def set_dirty(self, page_number):
        """
        Marca a página como modificada (dirty).
        """
        entry = self.entries.get(page_number)
        if entry:
            entry.dirty = True

    def __str__(self):
        result = ""
        for num, entry in self.entries.items():
            result += f"Page {num}: valid={entry.valid}, accessed={entry.accessed}, dirty={entry.dirty}, frame={entry.frame_number}\n"
        return result
