#!/usr/bin/python3
def multiple_returns(sentence):
    res = ()
    if len(sentence) == 0:
        return (0,"none")
    else:
        return(len(sentence), sentence[0])
