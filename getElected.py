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
    def __init__(self, name, party, gender, race, experience = False):
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
        return self.name + ' (' + self.party + ')'
    def __repr__(self):
        return str(self)
    def positions(self):
        correct = False
        while correct == False:
            guns = input("Do you support a greater degree of gun control? (Y/N) ")
            correct = True
            regex = r'^(([Yy](es)?)|([Nn](o)?))$'
            seeker = re.compile(regex)
            if seeker.search(guns) == None: correct = False
            elif 'y' in guns or 'Y' in guns: self.gunControl = True
            elif 'n' in guns or 'N' in guns: self.gunControl = False
        correct = False
        while correct == False:
            abort = input("Do you believe that abortion should be legal in most to all cases? (Y/N) ")
            correct = True
            regex = r'^(([Yy](es)?)|([Nn](o)?))$'
            seeker = re.compile(regex)
            if seeker.search(abort) == None: correct = False
            elif 'y' in abort or 'Y' in abort: self.proChoice = True
            elif 'n' in abort or 'N' in abort: self.proChoice = False
        correct = False
        while correct == False:
            gay = input("Do you believe that LGBT people should be protected from discrimination based on their sexual orientation or gender identity? (Y/N) ")
            correct = True
            regex = r'^(([Yy](es)?)|([Nn](o)?))$'
            seeker = re.compile(regex)
            if seeker.search(gay) == None: correct = False
            elif 'y' in gay or 'Y' in gay: self.gayRights = True
            elif 'n' in gay or 'N' in gay: self.gayRights = False
        correct = False
        while correct == False:
            tax = input("Do you believe that the top tax bracket and/or corporate taxes should be raised to create a more robust social safety net? (Y/N) ")
            correct = True
            regex = r'^(([Yy](es)?)|([Nn](o)?))$'
            seeker = re.compile(regex)
            if seeker.search(tax) == None: correct = False
            elif 'y' in tax or 'Y' in tax: self.taxCuts = False
            elif 'n' in tax or 'N' in tax: self.taxCuts = True
        correct = False
        while correct == False:
            health = input("Do you believe that the government has a responsibility to provide or assist in providing healthcare to the population? (Y/N) ")
            correct = True
            regex = r'^(([Yy](es)?)|([Nn](o)?))$'
            seeker = re.compile(regex)
            if seeker.search(health) == None: correct = False
            elif 'y' in health or 'Y' in health: self.healthCare = True
            elif 'n' in health or 'N' in health: self.healthCare = False
        correct = False
        while correct == False:
            immigration  = input("Should the US make it more difficult for illegal immigrants to enter and stay in the country? (Y/N) ")
            correct = True
            regex = r'^(([Yy](es)?)|([Nn](o)?))$'
            seeker = re.compile(regex)
            if seeker.search(immigration) == None: correct = False
            elif 'y' in immigration or 'Y' in immigration: self.immigration = False
            elif 'n' in immigration or 'N' in immigration: self.immigration = True
        
with open('Procedural_Counties.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    counties = []
    for row in reader:
        counties.append(County(row['name'], int(row['pop']), float(row['pvi']), int(row['whiNum']), int(row['blaNum']), int(row['hispNum'])))

def newCandidate():
    name = None
    correct = False
    while correct == False:
        party = input("Your candidate's party: D or R? ")
        correct = True
        regex = r'^(([Dd]((em)|(emocrat))?)|([Rr]((ep)|(epublican))?))$'
        seeker = re.compile(regex)
        if seeker.search(party) == None: correct = False
        elif 'r' in party or 'R' in party: party = 'R'
        elif 'd' in party or 'D' in party: party = 'D'
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
        elif 'w' in race or 'W' in race: race = 'W'
        elif 'b' in race or 'B' in race: race = 'B'
        elif race == 'h' or 'H' in race or 'p' in race: race = 'H'
        elif 'o' in race or 'O' in race: race = 'O'
    correct = False
    while correct == False:
        experience = input("Prior political experience? (Y/N) ")
        correct = True
        regex = r'^(([Yy](es)?)|([Nn](o)?))$'
        seeker = re.compile(regex)
        if seeker.search(experience) == None: correct = False
        elif 'y' in experience or 'Y' in experience: experience = True
        elif 'n' in experience or 'N' in experience: experience = False
    return Candidate(name,party, gender, race, experience)

def newOpponent():
    opponent = Candidate() 

def election(candidate):
    margin = 0
    pop = 0
    for c in counties:
        if candidate.party == 'R': c.lean = -c.lean
        c.margin = c.lean*c.pop*.01
        if candidate.gender == 'F':
            if candidate.party == 'D': c.margin += 0.10
            elif candidate.party == 'R': c.margin -= 0.05
        c.white = c.white*(.730 if candidate.race == 'W' else .660)
        c.black = c.black*(.626 if candidate.race == 'B' else .566)
        c.hispanic = c.hispanic*(.500 if candidate.race == 'H' else .452)
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
    print('county',' '*13,'margin',' '*2,'margin/electorate')
    for c in counties:
        print((c.name.split()[0] if not(counties[64] == c) else "New Hanover"),' '*((16-len(c.name.split()[0])) if not(counties[64] == c) else (5)),' '*(8-len(str(round(c.margin)))),round(c.margin),' '*(1 if c.margin < 0 else 2),round((c.margin/int(c.pop)),4))
    print("Overall margin: ",' '*(9-len(str(round(margin)))),round(margin),' '*(1 if margin < 0 else 2),round(margin/pop,4))

c = newCandidate()
c.positions()
election(c)
