import streamlit as st
import pandas as pd
import base64

import streamlit as st

st.markdown(
    """
    <style>
    /* Cambia lo sfondo dell'intera app */
    [data-testid="stAppViewContainer"] {
        background-color: white; /* Sostituisci con il colore che preferisci */
    }

    /* Cambia lo sfondo della barra laterale */
    [data-testid="stSidebar"] {
        background-color: #d3d3d3 !important; /* Grigio chiaro */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Funzione per caricare il file PDF
@st.cache_data
def get_pdf_download_link(file_path, file_label="Scarica il documento"):
    with open(file_path, "rb") as file:
        pdf_bytes = file.read()
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="decreto_sample.pdf">📄 {file_label}</a>'
    return href

# Titolo dell'app
st.image("logo.svg", width=800)
st.title("📄 Generatore di Decreti di Liquidazione")

st.subheader("Inserisci i dati richiesti per generare il Decreto di Liquidazione completo")

# Creazione delle colonne (due colonne di uguale larghezza)
col1, col2 = st.columns(2)

# Creazione dei campi di input
with col1:
    st.subheader("Premesse specifiche")
    n_protocollo_decreto = st.number_input("NUMERO DI PROTOCOLLO DEL DECRETO DI APPROVAZIONE", step=1)
    data_protocollo_decreto = st.date_input("DATA DI PROTOCOLLO DEL DECRETO DI APPROVAZIONE")
    n_visto_acquisto_mef = st.number_input("CODICE DEL VISTO RILASCIATO DAL MEF", step=1)
    data_visto_acquisto_mef = st.date_input("DATA DEL VISTO RILASCIATO DAL MEF")
    modalita_acquisto = st.text_input("MODALITA' DI ACQUISTO")
    n_ordine_acquisto = st.number_input("NUMERO DELL'ORDINE DI ACQUISTO", step=1)
    data_ordine_acquisto = st.date_input("DATA DELL'ORDINE DI ACQUISTO")
    n_protocollo_ordine_acquisto = st.number_input("NUMERO DI PROTOCOLLO DELL'ORDINE DI ACQUISTO", step=1)
    nome_mandataria_rti = st.text_input("NOME DELLA SOCIETA' MANDATARIA DEL RTI")
    n_lotto_acquisto = st.number_input("NUMERO DEL LOTTO DELLA CONVENZIONE/CONTRATTO", step=1)
    nome_acquisto = st.text_input("NOME DELLA CONVENZIONE/CONTRATTO")
    sede_mandataria_rti = st.text_input("SEDE LEGALE DELLA SOCIETA' MANDATARIA DEL RTI")
    n_cig_acquisto = st.text_input("NUMERO CIG DELLA CONVEZIONE/CONTRATTO", max_chars=10)
    n_cig_fornitura = st.text_input("NUMERO CIG DELLA FORNITURA SPECIFICA", max_chars=10)
    causale_acquisto = st.text_area("CAUSALE DELLA CONVEZIONE/CONTRATTO")
    importo_acquisto = st.number_input("IMPORTO DELLA CONVEZIONE/CONTRATTO", step=0.01)
    sede_acquirente = st.text_area("SEDE DELL'UFFICIO MLPS ACQUIRENTE")
    impegno_spesa = st.number_input("IMPEGNO DI SPESA", step=0.01)
    nome_rti = st.text_input("NOME DEL RTI")
    categoria_servizio_mandante = st.text_input("CATEGORIA DI SERVIZIO DELLA SOCIETA' MANDANTE")
    n_decreto_fornitura = st.number_input("NUMERO DEL DECRETO CON CUI SI APPROVA LA FORNITURA", step=1)
    data_decreto_fornitura = st.date_input("DATA DEL DECRETO CON CUI SI APPROVA LA FORNITURA")
    n_visto_fornitura_mef = st.number_input("NUMERO DEL VISTO RILASCIATO DAL MEF PER LA FORNITURA SPECIFICA", step=1)
    data_visto_fornitura_mef = st.date_input("DATA DEL VISTORILASCIATO DAL MEF PER LA FORNITURA SPECIFICA")
    n_offerta_fornitura = st.number_input("NUMERO DELL'OFFERTA DI FORNITURA", step=1)
    data_offerta_fornitura = st.date_input("DATA DELL'OFFERTA DI FORNITURA")

with col2:
    st.subheader("Dispositivo")
    n_fattura_fornitura = st.text_input("NUMERO DI FATTURA DELLA FORNITURA")
    data_fattura_fornitura = st.date_input("DATA DI FATTURA DELLA FORNITURA")
    importo_fattura_fornitura = st.number_input("IMPORTO DELLA FORNITURA", step=0.01)
    nome_mandante = st.text_input("NOME DELLA SOCIETA' MANDANTE")
    data_accettazione_fattura_fornitura = st.date_input("DATA DI ACCETTAZIONE DELLA FATTURA")
    causale_fattura_fornitura = st.text_area("CAUSALE DELLA FORNITURA")
    importo_imponibile_fornitura = st.number_input("IMPORTO IMPONIBILE DELLA FORNITURA", step=0.01)
    importo_iva_fornitura = st.number_input("IMPORTO IVA DELLA FORNITURA", step=0.01)
    data_erogazione_fornitura = st.text_area("DATA DI EROGAZIONE DELLA FORNITURA")
    sede_mandante = st.text_input("SEDE DEL MANDANTE")
    n_piva_mandataria_rti = st.text_input("NUMERO DI PIVA DELLA SOCIETA' MANDATARIA DEL RTI", max_chars=11)
    cod_fisc_mandataria_rti = st.text_input("CODICE FISCALE DELLA SOCIETA' MANDATARIA DEL RTI", max_chars=11)
    n_iban_mandataria_rti = st.text_input("NUMERO IBAN DELLA SOCIETA' MANDATARIA DEL RTI")
    n_capitolo_stato_previsione = st.text_input("NUMERO DI CAPITOLO DELLO STATO PREVISIONALE")
    anno_esercizio_finanziario = st.number_input("ANNO DI ESERCIZIO FINANZIARIO", step=1, min_value=2024, max_value=2100)

# Bottone di generazione e download PDF
st.markdown("<hr>", unsafe_allow_html=True)  # Separatore estetico
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Genera e Scarica PDF"):
    pdf_link = get_pdf_download_link("decreto_sample.pdf")
    st.markdown(pdf_link, unsafe_allow_html=True)
