from encoding_tool import write_int32
from encoding_tool import read_int32
from encoding_tool import write_str
from encoding_tool import read_str
from encoding_tool import write_entity
from encoding_tool import read_entity

from change_set import ChangeSet
from world_model import Entity,EntityID

class IntComp:
    def __init__(self):
        self.value = None

    def set_value(self, _value):
        self.value = _value

    def get_value(self):
        return self.value

    def write(self, output_stream):
        write_int32(self.value, output_stream)

    def read(self, input_stream):
        self.value = read_int32(input_stream)


class StringComp:
    def __init__(self):
        self.value = None

    def set_value(self, _value):
        self.value = _value

    def get_value(self):
        return self.value

    def write(self, output_stream):
        write_str(self.value, output_stream)

    def read(self, input_stream):
        self.value = read_str(input_stream)


class StringListComp:
    def __init__(self):
        self.value_list = None

    def set_value(self, _value_list):
        self.value_list = _value_list

    def get_value(self):
        return self.value_list

    def write(self, output_stream):
        write_int32(len(self.value_list), output_stream)
        for value in self.value_list:
            write_str(value, output_stream)

    def read(self, input_stream):
        self.value_list.clear()
        list_len = read_int32(input_stream)
        for i in range(list_len):
            self.value_list.append(read_str(input_stream))




class ChangeSetComp:
    changes = None
    def __init__(self,n_changes=None):
        if n_changes is None:
            self.changes = ChangeSet()
        else:
            self.changes = ChangeSet(n_changes)
            
    def get_change_set(self):
        return self.changes
    
    def set_change_set(self, newChanges):
        self.changes = ChangeSet(newChanges)
    
    def write(self, output_stream):
        self.changes.write(output_stream)
        
    def read(self, input_stream):
        self.changes = ChangeSet()
        self.changes.read(input_stream)
    #TO-DO: toString method
    
class EntityComp:
    entity = None
    
    def __init__(self,n_entity=None):
        if n_entity.isinstance(Entity):
            self.entity = n_entity
        else:
            self.entity = None
        
    def get_entity(self):
        return self.entity
    
    def set_entity(self, e):
        if e.isinstance(Entity):
            self.entity = e
            
    def write(self, output_string):
        write_entity(self.entity,output_string)
        
    def read(self, input_string):
        self.entity = read_entity(input_string)
        
    #TO-DO: toString method
    
class EntityIDComp:
    value = None
    
    def __init__(self, value=None):
        self.value = value
        
    def get_value(self):
        return self.value
    
    def set_value(self, eid):
        if eid.isinstance(EntityID):
            self.value=eid
        return
    
    def write(self, output_stream):
        write_int32(self.value.getValue(),output_stream)
        
    def read(self,input_stream):
        self.value = EntityID(read_int32(input_stream))
        
    #TO-DO: toString method
    
class EntityIDListComp:
    ids = None
    
    def __init__(self,nids=None):
        if not (nids is None) and nids.instanceof(list):
            self.ids = nids
        else:
            self.ids = []
    
    def get_ids(self):
        return self.ids
    
    def set_ids(self,nids):
        if not (nids is None) and nids.instanceof(list):
            self.ids = nids
        return
    
    def write(self,output_stream):
        write_int32(len(self.ids), output_stream)
        for eid in self.ids:
            write_int32(eid.getValue(),output_stream)
        return
    
    def read(self,input_stream):
        self.ids.clear()
        count = read_int32(input_stream)
        for i in range(count):
            eid = EntityID(read_int32(input_stream))
            self.ids.append(eid)
        return
    
    #TO-DO: toString method
    
class EntityListComp:
    ents = None
    
    def __init__(self,nents=None):
        if not (nents is None) and nents.instanceof(list):
            self.ents = nents
        else:
            self.ents = []
    
    def get_entities(self):
        return self.ents
    
    def set_entities(self,nents):
        if not (nents is None) and nents.instanceof(list):
            self.ents = nents
        return
    
    def write(self,output_stream):
        write_int32(len(self.ents), output_stream)
        for ent in self.ents:
            write_entity(ent.getValue(),output_stream)
        return
    
    def read(self,input_stream):
        self.ents.clear()
        count = read_int32(input_stream)
        for i in range(count):
            e = Entity(read_entity(input_stream))
            self.ents.append(e)
        return
    
    #TO-DO: toString method
        
    
class IntListComp:
    ints = None
    
    def __init__(self,nints=None):
        if not (nints is None) and nints.instanceof(list):
            self.ints = nints
        else:
            self.ints = []
    
    def get_values(self):
        return self.ints
    
    def set_values(self,nints):
        if not (nints is None) and nints.instanceof(list):
            self.ints = nints
        return
    
    def write(self,output_stream):
        write_int32(len(self.ints), output_stream)
        for nt in self.ints:
            write_int32(nt,output_stream)
        return
    
    def read(self,input_stream):
        self.ints.clear()
        count = read_int32(input_stream)
        for i in range(count):
            e = read_int32(input_stream)
            self.ints.append(e)
        return
    
    #TO-DO: toString method
        

        

    

    

        
        