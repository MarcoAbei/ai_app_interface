import streamlit as st
import pandas as pd
import base64

st.markdown(
    """
    <style>
    body {
        background-color: #0066cd !important;
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
st.title("📄 Generazione e Download del Documento")

st.subheader("Inserisci i dati richiesti")

# Creazione dei campi di input
n_protocollo_decreto = st.number_input("N_PROTOCOLLO_DECRETO_APPROVAZIONE", step=1)
data_protocollo_decreto = st.date_input("DATA_PROTOCOLLO_DECRETO_APPROVAZIONE")
n_visto_acquisto_mef = st.number_input("N_VISTO_ACQUISTO_MEF", step=1)
data_visto_acquisto_mef = st.date_input("DATA_VISTO_ACQUISTO_MEF")
modalita_acquisto = st.text_input("MODALITA_ACQUISTO")
n_ordine_acquisto = st.number_input("N_ORDINE_ACQUISTO", step=1)
data_ordine_acquisto = st.date_input("DATA_ORDINE_ACQUISTO")
n_protocollo_ordine_acquisto = st.number_input("N_PROTOCOLLO_ORDINE_ACQUISTO", step=1)
nome_mandataria_rti = st.text_input("NOME_MANDATARIA_RTI")
n_lotto_acquisto = st.number_input("N_LOTTO_ACQUISTO", step=1)
nome_acquisto = st.text_input("NOME_ACQUISTO")
sede_mandataria_rti = st.text_input("SEDE_MANDATARIA_RTI")
n_cig_acquisto = st.text_input("N_CIG_ACQUISTO", max_chars=10)
n_cig_fornitura = st.text_input("N_CIG_FORNITURA", max_chars=10)
causale_acquisto = st.text_area("CAUSALE_ACQUISTO")
importo_acquisto = st.number_input("IMPORTO_ACQUISTO", step=0.01)
sede_acquirente = st.text_area("SEDE_ACQUIRENTE")
impegno_spesa = st.number_input("IMPEGNO_SPESA", step=0.01)
nome_rti = st.text_input("NOME_RTI")
categoria_servizio_mandante = st.text_input("CATEGORIA_SERVIZIO_MANDANTE")
n_decreto_fornitura = st.number_input("N_DECRETO_FORNITURA", step=1)
data_decreto_fornitura = st.date_input("DATA_DECRETO_FORNITURA")
n_visto_fornitura_mef = st.number_input("N_VISTO_FORNITURA_MEF", step=1)
data_visto_fornitura_mef = st.date_input("DATA_VISTO_FORNITURA_MEF")
n_offerta_fornitura = st.number_input("N_OFFERTA_FORNITURA", step=1)
data_offerta_fornitura = st.date_input("DATA_OFFERTA_FORNITURA")
n_fattura_fornitura = st.text_input("N_FATTURA_FORNITURA")
data_fattura_fornitura = st.date_input("DATA_FATTURA_FORNITURA")
importo_fattura_fornitura = st.number_input("IMPORTO_FATTURA_FORNITURA", step=0.01)
nome_mandante = st.text_input("NOME_MANDANTE")
data_accettazione_fattura_fornitura = st.date_input("DATA_ACCETTAZIONE_FATTURA_FORNITURA")
causale_fattura_fornitura = st.text_area("CAUSALE_FATTURA_FORNITURA")
importo_imponibile_fornitura = st.number_input("IMPORTO_IMPONIBILE_FORNITURA", step=0.01)
importo_iva_fornitura = st.number_input("IMPORTO_IVA_FORNITURA", step=0.01)
data_erogazione_fornitura = st.text_area("DATA_EROGAZIONE_FORNITURA")
sede_mandante = st.text_input("SEDE_MANDANTE")
n_piva_mandataria_rti = st.text_input("N_PIVA_MANDATARIA_RTI", max_chars=11)
cod_fisc_mandataria_rti = st.text_input("COD_FISC_MANDATARIA_RTI", max_chars=11)
n_iban_mandataria_rti = st.text_input("N_IBAN_MANDATARIA_RTI")
n_capitolo_stato_previsione = st.text_input("N_CAPITOLO_STATO_PREVISIONE")
anno_esercizio_finanziario = st.number_input("ANNO_ESERCIZIO_FINANZIARIO", step=1, min_value=1900, max_value=2100)

# Bottone di generazione e download PDF
if st.button("Genera e Scarica PDF"):
    pdf_link = get_pdf_download_link("decreto_sample.pdf")
    st.markdown(pdf_link, unsafe_allow_html=True)
