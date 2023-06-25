from mlsolver.kripke import KripkeStructure
from mlsolver.formula import Box_a, Atom

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

class PrivateAnnouncement:
    """
    Restrict the relations of the involved agents to the worlds where the announcement holds.
    """
    def __init__(self, agents: set, announcement, inner) -> None:
        self.agents = agents
        self.announcement = announcement
        self.inner = inner
    
    def semantic(self, ks: KripkeStructure, world_to_test):
        # Filter out worlds that are not related to the involved agents
        inv_agents = {w.name for w in ks.worlds if w.name[:2] in self.agents}
        
        # Create list of worlds where announcement does not hold
        ex_worlds = set(ks.nodes_not_follow_formula(self.announcement))
        exes = ex_worlds.intersection(inv_agents)

        # Create subset of relations
        relations = {}
        for agent, rels in ks.relations.items():
            # Evaluate relations if agent is involved in the private announcement.
            if(agent in self.agents):
                relations[agent] = set()
                for relation in rels:
                    # Only include relation if it does not point to a world where the announcement does not hold. 
                    if(not (relation[1] in exes and relation[0] in inv_agents)):
                        relations[agent].add(relation)
            # If not involved, copy original relations
            else:
                relations[agent] = rels
        
        # Create a new Kripke model with the original worlds and restricted relations.
        restricted_model = KripkeStructure(ks.worlds, relations)
        result = self.inner.semantic(restricted_model, world_to_test)
        return result
    
    def __str__(self) -> str:
        # if isinstance(self.inner, Atom):
        return "PrA_{0}[{1}] {2}".format(self.agents, self.announcement, self.inner)
        # else:
        #     return "PrA_{0}[{1}] ({2})".format(self.agents, self.announcement, self.inner)
        return "PrA_{0}[{1}] {2}".format(self.agents, self.announcement, self.inner)

class CommonKnowledge:
    """ Common Knowledge operator, as defined by Meyer and van der Hoek. """
    def __init__(self, inner) -> None:
        self.inner = inner
    
    def semantic(self, ks: KripkeStructure, world_to_test):
        # Create set of all relations
        relations = set()
        for key, value in ks.relations.items():
            relations = relations.union(value)
        
        # Create transitive relations until no more relations can be created.
        unfinished = True
        while(unfinished):
            unfinished = False
            updates = set()
            for rel1 in relations:
                for rel2 in relations:
                    if(rel1[1] == rel2[0] and (rel1[0], rel2[1]) not in relations):
                        updates.add((rel1[0], rel2[1]))
                        unfinished = True
            relations = relations.union(updates)
        
        # Check for all relations
        result = True
        for relation in relations:
            if relation[0] == world_to_test:
                result = result and self.inner.semantic(ks, relation[1])
        return result
    
    def __str__(self) -> str:
        if isinstance(self.inner, Atom):
            return "C" + " " + str(self.inner)
        else:
            return "C" + "(" + str(self.inner) + ")"

class Knows:
    """ Adapted Knowledge operator, which checks if the formula holds for every worlds reachable from this agent's view."""
    def __init__(self, agent, inner):
        self.inner = inner
        self.agent = agent

    def semantic(self, ks: KripkeStructure, world_to_test):
        # Change world to agent viewpoint world
        wtt_suffix = world_to_test[3:]
        wtt = self.agent + "_" + wtt_suffix
        return Box_a(self.agent, self.inner).semantic(ks, wtt)
    
    def __str__(self) -> str:
        op = "K{}".format(self.agent).translate(SUB)
        if isinstance(self.inner, Atom):
            return op + " {}".format(self.inner)
        else:
            return op + " ({})".format(self.inner)

class EveryoneKnows:
    def __init__(self, inner) -> None:
        self.inner = inner
    
    def semantic(self, ks: KripkeStructure, world_to_test):
        result = True
        for agent, value in ks.relations.items():
            result = result and Knows(agent, self.inner).semantic(ks, world_to_test)
        return result
    
    def __str__(self) -> str:
        if isinstance(self.inner, Atom):
            return "E" + " " + str(self.inner)
        else:
            return "E" + "(" + str(self.inner) + ")"

class And:
    def __init__(self, *args):
        self.args = args

    def semantic(self, ks, world_to_test):
        result = True
        for arg in self.args:
            result = result and arg.semantic(ks, world_to_test)
        return result

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __str__(self):
        output = "("
        for arg in self.args:
            output = output + arg.__str__() + " \u2227 "
        return output[:-3] + ")"


# Aliases
class K(Box_a):
    def __str__(self) -> str:
        op = "K{}".format(self.agent).translate(SUB)
        if isinstance(self.inner, Atom):
            return op + " {}".format(self.inner)
        else:
            return op + " ({})".format(self.inner)
    pass

class PrA(PrivateAnnouncement):
    pass

class C(CommonKnowledge):
    pass

class E(EveryoneKnows):
    pass
