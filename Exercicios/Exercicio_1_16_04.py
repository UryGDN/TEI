import os
os.system("cls")

nm_prod = input("Nome do Produto: ")
vl_prod = 0
tax = 1

while vl_prod <= 0:
    vl_prod = float(input("Valor do produto: "))
    if vl_prod <= 0:
        print("Tu é retardado? produto gratis")
        continue
    else:
        break
    
    
if vl_prod >= 50 and vl_prod < 200:
    tax = 0.95
elif vl_prod >= 200 and vl_prod < 500:
    tax = 0.94
elif vl_prod >= 500 and vl_prod < 1000:
    tax = 0.93
elif vl_prod >= 1000:
    tax = 0.92


vl_prod_new = vl_prod * tax

print("Nome do produto: {0}, Valor Original {1}, Valor Novo {2}".format(nm_prod, vl_prod, vl_prod_new))
if tax == 1:
    print("O produto não teve nem um desconto")