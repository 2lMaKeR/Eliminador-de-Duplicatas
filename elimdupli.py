contatos=[
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
    {"num":""},
]

contatosUni={}

for contato in contatos:
    tel = contato["num"]
    chave=(tel)
    if chave not in contatosUni:
        contatosUni[chave]=contato

contatosUni=list(contatosUni.values())

#for contato in contatosUni:
#    print(contato)

numInter=[]
for contato in contatosUni.values():
    numInter.append(contato["num"])

print(";".join(numInter))