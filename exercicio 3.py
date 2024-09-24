import json

with open('faturamento.json', 'r') as files:
    dados = json.load(files)

faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamento_diario)

maior_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum (1 for valor in faturamento_diario if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")