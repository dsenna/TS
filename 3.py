faturamento_diario = [1500, 2100, 1800, 1900, 2400, 0, 0, 2250, 2500, 2100, 1900, 2200, 0, 0, 2000, 1700, 1900, 2300, 2000, 0, 0, 2400, 2000, 2300, 2500, 1900,0,0]
 
menor_faturamento = min(faturamento_diario)

maior_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)

print(f"Menor faturamento diário: {menor_faturamento}")
print(f"Maior faturamento diário: {maior_faturamento}")
print(f"Dias com faturamento diário acima da média mensal ({media_mensal:.2f}): {dias_acima_da_media}")