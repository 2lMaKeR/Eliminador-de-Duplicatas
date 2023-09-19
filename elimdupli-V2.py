contatosUni={}
print("###############################")
print("")
print("ELIMINADOR DE DUPLICATAS V2!!")
print("")
print("insira os números que deseja analisar,")
print("quando terminar digite 'sair' para finalizar a lista.")
print("(OBS: sem as '')")
print("")

while True:
    tel=input("Digite o número do contato: ")

    if tel.lower()=='sair':
        break
    
    chave=(tel)

    if chave not in contatosUni:
        contatosUni[chave]={"telefone": tel}
    else:
        print("Contato já registrado.")

numInter=[]
for contato in contatosUni.values():
    numInter.append(contato["telefone"])

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(";".join(numInter))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
