quantidade= float(input("Digite o valor kWh consumido: "))
instalacao= input("Escolha o tipo de intalação: ")

def kwh():
    return quantidade
def inst():
    var1 = 0.40
    var2= 0.65
    var3= 0.55
    var4= 0.60
    var5= 0.55
    var6= 0.60
    if instalacao == "R" :
        if  quantidade <= 500 :
           return var1
        else:
           return var2 
        
    if instalacao == "I":
        if  quantidade <= 1000:
           return var3
        else:
           return var4
    if instalacao == "C":
        if  quantidade <= 5000:
           return var5 
        else:
           return var6 
    
def principal():
    total = quantidade * inst()
    return total
print(f"O valor a pagar será de: {principal()}R$")



