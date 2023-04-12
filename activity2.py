num = int(input("Digite um número inteiro: "))

fibonacci = [0, 1] 
while fibonacci[-1] < num:  
    fibonacci.append(fibonacci[-1] + fibonacci[-2])  

if num in fibonacci:  
    print(f"{num} pertence à sequência de Fibonacci!")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
