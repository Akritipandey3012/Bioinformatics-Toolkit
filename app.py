import streamlit as st

st.set_page_config(page_title="Bioinformatics Toolkit", page_icon="🧬")

st.title("🧬 Bioinformatics Toolkit v1.0")

option = st.sidebar.selectbox(
    "Choose Tool",
    [
        "DNA Validation",
        "GC Content",
        "DNA to RNA",
        "Start Codon Finder",
        "Motif Finder",
        "Restriction Site Finder (EcoRI)",
        "Mutation Detection"
    ]
)

# DNA Validation
if option == "DNA Validation":

    dna = st.text_input("Enter DNA Sequence")

    if st.button("Validate"):

        dna = dna.upper()

        valid = True

        for base in dna:
            if base not in "ATGC":
                valid = False

        if valid:
            st.success("Valid DNA Sequence ✅")
        else:
            st.error("Invalid DNA Sequence ❌")


# GC Content
elif option == "GC Content":

    dna = st.text_input("Enter DNA Sequence")

    if st.button("Calculate GC Content"):

        dna = dna.upper()

        if len(dna) > 0:

            g = dna.count("G")
            c = dna.count("C")

            gc = ((g + c) / len(dna)) * 100

            st.success(f"GC Content = {round(gc,2)} %")


# DNA to RNA
elif option == "DNA to RNA":

    dna = st.text_input("Enter DNA Sequence")

    if st.button("Convert"):

        rna = dna.upper().replace("T", "U")

        st.success(f"RNA Sequence: {rna}")


# Start Codon Finder
elif option == "Start Codon Finder":

    dna = st.text_input("Enter DNA Sequence")

    if st.button("Find Start Codon"):

        pos = dna.upper().find("ATG")

        if pos != -1:
            st.success(f"Start codon found at position {pos+1}")
        else:
            st.warning("No start codon found")


# Motif Finder
elif option == "Motif Finder":

    dna = st.text_input("Enter DNA Sequence")

    motif = st.text_input("Enter Motif")

    if st.button("Find Motif"):

        dna = dna.upper()
        motif = motif.upper()

        positions = []

        for i in range(len(dna)-len(motif)+1):

            if dna[i:i+len(motif)] == motif:
                positions.append(i+1)

        if positions:
            st.success(f"Motif found at positions: {positions}")
        else:
            st.warning("Motif not found")


# Restriction Site Finder
elif option == "Restriction Site Finder (EcoRI)":

    dna = st.text_input("Enter DNA Sequence")

    if st.button("Find EcoRI Site"):

        site = "GAATTC"

        pos = dna.upper().find(site)

        if pos != -1:
            st.success(f"EcoRI site found at position {pos+1}")
        else:
            st.warning("EcoRI site not found")


# Mutation Detection
elif option == "Mutation Detection":

    dna1 = st.text_input("First DNA Sequence")

    dna2 = st.text_input("Second DNA Sequence")

    if st.button("Detect Mutation"):

        dna1 = dna1.upper()
        dna2 = dna2.upper()

        if len(dna1) != len(dna2):

            st.error("DNA lengths are different")

        else:

            mutations = []

            for i in range(len(dna1)):

                if dna1[i] != dna2[i]:

                    mutations.append(
                        f"Position {i+1}: {dna1[i]} → {dna2[i]}"
                    )

            if mutations:

                st.success("Mutations Found")
                for m in mutations:
                    st.write(m)

            else:
                st.success("No mutation found")
