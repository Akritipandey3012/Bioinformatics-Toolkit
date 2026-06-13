import streamlit as st

st.title("🧬 Bioinformatics Toolkit")

dna = st.text_input("Enter DNA Sequence")

if st.button("Calculate GC Content"):

    if len(dna) > 0:

        g = dna.count("G")
        c = dna.count("C")

        gc = ((g+c)/len(dna))*100

        st.write("GC Content =", round(gc,2), "%")