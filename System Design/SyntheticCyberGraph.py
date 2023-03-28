#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install stix2


# In[56]:


from stix2 import Malware, KillChainPhase
import random

# Create a Kill Chain Phase object
kill_chain_phase = KillChainPhase(kill_chain_name="lockheed-martin-cyber-kill-chain", phase_name="delivery")


malware_types=('ZBOT','EXE','PDF')

objectType = "malware"
labels = "exploit", "rouge software"
name = random.choice(malware_types)+ " " + objectType

malware = Malware(type = objectType, labels=labels, name=name,is_family=False)

print(malware.serialize(pretty=True))


# In[59]:


from stix2 import ThreatActor
import random

threat_actors=('1277 Vortex','0091 Rico','Batty Boyz')

objectType = "threat-actor"
labels = "adversary", "attacker", "enemy"
name = random.choice(threat_actors)+ " " + objectType

actor = ThreatActor(type = objectType, labels=labels, name=name)

print(actor.serialize(pretty=True))


# In[42]:


from stix2 import AttackPattern
import random

attack_patterns=('Phishing','Pharming','DOS')

objectType = "attack-pattern"
labels = "approach", "attack"
name = random.choice(attack_patterns)+ " " + objectType

pattern = AttackPattern(type = objectType, labels=labels, name=name)

print(pattern.serialize(pretty=True))


# In[20]:


from stix2 import Identity 
import random

identities=('East Napole College','Chroning Parking and Transportation','Channing State University')

objectType = "identity"
labels = "victim", "injured party"
name = random.choice(identities)+ " " + objectType

identity = Identity(type = objectType, labels=labels, name=name)

print(identity.serialize(pretty=True))


# In[27]:


from stix2 import Campaign 
import random

campaigns=('Operation Great Escape','Operation Rock Parrot','Operation RedBack')
descriptions=('Denial of service attack to block users from a network.','A pharming campaign meant for a client to unknowingly download malicious spyware','A phishing campaign meant to impersonate a payment service.')


objectType = "campaign"
labels = "operation", "strategy", "course of action"
name = random.choice(campaigns)+ " " + objectType
description = random.choice(descriptions)+ " " + objectType

campaign = Campaign(type = objectType, labels=labels, name=name, description=description)

print(campaign.serialize(pretty=True))


# In[45]:


from stix2 import Relationship

relationship = Relationship(relationship_type='uses',
                            source_ref=actor.id,
                            target_ref=malware.id)
print(relationship.serialize(pretty=True))


# In[46]:


from stix2 import Relationship

relationship2 = Relationship(relationship_type='targets',
                            source_ref=actor.id,
                            target_ref=identity.id)
print(relationship.serialize(pretty=True))


# In[47]:


from stix2 import Relationship

relationship3  = Relationship(relationship_type='attributed-to',
                            source_ref=campaign.id,
                            target_ref=actor.id)
print(relationship.serialize(pretty=True))


# In[48]:


from stix2 import Relationship

relationship4 = Relationship(relationship_type='uses',
                            source_ref=campaign.id,
                            target_ref=pattern.id)
print(relationship.serialize(pretty=True))


# In[49]:


from stix2 import Location

locationTar = Location(name="Adelaide, South Australia", latitude=34.9285, longitude=138.6007)
print(locationTar.serialize(pretty=True))


# In[50]:


from stix2 import Location

locationAct = Location(name="San Juan, Puerto Rico", latitude=18.4671, longitude=66.1185)
print(locationTar.serialize(pretty=True))


# In[51]:


from stix2 import Relationship

relationship5 = Relationship(relationship_type='located-at',
                            source_ref=identity.id,
                            target_ref=locationTar.id)
print(relationship.serialize(pretty=True))


# In[52]:


from stix2 import Relationship

relationship6 = Relationship(relationship_type='originates-from',
                            source_ref=campaign.id,
                            target_ref=locationAct.id)
print(relationship.serialize(pretty=True))


# In[60]:


from stix2 import Bundle

bundle = Bundle(malware, actor, pattern, identity, campaign, locationTar, locationAct, relationship, relationship2, relationship3, relationship4, relationship5, relationship6)
print(bundle.serialize(pretty=True))


# In[ ]:




