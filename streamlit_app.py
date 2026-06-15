sal = float(input("Digite seu salário mensal R$: "))
montante_renda_passiva = sal * 200
investimento_ideal = sal * 0.10
reserva_emergencia = sal * 6
contas_fixas = sal * 0.60
lazer = sal * 0.30

# Exibição dos resultados com formatação limpa e alinhada
print(f"\n{'='*15} PLANEJAMENTO FINANCEIRO {'='*15}")
print(f"Com o salário atual de:         R$ {sal:,.2f}")
print(f"Montante para viver de renda:   R$ {montante_renda_passiva:,.2f}")
print(f"Investimento mensal ideal (10%): R$ {investimento_ideal:,.2f}")
print(f"Reserva de emergência (6 meses):R$ {reserva_emergencia:,.2f}")
print(f"Gasto máximo com contas (60%):  R$ {contas_fixas:,.2f}")
print(f"Valor máximo para lazer (30%):  R$ {lazer:,.2f}")
print("=" * 55)
