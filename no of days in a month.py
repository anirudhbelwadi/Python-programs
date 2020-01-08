month=input("Enter a month :")
if month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October" or month=="December":
    print("No of days : 31")
elif month=="February":
          i=input("Leap year or not?(Y/N) ")
          if i=="Y":
              print("No of days : 29")
          else:
              print("No of days : 28")
else:
          print("No of days : 30")
