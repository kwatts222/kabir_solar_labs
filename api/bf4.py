import requests
from bs4 import BeautifulSoup


def result(country):
    country_dict={}
    link= "https://en.wikipedia.org/wiki/"+country
    flag_link="https://en.wikipedia.org/wiki/File:Flag_of_{}.svg".format(country.title())

    page = requests.get(link)
    flag_page= requests.get(flag_link)
    soup2= BeautifulSoup(page.text, 'lxml')
    image=soup2.findAll('img')[0].get('src')
    country_dict["flag_link"] = "https:"+image

    soup = BeautifulSoup(page.text, 'lxml')
    object= soup.find(id="mw-content-text")
    country_info= object.find_all(class_= "infobox-label")
    country_data = object.find_all(class_= "infobox-data")



    kabir_info=[]
    kabir_data=[]


    for i in range(len(country_data)):
        
        
        if "Capital" in country_info[i].get_text().replace('\xa0', " ") or "capital" in country_info[i].get_text().replace('\xa0', " "):
            kabir_info.append("Capital")
            if country_data[i].find('ul'):
                datas = country_data[i].ul.find_all("li")
                lis= []
                for d in datas:
                    lis.append(d.find("a").get_text())
                kabir_data.append(lis)
            else:
                kabir_data.append(country_data[i].find("a").get_text().replace('\xa0', " "))
        
        if "Largest city" in country_info[i].get_text().replace('\xa0', " ") or "largest city" in country_info[i].get_text().replace('\xa0', " "):
            kabir_info.append("Largest City")
            if country_data[i].find('ul'):
                datas = country_data[i].ul.find_all("li")
                lis= []
                for d in datas:
                    lis.append(d.find("a").get_text())
                kabir_data.append(lis)
            else:
                kabir_data.append(country_data[i].find("a").get_text().replace('\xa0', " "))
        

        if "Official languages" in country_info[i].get_text().replace('\xa0', " ") or "Official language" in country_info[i].get_text().replace('\xa0', " "):
            kabir_info.append("Official Language")
            if country_data[i].find('ul'):
                datas = country_data[i].ul.find_all("li")
                lis= []
                for d in datas:
                    lis.append(d.find("a").get_text())
                kabir_data.append(lis)
            else:
                kabir_data.append(country_data[i].find("a").get_text().replace('\xa0', " "))
        
        if ("Total" in country_info[i].get_text().replace('\xa0', " ") or "total" in country_info[i].get_text().replace('\xa0', " "))  and "km2" in country_data[i].get_text().replace('\xa0', " "):
            kabir_info.append("Area")
            if country_data[i].find('ul'):
                datas = country_data[i].ul.find_all("li")
                lis= []
                for d in datas:
                    lis.append(d.find("a").get_text())
                kabir_data.append(lis)
            else:
                kabir_data.append(country_data[i].get_text().replace('\xa0', " "))
        
        if country_info[i].get_text().replace('\xa0', " ") == "GDP (nominal)":
            kabir_info.append(country_info[i].get_text().replace('\xa0', " "))
            if country_data[i+1].find('ul'):
                datas = country_data[i+1].ul.find_all("li")
                lis= []
                for d in datas:
                    lis.append(d.find("a").get_text())
                kabir_data.append(lis)
            else:
                kabir_data.append(country_data[i+1].get_text().replace('\xa0', " "))
        
        if "2022 census" in country_info[i].get_text().replace('\xa0', " ") or "2022 estimate" in country_info[i].get_text().replace('\xa0', " "):
            
            if country_data[i].find('ul'):
                pass
            else:
                kabir_info.append("Population")
                kabir_data.append(country_data[i].get_text().replace('\xa0', " "))
    
    for i in range(len(kabir_info)):
        country_dict[kabir_info[i]]=kabir_data[i] 
        
    # print(country_dict)
    return country_dict
    

# result("russia")
    
