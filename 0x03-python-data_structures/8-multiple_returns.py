#!/usr/bin/python3
def multiple_returns(sentence):
    res = ()
    if len(sentence) == 0:
        return (none,)
    else:
        return(len(sentence), sentence[0])
