import streamlit as st
import pandas as pd
import base64

# Impostare l'app in modalità full screen
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Cambia lo sfondo dell'intera app */
    [data-testid="stAppViewContainer"] {
        background-color: #0066cd; /* Sostituisci con il colore che preferisci */
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
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="decreto_sample.pdf" style="color: white; text-decoration: none; font-weight: bold;">📄 {file_label}</a>'
    return href

# Titolo dell'app
st.image("logo.svg", width=800)
st.title("📄 Generatore di Decreti di Liquidazione")

st.subheader("Inserisci i dati richiesti per generare il Decreto di Liquidazione completo")

# Dizionario con valori predefiniti
default_values = {
    "NUMERO DI PROTOCOLLO DEL DECRETO DI APPROVAZIONE": 785,
    "DATA DI PROTOCOLLO DEL DECRETO DI APPROVAZIONE": "2023-07-19",
    "CODICE DEL VISTO RILASCIATO DAL MEF": 242,
    "DATA DEL VISTO RILASCIATO DAL MEF": "2023-08-08",
    "MODALITA' DI ACQUISTO": "Ordine principale di fornitura",
    "NUMERO DELL'ORDINE DI ACQUISTO": 7258444,
    "DATA DELL'ORDINE DI ACQUISTO": "2022-05-24",
    "NUMERO DI PROTOCOLLO DELL'ORDINE DI ACQUISTO": 3998,
    "NOME DELLA SOCIETA' MANDATARIA DEL RTI": "Engie servizi s.p.a",
    "NUMERO DEL LOTTO DELLA CONVENZIONE/CONTRATTO": 10,
    "NOME DELLA CONVENZIONE/CONTRATTO": "Convenzione Facility Management 4",
    "SEDE LEGALE DELLA SOCIETA' MANDATARIA DEL RTI": "Roma, Via Giorgio Ribotta n. 31",
    "NUMERO CIG DELLA CONVEZIONE/CONTRATTO": "9773340F4B"
    "CAUSALE DELLA CONVEZIONE/CONTRATTO": "manutenzione impianti elettrici, manutenzione impianti elevatori, manutenzione impianti antincendio, manutenzione impianti di sicurezza e controllo accessi, manutenzione reti, servizio di pulizia, servizio di disinfestazione, servizio di raccolta e smaltimento rifiuti speciali"
    "IMPORTO DELLA CONVEZIONE/CONTRATTO": 7531095.97 
    "SEDE DELL'UFFICIO MLPS ACQUIRENTE": "Roma alla Via Flavia n. 6, Via Fornovo n. 8, Via V. Veneto n. 56, Via San Nicola da Tolentino. n. 5, Via Fornovo n. 8, palazzina C, sede ANPAL, Via Flavia n. 6, 5° piano"
    "IMPEGNO DI SPESA": 7383095.97
    "NOME DEL RTI": "RTI Engie servizi S.p.A. (Mandataria – Capogruppo) – Consorzio Stabile Energie Locali S.c.a r.l. – Colser Soc.Cooperativa – Consorzio Nazionale Cooperative Pluriservizi Attività 360 Soc. Cooperativa – Consorzio GISA –Society Moderne Facility Management S.r.l."
    "CATEGORIA DI SERVIZIO DELLA SOCIETA' MANDANTE": "servizi di pulizia, di disinfestazione e di raccolta e smaltimento rifiuti speciali"
    "NUMERO DEL DECRETO CON CUI SI APPROVA LA FORNITURA": 599
    "DATA DEL DECRETO CON CUI SI APPROVA LA FORNITURA": "2024-05-21"
    "NUMERO DEL VISTO RILASCIATO DAL MEF PER LA FORNITURA SPECIFICA": 4656
    "DATA DEL VISTO RILASCIATO DAL MEF PER LA FORNITURA SPECIFICA": "2025-05-20"
    "NUMERO DELL'OFFERTA DI FORNITURA": 7258444
    "DATA DELL'OFFERTA DI FORNITURA": "2024-11-22"
    "NUMERO DI FATTURA DELLA FORNITURA": "21/14314"
    "DATA DI FATTURA DELLA FORNITURA": "2024-29-11"
    "IMPORTO DELLA FORNITURA": 5909.05
    "NOME DELLA SOCIETA' MANDANTE": "Colser Soc. Cooperativa"
    "DATA DI ACCETTAZIONE DELLA FATTURA": "2024-12-02"
    "CAUSALE DELLA FORNITURA": "fornitura di materiale igienico-sanitario"
    "IMPORTO IMPONIBILE DELLA FORNITURA": 4843.48
    "IMPORTO IVA DELLA FORNITURA": 1065.57
    "DATA DI EROGAZIONE DELLA FORNITURA": "2025-11-01"
    "NUMERO DI PIVA DELLA SOCIETA' MANDATARIA DEL RTI": "00378740344"
    "CODICE FISCALE DELLA SOCIETA' MANDATARIA DEL RTI": "00378740344"
    "NUMERO IBAN DELLA SOCIETA' MANDATARIA DEL RTI": "IT20W0200805364000103166235"
    "NUMERO DI CAPITOLO DELLO STATO PREVISIONALE": "3111 pg 7"
    "ANNO DI ESERCIZIO FINANZIARIO": 2024
}

# Creazione delle colonne (due colonne di uguale larghezza)
col1, col2 = st.columns(2)

def animated_input(label, key, default_value, delay=0.5):
    time.sleep(delay)
    return st.text_input(label, value=default_value, key=key)

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
    data_visto_fornitura_mef = st.date_input("DATA DEL VISTO RILASCIATO DAL MEF PER LA FORNITURA SPECIFICA")
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
    #sede_mandante = st.text_input("SEDE DEL MANDANTE")
    n_piva_mandataria_rti = st.text_input("NUMERO DI PIVA DELLA SOCIETA' MANDATARIA DEL RTI", max_chars=11)
    cod_fisc_mandataria_rti = st.text_input("CODICE FISCALE DELLA SOCIETA' MANDATARIA DEL RTI", max_chars=11)
    n_iban_mandataria_rti = st.text_input("NUMERO IBAN DELLA SOCIETA' MANDATARIA DEL RTI")
    n_capitolo_stato_previsione = st.text_input("NUMERO DI CAPITOLO DELLO STATO PREVISIONALE")
    anno_esercizio_finanziario = st.number_input("ANNO DI ESERCIZIO FINANZIARIO", step=1, min_value=2020, max_value=2100)

# Bottone di generazione e download PDF
st.markdown("<hr>", unsafe_allow_html=True)  # Separatore estetico
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Genera e Scarica PDF"):
    pdf_link = get_pdf_download_link("decreto_sample.pdf")
    st.markdown(pdf_link, unsafe_allow_html=True)
