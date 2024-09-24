faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

percentual_por_estado = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_por_estado.items()}

for estado, percentual in percentual_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")