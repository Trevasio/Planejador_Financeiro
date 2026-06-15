import streamlit as st

st.set_page_config(page_title="Planejador Financeiro", page_icon="💰", layout="centered")

st.title("💰 Meu Planejamento Financeiro")
st.write("Insira seu salário mensal para calcular suas metas automaticamente.")

# CSS para forçar textos gigantes em qualquer navegador de celular
st.markdown("""
    <style>
    /* Tamanho do texto do campo de entrada */
    .stNumberInput label p {
        font-size: 26px !important;
        font-weight: bold !important;
        color: #1E88E5 !important;
    }
    /* Deixa as caixas de texto com letras maiores */
    input {
        font-size: 22px !important;
    }
    /* Estilo customizado para os títulos dos resultados */
    .titulo-resultado {
        font-size: 24px !important;
        font-weight: bold !important;
        margin-top: 15px !important;
        display: block;
    }
    /* Estilo customizado para os valores numéricos */
    .valor-resultado {
        font-size: 28px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# Campo de entrada que começa vazio (value=None)
sal = st.number_input("Digite seu salário mensal R$:", min_value=0.0, step=100.0, value=None, placeholder="Ex: 3000.00")

if sal is not None and sal > 0:
    montante_renda_passiva = sal * 200
    investimento_ideal = sal * 0.10
    reserva_emergencia = sal * 6
    contas_fixas = sal * 0.60
    lazer = sal * 0.30

    st.markdown("---")
    st.subheader("📊 Seus Números:")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"<span class='titulo-resultado'>📌 Renda Passiva Alvo</span><span class='valor-resultado' style='color:#2E7D32;'>R$ {montante_renda_passiva:,.2f}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='titulo-resultado'>📌 Gasto Fixo Máximo (60%)</span><span class='valor-resultado' style='color:#C62828;'>R$ {contas_fixas:,.2f}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='titulo-resultado'>📌 Investimento Mensal (10%)</span><span class='valor-resultado' style='color:#1565C0;'>R$ {investimento_ideal:,.2f}</span>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<span class='titulo-resultado'>📌 Reserva de Emergência</span><span class='valor-resultado' style='color:#EF6C00;'>R$ {reserva_emergencia:,.2f}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='titulo-resultado'>📌 Valor para Lazer (30%)</span><span class='valor-resultado' style='color:#AD1457;'>R$ {lazer:,.2f}</span>", unsafe_allow_html=True)

    st.markdown("---")
