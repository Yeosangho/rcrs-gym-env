# -*- coding: utf-8 -*-
"""
change_set.py
v1.0 - 19/March/2018
Kevin Rodriguez Siu

This module mimics the function of the rescuecore2.worldmodel.ChangeSet class

"""

import encoding_tool as et
from world_model import Entity,EntityID

class ChangeSet:
    changes = None
    deleted = None
    entityURNs = None
    
    def __init__(self,other=None):
        if not (other is None):
            self.__init__()
            self.merge(other)
        else:
             self.changes = {} #Map <EntityID, Map <String, Property > >
             self.deleted = [] #Set <EntityID>
             self.entityURNs = {} #Map <EntityID, String>
        pass
             
    def addChange(self, *args):
        if len(args)==2:
            ent,prop = args
            self.addChange(ent.getID(), ent.getURN(), prop)
            pass
        elif len(args)==3:
            ent_id, ent_urn, prop = args
            if ent_id in self.deleted:
                return
            propy = prop.copy()
            
            if not self.changes.has_key(ent_id):
                self.changes[ent_id] = {}
            
            temp_hash = self.changes[ent_id] 
            temp_hash[propy.getURN] = propy
            self.changes[ent_id] = temp_hash
            self.entityURNs[ent_id] = ent_urn
        return
    
    def entityDeleted(self, ent_id):
        self.deleted.append(ent_id)
        self.changes.pop(ent_id,None)  
        
    def getChangedProperties(self, ent_id):
        if self.changes.has_key(ent_id):
            return self.changes[ent_id].values()
        return []
    
    def getChangedProperty(self, ent_id, urn):
        props = self.changes.get(ent_id)
        if not (props is None):
            return props.get(urn)
        return None
    
    def getChangedEntities(self):
        return self.changes.keys()
    
    def getDeletedEntities(self):
        return self.deleted
    
    def getEntityURN(self, ent_id):
        return self.entityURNs.get(ent_id)
    
    def merge(self, other):
        if other.isinstance(ChangeSet):
            o_changes = other.changes
            o_deleted = other.deleted
            for k,v in o_changes.iteritems():
                e_id = k
                urn = other.getEntityURN(e_id)
                for p in v.values():
                    self.addChange(e_id,urn,p)   
            for e in o_deleted:
                if e not in self.deleted:
                    self.deleted.append(e)
            
        return
    
    def addAll(self, c):
        for elem in c:
            if elem.isinstance(Entity):
                for p in elem.getProperties():
                    if p.isDefined():
                        self.addChange(elem,p)
        return
    
    def write(self, output_stream):
        et.write_int32(len(self.changes), output_stream)
        for k,v in self.changes.iteritems():
            e_id = k
            props = v
            et.write_int32(e_id.getValue(),output_stream)
            et.write_str(self.getEntityURN(e_id),output_stream)
            et.write_int32(len(props),output_stream)
            for p in props:
                et.write_property(p,output_stream)
            et.write_int32(len(self.deleted),output_stream)
            for e_id in self.deleted:
                et.write_int32(e_id.getValue(),output_stream)
        return
    
    def read(self, input_stream):
        self.changes.clear()
        self.deleted.clear()
        
        entityCount = et.read_int32(input_stream)
        for i in range(entityCount):
            e_id = EntityID(et.read_int32(input_stream))
            urn = et.read_str(input_stream)
            propCount = et.read_str(input_stream)
            for j in range(propCount):
                p = et.read_property(input_stream)
                if not (p is None):
                    self.addChange(e_id,urn,p)
        deletedCount = et.read_int32(input_stream)
        for i in range(deletedCount):
            e_id = EntityID(et.read_int32(input_stream))
            self.deleted.append(e_id)
        return
    
    def toString(self):
        result = ""
        result += "ChangeSet:"
        #TO-DO: Complete toString features
        return result 
    
    def debug(self):
        result = ""
        #TO-DO: Complete Debug features
        return result
        
            
        
        
                
            
    
    
            
    
    
        
    