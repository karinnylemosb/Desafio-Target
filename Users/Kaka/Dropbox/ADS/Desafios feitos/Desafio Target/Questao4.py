def porcentagem (estado, faturamentoTotal):
    return round(((100*estado)/faturamentoTotal),2)


sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53


faturamentoTotal = sp + rj + mg + es + outros


print("Porcentagem do faturamento de SP:" + str(porcentagem(sp, faturamentoTotal)) + '%')
print("Porcentagem do faturamento de RJ:" + str(porcentagem(rj, faturamentoTotal)) + '%')
print("Porcentagem do faturamento de MG:" + str(porcentagem(mg, faturamentoTotal)) + '%')
print("Porcentagem do faturamento de ES:" + str(porcentagem(es, faturamentoTotal)) + '%')
print("Porcentagem de outros faturamentos:" + str(porcentagem(outros, faturamentoTotal)) + '%')
