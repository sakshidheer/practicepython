
def getFileDataAsDict(filePath , sep="="):
    with open(filePath) as items:
        dictionary = {}
        for item in items: #get each line of item
            itemIdAndName = item.strip().split("=")
            dictionary[itemIdAndName[0].strip()] =itemIdAndName[1].strip()  
        return dictionary   

pokeDict = getFileDataAsDict("asserts/exercise3/pokemons.txt")
abilitiesDict = getFileDataAsDict("asserts/exercise3/Abilities.txt")
evolutionChartDict = getFileDataAsDict("asserts/exercise3/EvolutionChart.txt")
speciesDict = getFileDataAsDict("asserts/exercise3/Species.txt")

def printAndAddInfoToFile(pokemon_name, name):
    abilities = abilitiesDict[pokemon_name]
    evolutionChart = evolutionChartDict[pokemon_name]
    species = speciesDict[pokemon_name]
    print(abilities)
    print(evolutionChart)
    print(species)
    with open("{}.txt".format(name),"a+") as userfile:
        userfile.write("{} details:\n ".format(pokemon_name))
        userfile.write("Abilities: {}\n".format(abilities))
        userfile.write("Evolution Chart: {}\n".format(evolutionChart))
        userfile.write("Species: {}\n".format(species))
        userfile.write("************************************\n\n\n")
    
print("Welcome to pokemon info center")
name = input("Please enter your name: ")
pokeDict = getFileDataAsDict("asserts/exercise3/pokemons.txt")
abilitiesDict = getFileDataAsDict("asserts/exercise3/Abilities.txt")
evolutionChartDict = getFileDataAsDict("asserts/exercise3/EvolutionChart.txt")
speciesDict = getFileDataAsDict("asserts/exercise3/Species.txt")
wantToContinue = True
while wantToContinue:
    print(*pokeDict.items(), sep="\n")
    pokemon_id = input(
        "Enter the number from the list corresponding to the pokemon you want to know about : ")
    pokemon_name = pokeDict[pokemon_id]
    print("Entered pokemon name is {}. Fetching details....".format(pokemon_name))
    printAndAddInfoToFile(pokemon_name,name)
    usercontinuerequest = input("Do you want to continue? Enter y to continue")
    if usercontinuerequest.lower() != 'y':
       wantToContinue = False

