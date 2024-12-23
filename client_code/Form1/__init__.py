from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from random import choice

class Form1(Form1Template):
    
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
    
    def get_old_insult_click(self, **event_args):
        self.make_old_insult()
        
    def get_insult_click(self, **event_args):
        self.make_insult()

    def get_compliment_click(self, **event_args):
        self.make_compliment()
        
    def get_badsanta_click(self, **event_args):
        self.make_badsanta_insult()
        
    def get_nicesanta_click(self, **event_args):
        self.make_nicesanta_compliment()
        
    def make_old_insult(self):
        insult1 = ['artless', 'bawdy', 'beslubbering', 'bootless',
            'burly-boned', 'caluminous', 'churlish', 'clouted',
            'cockered', 'craven', 'cullionly', 'currish', 'dankish',
            'dissembling', 'droning', 'errant', 'fawning', 'fishified',
            'fobbing', 'frothy', 'froward', 'fusty', 'gleeking',
            'goatish', 'gorbellied', 'impertinent', 'infectious',
            'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled',
            'mewling', 'misbegotten', 'odiferous', 'paunchy', 'poisonous',
            'pribbling', 'puking', 'puny', 'qualling', 'rank', 'reeky',
            'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly',
            'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous',
            'warped', 'Wart-necked', 'wayward', 'weedy', 'wimpled',
            'yeasty'
        ]
        insult2 = ['base-court', 'bat-fowling', 'beef-witted',
            'beetle-headed', 'boil-brained', 'brazen-faced',
            "bunch-back'd", 'clapper-clawed', 'clay-brained',
            'common-kissing', 'crook-pated', 'dismal-dreaming',
            'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing',
            'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed',
            'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged',
            'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born',
            'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured',
            'knotty-pated', 'leaden-footed', 'lily-livered',
            'malmsey-nosed', 'milk-livered', 'motley-minded',
            'muddy-mettled', 'onion-eyed', "pigeon-liver'd",
            'plume-plucked', 'pottle-deep', 'pox-marked', 'rampallian',
            'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed',
            'scale-sided', 'scurvy-valiant', 'shard-borne',
            'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited',
            'tickle-brained', 'toad-spotted', 'unchin-snouted',
            "unwash'd", 'weather-bitten', 'whoreson'
        ]
        insult3 = ['apple-john', 'baggage', 'barnacle', 'Basket-Cockle',
            'bladder', 'blind-worm', 'boar-pig', 'bugbear', 'bum-bailey',
            'canker-blossom', 'clack-dish', 'clotpole', 'codpiece',
            'coxcomb', 'death-token', 'devil-monk', 'dewberry',
            'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker',
            'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy',
            'hedge-pig', 'horn-beast', 'hugger-mugger', 'joithead',
            'jolt-head', 'knave', 'lewdster', 'lout', 'maggot-pie',
            'malcontent', 'malt-worm', 'mammet', 'measle', 'minnow',
            'miscreant', 'moldwarp', 'mumble-news', 'nut-hook',
            'pigeon-egg', 'pignut', 'popinjay', 'pumpion', 'puttock',
            'rascal', 'ratsbane', 'scullian', 'scut', 'skainsmate',
            'strumpet', 'toad', 'varlot', 'vassal', 'wagtail',
            'whey-face'
        ]
        self.output.text = ("Thou art a " + choice(insult1) + " " +
            choice(insult2) + " " + choice(insult3) + ".")
        
    def make_insult(self):
        insult1 = ['animalistic', 'appalling', 'awful', 'bad-looking',
            'beastly', 'deformed', 'disfigured', 'foul', 'frightful',
            'grisly', 'gross', 'grotesque', 'hard-featured', 'hideous',
            'horrid', 'ill-favored', 'loathsome', 'misshapen',
            'monstrous', 'not much to look at', 'repelling', 'repugnant',
            'repulsive', 'revolting', 'unbeautiful', 'uncomely',
            'uninviting', 'unlovely', 'unsightly',
        ]
        insult2 = ['abrupt', 'abusive', 'bad-mannered', 'barbaric',
            'barbarous', 'blunt', 'boorish', 'brusque', 'brutish',
            'cheeky', 'churlish', 'coarse', 'crabbed', 'crude', 'curt',
            'discourteous', 'graceless', 'gross', 'gruff', 'ignorant',
            'illiterate', 'impertinent', 'impolite', 'impudent',
            'inconsiderate', 'insolent', 'insulting', 'intrusive',
            'loutish', 'obscene', 'raw', 'savage', 'scurrilous', 'surly',
            'uncivil', 'uncivilized', 'uncouth', 'uncultured',
            'uneducated', 'ungracious', 'unmannerly', 'unpolished',
            'unrefined', 'vulgar', 'wild',
        ]
        insult3 = ['bad guy', 'bad person', 'baddie', 'baddy',
            'black marketeer', 'blackmailer', 'blockhead', 'bonehead',
            'clodpoll', 'con', 'convict', 'cretin', 'crook', 'culprit',
            'delinquent', 'desperado', 'deuce', 'dimwit', 'dork',
            'dumbbell', 'dunce', 'evildoer', 'ex-con', 'felon', 'fool',
            'fugitive', 'gangster', 'guerilla', 'hood', 'hoodlum',
            'hooligan', 'hustler', 'ignoramus', 'imbecile',
            'inside person', 'jailbird', 'jerk', 'lawbreaker',
            'malefactor', 'mobster', 'moron', 'mug', 'muttonhead',
            'nincompoop', 'ninny', 'nitwit', 'offender', 'outlaw',
            'pinhead', 'racketeer', 'simpleton', 'sinner', 'slippery eel',
            'thug', 'tomfool', 'twit', 'wrongdoer', 'yardbird',
        ]
        self.output.text = ("You are a " + choice(insult1) + " " +
            choice(insult2) + " " + choice(insult3)+ ".")

    def make_compliment(self):
        complimentary_descriptions1 = ['affectionate', 'altruistic', 'amiable', 'amicable',
        'beneficent', 'benevolent', 'bounteous', 'charitable',
        'compassionate', 'congenial', 'considerate', 'cordial',
        'courteous', 'friendly', 'gentle', 'good-hearted', 'gracious',
        'humane', 'humanitarian', 'kindhearted', 'kindly', 'loving',
        'neighborly', 'obliging', 'philanthropic', 'softhearted',
        'sympathetic', 'tenderhearted', 'thoughtful', 'tolerant',
        'understanding'
        ]
        complimentary_descriptions2 = ['able', 'adept', 'agile', 'alert', 'astute',
        'bold', 'brainy', 'bright', 'brilliant', 'brisk', 'canny',
        'clever', 'consummate', 'cool', 'crafty', 'cultivated',
        'effective', 'eggheaded', 'expert', 'fresh', 'genius',
        'gifted', 'good', 'hip', 'ingenious', 'keen', 'knowing',
        'masterly', 'nimble', 'on the ball', 'polished', 'practiced',
        'proficient', 'quick', 'quick-witted', 'ready', 'resourceful',
        'sassy', 'savvy', 'sharp', 'shrewd', 'skillful', 'slick',
        'talented', 'wise', 'wised up', 'with it'
        ]
        complimentary_nouns = ['academician', 'architect', 'author', 'brain', 'builder',
        'child genius', 'creator', 'designer', 'egghead', 'Einstein',
        'experimenter', 'founder', 'freak', 'genius', 'good egg',
        'good guy', 'good person', 'highbrow', 'innovator',
        'intellect', 'intellectual', 'maker', 'person of his word',
        'person of honor', 'marvel', 'mastermind', 'miracle',
        'moonwalker', 'natural', 'nice guy', 'one in a million',
        'originator', 'phenomenon', 'pioneer', 'polished person',
        'prodigy', 'rarity', 'refined person', 'rocket scientist',
        'sage', 'scholar', 'sensation', 'spectacle', 'star person',
        'stunner', 'talent', 'whiz', 'whiz kid', 'wizard', 'wonder',
        'wonder child', 'wunderkind'
        ]
        self.output.text = ("You are a " + choice(complimentary_descriptions1) + " " +
        choice(complimentary_descriptions2) + " " + choice(complimentary_nouns)+ ".")
        
    def make_badsanta_insult(self):
        insult1 = [
            'coal-hearted', 'elf-frightening', 'ornament-smashing', 'frostbitten', 
            'pine-needle-covered', 'gift-wrapping-phobic', 'tinsel-tangled', 
            'snowball-dodging', 'gingerbread-crumbling', 'holly-prickly', 
            'sleigh-stopping', 'reindeer-scaring', 'carol-cringing', 
            'peppermint-soured', 'wreath-ruining', 'tree-toppling', 
            'sugarplum-soured', 'egg-nog-spilling', 'stocking-tearing', 
            'mistletoe-missing', 'cracker-breaking', 'ice-skating-failing', 
            'chimney-clogging', 'rudolph-insulting', 'bell-clanging', 
            'nutcracker-breaking', 'blizzard-bringing', 'turkey-burning', 
            'gravy-splashing', 'icicle-dripping'
        ]
        insult2 = [
            'sleigh-busting', 'reindeer-kicking', 'tree-burning', 
            'carol-mocking', 'stocking-snatching', 'pudding-spitting', 
            'elf-insulting', 'mistletoe-avoiding', 'present-hoarding', 
            'Santa-snubbing', 'snowman-pelting', 'gravy-splashing', 
            'cracker-crushing', 'holly-shredding', 'bauble-busting', 
            'gift-shoving', 'yule-log-hating', 'frosty-sneering', 
            'candy-cane-breaking', 'tinsel-tangling', 'turkey-mauling', 
            'snow-shoveling-avoiding', 'chimney-blocking', 'north-pole-denying', 
            'holiday-spoiling', 'egg-nog-spilling', 'wrapping-paper-ripping', 
            'fireplace-hogging', 'cookie-stealing', 'holiday-ghost-insulting'
        ]
        insult3 = [
            "scrooge", "grinch", "miser", "cheapskate", "skinflint", "tightwad", 
            "humbug", "killjoy", "spoilsport", "curmudgeon", "naysayer", "penny-pincher", 
            "churl", "grouch", "grump", "crank", "sourpuss", "wet blanket", "party pooper", 
            "buzzkill", "downer", "fuddy-duddy", "stick-in-the-mud", "bah humbug", "hoarder", 
            "pack rat", "gloom-monger", "joy-snuffer", "gift-shunner", "ornament-breaker", 
            "snowflake-crusher", "tinsel-tangler", "carol-mocker", "elf-basher", 
            "reindeer-scorner", "coal-stuffer", "holiday-ruiner", "present-thief", 
            "tree-toppler", "wrapping-wrecker", "Santa-skeptic", "cheer-dampener"
        ]
        self.output.text = ("You are a " + choice(insult1) + " " +
            choice(insult2) + " " + choice(insult3)+ ".")

    def make_nicesanta_compliment(self):
        complimentary_descriptions1 = [
            "angelic", "awe-inspiring", "beautiful", "cheerful", "charming", 
            "delightful", "festive", "frost-kissed", "graceful", "handsome", 
            "heartwarming", "holly-bright", "jolly", "jubilant", "light-filled", 
            "lovely", "merry", "ornamented", "peppermint-sweet", "radiant", 
            "reindeer-friendly", "sleigh-ready", "snow-glowing", "sparkling", 
            "star-lit", "sugar-dusted", "tinsel-twinkling", "tree-bright", 
            "warm-hearted", "wreath-wrapped"
        ]
        complimentary_descriptions2 = [
            "kind-hearted", "considerate", "courteous", "cultured", "gracious", 
            "heartfelt", "joyous", "mannerly", "noble", "pleasant", "polite", 
            "refined", "respectful", "selfless", "sweet-natured", "thoughtful", 
            "understanding", "well-behaved", "well-bred", "well-mannered", 
            "chivalrous", "festively charming", "peaceful", "jolly-natured", 
            "holiday-spirited", "snow-soft", "bright-hearted", "gingerbread-kind", 
            "warm and welcoming", "tinsel-graced", "cheerfully patient"
        ]
        complimentary_nouns = [
            "saint", "angel", "elf", "gift-giver", "tree-decorator", "holiday-maker", 
            "stocking-stuffer", "reindeer-wrangler", "carol-singer", "light-hanger", 
            "cookie-baker", "present-wrapper", "peppermint-purveyor", "tinsel-hanger", 
            "snow-sculptor", "mistletoe-magic", "joy-bringer", "cheer-spreader", 
            "Santa-helper", "kind-hearted soul", "Yule-log-master", "holiday-spirit", 
            "magic-maker", "snowflake-dancer", "sleigh-driver", "North Pole dreamer", 
            "Christmas star", "sugarplum fairy", "festive wonder", "holiday hero", 
            "jingle-bell ringer", "peace-bringer", "seasonal sweetheart"
        ]
        self.output.text = ("You are a " + choice(complimentary_descriptions1) + " " +
            choice(complimentary_descriptions2) + " " + choice(complimentary_nouns)+ ".")
        
    
    
