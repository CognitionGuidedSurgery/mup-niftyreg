from msml.sorts import *

sorts_definition = default_sorts_definition()

@sorts_definition.register_physical
class NII(InFile):
    pass



register_conversion(str, NII, NII, 100)