import streamlit as st
from functions.noten import parse_list, weighted_average, grade_label

st.title("Notenrechner (CH‑Skala: 6=best, 4=Bestanden)")
st.write("Noten kommasepariert eingeben. Optional Gewichte (kommasepariert). Beispiel: Noten: 5,4.5,3.5  Gewichte: 2,1,1")

with st.form("noten_form"):
    grades_s = st.text_input("Noten (kommasepariert)", value="5,4.5,4")
    weights_s = st.text_input("Gewichte optional (kommasepariert)", value="")
    submit = st.form_submit_button("Berechnen")

if submit:
    grades = parse_list(grades_s)
    weights = parse_list(weights_s) if weights_s.strip() != "" else None
    avg = weighted_average(grades, weights)
    if avg is None:
        st.error("Ungültige Eingabe. Prüfe Noten/Gewichte.")
    else:
        st.subheader("Ergebnis")
        st.write(f"Durchschnitt: **{avg:.2f}**")
        st.write(f"Bewertung: **{grade_label(avg)}**")
        st.write("- Hinweis: Schweizer Skala (6 = beste Note; 4 = bestanden).")
