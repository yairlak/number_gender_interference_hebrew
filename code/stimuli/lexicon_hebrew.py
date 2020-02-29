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
nouns['animate']['masculine']['singular'] = ['אורח', 'אמן', 'אמריקאי', 'בחור', 'דוגמן', 'חבר', 'סופר', 'ילד', 'פקיד', 'מדריך', 'מנהיג', 'מנהל', 'נהג', 'נשיא', 'סטודנט', 'עובד', 'שחקן', 'שכן', 'תלמיד']

nouns['animate']['masculine']['plural'] = ['אורחים', 'אמנים', 'אמריקאיים', 'בחורים', 'דוגמנים', 'חברים', 'סופרים', 'ילדים', 'פקידים', 'מדריכים', 'מנהיגים', 'מנהלים', 'נהגים', 'נשיאים', 'סטודנטים', 'עובדים', 'שחקנים', 'שכנים', 'תלמידים']

nouns['animate']['feminine']['singular'] = ['אורחת', 'אמנית', 'אמריקאית', 'בחורה', 'דוגמנית', 'חברה', 'סופרת', 'ילדה', 'פקידה', 'מדריכה', 'מנהיגה', 'מנהלת', 'נהגת', 'נשיאה', 'סטודנטית', 'עובדת', 'שחקנית', 'שכנה', 'תלמידה']

nouns['animate']['feminine']['plural'] = ['אורחות', 'אמניות', 'אמריקאיות', 'בחורות', 'דוגמניות', 'חברות', 'סופרות', 'ילדות', 'פקידות', 'מדריכות', 'מנהיגות', 'מנהלות', 'נהגות', 'נשיאות', 'סטודנטיות', 'עובדות', 'שחקניות', 'שכנות', 'תלמידות']

# INANIMATE
nouns['inanimate']['masculine']['singular'] = ['מחשב', 'כדור', 'חלון', 'ארטיק', 'בושם', 'מעיל', 'מטבח', 'בקבוק', 'כביש', 'כסא']

nouns['inanimate']['masculine']['plural'] = ['מחשבים', 'כדורים', 'חלונות', 'ארטיקים', 'בשמים', 'מעילים', 'מטבחים', 'בקבוקים', 'כבישים', 'כסאות'  ]

nouns['inanimate']['feminine']['singular'] = ['שרשרת', 'צלחת', 'חולצה', 'מכונית', 'ארוחה', 'גלידה' , 'טלוויזיה', 'מיטה', 'מנורה', 'משחה']

nouns['inanimate']['feminine']['plural'] = ['שרשראות', 'צלחות', 'חולות', 'מכוניות', 'ארוחות', 'גלידות', 'טלווזיות', 'מיטות', 'מנורות', 'משחות']




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

verbs['animate']['unaccusative']['masculine']['singular'] = ['מתמוטט', 'נופל', 'נרטב', 'מתייבש', 'מתלכלך', 'מתקרר', 'מתחמם', 'נעלם', 'מצטנן', 'מתעלף']
verbs['animate']['unaccusative']['masculine']['plural'] = ['מתעלפים', 'מצטננים', 'נעלמים', 'מתחממים', 'מתקררים', 'מתלכלכים', 'מתייבשים', 'נרטבים', 'נופלים', 'מתמוטטתים']
verbs['animate']['unaccusative']['feminine']['singular'] = ['מתמוטטת', 'נופלת', 'נרטבת', 'מתייבשת', 'מתלכלכת', 'מתקררת', 'מתחממת', 'נעלמת', 'מצטננת', 'מתעפלת' ]
verbs['animate']['unaccusative']['feminine']['plural'] = ['מתעלפות', 'מצטננות', 'נעלמות', 'מתחממות', 'מתקררות', 'מתלכלכות', 'מתייבשות', 'נרטבות', 'נופלות', 'מתמוטטות' ]

# INANIMATE
verbs['inanimate']['unaccusative']['masculine']['singular'] = ['נמס', 'קופא', 'נגמר', 'נכבה', 'נשפך', 'נדלק', 'מתקלקל', 'מתפרק', 'מתרסק', 'נוזל']
verbs['inanimate']['unaccusative']['masculine']['plural'] = ['נוזלים', 'מתרסקים', 'מתפרקים', 'מתקלקלים', 'נדלקים', 'נשפכים', 'נכבים', 'נגמרים', 'קופאים', 'נמסים']
verbs['inanimate']['unaccusative']['feminine']['singular'] = ['נמסה', 'קופאת', 'נגמרת', 'נכבת', 'נשפכת', 'נדלקת', 'מתקלקלת', 'מתפרקת', 'מתרסקת', 'נוזלת']
verbs['inanimate']['unaccusative']['feminine']['plural'] = ['נוזלות', 'מתרסקות', 'מתפרקות', 'מתקלקלות', 'נדלקות', 'נשפכות', 'נכבות', 'נגמרות', 'קופאות', 'נמסות']


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
