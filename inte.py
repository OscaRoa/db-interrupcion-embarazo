import pandas as pd

try:
    data = pd.read_csv('./data/interrupcion-legal-del-embarazo.csv')
except FileNotFoundError:
    url = "https://datos.cdmx.gob.mx/explore/dataset/interrupcion-legal-del-embarazo/download/?format=csv&timezone=America/Mexico_City&lang=es&use_labels_for_header=true&csv_separator=%2C"
    data = pd.read_csv(url)
    data.to_csv('./data/interrupcion-legal-del-embarazo.csv')

descriptive = data.describe(include = "all")

with pd.option_context('display.max_columns', None, 'display.max_rows', None):
    print(descriptive)
