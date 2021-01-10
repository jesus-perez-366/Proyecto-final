import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import random
import src.estructura as est
import os
from dotenv import load_dotenv
load_dotenv()

def prueba(x, y, z, o, t, e, c):
    '''
    Funcion que extrae de un archivo .txt los datos de Date, User y Message de una conversacion de chat, 
    para luego agregarla a la base de datos 
    '''
    dict1 = {'1' : 'Madrid', '2' : 'Valencia'}
    opcion=y.replace(' ', '-')
    opcion=opcion.replace(' ', '-').replace(',', '')
    url=f'https://www.redpiso.es/alquiler-viviendas/{dict1[x]}/{opcion}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    precios = soup.find_all("h3")
    longitud = []
    latitud = []
    link2 = []
    metros = []
    list_precios = []
    ubicacion = []
    habitacion=[]
    baño=[]
    label=[]
    inmobiliaria=[]
    dict_1={}
    com=[]
    key=os.getenv("key")
    ubicacion3=[]
    if precios !=[]:
        list_precios=[i.text.strip() for i in precios ]

        label = soup.find_all("div", class_="property-list-options-emblem")
        label = [i.text.strip() for i in label]

        metros2 = soup.find_all("div", class_='property-list-options-item')
        count=1

        for i in metros2:
            y = re.findall(r"^\d.*m²",i.text)
            h = re.findall(r".*hab",i.text)
            b = re.findall(r"\d$",i.text)
            if count==1 and y!=[]:
                metros.append(y[0])
                count+=1

            elif count ==2 and h !=[]:
                habitacion.append(h[0].strip())
                count+=1

            elif count ==3 and b !=[]:
                baño.append(b[0])
                count=1

            elif count==1 and y==[] and b==[] and h==[]:
                metros.append(None)
                count=2


            elif count == 1 and h== []:
                baño.append(b[0])
                habitacion.append(None)
                metros.append(None)
                count=1

            elif count == 1 and b== []:
                baño.append(None)
                habitacion.append(h[0].strip())
                metros.append(None)
                count=1

            elif count == 2 and b== []:
                baño.append(None)
                habitacion.append(None)
                metros.append(y[0])
                count=2

            elif count == 2 and y== []:
                baño.append(b[0])
                habitacion.append(None)
                count=1

            elif count == 3 and y== []:
                baño.append(None)
                habitacion.append(h[0].strip())
                metros.append(None)
                count=1

            elif count == 3 and h== []:
                baño.append(None)
                habitacion.append(None)
                metros.append(y[0])
                count=2

        ubicacion2 = soup.find_all("a", class_='item-link')
        ubicacion2 = [i.text for i in ubicacion2]
        ubicacion = [re.sub(r'.*alquiler en ',"",i) for i in ubicacion2]

        link = soup.find_all("a", class_="item-link")
        link2 = [re.findall(r'href=[\'"]?([^\'" >]+)',str(i)) for i in link]

        caract2 = []
        for i in link2:
            inmobiliaria.append('RedPiso')
            response = requests.get(i[0])
            soup = BeautifulSoup(response.content)
            geo = soup.find_all("img", class_="img-property-map")
            geo2 = [re.findall(r'center=[\'"]?([^\'" >]+&)',str(i)) for i in geo]
            if geo2 == []:
                latitud.append(None)
                longitud.append(None)
            else:   
                d = re.sub(r'&amp.*',"",geo2[0][0])
                latitud.append(re.findall(r'.*,',d)[0][:-1])
                longitud.append(re.findall(r',.*',d)[0][1:])

            general = soup.find_all("div", class_="col-lg-3 col-md-4 col-sm-6 property-features-item")

            caract=[y.find_all("span")[0].text.strip() for y in general]
            caract2.append(str(caract))




        pag=1
        d = True
        while d:
            pag+=1
            url=f'https://www.redpiso.es/alquiler-viviendas/{dict1[x]}/{opcion}/pagina-{pag}'
            response = requests.get(url)
            soup = BeautifulSoup(response.content)
            soup
            precios = soup.find_all("h3")
            if precios !=[]:
                for i in precios:
                    list_precios.append(i.text.strip())
                    inmobiliaria.append('RedPiso')


                metros2 = soup.find_all("div", class_='property-list-options-item')
                for i in metros2:
                    y = re.findall(r"^\d.*m²",i.text)
                    h = re.findall(r".*hab",i.text)
                    b = re.findall(r"\d$",i.text)
                    if count==1 and y!=[]:
                        metros.append(y[0])
                        count+=1

                    elif count ==2 and h !=[]:
                        habitacion.append(h[0].strip())
                        count+=1

                    elif count ==3 and b !=[]:
                        baño.append(b[0])
                        count=1

                    elif count==1 and y==[] and b==[] and h==[]:
                        metros.append(None)
                        count=2


                    elif count == 1 and h== []:
                        baño.append(b[0])
                        habitacion.append(None)
                        metros.append(None)
                        count=1

                    elif count == 1 and b== []:
                        baño.append(None)
                        habitacion.append(h[0].strip())
                        metros.append(None)
                        count=1

                    elif count == 2 and b== []:
                        baño.append(None)
                        habitacion.append(None)
                        metros.append(y[0])
                        count=2

                    elif count == 2 and y== []:
                        baño.append(b[0])
                        habitacion.append(None)
                        count=1

                    elif count == 3 and y== []:
                        baño.append(None)
                        habitacion.append(h[0].strip())
                        metros.append(None)
                        count=1

                    elif count == 3 and h== []:
                        baño.append(None)
                        habitacion.append(None)
                        metros.append(y[0])
                        count=2



                ubicacion2 = soup.find_all("a", class_='item-link')
                ubicacion2 = [i.text for i in ubicacion2]
                for i in ubicacion2:
                    ubicacion.append(re.sub(r'.*alquiler en ',"",i))

                label2 = soup.find_all("div", class_="property-list-options-emblem")
                for i in label2:
                    label.append(i.text.strip())

                link = soup.find_all("a", class_="item-link")
                for i in link:
                    y = re.findall(r'href=[\'"]?([^\'" >]+)',str(i))
                    link2.append(y)
                    if type(y) != str:
                        y=y[0]
                    response = requests.get(y)
                    soup = BeautifulSoup(response.content)
                    geo = soup.find_all("img", class_="img-property-map")
                    geo2 = [re.findall(r'center=[\'"]?([^\'" >]+&)',str(i)) for i in geo]
                    if geo2 == []:
                        latitud.append(None)
                        longitud.append(None)
                    else:   
                        d = re.sub(r'&amp.*',"",geo2[0][0])
                        latitud.append(re.findall(r'.*,',d)[0][:-1])
                        longitud.append(re.findall(r',.*',d)[0][1:])

                    general = soup.find_all("div", class_="col-lg-3 col-md-4 col-sm-6 property-features-item")
                    caract=[y.find_all("span")[0].text.strip() for y in general]
                    caract2.append(str(caract))

            else:
                d = False

    else:
        pass




    #para habitalicia



    opcion=opcion.replace('-', '_').replace('ñ','n').replace('_El','').replace('_Los','').replace('_Las','').replace('ó','o').replace('á','a').replace('é','e').replace('Rivas_', 'rivas___')
    opcion = opcion.lower()
    url=f'https://www.habitaclia.com/alquiler-{opcion}.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    num=soup.find_all("h2", class_="f-right")
    if num != []:
        num=re.findall(r"^\d.*anunc",num[0].text)
        num=num[0].replace(' anunc','')
        num2=0
        pag=0
        while int(num)!=num2:
            try:
                soup=soup.find_all("section", class_="list-items")[0]
                precios = soup.find_all("span", class_="font-2")
                for i in precios:
                    num2+=1
                    list_precios.append(i.text.strip())
                    inmobiliaria.append('Habitalicia')
            except: 
                num2+=1
                list_precios.append('0 €')
                inmobiliaria.append('Habitalicia')

            metros2 = soup.find_all("p", class_="list-item-feature")
            for i in metros2:
                try:
                    y = re.findall(r".*m2",i.text)[0]
                    print(i)
                    y = re.sub(r'm2',"m²",y)
                except:
                    y = []
                if y == []:
                    print('prueba')
                    metros.append(None)  
                else: 
                    metros.append(y)

                h = re.findall(r"\ .*hab",i.text)
                if h == []:
                    habitacion.append(None)  
                else:
                    h=h[0].strip()[2:]
                    habitacion.append(h)

                b = re.findall(r"\d ba",i.text)   
                if b == []:
                    baño.append(None)  
                else:
                    b=b[0][0] 
                    baño.append(b)

                label.append(None)

            ubicacion2 = soup.find_all("p", class_="list-item-location")
            ubicacion2 = [i.text.rstrip().lstrip() for i in ubicacion2]
            for i in ubicacion2:
                if 'mapa' in i:
                    p = ((re.sub(r'Ver mapa',"",i)).rstrip()+', Madrid').replace('-',', ')
                    ubicacion.append(p)
                    ubicacion3.append(p)
                    latitud.append(None)
                    longitud.append(None)

                else:
                    p = (i+', Madrid').replace('-',', ')
                    ubicacion.append(p)
                    ubicacion3.append(p)
                    latitud.append(None)
                    longitud.append(None)
        
            
                        
            set_ubicacion=set(ubicacion3)
            for i in set_ubicacion:
                if i not in  com:
                    print(i)
                    
                    try:
                        com.append(i)
                        i = i.replace('  ',' ').replace(' ','+')
                        url2 = f'https://maps.googleapis.com/maps/api/geocode/json?address={p}&key={key}'
                        response2 = requests.get(url2)
                        soup2 = BeautifulSoup(response2.content)
                        d=json.loads(str(soup2.text))
                        f=d['results'][0]['geometry']['location']
                        dict_1[i]=[f['lat'],f['lng']]
                        print(com)

                    except:
                        print('error')
                        dict_1[i]=[None,None]
                
            

            link = soup.find_all("h3", class_="list-item-title")
            for i in link:
                y = re.findall(r'href=[\'"]?([^\'" >]+)',str(i))
                link2.append(y)

            pag+=1 
            print(pag)
            url=f'https://www.habitaclia.com/alquiler-{opcion}-{pag}.htm'
            response = requests.get(url)
            soup = BeautifulSoup(response.content)



    else:
        pass

    try:
        df_data = est.crear_primer_data(inmobiliaria, ubicacion, list_precios, metros, habitacion, baño, label, latitud, longitud, link2)
        latitud2=[]
        longitud2=[]
        for i,row in df_data.iterrows():
            i = row['Ubicacion'].replace('  ',' ').replace(' ','+')
            if i in dict_1 and row['Inmobiliaria']=='Habitalicia': 
                latitud2.append(dict_1[i][0])
                longitud2.append(dict_1[i][1])
            else:
                latitud2.append(row['latitud'])
                longitud2.append(row['longitud'])
        df_data['latitud'] = latitud2
        df_data['longitud'] = longitud2

        df2 = est.crear_data_clean(df_data)
        df2 = df_data.drop(df_data[df_data['info']=='ALQUILADO'].index)
        df2 = df2.drop('info', axis=1)
        df2['Precio']=df2['Precio'].str.replace('€', 'EUR')
        df2['Metros']=df2['Metros'].str.replace('m²', ' m2')
        df2['hab']=df2['hab'].str.replace('hab', '')
        df2[['latitud','longitud']]=df2[['latitud','longitud']].astype('float')
        df2['latitud'] = df2['latitud'].fillna(df2.latitud.mean()) 
        df2['longitud'] = df2['longitud'].fillna(df2.longitud.mean()) 
        df2=df2.dropna(subset=['latitud'])
        df2=df2.dropna(subset=['longitud'])



        if int(o) == 2:
            df2['Precio']=df2['Precio'].str.replace('EUR', '')
            df2['Precio']=df2['Precio'].str.replace('.', '')
            df2['Precio']=df2['Precio'].apply(lambda x: x.lstrip().rstrip())
            df2['Precio']=df2['Precio'].astype('int')
            df2= df2.sort_values('Precio',ascending=False)
            df2['Precio']=df2['Precio'].astype('str')
            df2['Precio']=df2['Precio'].apply(lambda x: x+' EUR')
            if int(z)>0 and int:
                df2['hab'] = df2['hab'].fillna('0')
                df2.hab=df2.hab.apply(lambda x: x.rstrip().lstrip())
                if str(z) not in df2['hab'].unique().tolist():
                    return ('no esta colocamon return no hay pisos con esta cantidad de habitaciones')
                else:
                    if int(z)==1:
                        df2=df2[df2['hab']==str(z)]
                    else:
                        df2=df2[df2['hab']>=str(z)]
            else:
                pass

            if int(t) == 1:
                df2=df2.head(20)
            
            else:
                pass

        else:
            df2['Precio']=df2['Precio'].str.replace('EUR', '')
            df2['Precio']=df2['Precio'].str.replace('.', '')
            df2['Precio']=df2['Precio'].apply(lambda x: x.lstrip().rstrip())
            df2['Precio']=df2['Precio'].astype('int')
            df2= df2.sort_values('Precio',ascending=True)
            df2['Precio']=df2['Precio'].astype('str')
            df2['Precio']=df2['Precio'].apply(lambda x: x+' EUR')
            if int(z)>0:
                df2['hab'] = df2['hab'].fillna('0')
                df2.hab=df2.hab.apply(lambda x: x.rstrip().lstrip())
                if str(z) not in df2['hab'].unique().tolist():
                    return 'no esta colocamon return no hay pisos con esta cantidad de habitaciones'
                else:
                    if int(z)==1:
                        df2=df2[df2['hab']==str(z)]
                    else:
                        df2=df2[df2['hab']>=str(z)]

            if int(t) == 1:
                df2=df2.head(20)
            else:
                pass


        df2['hab'] = df2['hab'].fillna('0')
        df2['baño'] = df2['baño'].fillna('0')
        try:
            df2.hab=df2.hab.apply(lambda x: x.rstrip().lstrip())
        except:
            pass

        # df2= est.modificar_coordenadas(df2)
        df3 = df2[df2['Inmobiliaria']=='RedPiso']
        df4 = df2[df2['Inmobiliaria']=='Habitalicia']
        df4= est.modificar_coordenadas(df4)


        if e=='1':

            try:
                
                df2.to_csv('output/Archivo.csv')
                # send_attachment.py
    # import necessary packages
                est.envio_correo(c)
                

            except:
                pass
        else:
            pass



        map_1 = est.crear_mapa (df2)
        map_1 = est.dibujar_mapa(map_1, 'RedPiso', df3, 'red', "glass")
        map_1 = est.dibujar_mapa(map_1, 'Habitalicia', df4, 'orange', "glass")
        folium.LayerControl().add_to(map_1)
        map_1.save('templates/map.html')

    except:
        return ('No hay coincidencia')



