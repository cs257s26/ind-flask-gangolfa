import csv
import sys
from pathlib import Path

# Get the directory of this script
DEFAULT_DATA_PATH = Path(__file__).parent/'data'/'interpol_classified_stolen_art.csv'
ARTIST_DATA_PATH = Path(__file__).parent/'data'/'artists.csv'

def load_data(data_path) -> list:
    """Returns a list of the provided csv file.

    Args:
        data_path (str): The path to the data. 

    Returns:
        list: A list containing the rows or content of the CSV file.
    """
    
    data = []
    
    with open(data_path, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

    return data

def find_creator(name_of_artwork: str) -> str | None:
    """Returns who created the given piece of artwork

    Args:
        name_of_artwork (str): the name of the artwork
    
    Returns:
        string or None: the name of the creator if the artwork is in the database,
            otherwise None"""
    
    # Checks if the type of input is correct
    if (type(name_of_artwork) != str):
         raise TypeError("please provide a valid input")

    # by default assumes we use the stolen art csv
    data = load_data(DEFAULT_DATA_PATH)

    # goes through the data and finds the artwork
    for row in data:
        if row[0] == name_of_artwork:
            return row[1]
    
    # returns None if the artwork isn't in our database
    return None

def origin_count(origin: str) -> str | None:
    """Returns the number of artist in total from given orgin

    Args:
        orgin (str): the country of artist's orgin 
    
    Returns:
        string or None: the count of artists from that orgin if in our database,
            otherwise None"""
    
    # Checks if the type of input is correct
    if (type(origin) != str):
        raise TypeError("Please provide a valid input.")

    # artists data
    artist_data = load_data(ARTIST_DATA_PATH)

    origin_count = 0

    # goes through the data and finds the artwork
    for row in artist_data:
        if row[1] == origin:
            origin_count+=1
    
    # returns None if the artwork isn't in our database
    if(origin_count == 0):
        return None
    else:
        return("The number of artists with stolen art who are from " + origin + ": " + str(origin_count))
    
def count_stolen_by_artist(artist:str) -> int:
    """Returns the number of stolen artwork by a given artist

    Args:
        artist (str): the artist whom you want stolen works count 
    
    Returns:
        int: the count of stolen works by a given artist"""
    

    if (type(artist) != str):
        raise TypeError("Please provide a valid input.")

    data = load_data(DEFAULT_DATA_PATH)
    stolen_count = 0

    for row in data:
        if artist in row[1]:
            stolen_count+=1

    return stolen_count



def main(args):
    if args[0] == "--art":
        print(find_creator(args[1]))
    elif args[0] == "--origin":
        print(origin_count(args[1]))
    elif args[0] == "--count_stolen":
        print(count_stolen_by_artist(args[1]))
    else:
        print("No tag")
    

if __name__ == '__main__':
    main(sys.argv[1:])