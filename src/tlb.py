from collections import OrderedDict

class TLB:
    def __init__(self, capacity=16):
        # Dicionário ordenado: chave = número da página, valor = quadro físico
        self.capacity = capacity
        self.entries = OrderedDict()

    def lookup(self, page_number):
        """
        Verifica se a página está na TLB.
        Retorna:
            - quadro físico (frame) se encontrado (TLB hit)
            - None se não encontrado (TLB miss)
        """
        if page_number in self.entries:
            # Move para o final, indicando que foi usado recentemente
            self.entries.move_to_end(page_number)
            return self.entries[page_number]
        else:
            return None

    def insert(self, page_number, frame_number):
        """
        Insere um mapeamento página → quadro na TLB.
        Se já existir, atualiza.
        Se exceder capacidade, remove o menos recentemente usado (LRU).
        """
        if page_number in self.entries:
            # Atualiza e move para o final (mais recente)
            self.entries.move_to_end(page_number)
        self.entries[page_number] = frame_number

        if len(self.entries) > self.capacity:
            # Remove o primeiro item (menos usado)
            self.entries.popitem(last=False)

    def __str__(self):
        return str(self.entries)
