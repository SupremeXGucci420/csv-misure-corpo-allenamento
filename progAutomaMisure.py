import pyfiglet
import csv
  
result = pyfiglet.figlet_format("SoS Parki", font = "isometric1" )
print(result)

print(" ")
print(" ")
print("------------------------------------ ")
print(" ")

sceltaPeso = input("Vuoi aggiungere il peso? s/n: ")
if(sceltaPeso=='s'):
    data = input("Data Pesata aaaa/mm/gg -->: ")
    pesoOd = input("Inserire il peso in kg: ")
    print("---------Pesata Completata---------------")
else:
    data = ""
    pesoOd = ""

print("---------Inserimento misure---------------")
print(" ")

dataMisure = input("Data misure aaaa/mm/gg -->: ")
vita = input("Inserire le dimensioni della vita: ")
torace = input("Inserire le dimensioni del torace: ")
braccioSx = input("Inserire le dimensioni del braccio sinistro: ")
braccioDx = input("Inserire le dimensioni del braccio destro: ")
cosciaSx = input("Inserire le dimensioni della coscia sinistra: ")
cosciaDx = input("Inserire le dimensioni della coscia destra: ")
culo = input("Inserire le dimensioni del culo: ")

with open('misure.csv', mode='a') as misure_file:
    misure_writer = csv.writer(misure_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #misure_writer.writerow(['data pesata','peso','Media',' ','Data misure','Vita','Torace','Braccio sx','Braccio dx','Coscia sx','Coscia dx','Culo'])    
    misure_writer.writerow([data,pesoOd,' ',' ',dataMisure,vita,torace,braccioSx,braccioDx,cosciaSx,cosciaDx,culo])


# dataframe Name and Age columns
#df = pd.DataFrame([(data,pesoOd,' ',' ',dataMisure,vita,torace,braccioSx,braccioDx,cosciaSx,cosciaDx,culo)],
#                   columns = ('data pesata','peso','Media',' ','Data misure','Vita','Torace','Braccio sx','Braccio dx','Coscia sx','Coscia dx','Culo'))


#with pd.ExcelWriter('demo.xlsx', engine="openpyxl" ,mode='a', if_sheet_exists='replace') as writer:
#    df.to_excel(writer,sheet_name='Foglio1',index=False)

print(" ")
print(" ")

print("------------Processo terminato----------------")
print(" ")
print(" ")


#writer.close()





#print(df)
