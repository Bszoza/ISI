import csv #biblioteka ktora pomoże mi zapisać w porzadnay sposób dane do pliku
def ip_addresses():
    with open("pc.csv","w") as f: #w = write
        kolumny=['pc_name','ip'] #nazywam kolumny
        zapis=csv.DictWriter(f,fieldnames=kolumny)#Otweiram plik do zapisu danych
        zapis.writeheader()#wpisuje nazwy kolumn do pliku
        for i in range(1,101):
            zapis.writerow({'pc_name':"P"+str(i),'ip':"172.30.2."+str(i)})
ip_addresses()


