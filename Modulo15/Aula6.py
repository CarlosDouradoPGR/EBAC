# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


### Criar uma função que gere todos os gráficos

def plot_relatorios(data=pd.DataFrame(), tipo=str.lower):
    # Gráfico idademae x escmae
    if tipo == "idademae ~ escmae":
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15, 5))
        sns.lineplot(y="IDADEMAE",
                     x="DTNASC",
                     data=data,
                     errorbar=None)
#        plt.xticks(sinasc["DTNASC"].dt.month)


    # Histograma do peso do bebê
    elif tipo == "peso":
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15, 5))
        sns.histplot(x="PESO", data=data)
        axes.set_title("Histograma do peso")
        axes.set_ylabel("Frequência")

    # APGAR5 x Peso
    elif tipo == "apgar5 ~ peso":
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15, 5))
        sns.barplot(ax=axes, x="APGAR5", y="PESO", data=data, palette="flare", errorbar=None, estimator="mean")
        sns.lineplot(ax=axes, x="APGAR5", y="PESO", data=data)
        axes.set_title("APGAR5 x Peso")

    # APGAR5 x Gestação
    elif tipo == "apgar5 ~ gestacao":
        # APGAR 5 x Gestação
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15, 5))
        sns.pointplot(ax=axes, x="GESTACAO", y="APGAR5", data=data, errorbar=None, estimator="mean",
                      order=["42 semanas e mais",
                             "37 a 41 semanas",
                             "32 a 36 semanas",
                             "28 a 31 semanas",
                             "22 a 27 semanas",
                             "Menos de 22 semanas"])
        axes.set_title("APGAR5 x Gestação")

    # APGAR5 não realizado
    elif tipo == "apgar5 ~ nulos":
        # Valores não nulos em APGAR5
        apgar5 = sinasc["APGAR5"].count()
        # Valores nulos
        apgar_null = sinasc["APGAR5"].isnull().sum()

        # Quantidade de vezes que não foi realizado o APGAR1 e o APGAR2 naquele mês
        plt.close("all")
        fig, axes = plt.subplots(figsize=(6, 6))

        plt.pie([apgar5, apgar_null], labels=[f"{round(apgar5 * 100 / (apgar5 + apgar_null), 2)}%",
                                              f"{round(apgar_null * 100 / (apgar5 + apgar_null), 2)}%"])
        plt.title("Realizaram APGAR5")
        plt.legend(["Realizado", "Não realizado"], loc='upper right')


    # Escolaridade da mãe x pai ausente
    elif tipo == "escamae ~ pai":
        plt.close("all")
        # Quantidade de Pai ausente e Escolaridade da mãe
        ### DataFrame com a idade do pai nula
        idadepai_null = sinasc.loc[sinasc["IDADEPAI"].isnull() == True][
            ["ESCMAE"]].value_counts().to_frame().reset_index()

        ### DataFrame com a idade do pai não nula
        idadepai = sinasc.loc[sinasc["IDADEPAI"].isnull() == False][["ESCMAE"]].value_counts().to_frame().reset_index()

        fig, axes = plt.subplots(1, 2, figsize=(15, 5))

        sns.barplot(ax=axes[0], x="ESCMAE", y="count", data=idadepai_null, palette="mako", order=["12 anos ou mais",
                                                                                                  "8 a 11 anos",
                                                                                                  "4 a 7 anos",
                                                                                                  "1 a 3 anos",
                                                                                                  "Nenhuma"])
        axes[0].set_ylabel("Freqência")
        axes[0].set_title("Pai ausentes")
        axes[0].set_xlabel("Escolaridade da mãe")

        sns.barplot(ax=axes[1], x="ESCMAE", y="count", data=idadepai, palette="mako", order=["12 anos ou mais",
                                                                                             "8 a 11 anos",
                                                                                             "4 a 7 anos",
                                                                                             "1 a 3 anos",
                                                                                             "Nenhuma"])
        axes[1].set_ylabel("Freqência")
        axes[1].set_title("Pais presentes")
        axes[1].set_xlabel("Escolaridade da mãe")
    st.pyplot(fig=fig)
    return None


sinasc = pd.read_csv("..\Modulo14\Support_Exercise_M14\input\SINASC_RO_2019.csv")
sinasc["DTNASC"] = pd.to_datetime(sinasc["DTNASC"])
st.title("Olá")
st.write("Aqui estão os grãficos solicitados")



min_data = sinasc.DTNASC.min()
max_data = sinasc.DTNASC.max()

st.write(min_data)
st.write(max_data)


datas = sinasc.DTNASC.unique()
datas = sorted(datas)

data_inicial = st.date_input('Data Inicial',
              value=min_data,
              min_value=min_data,
              max_value=max_data)

data_final = st.date_input('Data Final',
              value=min_data,
              min_value=min_data,
              max_value=max_data)


st.write("Data inicial: ", data_inicial)
st.write("Data final: ", data_final)

teste = sinasc[(sinasc['DTNASC'] <= pd.to_datetime(data_final)) & (sinasc['DTNASC'] >= pd.to_datetime(data_inicial))]
st.write(teste)
### Sabemos que todos os arquivos csv começam com : "SINASC_RO_2019_"
### Podemos dessa forma apenas adicionar as iniciais do mês ao final da string


plot_relatorios(data=teste, tipo="idademae ~ escmae")
# plt.savefig('./fig_relatorio/' + "2019_" + i + '/idadema_escmae.png')

plot_relatorios(data=teste, tipo="peso")
# plt.savefig('./fig_relatorio/' + "2019_" + i + '/peso.png')

plot_relatorios(data=teste, tipo="apgar5 ~ peso")
# plt.savefig('./fig_relatorio/' + "2019_" + i + '/apgar5_peso.png')

plot_relatorios(data=teste, tipo="apgar5 ~ gestacao")
# plt.savefig('./fig_relatorio/' + "2019_" + i + '/apgar5_gestacao.png')

plot_relatorios(data=teste, tipo="apgar5 ~ nulos")
# plt.savefig('./fig_relatorio/' + "2019_" + i + '/apgar5_nulos.png')

plot_relatorios(data=teste, tipo="escamae ~ pai")
# plt.savefig('./fig_relatorio/' + "2019_" + i + '/escmae_pai.png')
