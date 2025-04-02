import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        
        
        for var in self.domains.keys():
            for word in self.domains[var]:
                if len(word)!=len(var):
                    self.domains[var].remove(word)
        
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        raise NotImplementedError

    def revise(self, x, y):
        (x_pos,y_pos)=self.crossword.overlaps(x,y)
        if x is None or y is None:
            return False
        for word in self.domains[x]:
            if word[x_pos]!=y[y_pos]:
                self.domains.remove(word)
        return True        
            
            
            
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        raise NotImplementedError

    def ac3(self, arcs=None):
        file=[]
        if arcs is None:
            for v in self.crossword.variables:
                my_var=v
                for v in self.crossword.varibales:
                    if v!=my_var:
                        file.append(my_var,v)
        else:
            file=arcs
        
        for arc in file:
            if self.revise(arc[0],arc[1]):
                if self.domains[arc[0]]==set():
                    return False
                y=arc[0]
                for v  in self.crossword.variables:
                    if arc!=y:
                        file.append(arc)
                
        return True
                        
    def assignment_complete(self, assignment):
        if any(assignment.values())==None:
            return False
        return True

    def consistent(self, assignment):
        def compare(liste):
            seconde_liste=[]
            for e in liste:
                if e not in seconde_liste:
                 seconde_liste.append(e)
                else:
                    return False
        values=[v for v in assignment.values]
        if compare(values)==False:
                return False
           
        for var in assignment.keys():
            if len(var)!=assignment[var]:
                return False
            for voisin  in var.neighbors:
                if self.revise(var,voisin)==False:
                    return False
        return True
    
        

    def order_domain_values(self, var, assignment):
        liste=[]
        voisins=[]
        for v in self.neigbors[var]:
            if assignment[v]==None:
                voisins.append(v)
        for value in self.crossword.domains(var):
            count=0
            for v in voisins:
                x_pos,ypos=self.crossword.overlaps(var,v)
                for possible_value in self.crossword.domains[v]:
                    if var[x_pos]!=possible_value[ypos]:
                        count+=1
            liste.append(value,count)
        liste_triee = sorted(liste, key=lambda x: x[1])
        
        res=[e[0] for e in liste_triee ]
        return res

            
            
                

    def select_unassigned_variable(self, assignment):
        
        unassigned_variables=[]
        
        for var in assignment:
            if assignment[var]==None:
                unassigned_variables.append(var)
        lengths=[]
        for var in unassigned_variables:
            lengths.append(var,len(self.domains[var]))
        length_2=[l[1] for l in lengths]
        min_legth=min(length_2)
        
        meme_longeur=[]
        for l in lengths:
            if l[1]==min_legth:
                meme_longeur.append(l)
        if len(meme_longeur)<1:
            return l[0]
        else:
            lengths_neighbors=[(len(self.crossword.neigbors(l)),l) for l in meme_longeur]
            sorted(lengths_neighbors)
            return lengths_neighbors[0][1]
        
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        raise NotImplementedError

    def backtrack(self, assignment):
    # Si l'assignation est complète, on retourne l'assignation finale
        if self.assignment_complete(assignment):
            return assignment

        # Sélectionner une variable non assignée
        var = self.select_unassigned_variable(assignment)

        # Essayer chaque valeur possible pour cette variable
        for value in self.order_domain_values(var, assignment):
            # Assigner temporairement la valeur à la variable
            assignment[var] = value

            # Vérifier si l'assignation reste cohérente
            if self.consistent(assignment):
                # Continuer la recherche avec cette assignation
                result = self.backtrack(assignment)
                if result is not None:
                    return result  # Une solution valide a été trouvée

            # Supprimer l'assignation en cas d'échec et essayer une autre valeur
            assignment.pop(var)

        # Si aucune valeur ne fonctionne, on retourne None pour signaler l'échec
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
