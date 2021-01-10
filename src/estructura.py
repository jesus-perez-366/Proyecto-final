
import random
import pandas as pd
import folium
from folium import Marker, Icon, Map
from folium.plugins import MarkerCluster
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
load_dotenv()



def crear_mapa (data):
    return Map(location= [data['latitud'].mean(),data['longitud'].mean()], zoom_start = 15)


def dibujar_mapa(map, inmob, data, color, icono):
    mc=MarkerCluster(name=inmob)
    for i,row in data.iterrows():
        distrito = {
            "location" : [row["latitud"], row["longitud"]],
            "tooltip" : row[['Precio', 'Metros', 'hab', 'baño']]}

        icon = Icon( color = color,
                    prefix = "fa",
                    icon = icono,
                    icon_color = "black"
                )
       

        mc.add_child(folium.Marker (**distrito,icon = icon, popup='<a href="'+ row['Url'] +'"target="_blank">link</a>'))

        
        #
    map.add_child(mc)
    return map

def modificar_coordenadas(data):
    data.latitud=data.latitud.apply(lambda x: x+(round(random.uniform(-0.002,0.002),5)))
    data.longitud=data.longitud.apply(lambda x: x+(round(random.uniform(-0.002,0.002),5)))
    return data


def crear_data_clean(data):
    df2 = data.drop(data[data['info']=='ALQUILADO'].index)
    df2 = df2.drop('info', axis=1)
    df2['Precio']=df2['Precio'].str.replace('€', 'EUR')
    df2['Metros']=df2['Metros'].str.replace('m²', ' m2')
    df2['hab']=df2['hab'].str.replace('hab', '')
    df2[['latitud','longitud']]=df2[['latitud','longitud']].astype('float')
    # df2.latitud=df2.latitud.interpolate() 
    # df2.longitud=df2.longitud.interpolate()
    df2['latitud'] = df2['latitud'].fillna(df2.latitud.mean()) 
    df2['longitud'] = df2['longitud'].fillna(df2.longitud.mean()) 
    df2=df2.dropna(subset=['latitud'])
    df2=df2.dropna(subset=['longitud'])
    return df2

def crear_primer_data(inmobiliaria, ubicacion, list_precios, metros, habitacion, baño, label, latitud, longitud, link2):

    df_data=pd.DataFrame(inmobiliaria, columns=['Inmobiliaria'])
    df_data['Ubicacion']=pd.DataFrame(ubicacion)
    df_data['Precio']=pd.DataFrame(list_precios)
    df_data['Metros']=pd.DataFrame(metros)
    df_data['hab']=pd.DataFrame(habitacion)
    df_data['baño']=pd.DataFrame(baño)
    df_data['info']=pd.DataFrame(label)
    df_data['latitud']=pd.DataFrame(latitud)
    df_data['longitud']=pd.DataFrame(longitud)
    df_data['Url']=pd.DataFrame(link2)
    return df_data

def envio_correo(c):
    
    # create message object instance
    msg = MIMEMultipart()
    
    # setup the parameters of the message
    password = os.getenv("password")
    msg['From'] = "Firemax366@gmail.com"
    msg['To'] = c
    msg['Subject'] = "Pisos en alquiler"
    nombre_adjunto = 'Archivo.csv'

    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open('output/Archivo.csv', 'rb')
    
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    msg.attach(adjunto_MIME)
    
    
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
