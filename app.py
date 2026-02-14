import streamlit as st
import time
import random
from PIL import Image
import base64

# Configuração da página
st.set_page_config(page_title="👁️‍🗨️ SYSTEM: ACTIVE", layout="centered", initial_sidebar_state="collapsed")

# Estilo CSS para fundo preto, fonte terminal e efeitos
st.markdown("""
<style>
    body { background-color: #000; color: #0f0; }
    .stApp { background-color: #000; }
    h1, h2, h3, p, div { color: #0f0 !important; font-family: 'Courier New', monospace; }
    .blink { animation: blink 1.2s infinite; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
</style>
""", unsafe_allow_html=True)

# Tela principal
st.title("👁️‍🗨️ SISTEMA DE VIGILÂNCIA ATIVO")
st.write("Acesso restrito. Nível de ameaça: **CRÍTICO**")

if st.button("🔴 INICIAR VARREDURA PROFUNDA"):
    # Simula análise em tempo real
    messages = [
        "INICIANDO PROTOCOLO X9...",
        "ESCOANEANDO REDE LOCAL...",
        "DETECTANDO DISPOSITIVOS...",
        "ANALISANDO HISTÓRICO DE NAVEGAÇÃO...",
        "VERIFICANDO CÂMERAS CONECTADAS...",
        "ACESSO À WEBCAM: **PERMITIDO**",
        "LOCALIZAÇÃO GPS: FIXADA",
        "IDENTIDADE CONFIRMADA: **TONY BORA**",
        "AMBIENTE: COMPROMETIDO",
        "⚠️ MOVIMENTO DETECTADO EM CÂMERA 2"
    ]

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i, msg in enumerate(messages):
        time.sleep(random.uniform(0.8, 1.5))
        progress_bar.progress(int((i + 1) / len(messages) * 100))
        status_text.markdown(f'<p class="blink">→ {msg}</p>', unsafe_allow_html=True)

    time.sleep(1)
    st.balloons()  # só pra desativar UI normal — substitua por som se quiser
    st.markdown('<h2 style="color:red;">💀 ALERTA MÁXIMO: VOCÊ ESTÁ SENDO OBSERVADO</h2>', unsafe_allow_html=True)

    # Mostra imagem assustadora (adicione seu próprio arquivo em assets/)
    try:
        img = Image.open("assets/scary_image.jpg")
        st.image(img, use_column_width=True)
    except:
        st.text("⚠️ IMAGEM SECRETA CARREGADA NA MEMÓRIA\n(Não visível por segurança)")

    st.markdown("""
    <h3 style="color:#f00;">⚠️ NÃO FECHE ESTA JANELA.</h3>
    <p>Seu dispositivo foi marcado no Protocolo Eclipse.<br>
    Desligar = ativa rastreamento biométrico.<br>
    <b>Permaneça conectado.</b></p>
    """, unsafe_allow_html=True)

    # Opcional: tocar som (não suportado nativo no Streamlit, mas pode usar HTML5 se rodar local)
    # st.audio("assets/scan_sound.mp3", format="audio/mp3")
