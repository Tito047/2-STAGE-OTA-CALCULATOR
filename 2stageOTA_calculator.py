import numpy as np
k = 1.380649e-23
Temp = input("Enter the Temperature of operation in Kelvin ")
Temp = float(Temp)
Sxx = input("Enter the Power Spectral Density of the Thermal Noise in JKOhm ")
Sxx = float(Sxx)
Gm1 =  16*(k*Temp)/(3*Sxx)
print(Gm1)
fgbw = input("Enter the Gain Band Width product of the OTA ")
fgbw = float(fgbw)
Cc = Gm1/(2*(np.pi)*fgbw)
print("Compensention Capacitor value is ",(Cc*1e9),"nF")
SR = input("Enter the Slew Rate of the OTA ")
SR = float(SR)
ID1 = SR*Cc/2
Cl = input("Enter load capacitor value")
Cl = float(Cl)
ID8 = 2*(1 + (Cl/Cc))*ID1