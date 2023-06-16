from formula_extended import PrivateAnnouncement
from mlsolver.formula import *
from mlsolver.kripke import KripkeStructure, World
from converter import convert
from param import *
import json

if __name__ == "__main__":
    with open(DIR_NW_MODELS + "simple" + ".json", 'r') as json_file:
        model = json.load(json_file)
    kripkemodel = convert(model["networks"])

    formula = PrivateAnnouncement({"01", "02"}, Atom("p"), Box_a("02", Atom("p")))
    world = "0"
    test = formula.semantic(kripkemodel, world)
    pass