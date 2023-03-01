import csv
import matplotlib.pyplot as plt
import os
import sys

filearray = os.listdir()
filearray = [file for file in filearray if file.endswith(".csv")]
print(filearray)
print("몇 번째")
answer = input()

f = open(filearray[int(answer)], 'r', encoding='utf-8')
rdr = csv.reader(f)
csvarray = []
for line in rdr:
    csvarray.append(line)
f.close()

print(csvarray)
co2array = []
temperarray = []
timearray = []
imu_x_array=[]
imu_y_array=[]
imu_z_array=[]
time2array = []
for i in range(len(csvarray)):
    try:
        if csvarray[i][1] == 'MSG_3':
            co2array.append(csvarray[i+1][2])
            temperarray.append(csvarray[i+1][3])
            timearray.append(csvarray[i+1][0][8:])
        if csvarray[i][1] == 'IMU':
            imu_x_array.append(csvarray[i][2])
            imu_y_array.append(csvarray[i][3])
            imu_z_array.append(csvarray[i][4])

    except Exception as e:
        pass

for i in range(0, len(co2array)):
    time2array.append(timearray[i])

print(co2array)
print(temperarray)
print(imu_x_array)
print(imu_y_array)
print(imu_z_array)

print(timearray)
print(len(co2array))
print(len(timearray))
plt.rc('font', size=5)
timearray = list(map(int, timearray))
plt.plot(timearray, co2array, 'r', label='co2')
plt.plot(timearray, temperarray, 'g', label='temperature')
plt.xlabel('time')
plt.ylabel('value')
plt.legend()
plt.grid(True)
plt.title('KSAT Team CANSAT DATA')

plt.savefig('graph.png', dpi=600)
plt.show()
sys.exit()


