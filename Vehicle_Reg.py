import streamlit as st
import pandas as pd
import re
from collections import Counter

st.set_page_config(page_title="Vehicle Registration Analyzer", layout="wide")

pattern=r"\b[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}\b"

st.title("Vehicle Registration Analyzer")

vehicle=st.text_input("Enter Vehicle Number")

if vehicle:
    if re.fullmatch(pattern,vehicle.upper()):
        m=re.match(r"([A-Z]{2})([0-9]{1,2})([A-Z]{1,3})([0-9]{4})",vehicle.upper())
        st.success("Valid Vehicle Number")
        st.write({
            "State":m.group(1),
            "RTO":m.group(2),
            "Series":m.group(3),
            "Number":m.group(4)
        })
    else:
        st.error("Invalid Vehicle Number")

file=st.file_uploader("Upload Vehicle Records",type="txt")

if file:
    text=file.read().decode()

    text=re.sub(r"[- ]","",text.upper())

    vehicles=re.findall(pattern,text)

    if vehicles:
        df=pd.DataFrame({"Vehicle Number":vehicles})
        df["State"]=df["Vehicle Number"].str[:2]

        st.subheader("Vehicle Records")
        st.dataframe(df,use_container_width=True)

        st.metric("Total Vehicles",len(df))
        st.metric("Unique Vehicles",df["Vehicle Number"].nunique())

        duplicates=[k for k,v in Counter(vehicles).items() if v>1]

        if duplicates:
            st.subheader("Duplicate Vehicles")
            st.write(duplicates)

        state=st.text_input("Search State Code")

        if state:
            result=df[df["State"]==state.upper()]
            st.dataframe(result,use_container_width=True)

        st.subheader("State Wise Count")
        st.bar_chart(df["State"].value_counts())

        csv=df.to_csv(index=False).encode()
        st.download_button("Download CSV",csv,"cleaned_vehicle_records.csv","text/csv")
    else:
        st.warning("No valid vehicle numbers found.")