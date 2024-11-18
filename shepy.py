import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("/Users/hp/Desktop/pharmacy ms.csv") 
df=df.rename({0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,15:16,16:17,17:18,18:19,19:20},axis=0)
while (True):
    print("+-------------------------------+")
    print("+           MEDINEST           +")
    print("+            PHARMA             +")
    print("+    'YOUR PATH TO WELLNESS'    +")
    print("+-------------------------------+")
    print("          HOME PAGE             ")
    print("1-ABOUT OUR STORE")
    print("2-FETCH ALL DATA")
    print("3-DATA ANLYSIS")
    print("4-WORKING ON RECORDS")
    print("5-DATA VISUALISATION")
    print("6-EXIT")
    a=int(input("ENTER YOUR CHOICE:"))
    if a==1:
        print("Welcome to Medinest,your trusted destination for all your healthcare needs")
        print("We are proud to offer a wide range of prescription medications,over-the-counter products,vitamins,and health essentials")
        print("Our shelves are stocked with high-quality products from reliable brands,all at affordable prices")
        print("Whether you need expert advice,personalized care,or quick refills,our mission is to provide exceptional service")
        print("While ensuring your health remains our top priority")
        print("Thank you for choosing us as your pharmacy of choice!")
    elif a==2:
        print(df.to_string())
    elif a==3:
        while (True):
          print("+----------------------------------+")
          print("+      DATA ANALYSIS            +")
          print("+----------------------------------+")
          print("1-Display all available medicines")
          print("2-Display the dosge of all brands")
          print("3-Most expensive product")
          print("4-Cheapest product")
          print("5-Best seller of all time")
          print("6-Least sold product")
          print("7-Highest dosage medicine")
          print("8-Lowest dosage medicine")
          print("9-Average sales per month")
          print("10-Total sales per month")
          print("11-Sort the data according to stock")
          print("12-Sort the data according to sales")
          print("13-Sort the data according to price")
          print("14-Sort the data according to dosage")
          print("15-Exit")
          b=int(input("ENTER YOUR CHOICE:"))
          if b==1:
              print("The medicines available:")
              print(df.iloc[0:21,0:2])
          elif b==2:
              print("The dosage of all medicines:")
              print(df.iloc[0:21,0:3])
          elif b==3:
              print("The most expensive medicine of the pharmacy is:")
              print(df[['medicine name','price per unit']].max())
          elif b==4:
              print("The most cheapest medicine of the pharmacy is:")
              print(df[['medicine name','price per unit']].min())
          elif b==5:
              print("Best seller of all time:")
              print(df[['medicine name','quantity sold']].max())
          elif b==6:
              print("The leat sold product:")
              print(df[['medicine name','quantity sold']].min())
          elif b==7:
              print("The medicine with highest dasage is:")
              print(df[['medicine name','dosage']].max())
          elif b==8:
              print("The medicine with lowest dosage is:")
              print(df[['medicine name','dosage']].min())
          elif b==9:
              print("Average sales per months:")
              print(df['quantity sold'].mean())
          elif b==10:
              print("Total sales per month:")
              print(df[['quantity sold','price per unit']].sum())
          elif b==11:
              df=df.sort_values(by=['quantity in stock'])
              print(df.to_string())
          elif b==12:
              df=df.sort_values(by=['quantity sold'])
              print(df.to_string())
          elif b==13:
              df=df.sort_values(by=['price per unit'])
              print(df.to_string())
          elif b==14:
              df=df.sort_values(by=['dosage'])
              print(df.to_string())
          elif b==15:
              print("BACK TO HOME PAGE.........")
              break
          df=df.sort_index()
    elif a==4:
          while (True):
              print("+---------------------------------------------+")
              print("+             WORKING ON RECORDS              +")
              print("+---------------------------------------------+")
              print(" 1 - Add a new medicine")
              print(" 2 - Update a record")
              print(" 3 - Delete a medicine")
              print(" 4 -Exit")
              c=int(input("ENTER YOUR CHOICE:"))
              if c==1:
                  medicine_code=int(input("Enter medicine code for new medicine:"))
                  medicine_name=input("Enter the new medicine name:")
                  dosage=str(input("Enter the dosages of all medicines:"))
                  quantity_in_stock=int(input("Enter the stocks of medicines:"))
                  quantity_sold=int(input("Enter the no.of sold product:"))
                  remaining_stock=int(input("Enter the remaining stocks:"))
                  price_per_unit=float(input("Enter the price of the product:"))
                  df.loc[medicine_code]=[medicine_code,medicine_name,dosage,quantity_in_stock,quantity_sold,remaining_stock,price_per_unit]
                  print("DATA SUCCESSFULLY INSERTED!")
              elif c==2:
                  medicine_code=int(input("Enter the medicine code for the medicine to be updated:"))
                  medicine_name=(input("Enter the medicine name to be updated:"))
                  dosage=str(input("Enter the amount of dosage:"))
                  quantity_in_stock=int(input("Enter the stock of the medicine:"))
                  quantity_sold=int(input("Enter the no.of sold product:"))
                  remaining_stock=int(input("Enter the remaining stocks:"))
                  price_per_unit=float(input("Enter the price of the product:"))
                  df.loc[medicine_code]=[medicine_code,medicine_name,dosage,quantity_in_stock,quantity_sold,remaining_stock,price_per_unit]
                  print("DATA SUCCESSFULLY UPDATED!")
                  print(df.to_string())
              elif c==3:
                  medicine_code=int(input("Enter the medicine code for the medicine to be deleted:"))
                  df.drop(medicine_code,axis=0,inplace=True)
                  print(df.to_string())
              elif c==4:
                  print("BACK TO HOME PAGE............")
                  break
    elif a==5:
          while (True):
             print("+-----------------------------------------------+")
             print("+            DATA VISUALISATION                 +")
             print("+-----------------------------------------------+")
             print(" 1 - Line plot")
             print(" 2 - Vertical bar plot")
             print(" 3 - Pie chart")
             print(" 4   - Exit")
             d=int(input("ENTER YOUR CHOICE:"))
             if d==1:
                 while (True):
                     print(" Line plot sub menu ")
                     print(" 1 - Stocks analysis")
                     print(" 2 - Sales analysis")
                     print(" 3 - remaining analysis")
                     print(" 4 - Exit")
                     e=int(input("ENTER YOUR CHOICE:"))
                     if e==1:
                         dff=pd.DataFrame(df.iloc[:,1:4:2])
                         dff.plot('medicine name','quantity in stock',marker='*',color='r',linestyle='--',markeredgecolor='k')
                         plt.xlabel("MEDICINE NAMES")
                         plt.ylabel("STOCK")
                         plt.title("STOCKS ANALYSIS")
                         plt.show()
                     elif e==2:
                         dff=pd.DataFrame(df.iloc[:,1:5:3])
                         dff.plot('medicine name','quantity sold',marker='*',color='b',linestyle='--',markeredgecolor='k')
                         plt.xlabel("MEDICINE NAMES")
                         plt.ylabel("SALES")
                         plt.title("SALES ANALYSIS")
                         plt.show()
                     elif e==3:
                         dff=pd.DataFrame(df.iloc[:,1:7:4])
                         dff.plot('medicine name','remaining stock',marker='*',color='g',linestyle='--',markeredgecolor='k')
                         plt.xlabel("MEDICINE NAMES")
                         plt.ylabel("REMAINING")
                         plt.title("REMAINING ANALYSIS")
                         plt.show()
                     elif e==4:
                         print("BACK TO DATA VISUALISATION MENU........")
                         break
             elif d==2:
                 while (True):
                     print(" Vertical bar plot sub menu ")
                     print(" 1 - Stocks analysis")
                     print(" 2 - Sales analysis")
                     print(" 3 - remaining analysis")
                     print(" 4 - Exit")
                     f=int(input("ENTER YOUR CHOICE:"))
                     if f==1:
                         dff=pd.DataFrame(df.iloc[:,1:4:2])
                         dff.plot('medicine name','quantity in stock',kind='bar',color='blue')
                         plt.xlabel("MEDICINE NAMES")
                         plt.ylabel("STOCKS")
                         plt.title("STOCKS ANALYSIS")
                         plt.legend()
                         plt.xticks(rotation='vertical')
                         plt.show()
                     elif f==2:
                         dff=pd.DataFrame(df.iloc[:,1:5:3])
                         dff.plot('medicine name','quantity sold',kind='bar',color='purple')
                         plt.xlabel("MEDICINE NAMES")
                         plt.ylabel("SALES")
                         plt.title("SALES ANALYSIS")
                         plt.legend()
                         plt.xticks(rotation='vertical')
                         plt.show()
                     elif f==3:
                         dff=pd.DataFrame(df.iloc[:,1:7:4])
                         dff.plot('medicine name','remaining stock',kind='bar',color='red')
                         plt.xlabel("MEDICINE NAMES")
                         plt.ylabel("REMAINING STOCK")
                         plt.title("REMAINING ANALYSIS")
                         plt.legend()
                         plt.xticks(rotation='vertical')
                         plt.show()
                     elif f==4:
                         print("BACK TO DATA VISUALISATION MENU.............")
                         break
             elif d==3:
                 while (True):
                     print("PIE CHART SUB MENU")
                     print(" 1 - Stocks analysis")
                     print(" 2 - Sales analysis")
                     print(" 3 - remaining analysis")
                     print(" 4 - Exit")
                     g= int(input("ENTER YOUR CHOICE:"))
                     if g==1:
                         dff=pd.DataFrame(df)
                         dff.index=df['medicine name']
                         dff.plot.pie(y='quantity in stock',label='medicine name',legend=False,title='STOCKS ANALYSIS')
                         plt.show()
                     elif g==2:
                         dff=pd.DataFrame(df)
                         dff.index=df['medicine name']
                         dff.plot.pie(y='quantity sold',label='Medicine Name',legend=False,title='SALES ANALYSIS')
                         plt.show()
                     elif g==3:
                         dff=pd.DataFrame(df)
                         dff.index=df['medicine name']
                         dff.plot.pie(y='remaining stock',label='medicine name',legend=False,title='REMAINING ANALYSIS')
                         plt.show()
                     elif g==4:
                         print("BACK TO DATA VISUALISATION MENU...............")
                         break
             elif d==4:
                 print("BACK TO HOME PAGE...............")
                 break
    elif a==6:
        print("THANK YOU FOR VISITING MEDINEST PHARAMCY.")
        break
                    
                
    
                    
           
                            
                  
