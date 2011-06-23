#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
FROM THE GITHUB WIKI:
A collection of semi-formal, language based rules to describe the course
prerequisites. In order to automatically check the the curriculum for validity
these rules should be followed (the user input box will use a guided input to
help the user form the rules). All rules which do not conform to the rules are
then saved as free text, and always marked specially for certifiers to look
carefully at. The rules can be something like

6 credits of Mathematics courses
or
The course MAT2ST02H****
(The latter rule is based on the course ID, described below)

###############################################################################


The parsing of text has 2 functions.
1. Support the guided entry of prerequisites.
2. Verify that a finished list of prerequisites

Ekki allar reglur í belg og biðu heldur listi af stuttum strengjum sem geta:
    a) mappast á reglur
    b) vistast sem freeform texti

'''

def rule_course_list(s):
    '''
    "Eftirfarandi áfangar ISL2BL03H,ISL2BL03H,ISL2BL03H"
    '''
    if not s.startswith('Eftirfarandi áfangar'):
        return False, None
    l = s.split(',')
    l[0] = l[0].split(' ')[-1]
    for item in l:
        if not is_course(item):
            return False, None
    return True, l


class RuleParser(object):
    def __init__(self):
        self.rulelist = [rule_course_list]

    def parse_text(self, text):
        sentences = text.split('.')
        l = [process_sentence(s) for s in sentences]

        # build html
            
    def process_sentence(self, s):
        for rule in self.rulelist:
            is_match, result = rule(s)
            if is_match:
                return result, s

    def validate_curricula(self, curricula):
        '''
        
        '''
        pass
