from mlsolver.kripke import KripkeStructure
from mlsolver.formula import Box_a

class PrivateAnnouncement:
    def __init__(self, agents: set, announcement, inner) -> None:
        self.agents = agents
        self.announcement = announcement
        self.inner = inner
    
    def semantic(self, ks: KripkeStructure, world_to_test):
        # Create list of worlds where announcement does not hold
        ex_worlds = ks.nodes_not_follow_formula(self.announcement)

        # Create subset of relations
        relations = {}
        for agent, rels in ks.relations.items():
            if(agent in self.agents):
                relations[agent] = set()
                for relation in rels:
                    if(relation[1] not in ex_worlds):
                        relations[agent].add(relation)
            else:
                relations[agent] = rels
        
        restricted_model = KripkeStructure(ks.worlds, relations)
        result = self.inner.semantic(restricted_model, world_to_test)
        return result

class PrivateAnnouncementV2:
    def __init__(self, agents: set, announcement, inner) -> None:
        self.agents = agents
        self.announcement = announcement
        self.inner = inner
    
    def semantic(self, ks: KripkeStructure, world_to_test):
        # Create list of worlds where announcement does not hold
        ex_worlds = ks.nodes_not_follow_formula(self.announcement)

        # Create subset of relations
        relations = {}
        for agent, rels in ks.relations.items():
            if(agent in self.agents):
                relations[agent] = set()
                for relation in rels:
                    if(relation[1] not in ex_worlds and relation[0] == world_to_test):
                        relations[agent].add(relation)
            else:
                relations[agent] = rels
        
        restricted_model = KripkeStructure(ks.worlds, relations)
        result = self.inner.semantic(restricted_model, world_to_test)
        return result

class CommonKnowledge:
    def __init__(self, inner) -> None:
        self.inner = inner
    
    def semantic(self, ks: KripkeStructure, world_to_test):
        # Create set of all relations
        relations = set()
        for key, value in ks.relations.items():
            relations = relations.union(value)
        
        # Create transitive relations until complete
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

class EveryoneKnows:
    def __init__(self, inner) -> None:
        self.inner = inner
    
    def semantic(self, ks: KripkeStructure, world_to_test):
        wtt_suffix = world_to_test[3:]
        
        # Create set of all relations
        result = True
        for agent, value in ks.relations.items():
            wtt = agent + "_" + wtt_suffix
            result = result and Knows(agent, self.inner).semantic(ks, wtt)
        return result

# Aliases
class Knows(Box_a):
    pass

class PrA(PrivateAnnouncement):
    pass

class PrA2(PrivateAnnouncementV2):
    pass

class C(CommonKnowledge):
    pass

class E(EveryoneKnows):
    pass
