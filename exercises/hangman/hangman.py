#!/usr/bin/env python3

wordlist = ['apple','house','chair','water','pizza','dance','smile','light','music','happy',
'jungle','rocket','castle','window','monkey','orange','garden','travel','cookie','shadow',
'rhythm','oxygen','wizard','galaxy','crypt','jigsaw','quiver','zephyr','sphinx','vortex',
'letter','coffee','balloon','butter','success','mirror','muffin','tennis','address','bookkeeper',
'knife','ghost','island','hour','wreck','thumb','honest','gnome','whistle','doubt',
'adventure','butterfly','dangerous','education','important','knowledge','microwave','newspaper','telephone','volcano',
'quiz','jaw','fog','ice','web','zip','owl','egg','toy','sun',
'tiger','dolphin','forest','ocean','eagle','panda','cactus','tulip','rainbow','snowflake',
'banjo','kazoo','zipper','igloo','ninja','koala','unicorn','pickle','tundra','sloth',
'absurd','bizarre','chaos','enigma','frenzy','glitch','haphazard','juxtapose','quandary','whimsical']


class Hangman:
    def __init__(self,wordchoice):
        self.word=wordlist[wordchoice-1]
        self.guessed=set()
        self.answer=set(self.word)
        self.turn=1
        print('you\'re playing hangman!')
        self.promptuser()
        

    def promptuser(self):
        print()
        print(' '.join([c if (c in self.guessed) else '_' for c in self.word]))
        print(f'You have guessed: {self.guessed}')
        if self.answer <= self.guessed:
            print(f'nice job. you guessed the word in {self.turn} turns')
            return
        elif self.turn > 26:
            print('you did not solve the problem in 26 turns. better luck next time.')
            return
        self.recentGuess=input('Guess one letter: ')
        self.guessed.add(self.recentGuess)
        self.turn+=1
        self.promptuser()
        


wordchoice=int(input('Enter a number between 1 and 100: '))

game=Hangman(wordchoice)