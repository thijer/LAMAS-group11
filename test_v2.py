from formula_extended import *
from mlsolver.formula import *
from mlsolver.kripke import KripkeStructure, World
from converter import convert, gc, convert_v3 as convert
from param import *
import json

if __name__ == "__main__":
    with open(DIR_NW_MODELS + "simple_3a" + ".json", 'r') as json_file:
        model = json.load(json_file)
    kripkemodel = convert(model["networks"])
    world = "03_0"

    # At first, 03 does not know "p".
    print(Not(Knows("03", Atom("p"))).semantic(kripkemodel, world))

    # At first, not everyone knows "p".
    print(Not(E(Atom("p"))).semantic(kripkemodel, world))

    # After PA(2,3), everyone knows "p"
    print(PrA2({"02", "03"}, Atom("p"), E(Atom("p"))).semantic(kripkemodel, world))

    # After PA(2,3), 3 does not know that 1 knows "p"
    print(PrA2({"02", "03"}, Atom("p"), Not(Knows("03", Knows("01", Atom("p"))))).semantic(kripkemodel, world))
    
    # After PA(2,3), Everyone knows "p" but "p" is not common knowledge
    print(PrA2({"02", "03"}, Atom("p"), And(E(Atom("p")), Not(C(Atom("p"))))).semantic(kripkemodel, world))
    
    # After PA(1,2,3), Everyone knows "p" and "p" is common knowledge
    print(PrA2({"01", "02", "03"}, Atom("p"), And(E(Atom("p")), C(Atom("p")))).semantic(kripkemodel, world))
    
