from dataclasses import dataclass, field

from bigraph_schema import allocate_core
from bigraph_schema.schema import Node, String, Float, Integer, Boolean
from bigraph_schema.methods import apply

@dataclass(kw_only=True)
class Gene(Node):
    transcript: String = field(default_factory=String)
    rate: Float = field(default_factory=Float)
    length: Integer = field(default_factory=Integer)

@dataclass(kw_only=True)
class RNAP(Node):
    free: Boolean = field(default_factory=Boolean)
    gene: String = field(default_factory=String)
    position: Integer = field(default_factory=Integer)

def rnap_update(schema, current, update, path):
    return update

@apply.dispatch
def apply(schema: RNAP, current, update, path):
    return rnap_update(schema, current, update, path), []

@dataclass(kw_only=True)
class RNAPList(Node):
    _schema_keys = Node._schema_keys | frozenset({'_element'})
    _element: RNAP = field(default_factory=RNAP)

@apply.dispatch
def apply(schema: RNAPList, current, update, path):
    return update

def register_types(core):
    core.register_type("rnap", RNAP)
    core.register_type("rnap_list", RNAPList)
    core.register_type("gene", Gene)
    return core