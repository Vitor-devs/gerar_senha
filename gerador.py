import string
import random
from time import sleep

print("Olá! Bem-vindo ao super gerador de senhas!")
sleep(1)

print("Aqui você poderá gerar uma senha forte do jeito que quiser")
sleep(1)

print("Espero que goste!")
sleep(1)

tamanho_senha = int(input("Digite quantos caracteres você quer na sua senha: "))
print('-'*30)
sleep(1)

local_senha = str(input("De qual aplicativo seria essa senha? "))
print('-'*30)
sleep(1)

numero_de_senhas = int(input("Digite quantas senhas você deseja criar: "))
print('-'*30)
sleep(1)

adc_pontuação = str(input("Deseja adicionar pontuação a senha? [S/N] (Ela já contém letras e números): ")).upper()[0]

if adc_pontuação in "Nn":
  print(f"As senhas geradas para o {local_senha} foram:")
  for x in range(numero_de_senhas):
    print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(tamanho_senha)))
  print('-'*30)

if adc_pontuação in "Ss":
  print(f"As senhas geradas para o {local_senha} foram:")
  for x in range(numero_de_senhas):
    print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(tamanho_senha)))
  print('-'*30)