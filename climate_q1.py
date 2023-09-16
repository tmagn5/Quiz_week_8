import matplotlib.pyplot as plt
import pandas as pd
        
years = []
co2 = []
temp = []

df = pd.read_csv("./climate_q1.py")

years.add(plt.plot[0])
co2.add(plt.plot[1])
temp.add(plt.plot[1])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
