#!/usr/bin/env python
# coding: utf-8

# In[2]:


from stix2 import Campaign, AttackPattern, Relationship
from random_word import RandomWords
import random

objects = []

n_camp = int(input("How many campaign objects would you like to create? "))
n_pat = int(input("How many attack pattern objects would you like to create? "))

for i in range(n_camp):
    
    objectType = "campaign"
    labels = "operation", "strategy", "course of action"
    name = "Operation" + RandomWords().get_random_word() + " " + objectType
    description = "An adversary is attacking a company through cyber breaches" + objectType

    campaign = Campaign(type = objectType, labels=labels, name=name, description=description)
    
    objects.append(campaign)
    
    print(campaign.serialize(pretty=True))
    
    
    for i in range(n_pat):

        attack_patterns=('virus', 'worm', 'Trojan', 'ransomware', 'spyware', 'adware', 'phishing', 'DoS', 'DDoS', 'SQL Injection', 'MitM', 'XSS', 'Password Attack', 'APT')

        objectType = "attack-pattern"
        labels = "approach", "attack"
        name = random.choice(attack_patterns)+ " " + objectType

        pattern = AttackPattern(type = objectType, labels=labels, name=name)
        objects.append(pattern)
        
        #Create Corresponding Campaign attack pattern relationship
        relationship = Relationship(relationship_type='uses',
                            source_ref=campaign.id,
                            target_ref=pattern.id)
        objects.append(relationship)

        print(pattern.serialize(pretty=True))



# In[5]:


from stix2 import Campaign, AttackPattern, ThreatActor, Malware, KillChainPhase, Relationship, Bundle
from random_word import RandomWords
import random

objects = []

n_camp = int(input("How many campaign objects would you like to create? "))
n_pat = int(input("How many attack pattern objects would you like to create? "))
n_mal = int(input("How many malware objects would you like to create per threat actor? "))

for i in range(n_camp):
    
    objectType = "campaign"
    labels = "operation", "strategy", "course of action"
    name = "Operation" + RandomWords().get_random_word() + " " + objectType
    description = "An adversary is attacking a company through cyber breaches" + objectType

    campaign = Campaign(type = objectType, labels=labels, name=name, description=description)
    
    objects.append(campaign)
    
    print(campaign.serialize(pretty=True))
    
    
    for i in range(n_pat):

        attack_patterns=('virus', 'worm', 'Trojan', 'ransomware', 'spyware', 'adware', 'phishing', 'DoS', 'DDoS', 'SQL Injection', 'MitM', 'XSS', 'Password Attack', 'APT')

        objectType = "attack-pattern"
        labels = "approach", "attack"
        name = random.choice(attack_patterns)+ " " + objectType

        pattern = AttackPattern(type = objectType, labels=labels, name=name)
        objects.append(pattern)
        
        #Create Corresponding Campaign attack pattern relationship
        relationship = Relationship(relationship_type='uses',
                            source_ref=campaign.id,
                            target_ref=pattern.id)
        objects.append(relationship)

        print(pattern.serialize(pretty=True))

     # Create a Threat Actor object
    objectType = "threat-actor"
    labels = "adversary", "attacker", "enemy"
    name = RandomWords().get_random_word() + " " + objectType

    actor = ThreatActor(type = objectType, labels=labels, name=name)
    
    objects.append(actor)
    
    #Create Corresponding campaign and threat actor relationship
    relationship2 = Relationship(relationship_type='attributed-to',
                                source_ref=actor.id,
                                target_ref=campaign.id)
    objects.append(relationship2)
    
    for i in range(n_mal):
    
            # Create a Kill Chain Phase object
        kill_chain_phase = KillChainPhase(kill_chain_name="lockheed-martin-cyber-kill-chain", phase_name="delivery")


        malware_types=('.EXE', '.PIF', '.APPLICATION', '.GADGET', '.MSI' , '.MSP', '.COM' , '.SCR', '.HTA', '.CPL', '.MSC', '.JAR', '.BAT', '.CMD', '.VB', '.VBS', '.VBE', '.JS', '.JSE', '.WS', '.WSF', '.WSC', '.WSH', '.PS1', '.PS1XML', '.PS2', '.PS2XML', '.PSC1', '.PSC2' , '.MSH', '.MSH1', '.MSH2', '.MSHXML', '.MSH1XML', '.MSH2XML' , '.SCF', '.LNK' , '.INF', '.SCF' , '.LNK', '.INF', '.REG' , '.DOC', '.XLS', '.PPT', '.DOCM', '.DOTM', '.XLSM', '.XLTM', '.XLAM', '.PPTM', '.POTM', '.PPAM', '.PPSM', '.SLDM')

             # Create a Malware object
        objectType = "malware"
        labels = "exploit", "rouge software"
        name = random.choice(malware_types)+ " " + objectType

        malware = Malware(type = objectType, labels=labels, name=name,is_family=False)

        objects.append(malware)

        #Create Corresponding actor and malware relationship
        relationship = Relationship(relationship_type='uses',
                                source_ref=actor.id,
                                target_ref=malware.id)
        objects.append(relationship)


bundle = Bundle(objects=objects)
    
print(bundle.serialize(pretty=True))




# In[12]:


from stix2 import Campaign, AttackPattern, ThreatActor, Malware, KillChainPhase, Relationship, Location, Identity, Bundle
from random_word import RandomWords
import random

objects = []

n_camp = int(input("How many campaign objects would you like to create? "))
n_pat = int(input("How many attack pattern objects would you like to create? "))
n_mal = int(input("How many malware objects would you like to create per threat actor? "))

for i in range(n_camp):
    
    objectType = "campaign"
    labels = "operation", "strategy", "course of action"
    name = "Operation" + RandomWords().get_random_word() + " " + objectType
    description = "An adversary is attacking a company through cyber breaches" + objectType

    campaign = Campaign(type = objectType, labels=labels, name=name, description=description)
    
    objects.append(campaign)
    
    print(campaign.serialize(pretty=True))
    
    #Create Location for campaign object 
    
    locations=("Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")

    objectType = "location"
    labels = "area", "locale"
    name = random.choice(locations)+ " " + objectType

    locationCam = Location(name=name, latitude=00.0000, longitude=00.0000)
    objects.append(locationCam)
    
    #Create Corresponding location and campaign relationship
    relationship3 = Relationship(relationship_type='originates-from',
                                source_ref=campaign.id,
                                target_ref=locationCam.id)
    objects.append(relationship3)
    
    for i in range(2):
        #Create identities along with campaign 
        identities=("Alia Townsend", "Alexis Paul", "Daphne Li", "Jorge Hart", "Gemma Holloway", "Sutton Berg", "Emmalyn Hood", "Brixton Jones", "Sophia Hammond", "Francis Wallace", "Arianna Case", "Bentlee Bautista", "Antonella Contreras", "Emilio Schneider", "Delaney Duncan", "Avery Collier", "Ivory Munoz", "Justin Mueller", "Imani Carrillo", "Wade Nava")

        objectType = "identity"
        labels = "victim", "injured party"
        name = random.choice(identities)+ " " + objectType

        identity = Identity(type = objectType, labels=labels, name=name)
    
        objects.append(identity)


        #Create Corresponding identity and campaign relationship
        relationship4 = Relationship(relationship_type='targets',
                                    source_ref=campaign.id,
                                    target_ref=identity.id)
        objects.append(relationship4)
        
        #Create Location for identity object 
    
        locations=("Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")

        objectType = "location"
        labels = "area", "locale"
        name = random.choice(locations)+ " " + objectType

        locationId = Location(name=name, latitude=00.0000, longitude=00.0000)
        objects.append(locationCam)

        #Create Corresponding location and identity relationship
        relationship5 = Relationship(relationship_type='located-at',
                                    source_ref=identity.id,
                                    target_ref=locationId.id)
        objects.append(relationship5)
    
    
    for i in range(n_pat):

        attack_patterns=('virus', 'worm', 'Trojan', 'ransomware', 'spyware', 'adware', 'phishing', 'DoS', 'DDoS', 'SQL Injection', 'MitM', 'XSS', 'Password Attack', 'APT')

        objectType = "attack-pattern"
        labels = "approach", "attack"
        name = random.choice(attack_patterns)+ " " + objectType

        pattern = AttackPattern(type = objectType, labels=labels, name=name)
        objects.append(pattern)
        
        #Create Corresponding Campaign attack pattern relationship
        relationship = Relationship(relationship_type='uses',
                            source_ref=campaign.id,
                            target_ref=pattern.id)
        objects.append(relationship)

        print(pattern.serialize(pretty=True))

     # Create a Threat Actor object
    objectType = "threat-actor"
    labels = "adversary", "attacker", "enemy"
    name = RandomWords().get_random_word() + " " + objectType

    actor = ThreatActor(type = objectType, labels=labels, name=name)
    
    objects.append(actor)
    
    #Create Corresponding campaign and threat actor relationship
    relationship2 = Relationship(relationship_type='attributed-to',
                                source_ref=actor.id,
                                target_ref=campaign.id)
    objects.append(relationship2)
    
    for i in range(n_mal):
    
            # Create a Kill Chain Phase object
        kill_chain_phase = KillChainPhase(kill_chain_name="lockheed-martin-cyber-kill-chain", phase_name="delivery")


        malware_types=('.EXE', '.PIF', '.APPLICATION', '.GADGET', '.MSI' , '.MSP', '.COM' , '.SCR', '.HTA', '.CPL', '.MSC', '.JAR', '.BAT', '.CMD', '.VB', '.VBS', '.VBE', '.JS', '.JSE', '.WS', '.WSF', '.WSC', '.WSH', '.PS1', '.PS1XML', '.PS2', '.PS2XML', '.PSC1', '.PSC2' , '.MSH', '.MSH1', '.MSH2', '.MSHXML', '.MSH1XML', '.MSH2XML' , '.SCF', '.LNK' , '.INF', '.SCF' , '.LNK', '.INF', '.REG' , '.DOC', '.XLS', '.PPT', '.DOCM', '.DOTM', '.XLSM', '.XLTM', '.XLAM', '.PPTM', '.POTM', '.PPAM', '.PPSM', '.SLDM')

             # Create a Malware object
        objectType = "malware"
        labels = "exploit", "rouge software"
        name = random.choice(malware_types)+ " " + objectType

        malware = Malware(type = objectType, labels=labels, name=name,is_family=False)

        objects.append(malware)

        #Create Corresponding actor and malware relationship
        relationship = Relationship(relationship_type='uses',
                                source_ref=actor.id,
                                target_ref=malware.id)
        objects.append(relationship)


bundle = Bundle(objects=objects)
    
print(bundle.serialize(pretty=True))



# In[2]:


from stix2 import Campaign, AttackPattern, ThreatActor, Malware, KillChainPhase, Relationship, Location, IntrusionSet, Identity, Bundle
from random_word import RandomWords
import random

objects = []

n_camp = int(input("How many campaign objects would you like to create? "))
n_pat = int(input("How many attack pattern objects would you like to create? "))
n_mal = int(input("How many malware objects would you like to create per threat actor? "))

objectType = "intrusion-set"
labels = "crusade"
name = RandomWords().get_random_word() + " " + objectType


intrusion = IntrusionSet(type = objectType, labels=labels, name=name)
    
objects.append(intrusion)


for i in range(n_camp):
    
    objectType = "campaign"
    labels = "operation", "strategy", "course of action"
    name = "Operation" + RandomWords().get_random_word() + " " + objectType
    description = "An adversary is attacking a company through cyber breaches" + objectType

    campaign = Campaign(type = objectType, labels=labels, name=name, description=description)
    
    objects.append(campaign)
    
   #Create Corresponding campaign and intrusion relationship
    relationship8 = Relationship(relationship_type='attributed-to',
                                source_ref=intrusion.id,
                                target_ref=campaign.id)
    objects.append(relationship8)

    


    
    #Create Location for campaign object 
    
    locations=("Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")

    objectType = "location"
    labels = "area", "locale"
    name = random.choice(locations)+ " " + objectType

    locationCam = Location(name=name, latitude=00.0000, longitude=00.0000)
    objects.append(locationCam)
    
    #Create Corresponding location and campaign relationship
    relationship3 = Relationship(relationship_type='originates-from',
                                source_ref=campaign.id,
                                target_ref=locationCam.id)
    objects.append(relationship3)
    
    for i in range(2):
        #Create identities along with campaign 
        identities=("Alia Townsend", "Alexis Paul", "Daphne Li", "Jorge Hart", "Gemma Holloway", "Sutton Berg", "Emmalyn Hood", "Brixton Jones", "Sophia Hammond", "Francis Wallace", "Arianna Case", "Bentlee Bautista", "Antonella Contreras", "Emilio Schneider", "Delaney Duncan", "Avery Collier", "Ivory Munoz", "Justin Mueller", "Imani Carrillo", "Wade Nava")

        objectType = "identity"
        labels = "victim", "injured party"
        name = random.choice(identities)+ " " + objectType

        identity = Identity(type = objectType, labels=labels, name=name)
    
        objects.append(identity)


        #Create Corresponding identity and campaign relationship
        relationship4 = Relationship(relationship_type='targets',
                                    source_ref=campaign.id,
                                    target_ref=identity.id)
        objects.append(relationship4)
        
        #Create Location for identity object 
    
        locations=("Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")

        objectType = "location"
        labels = "area", "locale"
        name = random.choice(locations)+ " " + objectType

        locationId = Location(name=name, latitude=00.0000, longitude=00.0000)
        objects.append(locationCam)

        #Create Corresponding location and identity relationship
        relationship5 = Relationship(relationship_type='located-at',
                                    source_ref=identity.id,
                                    target_ref=locationId.id)
        objects.append(relationship5)
    
    
    for i in range(n_pat):

        attack_patterns=('virus', 'worm', 'Trojan', 'ransomware', 'spyware', 'adware', 'phishing', 'DoS', 'DDoS', 'SQL Injection', 'MitM', 'XSS', 'Password Attack', 'APT')

        objectType = "attack-pattern"
        labels = "approach", "attack"
        name = random.choice(attack_patterns)+ " " + objectType

        pattern = AttackPattern(type = objectType, labels=labels, name=name)
        objects.append(pattern)
        
        #Create Corresponding Campaign attack pattern relationship
        relationship = Relationship(relationship_type='uses',
                            source_ref=campaign.id,
                            target_ref=pattern.id)
        objects.append(relationship)

     # Create a Threat Actor object
    objectType = "threat-actor"
    labels = "adversary", "attacker", "enemy"
    name = RandomWords().get_random_word() + " " + objectType

    actor = ThreatActor(type = objectType, labels=labels, name=name)
    
    objects.append(actor)
    
    #Create Corresponding campaign and threat actor relationship
    relationship2 = Relationship(relationship_type='attributed-to',
                                source_ref=actor.id,
                                target_ref=campaign.id)
    objects.append(relationship2)
    
    for i in range(n_mal):
    
            # Create a Kill Chain Phase object
        kill_chain_phase = KillChainPhase(kill_chain_name="lockheed-martin-cyber-kill-chain", phase_name="delivery")


        malware_types=('.EXE', '.PIF', '.APPLICATION', '.GADGET', '.MSI' , '.MSP', '.COM' , '.SCR', '.HTA', '.CPL', '.MSC', '.JAR', '.BAT', '.CMD', '.VB', '.VBS', '.VBE', '.JS', '.JSE', '.WS', '.WSF', '.WSC', '.WSH', '.PS1', '.PS1XML', '.PS2', '.PS2XML', '.PSC1', '.PSC2' , '.MSH', '.MSH1', '.MSH2', '.MSHXML', '.MSH1XML', '.MSH2XML' , '.SCF', '.LNK' , '.INF', '.SCF' , '.LNK', '.INF', '.REG' , '.DOC', '.XLS', '.PPT', '.DOCM', '.DOTM', '.XLSM', '.XLTM', '.XLAM', '.PPTM', '.POTM', '.PPAM', '.PPSM', '.SLDM')

             # Create a Malware object
        objectType = "malware"
        labels = "exploit", "rouge software"
        name = random.choice(malware_types)+ " " + objectType

        malware = Malware(type = objectType, labels=labels, name=name,is_family=False)

        objects.append(malware)

        #Create Corresponding actor and malware relationship
        relationship = Relationship(relationship_type='uses',
                                source_ref=actor.id,
                                target_ref=malware.id)
        objects.append(relationship)

#Create Corresponding campaign and intrusion relationship
relationship7 = Relationship(relationship_type='attributed-to',
                                source_ref=intrusion.id,
                                target_ref=campaign.id)
objects.append(relationship7)

    

bundle = Bundle(objects=objects)
    
print(bundle.serialize(pretty=True))



# In[ ]:




