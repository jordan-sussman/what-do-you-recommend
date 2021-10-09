import requests
import os
import sys

# Create input prompt and format it to be compatible for the url request
prompt = input("\nType below for music or movie recommendations\n      > ")
recommendation = prompt.replace(" ", "+") 
query = requests.get("https://tastedive.com/api/similar?q={}".format(recommendation))

# Compile list of recommendation results
print("\nHere's what I recommend:")
data = query.json()
for x in data['Similar']['Results']:
    results = str(x['Name'])
    print("- " + results)

#Automatically rerun to allow input for a new recommendation
os.execv(sys.executable, ['python'] + sys.argv)
