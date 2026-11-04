import matplotlib.pyplot



with open("/Users/l22/PycharmProjects/PythonProject/PhysSIM/tromsoe_1954_2025_med_makstemperatur.csv","r") as tromsoe:
    data_tromsoe = {}
    for line in tromsoe:
        line = line.strip().split(';')
        dato = line[2].split('.')
        try:
            year = dato[2]
            month = dato[1]
            day = dato[0]
            if year not in data_tromsoe:
                data_tromsoe[year] = {}
            if month not in data_tromsoe[year]:
                data_tromsoe[year][month] = {}
            if day not in data_tromsoe[year][month]:
                data_tromsoe[year][month][day] = {}
                data_tromsoe[year][month][day] = {'Max_temp': line[3],'Middle_temp': line[4],'Nedbør': line[5],'Høyeste middlevind': line[6], 'Snødybde': line[7]}
        except IndexError:
            pass

with open("/Users/l22/PycharmProjects/PythonProject/PhysSIM/venabu_1954_2025_med_makstemperatur.csv","r") as venabu:
    data_venabu = {}
    for line in venabu:
        line = line.strip().split(';')
        dato = line[2].split('.')
        try:
            year = dato[2]
            month = dato[1]
            day = dato[0]
            if year not in venabu:
                data_venabu[year] = {}
            if month not in data_venabu[year]:
                data_venabu[year][month] = {}
            if day not in data_venabu[year][month]:
                data_venabu[year][month][day] = {}
                data_venabu[year][month][day] = {'Max_temp': line[3],'Middle_temp': line[4],'Nedbør': line[5],'Høyeste middlevind': line[6], 'Snødybde': line[7]}
        except IndexError:
            pass

with open("/Users/l22/PycharmProjects/PythonProject/PhysSIM/vaernes_1954_2025_med_makstemperatur.csv","r") as vaernes:
    data_vaernes = {}
    for line in vaernes:
        line = line.strip().split(';')
        dato = line[2].split('.')
        try:
            year = dato[2]
            month = dato[1]
            day = dato[0]
            if year not in venabu:
                data_vaernes[year] = {}
            if month not in data_vaernes[year]:
                data_vaernes[year][month] = {}
            if day not in data_vaernes[year][month]:
                data_vaernes[year][month][day] = {}
                data_vaernes[year][month][day] = {'Max_temp': line[3],'Middle_temp': line[4],'Nedbør': line[5],'Høyeste middlevind': line[6], 'Snødybde': line[7]}
        except IndexError:
            pass

with open("/Users/l22/PycharmProjects/PythonProject/PhysSIM/sinnes_2014_2025.csv","r") as sinnes:
    data_sinnes = {}
    for line in sinnes:
        line = line.strip().split(';')
        dato = line[2].split('.')
        try:
            year = dato[2]
            month = dato[1]
            day = dato[0]
            if year not in sinnes:
                data_sinnes[year] = {}
            if month not in data_sinnes[year]:
                data_sinnes[year][month] = {}
            if day not in data_sinnes[year][month]:
                data_sinnes[year][month][day] = {}
                data_sinnes[year][month][day] = {'Max_temp': line[3],'Middle_temp': line[4],'Nedbør': line[5],'Høyeste middlevind': line[6], 'Snødybde': line[7]}
        except IndexError:
            pass

with open("/Users/l22/PycharmProjects/PythonProject/PhysSIM/roeros_1954_2025_med_makstemperatur.csv","r") as roeros:
    data_roeros = {}
    for line in roeros:
        line = line.strip().split(';')
        dato = line[2].split('.')
        try:
            year = dato[2]
            month = dato[1]
            day = dato[0]
            if year not in roeros:
                data_roeros[year] = {}
            if month not in data_roeros[year]:
                data_roeros[year][month] = {}
            if day not in data_roeros[year][month]:
                data_roeros[year][month][day] = {}
                data_roeros[year][month][day] = {'Max_temp': line[3],'Middle_temp': line[4],'Nedbør': line[5],'Høyeste middlevind': line[6], 'Snødybde': line[7]}
        except IndexError:
            pass

with open("/Users/l22/PycharmProjects/PythonProject/PhysSIM/oslo_blindern_1954_2025_med_makstemperatur.csv", "r") as oslo:
    data_oslo = {}
    for line in oslo:
        line = line.strip().split(';')
        dato = line[2].split('.')
        try:
            year = dato[2]
            month = dato[1]
            day = dato[0]
            if year not in oslo:
                data_oslo[year] = {}
            if month not in data_oslo[year]:
                data_oslo[year][month] = {}
            if day not in data_oslo[year][month]:
                data_oslo[year][month][day] = {}
                data_oslo[year][month][day] = {'Max_temp': line[3],'Middle_temp': line[4],'Nedbør': line[5],'Høyeste middlevind': line[6], 'Snødybde': line[7]}
        except IndexError:
            pass





# i want the code to read each line, assin


#3,4,5,6,7 is data in line_X

