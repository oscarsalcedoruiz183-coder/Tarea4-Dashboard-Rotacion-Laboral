from pathlib import Path
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

st.set_page_config(page_title='Rotación laboral IBM HR', layout='wide')
@st.cache_data
def cargar_datos():
    return pd.read_csv(Path(__file__).parent / 'dataset.csv')
df = cargar_datos()
st.title('Análisis de rotación laboral e ingresos — IBM HR Analytics')
st.caption('Exploración interactiva de los resultados de la Tarea 3')
with st.sidebar:
    st.header('Filtros')
    dept = st.selectbox('Departamento', ['Todos'] + sorted(df.Department.unique().tolist()))
    edad = st.slider('Edad', int(df.Age.min()), int(df.Age.max()), (int(df.Age.min()), int(df.Age.max())))
    estados = st.multiselect('Rotación laboral (Yes: Sí; No: No)', ['Yes','No'], default=['Yes','No'])
    ingreso = st.slider('Ingreso mensual', int(df.MonthlyIncome.min()), int(df.MonthlyIncome.max()), (int(df.MonthlyIncome.min()), int(df.MonthlyIncome.max())))
f = df[df.Age.between(*edad) & df.Attrition.isin(estados) & df.MonthlyIncome.between(*ingreso)].copy()
if dept != 'Todos':
    f = f[f.Department == dept]
f['Rotación'] = f.Attrition.map({'Yes':'Sí','No':'No'})
st.header('Exploración de datos')
a,b,c,d = st.columns(4)
a.metric('Registros', len(f))
b.metric('Ingreso promedio', f'{f.MonthlyIncome.mean():,.2f}' if len(f) else 'Sin datos')
c.metric('Desviación estándar del ingreso', f'{f.MonthlyIncome.std():,.2f}' if len(f)>1 else 'No disponible')
d.metric('Rotación', f'{f.Attrition.eq("Yes").mean():.2%}' if len(f) else 'Sin datos')
st.dataframe(f.drop(columns=['Rotación']), use_container_width=True)
st.header('Visualizaciones')
def mostrar(fig, ax, titulo, x='', y=''):
    ax.set(title=titulo, xlabel=x, ylabel=y)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
if f.empty:
    st.warning('No hay registros para los filtros seleccionados.')
else:
    a,b = st.columns(2)
    with a:
        fig,ax=plt.subplots(figsize=(7,4)); sns.countplot(data=f,x='Department',ax=ax); ax.tick_params(axis='x',rotation=15); mostrar(fig,ax,'Empleados por departamento','Departamento','Empleados')
        fig,ax=plt.subplots(figsize=(7,4)); sns.boxplot(data=f,x='Rotación',y='MonthlyIncome',ax=ax); mostrar(fig,ax,'Distribución de ingresos según rotación','Rotación laboral','Ingreso mensual')
    with b:
        fig,ax=plt.subplots(figsize=(7,4)); counts=f['Rotación'].value_counts(); ax.pie(counts,labels=counts.index,autopct='%1.1f%%'); mostrar(fig,ax,'Proporción de rotación laboral')
        fig,ax=plt.subplots(figsize=(7,4)); sns.scatterplot(data=f,x='TotalWorkingYears',y='MonthlyIncome',hue='Rotación',ax=ax); mostrar(fig,ax,'Experiencia e ingreso mensual','Años de experiencia','Ingreso mensual')
    fig,ax=plt.subplots(figsize=(10,5)); sns.barplot(data=f,x='MonthlyIncome',y='JobRole',hue='Rotación',errorbar=None,ax=ax); mostrar(fig,ax,'Ingreso promedio por cargo y rotación','Ingreso mensual','Cargo')
st.header('Validación estadística')
y=df.loc[df.Attrition.eq('Yes'),'MonthlyIncome']; n=df.loc[df.Attrition.eq('No'),'MonthlyIncome']; t,p=ttest_ind(y,n,equal_var=False)
st.caption('Resultado global de la Tarea 3: no cambia con los filtros.')
st.write(f'Prueba t de Welch: t = {t:.4f}; valor p = {p:.4e}.')
st.write(f'El ingreso promedio de quienes dejaron la empresa fue {y.mean():,.2f}, frente a {n.mean():,.2f} de quienes permanecieron. La diferencia es estadísticamente significativa al nivel del 5 %, pero no demuestra que el ingreso cause la salida.')
st.header('Hallazgos del análisis global')
st.markdown('''**¿Qué analicé?** Se estudiaron 1.470 registros del conjunto IBM HR Analytics, considerando los ingresos, los cargos, la experiencia y la permanencia de los empleados. El propósito es identificar patrones que puedan orientar las decisiones de recursos humanos.

**¿Qué encontré?** De los registros analizados, 237 corresponden a empleados que dejaron la empresa. Este grupo presenta un ingreso promedio inferior al de quienes permanecieron. También se observa que los niveles laborales más altos suelen estar asociados con ingresos mayores y que la experiencia se relaciona positivamente con la remuneración.

**¿Qué significa?** Estas diferencias permiten identificar grupos que merecen una revisión más detallada de sus condiciones laborales. Sin embargo, no permiten concluir que el salario sea la causa de la rotación, porque también pueden intervenir otros factores personales y organizacionales.

**¿Qué se recomendaría?** Revisar las condiciones salariales por cargo y departamento, fortalecer las oportunidades de crecimiento profesional y complementar los datos con encuestas de satisfacción y entrevistas de salida. Las visualizaciones anteriores permiten explorar estos patrones por grupos; los hallazgos escritos corresponden al conjunto completo y no necesariamente a cada selección.''')
