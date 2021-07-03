yourFirstName = input("What is your first name? ")
yourLastName = input("What is your last name? ")
yourParentsName = input("What is one of your parents' name? ")
characterName = yourFirstName[0:2]+yourLastName[0:2]+yourParentsName[round((len(yourParentsName)/2)):round((len(yourParentsName)/2))+2]
print(characterName)
