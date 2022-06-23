import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hikelog-876f2-firebase-adminsdk-v964y-897d9ff056.json"
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'hikelog-876f2',
})

db = firestore.client()

#function to add data
def addData(db): 
  #create variables to store data
  hname = input("Enter Hike Name: ")
  hdistance = input("What was the hike distance in miles?")
  hlocation = input("What state is the hike located in?")
  completion = int(input("How many times have you completed this hike?"))

  result = db.collection("hikelog").document(hname).get()
  if result.exists:
    print("Item already exists.")
    return

  data = {
    "hike_name": hname,
    "hike_distance(miles)": hdistance,
    "Location(State)": hlocation,
    "Times Completed": completion
    }
  #Store Data

  db.collection("hikelog").document(hname).set(data)
#Function to Modify data

def mod(db):
  hname = input("Enter Hike Name: ")
  completion = int(input("How many more times have you completed the hike?"))
  result = db.collection("hikelog").document(hname).get()
  if not result.exists:
    print("Invalid Name")
    return  
  data = result.to_dict()

  data["Times Completed"] += completion
  db.collection("hikelog").document(hname).set(data)

#function to delete data
def deletedata(db):
  hname = input("Enter Hike Name:")

  result = db.collection("hikelog").document(hname).get()
  if not result.exists:
    print("Invalid Name")
  
  db.collection("hikelog").document(hname).delete()
#Function to view data
def viewdata(db):
  hname = input("Which information would you like to see?")

  result = db.collection("hikelog").document(hname).get()
  if not result.exists:
    print("Invalid Name")
  data = result.to_dict()
  print(data)
#Main function to call functions
def main():
  choice = None

  while choice != "0":
    print()
    print("0) Exit")
    print("1) Add Hike")
    print("2) Add Completions to Hike")
    print("3) Delete Hike")
    print("4) View Hike")
    choice = input("> ")
    if choice == "1":
      addData(db)
    elif choice == "2":
      mod(db)
    elif choice == "3":
      deletedata(db)
    elif choice == "4":
      viewdata(db)

main()
  





