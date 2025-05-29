from tlb import TLB

tlb = TLB()

# Inserindo 3 páginas
tlb.insert(1, 100)
tlb.insert(2, 200)
tlb.insert(3, 300)

print("TLB após inserções:", tlb)

# Buscando página 2
res = tlb.lookup(2)
print("Lookup página 2:", res)

# Buscando página não existente
res = tlb.lookup(5)
print("Lookup página 5:", res)

# Inserindo até ultrapassar a capacidade
for i in range(4, 20):
    tlb.insert(i, i * 100)

print("TLB após overflow:", tlb)
