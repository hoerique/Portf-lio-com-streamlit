import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Portfólio", layout="wide")
# Criando colunas para alinhar a foto e o nome
col1, col2 = st.columns([1, 4])  # Ajusta a proporção das colunas

with col1:
    st.image("minha-foto.jpg", width=100)  # Ajuste o tamanho da imagem

with col2:
    st.markdown("<h1 style='margin-top: 10px;'>Bem-vindo ao Meu Portfólio</h1>", unsafe_allow_html=True)
# Título e descrição

st.text("Olá! Meu nome é Erique Ferreira Dias, e sou um desenvolvedor especializado em análise de dados, automação e inteligência artificial. Aqui você encontrará um pouco do meu trabalho, minhas habilidades e como posso ajudar você a transformar dados em insights poderosos.")

# Seção "O que você vai encontrar aqui?"
st.markdown("""
## O que você vai encontrar aqui?  
✅ **Projetos e dashboards interativos** – Soluções criadas com **Streamlit, Python e Power BI**.  
✅ **Automação e IA** – Aplicações inteligentes para otimizar processos.  
✅ **Consultoria e serviços** – Desenvolvimento de sistemas personalizados para sua empresa.  
✅ **Artigos e tutoriais** – Compartilho conhecimento sobre tecnologia, análise de dados e desenvolvimento.  
""", unsafe_allow_html=True)

# Adicione mais seções conforme necessário
st.markdown("""
## Meus Projetos
Aqui estão alguns dos projetos em que estou trabalhando atualmente:

- **Dashboard de Tráfego Pago**: Análise detalhada de campanhas de anúncios.
- **Automação de Processos**: Uso de IA para otimizar fluxos de trabalho.
- **Consultoria em Power BI**: Desenvolvimento de dashboards interativos para empresas.
""")


st.text("RH")
power_bi_url_1 = "https://app.powerbi.com/view?r=eyJrIjoiMWZmY2ViYTItNmZhYS00M2MzLTgyNWEtYzc5YzE3YzIwZjM3IiwidCI6ImNlMGZiOTYzLWM2ZjctNDU2Yi04OTI2LTQ5OWY0MDUxODcyMyJ9"
# """"Incorporando o Power BI com um iframe (ajustado para 600x373.5px)

st.markdown(f'<iframe width="600" height="373.5" src="{power_bi_url_1}" frameborder="0" allowFullScreen="true"></iframe>',
             unsafe_allow_html=True)

#financeiro
power_bi_url_2="https://app.powerbi.com/view?r=eyJrIjoiMDk5ZTdkNDgtYTM2Mi00Njk3LWE4ZGItYWJhZWMyZjlhMmI5IiwidCI6ImNlMGZiOTYzLWM2ZjctNDU2Yi04OTI2LTQ5OWY0MDUxODcyMyJ9"
st.text("Financeiro")
st.markdown(f'<iframe width="600" height="373.5" src="{power_bi_url_2}" frameborder="0" allowFullScreen="true"></iframe>',
             unsafe_allow_html=True)



st.markdown("""
## Contato
Você pode entrar em contato comigo pelos seguintes meios:
- **Email**: erick.dias@exemplo.com
- **LinkedIn**: [Erick no LinkedIn](https://www.linkedin.com/in/erickdias)
""")