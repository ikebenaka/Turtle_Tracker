#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2023
#--------------------------------------------------------------

#Ask user for the search date
user_date = input("Enter a date to search for Sara (M/D/YYYY):")

#Create a variable pointing to the data file
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a listdate
lineString = file_object.readline()

#Initialize empty dictionaries
date_dict = {}
location_dict = {}

#Iterate through all lines in the list
while lineString:
    
    if lineString[0] in ("#","u"):  #check if line is a data line as opposed to a header
        lineString = file_object.readline() #What does this do?
        continue #if it is a header, then disregard this line of data and move to the next line
    lineData = lineString.split() #if it is not a header (real data), split the string into a list of data items
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Omit suspect location records
    if obs_lc in ("1","2","3"): #only add acceptable location records
    
        #Add items to dictionaries
        date_dict[record_id] = obs_date #add date record to dictionary
        location_dict[record_id] = (obs_lat, obs_lon) #add location record to dictionary

    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    # Move to the next line
    lineString = file_object.readline()

#Initialize an empty key list
key_list = []

#Loop through all key, value pairs in the date dictionary
for key, value in date_dict.items():
    if value == user_date:   #See if any dates (values) match the user date
        key_list.append(key)     #If so, add the key to the list of keys



#Report whether no records were found
if len(key_list) == 0:
    print(f"There are no observations for Sara on {user_date}")
else:
    #Reveal locations for each key in key_list
    for key in key_list:
        lat, lng = location_dict[key]
        print(f"Record {key} indicates Sara was seen at lat: {lat}, lon: {lng} on {user_date}")