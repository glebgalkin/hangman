gameIntro = '''
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝'''

gameStatus = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    ''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

words = [
    "computer", "hangman", "challenge", "python", "wordplay", "strategy", "puzzle", "vocabulary", "education", "entertain",
    "language", "playful", "learning", "letters", "alphabet", "brainstorm", "guessing", "synonym", "education", "intelligence",
    "definition", "fun", "knowledge", "enigma", "riddle", "quiz", "brain", "creativity", "gameboard", "brainiac",
    "interactive", "clever", "linguistics", "literacy", "mind-bender", "vocabulary", "quizzical", "rhetoric", "brainteaser",
    "puzzlement", "spelling", "thinking", "linguistic", "synonymous", "cerebral", "intellectual", "conundrum", "playword",
    "teaser", "enigmatic"
]


GAME_ERROR_LIMIT = 5