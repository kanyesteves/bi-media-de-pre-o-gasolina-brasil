import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Gasoliina Brasil-BI"
)

df_2000 = pd.read_csv("../datasets/gasolina_2000+.csv", index_col=0)
df_2010 = pd.read_csv("../datasets/gasolina_2010+.csv", index_col=0)
df = pd.concat([df_2000, df_2010])

# ETL
df["DATA FINAL"] = pd.to_datetime(df["DATA FINAL"])
df["DATA INICIAL"] = pd.to_datetime(df["DATA INICIAL"])
df["ANO-MES"] = df["DATA FINAL"].apply(lambda x: "{}".format(x.year)) + df["DATA FINAL"].apply(lambda x: "/{:02d}".format(x.month))


# BODY
product = st.selectbox("Combustíveis", df["PRODUTO"].unique())
df_product = df[df["PRODUTO"] == product]
df_product["MES"] = df_product["DATA FINAL"].apply(lambda x: x.month)
df_product["ANO"] = df_product["DATA FINAL"].apply(lambda x: x.year)

st.divider()

st.title("Média do preço de revenda")
df_filtered_bar = df_product.groupby("ANO")[["ANO", "PREÇO MÉDIO REVENDA"]].mean()
st.bar_chart(df_filtered_bar, x="ANO", y="PREÇO MÉDIO REVENDA")

st.title("Percentual de aumento de ano a ano")
df_percentual = df_filtered_bar["PREÇO MÉDIO REVENDA"].pct_change() * 100
df_percentual = df_percentual.rename("Percentual de Aumento")
df_percentual
st.line_chart(df_percentual, x="ANO", y="PREÇO MÉDIO REVENDA")
