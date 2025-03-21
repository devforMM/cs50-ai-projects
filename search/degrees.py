import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data():
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"small/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"small/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"small/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors
epxlored=[]
load_data()
source="102"
target="144"
frontiere=QueueFrontier()
node=Node((None,"102"),None,None)
frontiere.add(node)
explored=[]
while True:
    print("##############################################################")
    if node.parent:
     print(f"le parent du noeud est {node.parent.id}")
    

    print(f"la source est {source} et le target est {target}")
    if frontiere.empty():
        print("pas de chemin trouve")
        break
    node=frontiere.remove()
    explored.append(node)
    print(f"le noeud est {node.id}")
    if node.id[1]==target:
        print("trouve")
        chemin=[]
        while node.id[1]!=source:
            chemin.append(node.id)
            node=node.parent
            print(node.id)
        chemin.reverse()
        print(f"le chemin trouve est {chemin}")
        break
    else:
        voisins=neighbors_for_person(node.id[1])
        for v in voisins:
            new_node=Node(v,parent=node,actions=None)
            if new_node not in explored:
             frontiere.add(new_node)
    
    print("###################################################################")
path=chemin

if path is None:
        print("Not connected.")
else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")




