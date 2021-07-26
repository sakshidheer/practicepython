def getFileDataAsDict(filePath , sep="="):
    with open(filePath) as items:
        dictionary = {}
        for item in items: #get each line of item
            itemIdAndName = item.strip().split("=")
            dictionary[itemIdAndName[0].strip()] =itemIdAndName[1].strip()  
        return dictionary   

print("Welcome to pokemon info center")
name = input("Please enter your name: ")
pokeDict = getFileDataAsDict("asserts/exercise3/pokemons.txt")
print(*pokeDict.items(), sep="\n")
pokemon_id = input(
    "Enter the number from the list corresponding to the pokemon you want to know about : ")
pokemon_name = pokeDict[pokemon_id]
print("Entered pokemon name is {}. Fetching details....".format(pokemon_name))
abilitiesDict = getFileDataAsDict("asserts/exercise3/Abilities.txt")
evolutionChartDict = getFileDataAsDict("asserts/exercise3/EvolutionChart.txt")
speciesDict = getFileDataAsDict("asserts/exercise3/Species.txt")
print(abilitiesDict[pokemon_name])
print(evolutionChartDict[pokemon_name])
print(speciesDict[pokemon_name])