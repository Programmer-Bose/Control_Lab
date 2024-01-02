import matplotlib.pyplot as plt
import numpy as np

#Time 
tim_i15 = np.array([15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 
                    180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 
                    330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 
                    495, 510, 525, 540, 555, 570, 585, 600, 615, 630, 645, 
                    660, 675, 690, 705, 720, 735, 750, 765, 780, 795, 810, 
                    825, 840, 855, 870, 885, 900, 915, 930])

#Temp at 15 Sec Interval
temp = np.array([28.30, 31.50, 35.60, 40.40, 45.60, 51.80, 52.60, 60.70, 
                65.50, 68.70, 73.50, 77.20, 80.40, 83.70, 86.40, 89.00, 
                91.20, 93.40, 95.40, 97.10, 98.80, 100.30, 101.60, 102.90, 
                104.10, 105.20, 106.10, 107.20, 107.80, 108.60, 109.30, 
                109.90, 110.40, 110.90, 111.30, 111.70, 112.10, 112.50, 
                112.80, 113.10, 113.40, 114.1,114.5,114.9,115.2,115.6,116.2,
                116.4,116.7,116.9,117.1,117.2,117.3,117.5,117.6,117.8,118.00,
                118.1,118.2,118.4,118.5,118.6])

plt.grid(True)

# Plotting with markers
plt.plot(tim_i15, temp, marker='o', label='Temp')



# Adding labels and title
plt.xticks(range(0,1000,50))
plt.yticks(range(0,140,5))
plt.xlabel('Time (Sec)')
plt.ylabel('Temperature(degree C)')
plt.title('Open Loop Study for Identification of Oven Parameters')





# Adding a legend
plt.legend(loc='upper right')

# Display the plot
plt.show()