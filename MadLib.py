# Assignment1: mad-lib - the Berkeley Software Distribution License Disclaimer
# Sean Bucholtz (section 3)
# 4/5/13

# greeting
print('Welcome to Sean\'s wild and crazy Mad-Lib! \n \n'
      'Here we\'ll put our own creative spin on the: \n \n"Berkeley Software' \
      ' Distribution' \
      'License Disclaimer"')

answer_1 = input('\n\nAre you ready? (Yes/No): ')

while ( answer_1 == 'Yes' or answer_1 == 'yes' or answer_1 == 'y' \
        or answer_1 == 'Y') : # loop allows user to keep playing 

    print( '\n \nLet\'s get bananas! \n' )

    # input 
    pos_1 = input( 'Choose a Verb (action or state of being) ending in \'ed: ')
    pos_2 = input( 'Pick a Person, Place, or Thing (Noun): ')
    pos_3 = input( 'What\'s you\'re favorite Adjective (describes a Noun)?: ')
    pos_4 = input( 'Select another Noun: ')
    pos_5 = input( 'Again, think of third Noun: ')
    pos_6 = input( 'Now a second Adjective: ')
    pos_7 = input( 'And another Adjective: ')
    pos_8 = input( 'Now a plural Noun: ')
    pos_9 = input( 'Think of a Verb ending in \'ing: ')
    pos_10 = input( 'Select another Noun, and make it plural again: ')
    pos_11 = input( 'What is your favorite school subject? ')
    pos_12 = input( 'What sort of mood are you in right now? ')
    pos_13 = input( 'Last, but not leaste pick one more Noun: ')

    # output
    print( '\nThis software is ' + pos_1  + ' by the ' + pos_2 + \
       ' holders and contributors "as is" and any\nexpress or ' + pos_3 + \
       ' warranties, including, but not limited to, the implied warranties' \
       ' of merchantability and ' + pos_4 + ' for a particular ' \
       + pos_5 + ' are disclaimed. In no event shall the ' \
       + pos_2 + ' owner or contributors be liable for any direct,' \
       ' indirect, ' + pos_6 + ', special, ' + pos_7 + ', or ' \
       'consequential ' + pos_8 + ' (including, but not limited to, ' \
       + pos_9 + ' of substitute goods or services; loss of use, ' \
       + pos_10 + ', or profits; or business interruption) however ' \
       'caused and on any theory of ' + pos_11 + ', whether in contract' \
       ', strict liability, or tort (including ' + pos_13 + ' out of ' \
       'the use of this software, even if advised of the possibility of such ' \
       + pos_9 + '.' )  
    print( '\nWhat a fascinating disclaimer we\'ve made!' )

    answer_1 = input('\nWould you like to go again? (Yes/No): ') 
    
else:
    print('\nGoodbye.')
