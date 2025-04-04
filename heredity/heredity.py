import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}



def main():

    # Check for proper usage
    
    people = load_data("./data/family0.csv")

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    res=1
    for p in people.keys():
            if p in one_gene:
               x=1
               if people[p]["mother"] is None or people[p]["father"] is None:
                   prob_gene=PROBS["gene"][1]
               else:
                   prob_gene=PROBS["mutation"]*PROBS["mutation"]+(1-PROBS["mutation"])*(1-PROBS["mutation"])      
            elif p in two_genes:
                x=2
                prob_gene=PROBS["gene"][2]
            else:
                x=0
                prob_gene=PROBS["gene"][0]
                
                
                
            if p in have_trait:
                proba=prob_gene*PROBS["trait"][x][True]
            else:
                proba=prob_gene*PROBS["trait"][x][False]
            res=res*proba    
    return res
            
def update(probabilities, one_gene, two_genes, have_trait, p):
    for people in probabilities.keys():
      if people in have_trait:
        if people in one_gene:
            probabilities[people]["gene"][1]+=p
        elif people in two_genes:
            probabilities[people]["gene"][2]+=p
        elif people in one_gene and people in two_genes:
            probabilities[people]["gene"][1]+=p
            probabilities[people]["gene"][2]+=p
        else:
            probabilities[people]["gene"][0]+=p
        probabilities[people]["trait"][True]+=p
      else:
        if people in one_gene:
            probabilities[people]["gene"][1]+=p
        elif people in two_genes:
            probabilities[people]["gene"][2]+=p
        elif people in one_gene and people in two_genes:
            probabilities[people]["gene"][1]+=p
            probabilities[people]["gene"][2]+=p
        else:
            probabilities[people]["gene"][0]+=p
        probabilities[people]["trait"][False]+=p          
          

def normalize(probabilities):
    
    for people in probabilities.keys():
        x=1/( probabilities[people]["trait"][True]+probabilities[people]["trait"][False])
        probabilities[people]["trait"][True]*=x
        probabilities[people]["trait"][False]*=x
        y=1/(probabilities[people]["gene"][0]+probabilities[people]["gene"][1]+probabilities[people]["gene"][2])
        probabilities[people]["gene"][0]*=y
        probabilities[people]["gene"][1]*=y
        probabilities[people]["gene"][2]*=y
        
        
        


if __name__ == "__main__":
    main()
