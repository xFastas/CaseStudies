import os 
import subprocess

with open("confusing.txt", "r") as f:
    gl = f.readlines()
    f.close()

ul = []
for line in gl:
    line = line[:-1]
    line = line.split(",")
    ul.append(line)

for line in ul:
    os.system("sudo usermod -a -G "+line[0]+" "+line[1])

