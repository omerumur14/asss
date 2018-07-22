from random import choice;
from random import sample;

def head_or_tail():
    v0 = ['HEAD','TAIL'];

    v1 = choice(v0);

    return(v1);

def rock_paper_scissors():
    v1=['ROCK','PAPER','SCİSSORS'];

    v2=sample(v1,2);

    print('1. '+v2[0]+'\n2. '+v2[1]);

    if(v2[0]=='ROCK' and v2[1]=='SCİSSORS'):
        print('ROCK win SCİSSORS lose');

    if(v2[1]=='ROCK' and v2[0]=='SCİSSORS'):
        print('ROCK win SCİSSORS lose');

    if(v2[0]=='ROCK' and v1[1]=='PAPER'):
        print('PAPER win ROCK lose');

    if(v2[1]=='ROCK' and v2[0]=='PAPER'):
        print('PAPER win ROCK lose');

    if(v2[0]=='SCİSSORS' and v2[1]=='PAPER'):
        print('SCİSSORS win PAPER lose');

    if(v2[1]=='SCİSSORS' and v2[0]=='PAPER'):
        print('SCİSSORS win PAPER lose');



def dice_roll(v0):

    v1 = [];

    for i in range(int(v0)):

        dice = ['1','2','3','4','5','6'];
        v2 = choice(dice);
        v1.append(v2);

    return(v1);
