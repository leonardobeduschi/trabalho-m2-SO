from page_table import PageTable

pt = PageTable()

# Lookup de página 5 (não está carregada)
res = pt.lookup(5)
print("Lookup página 5:", res)

# Tratando page fault
frame = pt.handle_page_fault(5)
print(f"Página 5 carregada no quadro {frame}")

# Lookup novamente (agora deve estar)
res = pt.lookup(5)
print("Lookup página 5:", res)

# Marcando como dirty
pt.set_dirty(5)

# Exibindo estado da tabela
print(pt)
