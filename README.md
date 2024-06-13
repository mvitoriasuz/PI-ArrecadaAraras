# Arrecada Araras 🦜
Projeto Integrador do 3º semestre da FATEC Araras

# Objetivo 
O objetivo é facilitar o processo de doação, conectando os doadores individuais a Ongs e instituições de caridades na cidade de Araras, e permitir que essas organizações recebam contribuições por meio de transferências instantâneas via PIX. Buscamos promover transparência e responsabilidade social.

## Tecnologias utilizadas

Esse projeto foi desenvolvido com as seguintes ferramentas:
<p align="left"> 
  <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/></a> 
  <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/></a> 
  <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/></a>
  <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/></a> 
  <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a> 
  <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/></a>
</p>

## Documentos
[Documentação](https://github.com/mvitoriasuz/PI-ArrecadaAraras/blob/main/Especificação%20de%20Requisito%20de%20Software/Especificação_de_Requisito_de_Software_v1.pdf)

## Para rodar esse projeto você precisa realizar a seguinte instrução
No ambiente Linux:
```console
git clone https://github.com/mvitoriasuz/PI-ArrecadaAraras.git
cd arrecadacoes/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test
pip install coverage
coverage run --source='.' manage.py test
coverage html
python manage.py runserver
```
No ambiente Windows:
```console
git clone https://github.com/mvitoriasuz/PI-ArrecadaAraras.git
cd arrecadacoes/
python -m venv env
cd env
cd Scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd arrecadacoes/
python manage.py migrate
python manage.py test
pip install coverage
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver
```

## Integrantes do Projeto
- [Marcelo Gomes Salvador](https://github.com/marcelosalvador)
- [Maria Vitoria Suzarth](https://github.com/mvitoriasuz)
- [Marina Borges Lima Correa](https://github.com/mborges007)
- [Mateus Augusto Brito de Souza](https://github.com/MateUZZOO7)
- [Matheus Luis dos Santos Guedes](https://github.com/matheusldsguedes)
- [Miguel Barbieri](https://github.com/M1quantum)
