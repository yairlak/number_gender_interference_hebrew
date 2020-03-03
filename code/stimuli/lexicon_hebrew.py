# -*- coding: utf-8 -*-


"""
NOUNS
"""
# Initialization
nouns = {}
for animacy in ['animate', 'inanimate']:
    nouns[animacy] = {}
    for gender in ['masculine', 'feminine']:
        nouns[animacy][gender] = {}

# ANIMATE
nouns['animate']['masculine']['singular'] = ['אורח', 'אמן', 'אמריקאי', 'בחור', 'דוגמן', 'חבר', 'ילד', 'מדריך', 'מנהיג', 'מנהל', 'נהג', 'נשיא', 'סופר',
 'סטודנט', 'עובד', 'פקיד', 'שחקן', 'שכן', 'תלמיד']

nouns['animate']['masculine']['plural'] = ['אורחים', 'אמנים', 'אמריקאיים', 'בחורים', 'דוגמנים', 'חברים', 'ילדים', 'מדריכים', 'מנהיגים', 'מנהלים', 'נהגים',
 'נשיאים', 'סופרים', 'סטודנטים', 'עובדים', 'פקידים', 'שחקנים', 'שכנים', 'תלמידים']

nouns['animate']['feminine']['singular'] = ['אורחת', 'אמנית', 'אמריקאית', 'בחורה', 'דוגמנית', 'חברה', 'ילדה', 'מדריכה', 'מנהיגה', 'מנהלת', 'נהגת', 'נשיאה',
 'סופרת', 'סטודנטית', 'עובדת', 'פקידה', 'שחקנית', 'שכנה', 'תלמידה']

nouns['animate']['feminine']['plural'] = ['אורחות', 'אמניות', 'אמריקאיות', 'בחורות', 'דוגמניות', 'חברות', 'ילדות', 'מדריכות', 'מנהיגות', 'מנהלות', 'נהגות',
 'נשיאות', 'סופרות', 'סטודנטיות', 'עובדות', 'פקידות', 'שחקניות', 'שכנות', 'תלמידות']

# INANIMATE
# nouns['inanimate']['masculine']['singular'] = ['ארטיק', 'בושם', 'בקבוק', 'חלון', 'כביש', 'כדור', 'כסא', 'מחשב', 'מטבח', 'מעיל']

# nouns['inanimate']['masculine']['plural'] = ['ארטיקים', 'בקבוקים', 'בשמים', 'חלונות', 'כבישים', 'כדורים', 'כסאות', 'מחשבים', 'מטבחים', 'מעילים']

# nouns['inanimate']['feminine']['singular'] = ['ארוחה', 'גלידה', 'חולצה', 'טלוויזיה', 'מיטה', 'מכונית', 'מנורה', 'משחה', 'צלחת', 'שרשרת']

# nouns['inanimate']['feminine']['plural'] = ['ארוחות', 'גלידות', 'חולות', 'טלווזיות', 'מיטות', 'מכוניות', 'מנורות', 'משחות', 'צלחות', 'שרשראות']

nouns[0]['inanimate']['masculine']['singular'] = ['ארטיק', 'מיץ', 'שוקולד']
nouns[0]['inanimate']['masculine']['plural'] = ['ארטיקים', 'מיצים', 'שוקולודים']
nouns[0]['inanimate']['feminine']['singular'] = ['גבינה', 'גלידה', 'שעווה']
nouns[0]['inanimate']['feminine']['plural'] = ['גבינות', 'גלידות', 'שעוות']

nouns[1]['inanimate']['masculine']['singular'] = ['כדור', 'כסא', 'מעיל']
nouns[1]['inanimate']['masculine']['plural'] = ['כדורים', 'כסאות', 'מעילים']
nouns[1]['inanimate']['feminine']['singular'] = ['חולצה', 'מטריה', 'צלחת']
nouns[1]['inanimate']['feminine']['plural'] = ['חולצות', 'מטריות', 'צלחות']

nouns[2]['inanimate']['masculine']['singular'] = ['חלון', 'מחשב', 'מטבח']
nouns[2]['inanimate']['masculine']['plural'] = ['חלונות', 'מחשבים', 'מטבחים']
nouns[2]['inanimate']['feminine']['singular'] = ['טלוויזיה', 'מיטה', 'מכונית']
nouns[2]['inanimate']['feminine']['plural'] = ['טלוויזיות', 'מיטות', 'מכוניות']


"""
VERBS
"""
# Initialization
verbs = {}
for animacy in ['animate', 'inanimate']:
    verbs[animacy] = {}
    for argument_struct in ['accusative', 'unaccusative']:
        verbs[animacy][argument_struct] = {}
        for gender in ['masculine', 'feminine']:
            verbs[animacy][argument_struct][gender] = {}


# ANIMATE
verbs['animate']['accusative']['masculine']['singular'] = ['מארח', 'מושך', 'מחזיק', 'מציל', 'מכיר', 'מצלם', 'תוקף', 'קופץ', 'מלמד', 'מרגיש',]
verbs['animate']['accusative']['masculine']['plural'] = ['מארחים', 'מושכים', 'מחזיקים', 'מצילים', 'מכירים', 'מצלמים', 'תוקפים', 'קופצים', 'מלמדים', 'מרגישים']
verbs['animate']['accusative']['feminine']['singular'] = ['מארחת', 'מושכת', 'מחזיקה', 'מצילה', 'מכירה', 'מצלמת', 'תוקפת', 'קופצת', 'מלמדת', 'מרגישה']
verbs['animate']['accusative']['feminine']['plural'] = ['מארחות', 'מושכות', 'מחזיקות', 'מצילות', 'מכירות', 'מצלמות', 'תוקפות', 'קופצות', 'מלמדות', 'מרגישות']

verbs['animate']['unaccusative']['masculine']['singular'] = ['מצטנן', 'מתחמם', 'מתייבש', 'מתלכלך', 'מתמוטט', 'מתעלף', 'מתקרר', 'נופל',
                                                             'נעלם','נרטב']
verbs['animate']['unaccusative']['masculine']['plural'] = ['מצטננים', 'מתחממים', 'מתייבשים', 'מתלכלכים', 'מתמוטטתים', 'מתעלפים', 'מתקררים', 'נופלים',
 'נעלמים', 'נרטבים']
verbs['animate']['unaccusative']['feminine']['singular'] = ['מצטננת', 'מתחממת', 'מתייבשת', 'מתלכלכת', 'מתמוטטת', 'מתעפלת', 'מתקררת',
 'נופלת', 'נעלמת', 'נרטבת']
verbs['animate']['unaccusative']['feminine']['plural'] = ['מתעלפות', 'מצטננות', 'נעלמות', 'מתחממות', 'מתקררות', 'מתלכלכות', 'מתייבשות'
                                                          , 'נרטבות', 'נופלות', 'מתמוטטות' ]

# INANIMATE
# verbs['inanimate']['unaccusative']['masculine']['singular'] = ['מתפרק', 'מתקלקל', 'מתרסק', 'נגמר', 'נדלק', 'נוזל', 'נכבה', 'נמס', 'נשפך', 'קופא']
# verbs['inanimate']['unaccusative']['masculine']['plural'] = ['מתפרקים', 'מתקלקלים', 'מתרסקים', 'נגמרים', 'נדלקים', 'נוזלים',
#                                                              'נכבים', 'נמסים', 'נשפכים','קופאים']
# verbs['inanimate']['unaccusative']['feminine']['singular'] = ['מתפרקת', 'מתקלקלת', 'מתרסקת', 'נגמרת', 'נדלקת', 'נוזלת', 'נכבת', 'נמסה',
#                                                               'נשפכת', 'קופאת']
# verbs['inanimate']['unaccusative']['feminine']['plural'] = ['מתפרקות', 'מתקלקלות', 'מתרסקות', 'נגמרות', 'נדלקות', 'נוזלות',
#                                                             'נכבות', 'נמסות', 'נשפכות', 'קופאות']

verbs[0]['inanimate']['unaccusative']['masculine']['singular'] = ['נגמר', 'נמס', 'קופא']
verbs[0]['inanimate']['unaccusative']['masculine']['plural'] = ['נגמרים', 'נמסים', 'קופאים']
verbs[0]['inanimate']['unaccusative']['feminine']['singular'] = ['נגמרה', 'נמסה', 'קפאה']
verbs[0]['inanimate']['unaccusative']['feminine']['plural'] = ['נגמרות', 'נמסות', 'קופאות']

verbs[1]['inanimate']['unaccusative']['masculine']['singular'] = ['נעלם', 'נפל,', 'נרטב']
verbs[1]['inanimate']['unaccusative']['masculine']['plural'] = ['נעלמים', 'נופלים', 'נרטבים']
verbs[1]['inanimate']['unaccusative']['feminine']['singular'] = ['נעלמה', 'נפלה', 'נרטבה']
verbs[1]['inanimate']['unaccusative']['feminine']['plural'] = ['נעלמות', 'נופלות', 'נרטבות']

verbs[2]['inanimate']['unaccusative']['masculine']['singular'] = ['מתלכלך', 'מתפרק', 'מתקלקל']
verbs[2]['inanimate']['unaccusative']['masculine']['plural'] = ['מתלכלכים','מתפרקים', 'מתקלקלים' ]
verbs[2]['inanimate']['unaccusative']['feminine']['singular'] = ['מתלכלכת', 'מתפרקת', 'מתקלקלת']
verbs[2]['inanimate']['unaccusative']['feminine']['plural'] = ['מתלכלכות', 'מתפרקות', 'מתקלקלות']


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
