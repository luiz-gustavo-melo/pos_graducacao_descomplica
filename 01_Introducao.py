# %%
saudacao = "bom dia"

nome = input("Digite o nome que receberá a saudaçã: ")

print (saudacao, ", ",nome, ". Seja bem-vindo!")



# %%

num_lista = input("Digite os números, separados por vírgula: ")
numeros = [
    int(item.strip()) # strip remove espaços em branco;
    for item in num_lista.split(",") # split separa a substring;
    if item.strip() 
]
print(numeros)

