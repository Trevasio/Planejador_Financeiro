import streamlit as st

st.set_page_config(page_title="Planejador Financeiro", page_icon="💰", layout="centered")

st.title("💰 Meu Planejamento Financeiro")
st.write("Insira seu salário mensal para calcular suas metas automaticamente.")

# CSS personalizado para deixar o texto do campo de entrada ("Digite seu salário...") bem grande
st.markdown("""
    <style>
    .stNumberInput label p {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #1E88E5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Campo de entrada que começa totalmente vazio (None) e aceita qualquer valor numérico
sal = st.number_input("Digite seu salário mensal R$:", min_value=0.0, step=100.0, value=None, placeholder="Ex: 3000.00")

# O código abaixo só roda se o usuário digitar um salário válido e maior que zero
if sal is not None and sal > 0:
    # Cálculos base do seu código
    montante_renda_passiva = sal * 200
    investimento_ideal = sal * 0.10
    reserva_emergencia = sal * 6
    contas_fixas = sal * 0.60
    lazer = sal * 0.30

    st.markdown("---")
    st.subheader("📊 Seus Números:")

    # Exibição dos resultados com títulos customizados e letras bem maiores
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### **Renda Passiva Alvo**<br><span style='font-size:26px; color:#2E7D32;'>R$ {montante_renda_passiva:,.2f}</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True) # Espaçador
        st.markdown(f"### **Gasto Fixo Máximo (60%)**<br><span style='font-size:26px; color:#C62828;'>R$ {contas_fixas:,.2f}</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"### **Investimento Mensal (10%)**<br><span style='font-size:26px; color:#1565C0;'>R$ {investimento_ideal:,.2f}</span>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"### **Reserva de Emergência**<br><span style='font-size:26px; color:#EF6C00;'>R$ {reserva_emergencia:,.2f}</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"### **Valor para Lazer (30%)**<br><span style='font-size:26px; color:#AD1457;'>R$ {lazer:,.2f}</span>", unsafe_allow_html=True)

    st.markdown("---")
