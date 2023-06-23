from formula_extended import PrivateAnnouncement, CommonKnowledge
from mlsolver.formula import *
from mlsolver.kripke import KripkeStructure, World
from mlsolver.tableau import ProofTree
from converter import convert
from param import *
import json

if __name__ == "__main__":
    with open(DIR_NW_MODELS + "simple" + ".json", "r") as json_file:
        model = json.load(json_file)
    kripkemodel = convert(model["networks"])
    print(kripkemodel)

    # formula = PrivateAnnouncement({"01", "02"}, Atom("p"), Box_a("02", Atom("p")))
    formula = PrivateAnnouncement({"01", "02"}, Atom("p"), CommonKnowledge(Atom("p")))

    world = "3"
    test = formula.semantic(kripkemodel, world)

    # model = kripkemodel.solve(f)

    print(test)

    pt = ProofTree(formula)
    pt.derive()

    print(pt)
