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
st.title("Analises de preços dos combustíveis no brasil")
col1, col2 = st.columns([2, 2])
product = col1.selectbox("Combustíveis", df["PRODUTO"].unique())
df_product = df[df["PRODUTO"] == product]
states = col2.multiselect("Estados", df_product["ESTADO"].unique())
df_product_states = df_product[df_product["ESTADO"].isin(states)]

if len(df_product_states) != 0:
    df_product_states["MES"] = df_product_states["DATA FINAL"].apply(lambda x: x.month)
    df_product_states["ANO"] = df_product_states["DATA FINAL"].apply(lambda x: x.year)
else:
    df_product["MES"] = df_product["DATA FINAL"].apply(lambda x: x.month)
    df_product["ANO"] = df_product["DATA FINAL"].apply(lambda x: x.year)

st.divider()
st.subheader("Média do preço de revenda")
col3, col4 = st.columns([2, 1])

if len(df_product_states) != 0:
    df_filtered_bar = df_product_states.groupby("ANO")[["ANO", "PREÇO MÉDIO REVENDA"]].mean()
else:
    df_filtered_bar = df_product.groupby("ANO")[["ANO", "PREÇO MÉDIO REVENDA"]].mean()

max_preco = df_filtered_bar.max()
col3.bar_chart(df_filtered_bar, x="ANO", y="PREÇO MÉDIO REVENDA")
col4.write(f"O aumento entre o ano 2004 e 2021 foi relativamente grande, mas o pico mesmo foi em {max_preco['ANO']:.0f}, onde o combustível {product} alcançou a média R$ {max_preco['PREÇO MÉDIO REVENDA']:.3f}")


st.subheader("Percentual de aumento de ano a ano")
col5, col6 = st.columns([1, 2])
df_percentual = df_filtered_bar["PREÇO MÉDIO REVENDA"].pct_change() * 100
df_percentual_formatted = df_percentual.to_frame().style.format("{:.2%}")
col5.write(f"O percentual apresentado no gráfico ao lado mostra claramente como o preço do combustível {product} teve bastante variação no aumento de em ano")
col6.bar_chart(df_percentual_formatted)
