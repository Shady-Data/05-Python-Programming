from random import randint

class mad_libs:

    def __init__(self):
        '''
        Default attributes for class:
            Dictionary nouns: wordbank for noun choices
            Dictionary verbs: wordbank for verb choices
            Dictionary adjectives: wordbank for adjectives choices
            Dictionary user_selection: contains user choices input
            Dictionary cardbank: contains random selections from the wordbanks (player hand)
            
        * WIP detach large dictionaries from code (CSV or json files)
            - add load calls for the csv/json files
        * Add phrasebank for prompts for the game
        * Modify user_selection/cardbank calls to be in line with prompts, (i.e. >4 nouns in a prompt)
        '''
        self.nouns = {1: 'FACTORY RESET BUTTON', 2: 'BLOOD RAGE', 3: 'IDIOT', 4: 'TOASTER', 5: 'LEGEND', 6: 'DEATH WISH', 7: 'THERAPY', 8: 'GOAL IN LIFE', 9: 'MARKETING IDEA', 10: 'PSYCHIC', 11: 'KNIFE', 12: 'SANDWICH', 13: 'HUNTING GROUND', 14: 'LETTUCE', 15: 'KITTY', 16: 'FRIENDLY GRANDMA', 17: 'FRENCH CHEF', 18: 'ANTI-DEPRESSANT DRUG', 19: 'CORN CAKE', 20: 'PRESIDENT OF THE NIGHT', 21: 'CANDLESTICK MAKER', 22: 'COFFEE POT', 23: 'BRETHREN', 24: 'NATIONAL SECURITY AGENCY', 25: 'TANK', 26: 'USELESS BRAKES', 27: 'INTERNATIONAL LAW ENFORCEMENT AGENCY', 28: 'SOUND BARRIER', 29: 'SKINNY WOMAN', 30: 'PRIVATE INVESTOR', 31: 'MAIN PEOPLE', 32: 'STOCK CAR', 33: 'ELASTIC BAND', 34: 'WHOLE BLOOD', 35: 'TELEPHONE', 36: 'MAD COW DISEASE', 37: 'SCOURGE UPON THE EARTH', 38: 'ROUGH-SKINNED NEWT', 39: 'KARATE', 40: 'PISTOL', 41: 'LEGAL WARRANT', 42: 'PEOPLE WHO ARE HURT', 43: 'IDEA HE SUGGESTED', 44: 'PARTY OF THE FIRST PART', 45: 'DLACE OF BUSINESS', 46: 'DOUBLE FAULT', 47: 'KITTY CAT', 48: 'FAMOUS LANDSCAPE PAINTING', 49: 'HAIRY LEGS', 50: 'OLD IRISH COTTAGE', 51: 'POCKET FLASK', 52: 'LIQUID OXYGEN', 53: 'LASER BEAMS', 54: 'PREVENTIVE STRIKE', 55: 'DINGLE BERRY', 56: 'READING PARTY', 57: 'GENERALIZED BOND', 58: 'INDIRECT EXPRESSION', 59: 'MESSINESS', 60: 'LOVE OF HER LIFE', 61: 'TRUST FUND', 62: 'VOLCANIC CRATER', 63: 'TRAVEL GUIDEBOOK', 64: 'ELECTRIC FURNACE', 65: 'INTERNAL RESPIRATION', 66: 'POLICE SQUAD', 67: 'MAD-DOG SKULLCAP', 68: 'SNEAKY CRIMINAL', 69: 'NEW VERSION', 70: 'KEEPSAKE MACHETE', 71: 'GAMING LAPTOP', 72: 'HISSY FIT', 73: 'DOG POOP', 74: 'DRAGON', 75: 'MEDIATION', 76: 'PATROLMAN', 77: 'PERVERT', 78: 'TOILET SEAT', 79: 'HAUNTED GRAVEYARD', 80: 'REALLY TOUGH GUY', 81: 'TWINKLING UNCLEANNESS', 82: 'WRINKLE', 83: 'PERSONAL CREDIT LINE', 84: 'MULTI-BILLIONAIRE', 85: 'MENTAL DISORDER', 86: 'SWEET TAILPIPE', 87: 'BOILING WATER', 88: 'DEER ANTLER', 89: 'BACKGROUND STORY', 90: 'STRIPED HYENA', 91: 'WEED WHACKER', 92: 'BACKSTABBING MISFORTUNE', 93: 'BAD STRIPED HYENA', 94: 'BAT-SHIT CRAZY AMISH FOLK', 95: 'BEAUTIFUL ELASTIC BAND', 96: 'BEST FAILURE', 97: 'BIG-BELLIED BAD MOOD', 98: 'BITCHY PEACE OFFERING', 99: 'BLOODY INDIGNATION', 100: 'BONE-CHILLING LEGAL WARRANT', 101: 'BORING HEARTBREAK', 102: 'BOTTLE-CONDITIONEDTRAINER', 103: 'BOTTLED SWEET TAILPIPE', 104: 'BRAINLESS WAYS OF THE WORLD', 105: 'BREWERY-FRESH SLEAZEBALL', 106: 'BRIGHT-EYED DOUBLE FAULT', 107: 'BROKENHEARTED DRUGGIE', 108: 'BULL-HEADED LOVER', 109: 'BUSTY DESCENDING COLOR', 110: 'BUXOM PERSONALITY', 111: 'CASK-CONDITIONED FREAK', 112: 'CAT-FRIENDLY READING PARTY', 113: 'CAUGHT-IN-THE-ACT JACKASS', 114: 'CHAUVINISTIC PUP', 115: 'CHEAP NATURAL HISTORY', 116: 'CHEEKY KEEPSAKE MACHETE', 117: 'CHEERFUL TOILET SEAT', 118: 'CHILLED GOOD-FOR-NOTHING', 119: 'CHUNKY DRUG ADDICT', 120: 'COCKY MATRIMONIAL LAW', 121: 'COLD-HEARTED ESKIMO', 122: 'COLORED SNUGGLE BUG', 123: 'COLOSSAL LOVE OF HER LIFE', 124: 'COMFORTING GROUCH', 125: 'COMIC DIVERGENT THINKING', 126: 'COMMON TOILET SEAT', 127: 'COMPASSIONATE BAD MOOD', 128: 'COMPLEX GUILT', 129: 'CONFRONTATIONAL FREAK', 130: 'CONSIDERATE LOUSE', 131: 'CONTEMPORARY QUEEN', 132: 'CONTENT DIRTBAG', 133: 'CONTROL-TOP LIGHT BULB', 134: 'CORRUPT BROKEN PROMISES', 135: 'CRAFT-BREWED POLICE SQUAD', 136: 'CRAPPY LACK OF MORALITY', 137: 'CRATE-TRAINED MOOD', 138: 'CRAWLY MISTAKE', 139: 'CRAZED MASTER'}
        self.verbs = {1: 'SURROUND', 2: 'STAB', 3: 'RETURN', 4: 'MEDICATE', 5: 'BLINDSIDE', 6: 'BOOGIE', 7: 'FLAP', 8: 'TRIP', 9: 'SWAT', 10: 'SUCK IN', 11: 'HARASS', 12: 'TRAP', 13: 'SNOOP', 14: 'EXPLODE', 15: 'SKETCH', 16: 'SCATTER', 17: 'CHALLENGE', 18: 'FIGHT', 19: 'BURY', 20: 'SPLATTER', 21: 'SMACK', 22: 'PEDDLE', 23: 'BALANCE', 24: 'TRIP UP', 25: 'BOGGLE', 26: 'POKE', 27: 'CRITIQUE', 28: 'FEAR', 29: 'INITIATE', 30: 'LINE UP', 31: 'RUN OVER', 32: 'SCHEDULE', 33: 'COOK', 34: 'IMPRISON', 35: 'UNDERESTIMATE', 36: 'CAJOLE', 37: 'WHEEDLE', 38: 'SOFT SOAP', 39: 'BUTTER UP', 40: 'SWEET-TALK', 41: 'PREVAIL', 42: 'SHRED', 43: 'DRINK', 44: 'DISPUTE', 45: 'ECHO', 46: 'MIMIC', 47: 'BERATE', 48: 'CASTIGATE', 49: 'UNDERRATE', 50: 'TAUNT'}
        self.adjectives = {1: 'DEAD', 2: 'HAIRLESS', 3: 'SADISTIC', 4: 'METAL', 5: 'WILD', 6: 'DOMESTICATED', 7: 'ABNORMAL', 8: 'MEDICATED', 9: 'MASSIVE', 10: 'DISRESPECTFUL', 11: 'IMPRESSIVE', 12: 'OUT OF CONTROL', 13: 'INTERNET WORTHY', 14: 'HILARIOUS', 15: 'SEXY', 16: 'HOT', 17: 'VERY TACTFUL', 18: 'BEARDED', 19: 'DUCK-LIKE', 20: 'VIOLENT', 21: 'SLIMY', 22: 'INSANELY CREEPY', 23: 'EMBARRASSED TO THE BONE', 24: 'SELF-CENTERED', 25: 'TALKING', 26: 'NAKED', 27: 'ANGRY', 28: 'SHAKY', 29: 'DEEP', 30: 'SICK', 31: 'LIPPY', 32: 'STICKY', 33: 'FLUFFY', 34: 'FROZEN', 35: 'UNHOLY', 36: 'PAINFULLY HONEST', 37: 'FILTHY', 38: 'FIGHTING', 39: 'BONKERS', 40: 'HARSH', 41: 'GREEDY', 42: 'CRAWLY', 43: 'INSANE', 44: 'HIDEOUS', 45: 'UNGODLY', 46: 'ABUSIVE', 47: 'HATEFUL', 48: 'IDIOTIC', 49: 'TWISTED', 50: 'USELESS', 51: 'YAPPING', 52: 'MAGICAL', 53: 'INDECENT', 54: 'GODAWFUL', 55: 'ARROGANT', 56: 'CONFUSED', 57: 'FLIRTING', 58: 'HIGH-END', 59: 'INSECURE', 60: 'MANIACAL', 61: 'SICKENED', 62: 'SLIPPERY', 63: 'STUBBORN', 64: 'TRIPPING', 65: 'VENGEFUL', 66: 'SINISTER', 67: 'COSTUMED', 68: 'COWARDLY', 69: 'HAUNTING', 70: 'STARTLED', 71: 'ALCOHOLIC', 72: 'DEMANDING', 73: 'SHIVERING', 74: 'OFFENSIVE', 75: 'NIGHTTIME', 76: 'STARTLING', 77: 'DISGUSTING', 78: 'SLAP HAPPY', 79: 'DISTURBING', 80: 'ADULTEROUS', 81: 'BLATHERING', 82: 'FLICKERING', 83: 'REBELLIOUS', 84: 'IMPERTINENT', 85: 'BULL HEADED', 86: 'HYPERACTIVE', 87: 'INFURIATING', 88: 'OUTNUMBERED', 89: 'PEA-BRAINED', 90: 'TERRITORIAL', 91: 'UNDERHANDED', 92: 'ZOMBIE LIKE', 93: 'MISCHIEVOUS', 94: 'AT-THE-READY', 95: 'FREE-LOADING', 96: 'HOUSE-BROKEN', 97: 'UP-T0-NO-G00D', 98: 'CRUEL-HEARTED', 99: 'MISUNDERSTOOD', 100: 'NARROW-MINDED', 101: 'SELF-ABSORBED', 102: 'FIERCELY-LOYAL', 103: 'OUT-OF-CONTROL', 104: 'FEAR-INSPIRING', 105: 'MENTALLY IMPAIRED'}
        # create default keys for user input values to be assigned
        self.user_selection = {'noun': '0', 'verb': '0', 'adjective': '0'}
        self.cardbank = {}

    def get_phrase_prompt(self):
        # need bank/file of phrases (one phrase per line)
        print('This is a placeholder phrase to play with')
        print('You played {} | {} | {}'.format(self.user_selection['noun'], self.user_selection['verb'], self.user_selection['adjective']))

        
    def print_available_cards(self):
        '''
        Prints all dictionary items in cardbank
        keys 1-4 are from the noun wordbank
        keys 5-8 are from the verb wordbank
        keys 9-12 are from the adjectives wordbank
        * Formating could be better
        '''
        print("Cards in hand are: ")
        print("Nouns: ")
        for key, value in self.cardbank.items():
            if key <= 4 :
                print('{:4} | {:^40}'.format(key, value))
        print("Verbs: ")
        for key, value in self.cardbank.items():
            if key >= 5 and key <= 8:
                print('{:4} | {:^40}'.format(key, value))
        print("Adjectives: ")
        for key, value in self.cardbank.items():
            if key >= 9 :
                print('{:4} | {:^40}'.format(key, value))

    def get_user_choices(self):
        '''
        Gets user input for each type of word (i.e. noun, verb, adjective)
        keys created from class init are:
        noun
        verb
        adjective
        *WIP needs better validation:
            - only checks if selection is in cardbank (does not check if type of word is correct for prompt)
            - possible feature: regex for partial word input checks/assignment
        '''
        self.print_available_cards()
        # iterate through the noun, verb, and adjective keys in user_selection
        for key in self.user_selection.keys():
            # loop continuosly until a valid entry from cardbank is selected
            while self.user_selection[key] not in self.cardbank.values():
                self.user_selection[key] = input("Please select a {}: ".format(key))
                # check if input is the key of the word
                if self.user_selection[key].isdigit():
                    self.user_selection[key] = self.cardbank[int(self.user_selection[key])]
                else:
                    # reassign user input to be all uppercase to match dictionary values
                    self.user_selection[key] = self.user_selection[key].upper()

    def get_user_cards(self):
        '''
        Adds dictionary entries to cardbank for user to "play"
        * Need to verify that range for randint call allows for assignment of last entry of wordbanks (may need to add +1 to len())
        '''
        # set accumalator for integer based key for dictionary entries
        key = 1
        # add references to wordbanks for loop calls (reduces lines of code)
        wordbanks = [self.nouns, self.verbs, self.adjectives]
        # iterate through each wordbank reference
        for bank in wordbanks:
            # set a repetition value to increment a while loop for sequential pulls from the same wordbank
            rep = 1
            # loop until accumalator reaches value 
            while rep < 5:
                # assign a random integer value between 1 and the length of the wordbank
                rng = randint(1, len(bank.keys()))
                # check if the value of the random integer key from the wordbank is already in the cardbank values (prevents duplicates)
                if bank[rng] in self.cardbank.values():
                    continue
                else:
                    # add the bank value of the rng key to the cardbank dictionary
                    self.cardbank[key] = bank[rng]
                    # increment the repetition accumalator for a successful loop
                    rep += 1
                    # increment the key accumalator to prevent re-assignment of the key value
                    key += 1


game = mad_libs()

# Need to set a startgame method to accomplish the calls below into a single call
game.get_user_cards()
game.get_user_choices()
game.get_phrase_prompt()

