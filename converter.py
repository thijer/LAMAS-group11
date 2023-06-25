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
    def check_kb(w0, w1, kb):
        # check if all accessible states 
        check = True
        for atom in kb:
            check = check and w0.assignment[atom] == w1.assignment[atom] 
        return check
    
    relations = {}
    for key, value in nw_model.items():
        relations[key] = set()
        for w0 in worlds:
            for w1 in worlds:
                if(check_kb(w0, w1, value["kb"])): relations[key].add((w0.name, w1.name))
    return KripkeStructure(worlds, relations)

def convert_v2(nw_model):
    # Create a Kripke model where there is a world for every atom, its negation, and agent. 

    # Build a list of all knowledge in the system
    atoms = set()
    for key, value in nw_model.items():
        for atom in value["kb"]:
            atoms = atoms.union({atom})
    
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
    for agent in nw_model.keys():
        for i, ass in enumerate(assignments):
            id = agent + "_" + str(i)
            worlds.append(World(id, ass))
    
    def check_kb(w0, w1, kb, agent):
        # Check if all accessible states 
        check = True
        for atom in kb:
            b0 = w0.assignment[atom] != w1.assignment[atom]
            b1 = w1.name[:2] == w0.name[:2] == agent
            check = check and not (b1 and b0) 
            pass
        check2 = (w1.name[:2] == agent)
        return check and check2
    
    
    relations = {}
    for agent, value in nw_model.items():
        relations[agent] = set()
        for w0 in worlds:
            for w1 in worlds:
                if(check_kb(w0, w1, value["kb"], agent)): relations[agent].add((w0.name, w1.name))
    return KripkeStructure(worlds, relations)

def convert_v3(nw_model):
    """ 
    Create a Kripke model where there is a world for every atom, its negation, and agent. 
    This function creates two worlds for every propositional atom and agent, su
    For example, when there agents a and b and propositional atom "p", we get worlds:
    {a_p, a_!p, b_p, b_!p}
    where we consider the subset {a_p, a_!p} the view of agent a of the knowledge in the system.
    """

    # Build a list of all knowledge in the system
    atoms = set()
    for key, value in nw_model.items():
        for atom in value["kb"]:
            atoms = atoms.union({atom})
    
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
    
    # Create a set of all possible value assignment combinations
    assignments = rec_assignments(atoms)

    worlds = []
    for agent in nw_model.keys():
        for i, ass in enumerate(assignments):
            id = agent + "_" + str(i)
            worlds.append(World(id, ass))
    
    def check_kb(w0, w1, kb, agent):
        # Check if a relation from w0 to w1 can be made for this agent. 
        check = True
        for atom in kb:                                 # if agent knows atom,
            b0 = not w1.assignment[atom]                # and atom is false,
            b1 = w1.name[:2] == w0.name[:2] == agent    # and both worlds are in view of agent,
            check = check and not (b1 and b0)           # do not allow relation.
            pass
        check2 = (w1.name[:2] == agent)                 # Only allow relation if it points to a world in agent's view.
        return check and check2
    
    
    relations = {}
    for agent, value in nw_model.items():
        relations[agent] = set()
        for w0 in worlds:
            for w1 in worlds:
                if(check_kb(w0, w1, value["kb"], agent)): relations[agent].add((w0.name, w1.name))
    return KripkeStructure(worlds, relations)

def convert_v4(nw_model):
    """ 
    Create a Kripke model where there is a world for every atom, its negation, and agent. 
    This function creates two worlds for every propositional atom and agent, su
    For example, when there agents a and b and propositional atom "p", we get worlds:
    {a_p, a_!p, b_p, b_!p}
    where we consider the subset {a_p, a_!p} the view of agent a of the knowledge in the system.
    """

    # Build a list of all knowledge in the system
    atoms = set()
    for key, value in nw_model.items():
        for atom in value["kb"]:
            atoms = atoms.union({atom})
    
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
    
    # Create a set of all possible value assignment combinations
    assignments = rec_assignments(atoms)

    worlds = []
    for agent in nw_model.keys():
        for i, ass in enumerate(assignments):
            id = agent + "_" + str(i)
            worlds.append(World(id, ass))
    
    def check_kb(w0, w1, kb, agent):
        # Check if a relation from w0 to w1 can be made for this agent. 
        check = True
        for atom in kb:                                         # if agent knows atom,
            b0 = w0.assignment[atom] != w1.assignment[atom]     # and atom is false,
            b1 = w1.name[:2] == w0.name[:2] == agent            # and both worlds are in view of agent,
            check = check and not (b1 and b0)                   # do not allow relation.
            pass
        check2 = (w1.name[:2] == agent)                 # Only allow relation if it points to a world in agent's view.
        return check and check2
    
    
    relations = {}
    for agent, value in nw_model.items():
        relations[agent] = set()
        for w0 in worlds:
            for w1 in worlds:
                if(check_kb(w0, w1, value["kb"], agent)): relations[agent].add((w0.name, w1.name))
    return KripkeStructure(worlds, relations)

def gc(agent, nw_model):
    """
    Return a set of all agents connected to agent in the network model, including agent.
    """
    return {agent, *nw_model["networks"][agent]["neighbours"]}

# test
if __name__ == "__main__":
    with open(DIR_NW_MODELS + "simple" + ".json", 'r') as json_file:
        model = json.load(json_file)
    kripkemodel = convert(model["networks"])
    pass
    