#key that will be used
weatherinfo= {
"temp" : 275.45 ,
"feels like" : 271.7 ,
"pressure" : 1014 ,
"humidity" : 74 ,
"temp_min" : 274.27 ,
"temp_max" : 276.48

}
#print ("current temperature is ", weatherinfo["temp"],"kelvin.")
list1= ["akash", "rishan", "nis", "rit"]


for key in weatherinfo.keys():
    print(key)
print("-------")
for value in weatherinfo.values():
    print(value)
for key,value in weatherinfo.items():
    print(key, "------", value)