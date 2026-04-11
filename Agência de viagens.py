# 1) Descrição (comentários)
# descontos progressivos dependendo do númemro de viajantes no mesmo grupo e mesma residência:
# Variáveis:
  # RECEBER VALOR BRUTO DO PACOTE
  # CATEGORIA DOS ASSENTOS NO VOO
  # QUATIDADE DE VIAJANTES QUE MORAM NA MESMA CASA


# TABELA CATEGORIA DE DESCONTOS:

#CATEGORIA             DESCONTOS       DESCONTOS
#ECONÔMICA            2 VIAJANTES         3%
#ECONÔMICA            3 VIAJANTES         4%
#ECONÔMICA         4 VIAJANTES OU MAIS    8%
#EXECUTIVA            2 VIAJANTES         5%
#EXECUTIVA            3 VIAJANTES         7%
#EXECUTIVA         4 VIAJANTES OU MAIS    8%
#PRIMEIRA CLASSE      2 VIAJANTES         5%
#PRIMEIRA CLASSE      3 VIAJANTES         15%

# O PROGRAMA DEVERÁ EXIBIR:
    # BRUTO DA VIAGEM (MESMO QUE FOI D IGITADO)
    # VALOR DO DESCONTO
    # VALOR LÍQUIDO DA VIAGEM (VALOR BRUTO MENOS OS DESCONTOS)
    # VALOR MÉDIO POR VIAJANTE

# 2) Entrada de dados (input):
valor_bruto= float(input("Digite o valor bruto: R$ "))
passageiros= int(input("quantos passageiros? "))
categoria= input("Digite a categoria: (economica/executiva/primeira clase)")

# 3)Processamento (regras de desconto):
desconto = 0
if categoria == "economica":
    if passageiros == 2:
        desconto = 0.03
    elif passageiros == 3:
        desconto = 0.05
    elif passageiros >= 4:
        desconto = 0.08
elif categoria == "executiva":
    if passageiros == 2:
        desconto = 0.05
    elif passageiros == 3:
        desconto = 0.07
    elif passageiros >= 4:
        desconto = 0.08
elif categoria == "primeira classe":
    if passageiros == 2:
        desconto = 0.1
    elif passageiros == 3:
        desconto = 0.15

# 4) cálculos:
valor_de_desconto = valor_bruto * desconto
valor_liquido = valor_bruto - valor_de_desconto
valor_por_pessoa = valor_liquido / passageiros

# 5) saída:
print(f"\nValor bruto: R${valor_bruto:.2f}")
print(f"Desconto: R${valor_de_desconto:.2f}")
print(f"Valor líquido: R${valor_liquido:.2f}")
print(f"Valor_por_pessoa: R${valor_por_pessoa:.2f}")

print("Esperamos que tenha gostado da experiência. Volte sempre!")
