import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

df = pd.read_csv("bikes_data.csv")

# Renomeando as colunas para termos mais fáceis de manusear
df.columns = ["montadora", "pais", "modelo","cilindrada" ,"potencia(hp)", "torque(N/m)", "tipo_transmissao", "modelo_transmissao", "assentos", "preco_irn", "anos", "aparencia", "tipo_corpo", "tipo_motor", "numero_cilindros"]

# Ajustando a coluna df[cilindrada]
df["cilindrada"] = df["cilindrada"].str.replace(" kW", "")
df["cilindrada"] = df["cilindrada"].str.replace("cc", "")
df["cilindrada"] = df["cilindrada"].str.replace("Electric", "0")
df["cilindrada"] = df["cilindrada"].str.replace(",", "")
df["cilindrada"] = df["cilindrada"].astype(float)

#-------------------------------------------------------------------------------------------
# Ajustando a coluna df[torque]

df['torque(N/m)'] = df["torque(N/m)"].str.replace(",", ".")
df['torque(N/m)'] = df["torque(N/m)"].str.replace("Nm", "")

for idx, v in enumerate(df["torque(N/m)"]):
    if "ft-lbs" in v:
        df.iloc[idx, 5] = round(float(v.replace("ft-lbs", "")) * 1.356, 2)

df.iloc[[319, 320, 321, 322, 323], 5] = [11.5, 11.5, 15, 14, 14]
df.iloc[240:245, 5] = [110, 110, 100, 76, 120]

for idx, v in enumerate(df["torque(N/m)"]):
    if type(v) == str:
        if "lb-ft" in v:
            df.iloc[idx, 5] = round(float(v.replace("lb-ft", "")) * 1.356, 2)
        elif "@" in v:
            df.iloc[idx, 5] = v.split(sep="@")[0]
    else:
        pass

df.drop(index=303, inplace=True)
df["torque(N/m)"] = df["torque(N/m)"].astype(float)
#----------------------------------------------------------------------------------------------------

var = df[df['cilindrada'] >= 600]

#1
st.title("Qual seria a melhor motocicleta pra você?")
#2
st.markdown("## Antes de decidir qual seria a melhor bicicleta para você, de uma olhada nas que estão disponiveis")

marca = df["montadora"].unique()

cilindrada = [150, 400, 600, 900, 1200, 1500]

#3
choice_marca = st.selectbox(
    'Selecione a marca que deseja conhecer mais', marca)

choice_cilindrada = st.selectbox(
    'Selecione a marca que deseja conhecer mais', cilindrada)

st.write(df[(df["montadora"] == choice_marca) & (df["cilindrada"] >= choice_cilindrada)])

st.markdown("----")
st.markdown("Talves você tenha percebido diferente características dentro da tabela acima principalmente em "
            "``tipo_corpo``, é importante lembrar que cada moto e construido para um proposito e para diferentes "
            "publicos, temos motos para o dia a dia, com baixa cilindrada e uma construção de corpo mais simples com as"
            "**Naked, ou Scooter** ou se você gosta de longas viagens ai temos várias opções. Se você gosta de correr e"
            "fazer curvas como na MotoGP temos as **Racing**, **SuperBike**, **Sport**")

st.markdown("## Selecione um dos tipos de motos para ler um pequeno resumo sobre ela")

tipo_corpo = df["tipo_corpo"].unique()

choice_corpo = st.selectbox(
    'Selecione o tipo de moto que deseja conhecer mais', tipo_corpo)

if choice_corpo == "Naked":
    st.write("São motos sem carenagem e com um estilo mais agressivo. Elas são ótimas para pilotagem em estradas e ruas, mas não são ideais para longas viagens.")
    image = Image.open("naked.jpg")
    st.image(image, caption="Z900 Kawasaki")
elif choice_corpo == "Racing":
    st.write("São motos projetadas para corridas em circuitos fechados. Elas são muito leves e possuem motores potentes.")
    image = Image.open("racing.jpg")
    st.image(image, caption="RS 125 Aprila")
elif choice_corpo == "Sport":
    st.write("São motos esportivas que possuem uma posição de pilotagem mais inclinada para frente. Elas são ótimas para pilotagem em estradas sinuosas e em alta velocidade.")
    image = Image.open("sport.jpg")
    st.image(image, caption="CBR 250 Honda")
elif choice_corpo == "Adventure":
    st.write("São motos projetadas para pilotagem off-road e em terrenos acidentados. Elas possuem suspensão elevada e pneus com cravos.")
    image = Image.open("adventure.webp")
    st.image(image, caption="F 850 GS Adventure BMW")
elif choice_corpo == "Cruiser":
    st.write("São motos com estilo clássico americano. Elas possuem uma posição de pilotagem relaxada e confortável.")
    image = Image.open("cruiser.webp")
    st.image(image, caption="Fat Boy 1868 cc Harley-Davidson")
elif choice_corpo == "Roadster":
    st.write("São motos com estilo clássico europeu. Elas possuem uma posição de pilotagem mais inclinada para frente do que as cruisers.")
    image = Image.open("roadster.jpg")
    st.image(image, caption="G 310R BM")
elif choice_corpo == "Superbike":
    st.write("São motos esportivas projetadas para corridas em circuitos fechados. Elas possuem motores potentes e aerodinâmica avançada.")
    image = Image.open("superbike.jpg")
    st.image(image, caption="S 1000 RR BMW")
elif choice_corpo == "Cafe Racer":
    st.write("São motos personalizadas com estilo retrô. Elas possuem uma posição de pilotagem mais inclinada para frente do que as naked.")
    image = Image.open("caferacer.jpg")
    st.image(image, caption="500X Brixton Motorcycles")
elif choice_corpo == "Bobber":
    st.write("São motos personalizadas com estilo retrô. Elas possuem uma posição de pilotagem relaxada e confortável.")
    image = Image.open("bober.jpg")
    st.image(image, caption="Perak 334cc Jawa")
elif choice_corpo == "Scrambler":
    st.write("São motos personalizadas com estilo retrô. Elas possuem pneus com cravos e suspensão elevada.")
    image = Image.open("scrambler.jpg")
    st.image(image, caption="Crossfire 500XC Brixton Motorcycles")
elif choice_corpo == "Sportbike":
    st.write("São motos esportivas projetadas para pilotagem em estradas sinuosas e em alta velocidade. Elas possuem uma posição de pilotagem mais inclinada para frente do que as naked.")
    image = Image.open("sportbike.jpg.jpg")
    st.image(image, caption="R1 998cc Yamaha")
elif choice_corpo == "Adventure touring":
    st.write("São motos projetadas para longas viagens em estradas sinuosas e off-road. Elas possuem suspensão elevada, pneus com cravos e malas laterais.")
    image = Image.open("adventuretouring.jpg")
    st.image(image, caption="TRK 502 Benelli")
elif choice_corpo == "Supermoto":
    st.write("São motos projetadas para corrida em circuito fechado e pilotagem off-road. Elas possuem pneus mistos (para asfalto e terra) e suspensão elevada.")
    image = Image.open("suoermoto.jpg")
    st.image(image, caption="SM700 GasGas")
elif choice_corpo == "Sport-touring":
    st.write("São motos esportivas projetadas para longas viagens em estradas sinuosas. Elas possuem carenagem frontal para proteção contra o vento.")
    image = Image.open("sport_touring.webp")
    st.image(image, caption="650GT CFMOTO")
elif choice_corpo == "Fighter":
    st.write("São motos personalizadas com estilo agressivo. Elas geralmente não possuem carenagem frontal.")
    image = Image.open("fighter.jpg")
    st.image(image, caption="X132 Hellcat Combat Fighter 2163 cc Confederate")
elif choice_corpo == "Scooter":
    st.write("É um tipo de moto com transmissão automática e motor pequeno. São ideais para uso urbano.")
    image = Image.open("scooter.webp")
    st.image(image, caption="CPX 125 cc Super Soco (Moto elétrica)")
# ---------------------------------------------------------------
st.markdown("------")
st.markdown("## Cilindrada não é tudo")
st.markdown("Como você pode acompanhar são varias opções e vários estilos, com certeza você irá encontrar o seu. \n"
            'Caso você não entenda muito sobre motos, você irá encotrar termos como cilindrada, cavalos(potência) e torque \n'
            'para não se decepcionar comparando uma moto de alta cilindrada e ela não atender suas espectativas de uma olhada nessre gráfico')

fig, axes = plt.subplots()
sns.scatterplot(x="torque(N/m)", y='cilindrada', data=df, color="r")

# 4
st.pyplot(fig)

st.markdown("Podemos perceber que nem sempre  uma cilindrada alto corresponde a força do motr e a sua velocidade, torque e"
            "cilindrada são coisas bem complexas para serem explicadas aqui, mas de forma bem resumida são: \n"
            "- Cilindrada: Cilindrada é o volume de ar e combustível que é queimado dentro dos cilindros do motor.\n"
            "- Torque: O torque é a força que a motocicleta possui para a saída e a retomada de velocidade, medida em kgf/m \n"
            "(quilograma força por metro) ou N/m (Newton por metro). Quanto maior for essa medida, melhor o motor responde à aceleração")
# Proposta da motocicleta
st.markdown("## Entenda a proposta da motocicleta")
st.markdown("Antes de comparar sua moto, se pergunte qual seu objetivo com ela, se você vai usar no dia a dia, para trabalhar pela cidade "
            "talvez uma moto de alta cilindrada não seja o ideal pois além de ter um alto custoi de manutenção ela pode ser difícil de manobrar "
            "entre os veiculos, por outro lado caso queria viajar longas distancias uma moto de alta cilindrada é bem melhor, mas dependendo "
            "do modelo pode deixar você cansado mais rápido, e se for pegar um off-road, com certeza as racing não iriam se dar bem nesse terreno")
st.markdown("### Tenter descrever em algumas palavras qual o tipo de experiência você proucura")
st.markdown("Exemplo: Busco uma motocicleta para trabalhar como entregador em grandes cidades")


idx1, idx2, idx3 = 0, 0, 0
texto = st.text_input("Sua vez: ").lower().split()

if texto:
    objetivo = ["trabalhar", "dia", "viajar", "correr"]
    cc = ["baixa","media","alta"]
    road = ["cidade","asfalto","chão","off-road","circuito"]

    for i in texto:
        if i in objetivo:
            idx1 = objetivo.index(i)
        elif i in cc:
            idx2 = cc.index(i)
        elif i in road:
            idx3 = road.index(i)

    choice = [idx1, idx2, idx3]

    if sum(choice) == 0:
        motos_recomendadas = df.loc[(df["tipo_corpo"] == "Naked") & (df["cilindrada"] < 200)]
    elif sum(choice) <= 4:
        motos_recomendadas = df.loc[(df["tipo_corpo"] == "Adventure") & (df["cilindrada"] >= 200) & (df["cilindrada"] < 600)]
    elif sum(choice) > 4:
         motos_recomendadas = df.loc[(df["tipo_corpo"] == "Superbike") & (df["cilindrada"] >= 600)]
    st.write("Essas são as motos que temos diponíveis que acreditamos ir de acordo com o que você proucura")
    st.write(motos_recomendadas)


