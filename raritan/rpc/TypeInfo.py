#
# Decodes IDL "typecode" to python class and vice versa.
#

import re

# TODO: generate prefix from "base-package" in config
prefix = "raritan.rpc"

class TypeInfo(object):

    @staticmethod
    def typeBaseName(typeId):
        b = typeId.split(":")[0] # remove version
        b = re.sub(r'_[0-9]*_[0-9]*_[0-9]*', r'', b) # remove version
        return b

    @classmethod
    def idlTypeIdToPyClass(cls, typeId):
        """Returns python class for given typeId.

        The module defining this class will be auto-imported.
        """
        pyName = "%s.%s" % (prefix, TypeInfo.typeBaseName(typeId))
        comps = pyName.split(".")
        # remove components from end until import succeeds
        while comps:
            modName = ".".join(comps)
            namespace = {}
            try:
                exec("import %s" % modName, namespace)
            except ImportError:
                comps.pop()
                continue
            exec("cls = %s" % pyName, namespace)
            return namespace['cls']
        raise ImportError("Unable to find package for %s." % typeId)

    @classmethod
    def pyClassToIdlName(cls, pyClass):
        return pyClass.idlType

    @classmethod
    def decode(cls, json):
        typeId = json
        return cls.idlTypeIdToPyClass(typeId)

    @classmethod
    def encode(cls, pyClass):
        return cls.pyClassToIdlName(pyClass)
