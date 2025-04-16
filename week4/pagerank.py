import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


    
    
        
    
        

def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    pages = list(corpus.keys())
    res = {p: (1 - damping_factor) / len(pages) for p in pages}  # Ajout de la proba pour toutes les pages

    links = corpus[page]
    if links:
        for link in links:
            res[link] += damping_factor / len(links)  # Ajout de la proba pour les liens existants
    else:
        # Si la page n'a pas de liens, elle se comporte comme si elle pointait vers toutes les pages
        for p in pages:
            res[p] += damping_factor / len(pages)

    return res




def sample_pagerank(corpus, damping_factor, n):
    pages = list(corpus.keys())
    res = {p: 0 for p in pages}  # Initialisation des scores
    
    random_page = random.choice(pages)  # Choisir une page de départ au hasard

    for _ in range(n):
        res[random_page] += 1  # Incrémenter la fréquence de visite
        t = transition_model(corpus, random_page, damping_factor)
        random_page = random.choices(list(t.keys()), weights=t.values(), k=1)[0]  # Choisir la prochaine page avec probas

    # Normaliser les valeurs
    for p in res:
        res[p] /= n

    return res




def iterate_pagerank(corpus, damping_factor=0.85, convergence_threshold=0.001):
    N = len(corpus)  # Nombre total de pages
    pagerank = {page: 1 / N for page in corpus}  # Initialisation avec 1/N pour chaque page
    
    while True:
        new_pagerank = {}
        
        for page in corpus:
            # Partie (1 - d) / N -> probabilité d'atterrir sur n'importe quelle page
            new_pagerank[page] = (1 - damping_factor) / N
            
            # Ajouter la somme des contributions des autres pages qui pointent vers cette page
            for potential_linking_page in corpus:
                if page in corpus[potential_linking_page]:  # Si cette page pointe vers "page"
                    num_links = len(corpus[potential_linking_page])
                    new_pagerank[page] += (damping_factor * pagerank[potential_linking_page] / num_links)
            
            # Si une page n'a pas de liens, on suppose qu'elle pointe vers toutes les pages (modèle de téléportation)
            if len(corpus[page]) == 0:
                for target_page in corpus:
                    new_pagerank[target_page] += (damping_factor * pagerank[page] / N)
        
        # Vérifier la convergence
        if all(abs(new_pagerank[p] - pagerank[p]) < convergence_threshold for p in pagerank):
            break
        
        pagerank = new_pagerank  # Mettre à jour les valeurs
    
    return pagerank

   



corpus = crawl("./corpus0")
ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
print(f"PageRank Results from Sampling (n = {SAMPLES})")
for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
ranks = iterate_pagerank(corpus, DAMPING)
print(f"PageRank Results from Iteration")
for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")