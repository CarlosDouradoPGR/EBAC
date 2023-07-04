# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

### Criar uma função que gere todos os gráficos

def plot_relatorios(data=pd.DataFrame(), tipo=str.lower):
    # Gráfico idademae x escmae
    if tipo == "idademae ~ escmae":
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15,5))
        sns.barplot(y= "IDADEMAE", x="ESCMAE", data=sinasc, errorbar=None, palette="flare", order=["12 anos ou mais",
                                                                                          "8 a 11 anos",
                                                                                          "4 a 7 anos",
                                                                                          "1 a 3 anos",
                                                                                          "Nenhuma"])
        axes.set_title("Idade da mãe x Escolaidade")
        
     # Histograma do peso do bebê   
    elif tipo == "peso":
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15,5))
        sns.histplot(x="PESO", data=sinasc)
        axes.set_title("Histograma do peso")
        axes.set_ylabel("Frequência")
        
    # APGAR5 x Peso
    elif tipo == "apgar5 ~ peso":
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15,5))
        sns.barplot(ax=axes, x="APGAR5", y="PESO", data=sinasc,palette="flare", errorbar=None, estimator="mean")
        sns.lineplot(ax=axes, x="APGAR5", y="PESO", data=sinasc)
        axes.set_title("APGAR5 x Peso")
        
    # APGAR5 x Gestação
    elif tipo == "apgar5 ~ gestacao":
        # APGAR 5 x Gestação
        plt.close("all")
        fig, axes = plt.subplots(figsize=(15,5))
        sns.pointplot(ax=axes, x="GESTACAO", y="APGAR5", data=sinasc, errorbar=None, estimator="mean", order=["42 semanas e mais",
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

        plt.pie([apgar5, apgar_null], labels=[f"{round(apgar5*100 / (apgar5 + apgar_null), 2)}%", 
                                              f"{round(apgar_null*100 / (apgar5 + apgar_null), 2)}%"])
        plt.title("Realizaram APGAR5")
        plt.legend(["Realizado", "Não realizado"],loc='upper right' )
        
        
    # Escolaridade da mãe x pai ausente 
    elif tipo == "escamae ~ pai":
        plt.close("all")
        # Quantidade de Pai ausente e Escolaridade da mãe
        ### DataFrame com a idade do pai nula
        idadepai_null = sinasc.loc[sinasc["IDADEPAI"].isnull() == True][["ESCMAE"]].value_counts().to_frame().reset_index()

        ### DataFrame com a idade do pai não nula
        idadepai = sinasc.loc[sinasc["IDADEPAI"].isnull() == False][["ESCMAE"]].value_counts().to_frame().reset_index()
        
        fig, axes = plt.subplots(1,2, figsize=(15, 5))

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
        
    return None


# Deixando uma lista com as iniciais dos meses solicitados
mes = sys.argv

### Sabemos que todos os arquivos csv começam com : "SINASC_RO_2019_"
### Podemos dessa forma apenas adicionar as iniciais do mês ao final da string


for i in mes[1:]:
    sinasc = pd.read_csv("..\Support_Exercise_M14\input\SINASC_RO_2019_"+i+".csv")
    
    os.makedirs('./fig_relatorio/'+"2019_" + i, exist_ok=True)
    
    plot_relatorios(data=sinasc, tipo="idademae ~ escmae")
    plt.savefig('./fig_relatorio/'+"2019_" +i+'/idadema_escmae.png')
    
    plot_relatorios(data=sinasc, tipo="peso")
    plt.savefig('./fig_relatorio/'+"2019_" +i+'/peso.png')
    
    plot_relatorios(data=sinasc, tipo="apgar5 ~ peso")
    plt.savefig('./fig_relatorio/'+"2019_" +i+'/apgar5_peso.png')
    
    plot_relatorios(data=sinasc, tipo="apgar5 ~ gestacao")
    plt.savefig('./fig_relatorio/'+"2019_" +i+'/apgar5_gestacao.png')
    
    plot_relatorios(data=sinasc, tipo="apgar5 ~ nulos")
    plt.savefig('./fig_relatorio/'+"2019_" +i+'/apgar5_nulos.png')
    
    plot_relatorios(data=sinasc, tipo="escamae ~ pai")
    plt.savefig('./fig_relatorio/'+"2019_" +i+'/escmae_pai.png')
    
    plt.close("all")