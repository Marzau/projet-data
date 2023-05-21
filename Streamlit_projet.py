import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from PIL import Image

# Charger les données COVID-19
st.subheader("Introduction")
st.write("La pandémie de COVID-19 a eu un impact majeur sur la santé publique à travers le monde. Une question qui s'est posée est de savoir si le tabagisme a influencé le taux de mortalité pendant cette période. Dans cette analyse, nous avons examiné les données disponibles pour déterminer si le tabac a eu un impact sur la mortalité liée au COVID-19.")
st.subheader("Problématique")
st.write("Le tabac a-t-il aidé à l'augmentation des cas de COVID-19 ainsi que l'augmentation du taux de mortalité lié au COVID-19 ?")
st.subheader("Analyse des données :")
st.write("Pour cette étude, nous avons utilisé une base de données internationale qui recueille des informations sur les cas confirmés de COVID-19 ainsi que les décès associés. Nous avons également recueilli des données sur les habitudes tabagiques des hommes et des femmes fumeurs de la population pour chaque région. Les données ont été collectées sur une période de trois ans (début à ~ fin covid).")
data_covid = pd.read_csv("owid-covid-data.csv", delimiter=",")
data_covid
st.write("Ci-dessous, toutes les colonnes présentes dans le dataset ")
colonnes = data_covid.columns
colonnes
st.write("Et enfin, le dataset final utilisé pour ce projet càd uniquement les données qui nous intéressent")
data_tabac = data_covid[['continent','location','date','total_cases','total_deaths','female_smokers','male_smokers']]
data_tabac

# Préparation des données
df = data_covid[['location', 'continent', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths','female_smokers','male_smokers']]
df = df.dropna()

# Analyse exploratoire de données
st.subheader("Analyse exploratoire de données")
image_path = 'C:/Users/User/Desktop/photos_streamlit/analyse_exploratoire.png'
image = Image.open(image_path)
st.image(image, caption='Analyse exploratoire de données', use_column_width=True)


# Régression linéaire pour prédire le nombre de cas
X = df[['total_cases']].values
y = df[['new_cases']].values
reg = LinearRegression().fit(X, y)
r_squared = reg.score(X, y)
coef = reg.coef_[0]

st.subheader("Régression linéaire pour prédire le nombre de nouveaux cas")
st.write("Coefficient de détermination :", r_squared)
st.write("Coefficient directeur :", coef)

# Visualisation des résultats de la régression linéaire
st.subheader("Visualisation des résultats de la régression linéaire")
image_path = 'C:/Users/User/Desktop/photos_streamlit/rg.png'
image = Image.open(image_path)
st.image(image, caption='Visualisation des résultats de la régression linéaire', use_column_width=True)


# Graphique de l'évolution des cas et des décès
st.subheader("Graphique de l'évolution des cas et des décès")
image_path = 'C:/Users/User/Desktop/photos_streamlit/évolution.png'
image = Image.open(image_path)
st.image(image, caption="Graphique de l'évolution des cas et des décès", use_column_width=True)

st.subheader("Avant toutes choses nous voulons savoir comment évolue le taux de mortalité ? En fonction des cas confirmés oui mais pas que, car un cas confirmé n'est pas un décés obligatoire. Et donc qu'est ce qui crée ce taux de mortalité ?")
st.subheader("D'après ces graphes, nous pouvons voir sur quoi partir déjà. En général, plus le nombre de cas total est haut et plus le taux de mortalité est considérable, l'évolution est assez linéaire, voir même exponentielle. Nous pouvons en déduire que ces deux paramètres sont étroitement liés.")


# Affichage des statistiques descriptives
st.subheader("Statistiques descriptives")
st.write(df.describe())


st.subheader("Pour se donner une idée, voici le top 20 des pays ayant eu le plus de cas durant la pandémie :")
image_path = 'C:/Users/User/Desktop/photos_streamlit/top20.png'
image = Image.open(image_path)
st.image(image, caption="top 20 des pays ayant eu le plus de cas durant la pandémie", use_column_width=True)


# Analyse du taux de mortalité et des autres facteurs
st.subheader("Analyse du taux de mortalité et des autres facteurs")
# Votre code d'analyse du taux de mortalité et d'autres facteurs ici

# Affichage des 5 premières lignes du dataframe par continent
st.subheader("Nombre total de cas et de décès par continent")
data_covid_country = data_covid.groupby(['continent']).max()[['total_cases', 'total_deaths', 'new_cases', 'new_deaths']].reset_index()
st.write(data_covid_country.head())

# Graphique du nombre total de cas par continent
fig_cases = plt.figure()
data_covid_country.plot(x='continent', y='total_cases', kind='bar', rot=90)
plt.xlabel('Continent')
plt.ylabel('Nombre de cas')
plt.title('Nombre total de cas de Covid-19 par continent')
st.pyplot(plt)

# Graphique du nombre total de décès par continent
fig_deaths = plt.figure()
data_covid_country.plot(x='continent', y='total_deaths', kind='bar', rot=90)
plt.xlabel('Continent')
plt.ylabel('Nombre de décès')
plt.title('Nombre total de décès de Covid-19 par continent')
st.pyplot(plt)

st.write("On voit bien que le continent d'Amérique du Nord (grossomodo les USA) sont bien au dessus des autres continent. On peux notamment voir que l'Asie a eu beaucoup de cas décelés mais pas beaucoup de mort. Pourquoi ? Ils se sont rapidement mis en confinement strict.\n\nPourrais-t-on déjà conclure que les Nord Américains sont les plus gros fumeurs ???")
image_path = 'C:/Users/User/Desktop/photos_streamlit/mortalite.png'
image = Image.open(image_path)
st.image(image, caption='Taux de mortalité en fonction du pourcentage de fumeurs', use_column_width=True)

st.subheader("Top 20 des pays avec les taux de tabagisme les plus élevés")
image_path = 'C:/Users/User/Desktop/photos_streamlit/top20tabac.png'
image = Image.open(image_path)
st.image(image, caption='Top 20 des pays avec les taux de tabagisme les plus élevés', use_column_width=True)
st.write("Ici AUCUN pays d'Amérique du Nord n'apparait dans le top 20. Nous pouvons donc déjà nous faire une idée.")

st.subheader("Nombre total de cas par pays")
image_path = 'C:/Users/User/Desktop/photos_streamlit/map.png'
image = Image.open(image_path)
st.image(image, caption='Nombre total de cas par pays', use_column_width=True)

st.subheader("Taux de mortalité en fonction du taux de tabagisme")
image_path = 'C:/Users/User/Desktop/photos_streamlit/tauxmortalite.png'
image = Image.open(image_path)
st.image(image, caption='Top 20 des pays avec les taux de tabagisme les plus élevés', use_column_width=True)
st.write("Taux de mortalité en fonction du taux de tabagisme")

st.write("On peux voir qu'il y a quand même une petite influence car plus le taux de tabagisme est haut et plus le taux de mortalité est haut aussi mais cela reste léger.\n\nPeut-on accuser un autre facteur : Maladie cardiovasculaire ? Diabete ? Asthme ? Vieillesse ?")

st.subheader("Comparaison du taux de mortalité selon les groupes d\'âge'")
image_path = 'C:/Users/User/Desktop/photos_streamlit/tauxmortalite2.png'
image = Image.open(image_path)
st.image(image, caption='Top 20 des pays avec les taux de tabagisme les plus élevés', use_column_width=True)


st.subheader("Comparaison du taux de mortalité selon les groupes d\'âge'")
image_path = 'C:/Users/User/Desktop/photos_streamlit/tauxmortalite3.png'
image = Image.open(image_path)
st.image(image, caption='Top 20 des pays avec les taux de tabagisme les plus élevés', use_column_width=True)

st.write("Notre analyse montre que le taux de tabagisme n'est qu'un facteur minime du taux de mortalité. D'après ces 2 graphes l'age joue beaucoup sur le taux de mortalité aussi. Un fumeur agés à plus de chance de décéder qu'un non fumeur.")

st.subheader("Taux de mortalité ayant une maladie cardiovasculaire")
image_path = 'C:/Users/User/Desktop/photos_streamlit/mortalite2.png'
image = Image.open(image_path)
st.image(image, caption='Top 20 des pays avec les taux de tabagisme les plus élevés', use_column_width=True)

st.subheader("Taux de mortalité en fonction du pourcentage de patients diabétiques")
image_path = 'C:/Users/User/Desktop/photos_streamlit/mortalite3.png'
image = Image.open(image_path)
st.image(image, caption='Top 20 des pays avec les taux de tabagisme les plus élevés', use_column_width=True)

st.subheader("Conclusion")
st.write("Pour finir, nous voyons que même si le taux de patients atteints de maladie cardiovasculaire est plus faible que le taux de fumeurs la valeur de la médiane cardiovasculaire est assez élevé et correspond à 33% de ce taux contrairement au graphique précédent.")


