import csv,sys,re

class County:
    def __init__(self, name, pop, lean, white, black, hispanic):
        self.name = name
        self.pop = pop
        self.lean = lean
        self.white = white
        self.black = black
        self.hispanic = hispanic
        self.margin = 0
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)

class Candidate:
    def __init__(self, name, party, gender = 'M', race = 'White', experience = False):
        self.name = name
        self.party = party
        self.gender = gender
        self.race = race
        self.experience = experience
        self.proChoice = None
        self.gayRights = None
        self.taxCuts = None
        self.gunControl = None
        self.healthCare = None
        self.immigration = None
    def __str__(self):
        return self.name + '(' + self.party + ')'
    def __repr__(self):
        return str(self)
    def positions(self):
        guns = input("Do you support a greater degree of gun control? (Y/N) ")
        if guns == 'Y': self.gunControl = True
        elif guns == 'N': self.gunControl = False
        else: return "Incorrect input"
        abort = input("Do you believe that abortion should be legal in most to all cases? (Y/N) ")
        if abort == 'Y': self.proChoice = True
        elif abort == 'N': self.proChoice = False
        else: return "Incorrect input"
        gay = input("Do you believe that LGBT people should be protected from discrimination based on their sexual orientation or gender identity? (Y/N) ")
        if gay == 'Y': self.gayRights = True
        elif gay == 'N': self.gayRights = False
        else: return "Incorrect input"
        tax = input("Do you believe that the top tax bracket and/or corporate taxes should be raised to create a more robust social safety net? (Y/N) ")
        if tax == 'Y': self.taxCuts = False
        elif tax == 'N': self.taxCuts = True
        else: return "Incorrect input"
        health = input("Do you believe that the government has a responsibility to provide or assist in providing healthcare to the population? (Y/N) ")
        if health == 'Y': self.healthCare = True
        elif health == 'N': self.healthCare = False
        else: return "Incorrect input"
        immigration  = input("Should the US make it more difficult for illegal immigrants to enter and stay in the country? (Y/N) ")
        if immigration == 'Y': self.immigration == False
        elif immigration == 'N': self.immigration == True
        else: return "Incorrect input"
        
with open('Procedural_Counties.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    counties = []
    for row in reader:
        counties.append(County(row['name'], int(row['pop']), float(row['pvi']), int(row['whiNum']), int(row['blaNum']), int(row['hispNum'])))

def newCandidate():
    correct = False
    while correct == False:
        party = input("Your candidate's party: D or R? ")
        correct = True
        regex = r'^(([Dd]((em)|(emocrat))?)|([Rr]((ep)|(epublican))?))$'
        seeker = re.compile(regex)
        if seeker.search(party) == None: correct = False
    correct = False
    while correct == False:
        gender = input("Your candidate's gender: M, F, or O? ")
        correct = True
        regex = r'^(([Mm](ale)?)|([Ff](emale)?)|([Oo](ther)?))$'
        seeker = re.compile(regex)
        if seeker.search(gender) == None: correct = False
    correct = False
    while correct == False:
        race = input ("Your candidate's race: White, Black, Hispanic, or Other? ")
        correct = True
        regex = r'^(([Ww](hite)?)|([Bb](lack)?)|([Hh](ispanic)?)|([Oo](ther)?))$'
        seeker = re.compile(regex)
        if seeker.search(race) == None: correct = False
    correct = False
    while correct == False:
        experience = input("Prior political experience? (Y/N) ")
        correct = True
        regex = r'^(([Yy](es)?)|([Nn](o)?))$'
        seeker = re.compile(regex)
        if seeker.search(experience) == None: correct = False
        elif 'y' in experience or 'Y' in experience: experience = True
        elif 'n' in experience or 'N' in experience: experience = False
    return Candidate(party, gender, race, experience)

def newOpponent():
    opponent = Candidate() 

def election(candidate):
    margin = 0
    pop = 0
    for c in counties:
        if candidate.party == 'R': c.lean = -c.lean
        c.margin = c.lean*c.pop*.01
        if candidate.proChoice == True: c.margin += .16*((c.white*((35-35)/70)) + (c.black*((49-13)/62)) + (c.hispanic*((44-24)/68)))
        else: c.margin += .16*((c.white*((35-35)/70)) + (c.black*((13-49)/62)) + (c.hispanic*((24-44)/68)))
        if candidate.gunControl == True: c.margin += .16*((c.white*((40-43)/83)) + (c.black*((60-17)/77)) + (c.hispanic*((43-31)/74)))
        else: c.margin += .16*((c.white*((43-40)/83)) + (c.black*((17-60)/77)) + (c.hispanic*((31-43)/74)))
        if candidate.gayRights == True: c.margin += .16*((c.white*((38-29)/67)) + (c.black*((40-17)/57)) + (c.hispanic*((44-22)/66)))
        else: c.margin += .16*((c.white*((29-38)/67)) + (c.black*((17-40)/57)) + (c.hispanic*((22-44)/66)))
        if candidate.taxCuts == True: c.margin += .16*((c.white*((38-47)/85)) + (c.black*((59-16)/75)) + (c.hispanic*((39-32)/76)))
        else: c.margin += .16*((c.white*((47-38)/85)) + (c.black*((16-59)/75)) + (c.hispanic*((32-39)/76)))
        if candidate.immigration == True: c.margin += .16*((c.white*((40-48)/88)) + (c.black*((50-23)/73)) + (c.hispanic*((48-31)/79)))
        else: c.margin += .16*((c.white*((48-40)/88)) + (c.black*((23-50)/73)) + (c.hispanic*((31-48)/79)))
        if candidate.healthCare == True: c.margin += .16*((c.white*((43-31)/74)) + (c.black*((63-16)/79)) + (c.hispanic*((43-32)/75)))
        else: c.margin += .16*((c.white*((31-43)/74)) + (c.black*((16-63)/79)) + (c.hispanic*((32-43)/75)))
        margin += c.margin
        pop += c.pop
    print('county',' ','margin')
    for c in counties:
        print(c.name.split()[0],' '*(16-len(c.name.split()[0])),round(c.margin),' '*(8-len(str(round(c.margin)))),round((c.margin/int(c.pop)),4))
    print("Overall margin: ",round(margin),' '*(8-len(str(round(margin)))),round(margin/pop,4))

c = newCandidate()
c.positions()
election(c)
