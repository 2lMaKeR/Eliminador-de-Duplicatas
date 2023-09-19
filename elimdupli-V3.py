entrada=input("Insira todos os números de contato: (separados por ;) ")
contatos=entrada.split(";")
contatosUni={}

for contato_str in contatos:
    telefone=contato_str.strip().split(",")
    chave=tuple(telefone)
    if chave not in contatosUni:
        contatosUni[chave]={"telefone":telefone}

numInter=[]
for contato in contatosUni.values():
    numInter.append(contato["telefone"])
numInter2=";".join(",".join(telefone) for telefone in numInter)

print("")
print(numInter2)