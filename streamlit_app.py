import streamlit as st

st.set_page_config(page_title="Planejador Financeiro", page_icon="💰")

st.title("💰 Meu Planejamento Financeiro")
st.write("Digite seu salário mensal para ver a divisão ideal baseada na regra 60/30/10.")

# Caixa de entrada visual para o celular
sal = st.number_input("Digite seu salário mensal R$:", min_value=0.0, value=2000.0, step=100.0)

if sal > 0:
    # Cálculos financeiros base do seu código original
    montante_renda_passiva = sal * 200
    investimento_ideal = sal * 0.10
    reserva_emergencia = sal * 6
    contas_fixas = sal * 0.60
    lazer = sal * 0.30

    st.markdown("---")
    st.subheader("📊 Seus Números:")

    # Organização visual em cartões na tela do celular
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Renda Passiva Alvo", value=f"R$ {montante_renda_passiva:,.2f}")
        st.metric(label="Gasto Fixo Máximo (60%)", value=f"R$ {contas_fixas:,.2f}")
        st.metric(label="Investimento Mensal (10%)", value=f"R$ {investimento_ideal:,.2f}")
    with col2:
        st.metric(label="Reserva de Emergência", value=f"R$ {reserva_emergencia:,.2f}")
        st.metric(label="Valor para Lazer (30%)", value=f"R$ {lazer:,.2f}")

