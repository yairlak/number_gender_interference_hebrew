# -*- coding: utf-8 -*-


"""
NOUNS
"""
# Initialization
nouns = {}
for animacy in ['animate', 'inanimate']:
    nouns[animacy] = {}
    for group in range(3):
        nouns[animacy][group] = {}
        for gender in ['masculine', 'feminine']:
            nouns[animacy][group][gender] = {}

# ANIMATE
nouns['animate'][0]['masculine']['singular'] = ['אורח',  'אמריקאי', 'בחור',  'חבר',  'ילד', 'מדריך' , 'נהג',  'סטודנט', 'שחקן', 'שכן', 'תלמיד']

nouns['animate'][0]['masculine']['plural'] = ['אורחים',  'אמריקאיים', 'בחורים',  'חברים', 'ילדים', 'מדריכים',  'נהגים', 'סטודנטים',  'שחקנים', 'שכנים', 'תלמידים']

nouns['animate'][0]['feminine']['singular'] = ['אורחת',  'אמריקאית', 'בחורה',  'חברה', 'ילדה', 'מדריכה', 'נהגת', 'סטודנטית',  'שחקנית', 'שכנה', 'תלמידה']

nouns['animate'][0]['feminine']['plural'] = ['אורחות',  'אמריקאיות', 'בחורות', 'חברות', 'ילדות', 'מדריכות',  'נהגות', 'סטודנטיות',   'שחקניות', 'שכנות', 'תלמידות']


# GROUP 0
nouns['inanimate'][0]['masculine']['singular'] = ['משקה', 'מסך', 'שביל']
nouns['inanimate'][0]['masculine']['plural'] = ['משקאות', 'מסכים', 'שבילים']

nouns['inanimate'][0]['feminine']['singular'] = ['ערמה', 'עוגיה', 'תרופה']
nouns['inanimate'][0]['feminine']['plural'] = ['ערמות', 'עוגיות', 'תרופות']

# GROUP 1
nouns['inanimate'][1]['masculine']['singular'] = ['כדור', 'כסא', 'שלט']
nouns['inanimate'][1]['masculine']['plural'] = ['כדורים', 'כסאות', 'שלטים']

nouns['inanimate'][1]['feminine']['singular'] = ['ספה', 'כורסא', 'תמונה']
nouns['inanimate'][1]['feminine']['plural'] = ['ספות', 'כורסאות', 'תמונות']

# GROUP 2
nouns['inanimate'][2]['masculine']['singular'] = ['חלון', 'מחשב', 'מטבח']
nouns['inanimate'][2]['masculine']['plural'] = ['חלונות', 'מחשבים', 'מטבחים']

nouns['inanimate'][2]['feminine']['singular'] = ['טלוויזיה', 'מיטה', 'מכונית']
nouns['inanimate'][2]['feminine']['plural'] = ['טלוויזיות', 'מיטות', 'מכוניות']


"""
VERBS
"""
# Initialization
verbs = {}
for animacy in ['animate', 'inanimate']:
    verbs[animacy] = {}
    for group in range(3):
        verbs[animacy][group] = {}
        for argument_struct in ['accusative', 'unaccusative']:
            verbs[animacy][group][argument_struct] = {}
            for gender in ['masculine', 'feminine']:
                verbs[animacy][group][argument_struct][gender] = {}


# ANIMATE
verbs['animate'][0]['accusative']['masculine']['singular'] = ['מחפש', 'מושך', 'מחזיק', 'מכיר', 'מלמד',  'מצלם', 'מרגש',  'תוקף']

verbs['animate'][0]['accusative']['masculine']['plural'] = ['מחפשים' ,'מושכים' ,'מחזיקים' ,'מכירים' ,'מלמדים'  ,'מצלמים', 'מרגשים' ,'תוקפים']

verbs['animate'][0]['accusative']['feminine']['singular'] = ['מחפשת', 'מושכת', 'מחזיקה', 'מכירה', 'מלמדת',  'מצלמת', 'מרגשת',  'תוקפת']

verbs['animate'][0]['accusative']['feminine']['plural'] = ['מחפשות', 'מושכות', 'מחזיקות', 'מכירות', 'מלמדות',  'מצלמות', 'מרגשות',  'תוקפות']

verbs['animate'][0]['unaccusative']['masculine']['singular'] = ['מצטנן', 'מתחמם', 'מתייבש', 'מתלכלך', 'מתמוטט', 'מתעלף', 'מתקרר', 'נופל', 'נעלם', 'נרטב']

verbs['animate'][0]['unaccusative']['masculine']['plural'] = ['מצטננים', 'מתחממים', 'מתייבשים', 'מתלכלכים', 'מתמוטטים', 'מתעלפים', 'מתקררים', 'נופלים', 'נעלמים', 'נרטבים']

verbs['animate'][0]['unaccusative']['feminine']['singular'] = ['מצטננת', 'מתחממת', 'מתייבשת', 'מתלכלכת', 'מתמוטטת', 'מתעלפת', 'מתקררת', 'נופלת', 'נעלמת', 'נרטבת']

verbs['animate'][0]['unaccusative']['feminine']['plural'] = ['מצטננות', 'מתחממות', 'מתייבשות', 'מתלכלכות', 'מתמוטטות', 'מתעלפות', 'מתקררות', 'נופלות', 'נעלמות', 'נרטבות']

verbs['inanimate'][0]['unaccusative']['masculine']['singular'] = ['נגמר', 'נאבד', 'נהרס']
verbs['inanimate'][0]['unaccusative']['masculine']['plural'] = ['נגמרים', 'נאבדים', 'נהרסים']
verbs['inanimate'][0]['unaccusative']['feminine']['singular'] = ['נגמרת', 'נאבדת', 'נהרסת']
verbs['inanimate'][0]['unaccusative']['feminine']['plural'] = ['נגמרות', 'נאבדות', 'נהרסות']

verbs['inanimate'][1]['unaccusative']['masculine']['singular'] = ['נעלם', 'נופל', 'נרטב']
verbs['inanimate'][1]['unaccusative']['masculine']['plural'] = ['נעלמים', 'נופלים', 'נרטבים']
verbs['inanimate'][1]['unaccusative']['feminine']['singular'] = ['נעלמת', 'נופלת', 'נרטבת']
verbs['inanimate'][1]['unaccusative']['feminine']['plural'] = ['נעלמות', 'נופלות', 'נרטבות']

verbs['inanimate'][2]['unaccusative']['masculine']['singular'] = ['מתלכלך', 'מתפרק', 'מתקלקל']
verbs['inanimate'][2]['unaccusative']['masculine']['plural'] = ['מתלכלכים','מתפרקים', 'מתקלקלים' ]
verbs['inanimate'][2]['unaccusative']['feminine']['singular'] = ['מתלכלכת', 'מתפרקת', 'מתקלקלת']
verbs['inanimate'][2]['unaccusative']['feminine']['plural'] = ['מתלכלכות', 'מתפרקות', 'מתקלקלות']


"""
PREPOSITIONS
"""
# LOCATION PREPOSITIONS
# -----
loc_preps = [ 'מלפני','מעל', 'ליד', 'מאחורי',  'לצד']


Words = {
	'nouns': nouns.copy(), 
	'verbs': verbs.copy(), 
	'loc_preps': loc_preps.copy(), 
}


