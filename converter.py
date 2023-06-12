import json
from param import *
from mlsolver.formula import Atom, Not
from mlsolver.kripke import World, KripkeStructure

def convert(nw_model):
    # Build a list of all knowledge in the system
    atoms = set()
    for key, value in nw_model.items():
        for atom in value["kb"]:
            atoms = atoms.union({atom})
    
    # Create worlds
    def rec_assignments(atoms: set, assignments: dict = {}):
        if(len(atoms) == 0): return [assignments]
        atoms = atoms.copy()
        atom = atoms.pop()
        ass1 = assignments
        ass2 = assignments.copy()
        ass1[atom] = True
        ass2[atom] = False
        ass1 = rec_assignments(atoms, ass1)
        ass2 = rec_assignments(atoms, ass2)
        return [*ass1, *ass2]
    
    assignments = rec_assignments(atoms)

    worlds = []
    for i, ass in enumerate(assignments):
        worlds.append(World(str(i), ass))
    
    # Create relations between states
    def check_kb(w0, w1):
        # check if all accessible states 
        check = True
        for atom in value["kb"]:
            check = check and w0.assignment[atom] == w1.assignment[atom] 
        return check
    
    relations = {}
    for key, value in nw_model.items():
        relations[key] = set()
        for w0 in worlds:
            for w1 in worlds:
                if(check_kb(w0, w1)): relations[key].add((w0.name, w1.name))
    return KripkeStructure(worlds, relations)

# test
if __name__ == "__main__":
    with open(DIR_NW_MODELS + "simple" + ".json", 'r') as json_file:
        model = json.load(json_file)
    kripkemodel = convert(model["networks"])
    pass
    