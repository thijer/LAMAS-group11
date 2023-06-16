from mlsolver.kripke import KripkeStructure

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
        for agent in self.agents:
            relations[agent] = set()
            for relation in ks.relations[agent]:
                if(relation[1] not in ex_worlds):
                    relations[agent].add(relation)
        
        restricted_model = KripkeStructure(ks.worlds, relations)
        result = self.inner.semantic(restricted_model, world_to_test)
        return result


        