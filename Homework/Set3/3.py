
date = "22/2/2020"

choice = input("Enter the choice of either '-' or '/'")

if choice == '-':
    date = date.replace('/','-')
elif choice == '/':
    date = date.replace('-','/')

print(date)
