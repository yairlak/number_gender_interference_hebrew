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
nouns['animate'][0]['masculine']['singular'] = ['אורח', 'אמן', 'אמריקאי', 'בחור', 'דוגמן', 'חבר', 'ילד', 'מדריך', 'מנהיג', 'מנהל', 'נהג', 'נשיא', 'סופר',
 'סטודנט', 'עובד', 'פקיד', 'שחקן', 'שכן', 'תלמיד']

nouns['animate'][0]['masculine']['plural'] = ['אורחים', 'אמנים', 'אמריקאיים', 'בחורים', 'דוגמנים', 'חברים', 'ילדים', 'מדריכים', 'מנהיגים', 'מנהלים', 'נהגים',
 'נשיאים', 'סופרים', 'סטודנטים', 'עובדים', 'פקידים', 'שחקנים', 'שכנים', 'תלמידים']

nouns['animate'][0]['feminine']['singular'] = ['אורחת', 'אמנית', 'אמריקאית', 'בחורה', 'דוגמנית', 'חברה', 'ילדה', 'מדריכה', 'מנהיגה', 'מנהלת', 'נהגת', 'נשיאה',
 'סופרת', 'סטודנטית', 'עובדת', 'פקידה', 'שחקנית', 'שכנה', 'תלמידה']

nouns['animate'][0]['feminine']['plural'] = ['אורחות', 'אמניות', 'אמריקאיות', 'בחורות', 'דוגמניות', 'חברות', 'ילדות', 'מדריכות', 'מנהיגות', 'מנהלות', 'נהגות',
 'נשיאות', 'סופרות', 'סטודנטיות', 'עובדות', 'פקידות', 'שחקניות', 'שכנות', 'תלמידות']

# INANIMATE
# nouns['inanimate']['masculine']['singular'] = ['ארטיק', 'בושם', 'בקבוק', 'חלון', 'כביש', 'כדור', 'כסא', 'מחשב', 'מטבח', 'מעיל']

# nouns['inanimate']['masculine']['plural'] = ['ארטיקים', 'בקבוקים', 'בשמים', 'חלונות', 'כבישים', 'כדורים', 'כסאות', 'מחשבים', 'מטבחים', 'מעילים']

# nouns['inanimate']['feminine']['singular'] = ['ארוחה', 'גלידה', 'חולצה', 'טלוויזיה', 'מיטה', 'מכונית', 'מנורה', 'משחה', 'צלחת', 'שרשרת']

# nouns['inanimate']['feminine']['plural'] = ['ארוחות', 'גלידות', 'חולות', 'טלווזיות', 'מיטות', 'מכוניות', 'מנורות', 'משחות', 'צלחות', 'שרשראות']

nouns['inanimate'][0]['masculine']['singular'] = ['ארטיק', 'מיץ', 'שוקולד']
nouns['inanimate'][0]['masculine']['plural'] = ['ארטיקים', 'מיצים', 'שוקולודים']
nouns['inanimate'][0]['feminine']['singular'] = ['גבינה', 'גלידה', 'שעווה']
nouns['inanimate'][0]['feminine']['plural'] = ['גבינות', 'גלידות', 'שעוות']

nouns['inanimate'][1]['masculine']['singular'] = ['כדור', 'כסא', 'מעיל']
nouns['inanimate'][1]['masculine']['plural'] = ['כדורים', 'כסאות', 'מעילים']
nouns['inanimate'][1]['feminine']['singular'] = ['חולצה', 'מטריה', 'צלחת']
nouns['inanimate'][1]['feminine']['plural'] = ['חולצות', 'מטריות', 'צלחות']

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
verbs['animate'][0]['accusative']['masculine']['singular'] = ['מארח', 'מושך', 'מחזיק', 'מציל', 'מכיר', 'מצלם', 'תוקף', 'קופץ', 'מלמד', 'מרגיש',]
verbs['animate'][0]['accusative']['masculine']['plural'] = ['מארחים', 'מושכים', 'מחזיקים', 'מצילים', 'מכירים', 'מצלמים', 'תוקפים', 'קופצים', 'מלמדים', 'מרגישים']
verbs['animate'][0]['accusative']['feminine']['singular'] = ['מארחת', 'מושכת', 'מחזיקה', 'מצילה', 'מכירה', 'מצלמת', 'תוקפת', 'קופצת', 'מלמדת', 'מרגישה']
verbs['animate'][0]['accusative']['feminine']['plural'] = ['מארחות', 'מושכות', 'מחזיקות', 'מצילות', 'מכירות', 'מצלמות', 'תוקפות', 'קופצות', 'מלמדות', 'מרגישות']

verbs['animate'][0]['unaccusative']['masculine']['singular'] = ['מצטנן', 'מתחמם', 'מתייבש', 'מתלכלך', 'מתמוטט', 'מתעלף', 'מתקרר', 'נופל',
                                                             'נעלם','נרטב']
verbs['animate'][0]['unaccusative']['masculine']['plural'] = ['מצטננים', 'מתחממים', 'מתייבשים', 'מתלכלכים', 'מתמוטטתים', 'מתעלפים', 'מתקררים', 'נופלים',
 'נעלמים', 'נרטבים']
verbs['animate'][0]['unaccusative']['feminine']['singular'] = ['מצטננת', 'מתחממת', 'מתייבשת', 'מתלכלכת', 'מתמוטטת', 'מתעפלת', 'מתקררת',
 'נופלת', 'נעלמת', 'נרטבת']
verbs['animate'][0]['unaccusative']['feminine']['plural'] = ['מתעלפות', 'מצטננות', 'נעלמות', 'מתחממות', 'מתקררות', 'מתלכלכות', 'מתייבשות'
                                                          , 'נרטבות', 'נופלות', 'מתמוטטות' ]

# INANIMATE
# verbs['inanimate']['unaccusative']['masculine']['singular'] = ['מתפרק', 'מתקלקל', 'מתרסק', 'נגמר', 'נדלק', 'נוזל', 'נכבה', 'נמס', 'נשפך', 'קופא']
# verbs['inanimate']['unaccusative']['masculine']['plural'] = ['מתפרקים', 'מתקלקלים', 'מתרסקים', 'נגמרים', 'נדלקים', 'נוזלים',
#                                                              'נכבים', 'נמסים', 'נשפכים','קופאים']
# verbs['inanimate']['unaccusative']['feminine']['singular'] = ['מתפרקת', 'מתקלקלת', 'מתרסקת', 'נגמרת', 'נדלקת', 'נוזלת', 'נכבת', 'נמסה',
#                                                               'נשפכת', 'קופאת']
# verbs['inanimate']['unaccusative']['feminine']['plural'] = ['מתפרקות', 'מתקלקלות', 'מתרסקות', 'נגמרות', 'נדלקות', 'נוזלות',
#                                                             'נכבות', 'נמסות', 'נשפכות', 'קופאות']

verbs['inanimate'][0]['unaccusative']['masculine']['singular'] = ['נגמר', 'נמס', 'קופא']
verbs['inanimate'][0]['unaccusative']['masculine']['plural'] = ['נגמרים', 'נמסים', 'קופאים']
verbs['inanimate'][0]['unaccusative']['feminine']['singular'] = ['נגמרה', 'נמסה', 'קפאה']
verbs['inanimate'][0]['unaccusative']['feminine']['plural'] = ['נגמרות', 'נמסות', 'קופאות']

verbs['inanimate'][1]['unaccusative']['masculine']['singular'] = ['נעלם', 'נפל,', 'נרטב']
verbs['inanimate'][1]['unaccusative']['masculine']['plural'] = ['נעלמים', 'נופלים', 'נרטבים']
verbs['inanimate'][1]['unaccusative']['feminine']['singular'] = ['נעלמה', 'נפלה', 'נרטבה']
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
loc_preps = ['ליד', 'מאחורי', 'מלפני', 'לצד']



Words = {
	'nouns': nouns.copy(), 
	'verbs': verbs.copy(), 
	'loc_preps': loc_preps.copy(), 
}


#"""
#ADJECTIVES
#"""
#adjectives = {}


#"""
#LOCATION NOUNS
#"""
# Initialization
#location_nouns = {}
#for animacy in ['animate', 'inanimate']:
#    location_nouns[animacy] = {}
#    for gender in ['masculine', 'feminine']:
#        location_nouns[animacy][gender] = {}

# Tokens
#location_nouns['masculine']['singular'] = nouns['masculine']['singular']
#location_nouns['masculine']['plural'] = nouns['masculine']['plural#']
#location_nouns['feminine']['singular'] = nouns['feminine']['singular']
#location_nouns['feminine']['plural'] = nouns['feminine']['plural']
