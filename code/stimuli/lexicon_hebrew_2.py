# -*- coding: utf-8 -*-


"""
DET
"""
# DEFINITE
# --------
# Initialization
determinants = {}
definit = {}
a = {}
for gender in ['masculine', 'feminine']:
    definit[gender] = {}
    a[gender] = {}

# Tokens
definit['masculine']['singular'] = ['The']
definit['masculine']['plural'] = ['The']
definit['feminine']['singular'] = ['The']
definit['feminine']['plural'] = ['The']

a['masculine']['singular'] = ['a', 'an']
a['masculine']['plural'] = ['']
a['feminine']['singular'] = ['a', 'an']
a['feminine']['plural'] = ['']

determinants = {'definit':definit, 'a':a}


"""
NOUNS
"""
# Initialization
nouns = {}
for gender in ['masculine', 'feminine']:
    nouns[gender] = {}

# Tokens
#nouns['masculine']['singular'] = ["אורח","אמן","אמריקאי","בחור","גנב","גנן","דוגמן","דוד","חבר","סופר","טבח","ילד","פקיד","מאמן","מדריך","מהנדס","מחנך","מנהיג","מנהל","מנתח","נהג","נשיא","סטודנט","עובד","רופא","שוטר","שחקן","שכן","תלמיד","תייר"]
    
#nouns['masculine']['plural'] = ["אורחים","אמנים","אמריקאיים","בחורים","גנבים","גננים","דוגמנים","דודים","חברים","סופרים","טבחים","ילדים","פקידים","מאמנים","מדריכים","מהנדסים","מחנכים","מנהיגים","מנהלים","מנתחים","נהגים","נשיאים","סטודנטים","עובדים","רופאים","שוטרים","שחקנים","שכנים","תלמידים","תיירים"]
    
#nouns['feminine']['singular'] = ["אורחת","אמנית","אמריקאית","בחורה","גנבת","גננית","דוגמנית","דודה","חברה","סופרת","טבחית","ילדה","פקידה","מאמנת","מדריכה","מהנדסת","מחנכת","מנהיגה","מנהלת","מנתחת","נהגת","נשיאה","סטודנטית","עובדת","רופאה","שוטרת","שחקנית","שכנה","תלמידה","תיירת"]
    
#nouns['feminine']['plural'] = ["אורחות","אמניות","אמריקאיות","בחורות","גנבות","גננות","דוגמניות","דודות","חברות","סופרות","טבחיות","ילדות","פקידות","מאמנות","מדריכות","מהנדסות","מחנכות","מנהיגות","מנהלות","מנתחות","נהגות","נשיאות","סטודנטיות","עובדות","רופאות","שוטרות","שחקניות","שכנות","תלמידות","תיירות"]
# Tokens

# ANIMATE
nouns['animate']['masculine']['singular'] = ['אורח', 'אמן', 'אמריקאי', 'בחור', 'דוגמן', 'חבר', 'סופר', 'ילד', 'פקיד', 'מדריך', 'מנהיג', 'מנהל', 'נהג', 'נשיא', 'סטודנט', 'עובד', 'שחקן', 'שכן', 'תלמיד']

nouns['animate']['masculine']['plural'] = ['אורחים', 'אמנים', 'אמריקאיים', 'בחורים', 'דוגמנים', 'חברים', 'סופרים', 'ילדים', 'פקידים', 'מדריכים', 'מנהיגים', 'מנהלים', 'נהגים', 'נשיאים', 'סטודנטים', 'עובדים', 'שחקנים', 'שכנים', 'תלמידים']

nouns['animate']['feminine']['singular'] = ['אורחת', 'אמנית', 'אמריקאית', 'בחורה', 'דוגמנית', 'חברה', 'סופרת', 'ילדה', 'פקידה', 'מדריכה', 'מנהיגה', 'מנהלת', 'נהגת', 'נשיאה', 'סטודנטית', 'עובדת', 'שחקנית', 'שכנה', 'תלמידה']

nouns['animate']['feminine']['plural'] = ['אורחות', 'אמניות', 'אמריקאיות', 'בחורות', 'דוגמניות', 'חברות', 'סופרות', 'ילדות', 'פקידות', 'מדריכות', 'מנהיגות', 'מנהלות', 'נהגות', 'נשיאות', 'סטודנטיות', 'עובדות', 'שחקניות', 'שכנות', 'תלמידות']

# INANIMATE
nouns['inanimate']['masculine']['singular'] = ['כסא']

nouns['inanimate']['masculine']['plural'] = []

nouns['inanimate']['feminine']['singular'] = []

nouns['inanimate']['feminine']['plural'] = []

"""
LOCATION NOUNS
"""
# Initialization
location_nouns = {}
for gender in ['masculine', 'feminine']:
    location_nouns[gender] = {}

# Tokens
location_nouns['masculine']['singular'] = nouns['masculine']['singular']
location_nouns['masculine']['plural'] = nouns['masculine']['plural']
location_nouns['feminine']['singular'] = nouns['feminine']['singular']
location_nouns['feminine']['plural'] = nouns['feminine']['plural']


"""
VERBS
"""
# Initialization
verbs = {}
for gender in ['masculine', 'feminine']:
    verbs[gender] = {}



# Tokens
verbs['animate']['accusative']['masculine']['singular'] = ['מארח', 'מושך', 'מחזיק', 'מציל', 'מכיר', 'מצלם', 'תוקף']
verbs['animate']['accusative']['masculine']['plural'] = ['מארחים', 'מושכים', 'מחזיקים', 'מצילים', 'מכירים', 'מצלמים', 'תוקפים']
verbs['animate']['accusative']['feminine']['singular'] = ['מארחת', 'מושכת', 'מחזיקה', 'מצילה', 'מכירה', 'מצלמת', 'תוקפת']
verbs['animate']['accusative']['feminine']['plural'] = ['מארחות', 'מושכות', 'מחזיקות', 'מצילות', 'מכירות', 'מצלמות', 'תוקפות']
verbs['animate']['unaccusative']['masculine']['singular'] = []
verbs['animate']['unaccusative']['masculine']['plural'] = []
verbs['animate']['unaccusative']['feminine']['singular'] = []
verbs['animate']['unaccusative']['feminine']['plural'] = []

# INANIMATE
verbs['inanimate']['unaccusative']['masculine']['singular'] = []
verbs['inanimate']['unaccusative']['masculine']['plural'] = []
verbs['inanimate']['unaccusative']['feminine']['singular'] = []
verbs['inanimate']['unaccusative']['feminine']['plural'] = []



#verbs['masculine']['singular'] = ["אוהב","דוחף","מאכיל","מארח","מאשים","מבדר","מבייש","מבין","מברך","מגדל","מושך","מחבק","מחזיק","מציל","מכיר","מלביש","מלטף","מנשק","מסיע","מסלק","מעיר","מפחיד","מפטר","מצלם","מקלל","מרגש","מרקיד","שומע","תוקף"]

#verbs['masculine']['plural'] = ["אוהבים","דוחפים","מאכילים","מארחים","מאשימים","מבדרים","מביישים","מבינים","מברכים","מגדלים","מושכים","מחבקים","מחזיקים","מצילים","מכירים","מלבישים","מלטפים","מנשקים","מסיעים","מסלקים","מעירים","מפחידים","מפטרים","מצלמים","מקללים","מרגשים","מרקידים","שומעים","תוקפים"]

#verbs['feminine']['singular'] =  ["אוהבת","דוחפת","מאכילה","מארחת","מאשימה","מבדרת","מביישת","מבינה","מברכת","מגדלת","מושכת","מחבקת","מחזיקה","מצילה","מכירה","מלבישה","מלטפת","מנשקת","מסיעה","מסלקת","מעירה","מפחידה","מפטרת","מצלמת","מקללת","מרגשת","מרקידה","שומעת","תוקפת"]

#verbs['feminine']['plural'] = ["אוהבות","דוחפות","מאכילות","מארחות","מאשימות","מבדרות","מביישות","מבינות","מברכות","מגדלות","מושכות","מחבקות","מחזיקות","מצילות","מכירות","מלבישות","מלטפות","מנשקות","מסיעות","מסלקות","מעירות","מפחידות","מפטרות","מצלמות","מקללות","מרגשות","מרקידות","שומעות","תוקפות"]

copula = {}
copula['singular'] = 'is'
copula['plural'] = 'are'

# MATRIX VERBS
# -----
# Initialization
matrix_verbs = {}
# Tokens
matrix_verbs['singular'] = ['remembers', 'says', 'declares']
matrix_verbs['plural'] =   ['remember' , 'say', 'declare']


"""
PREPOSITIONS
"""
# LOCATION PREPOSITIONS
# -----
# Tokens (second word will be used to choose the right article from determinats{} - 'a'/'definit'/)
loc_preps = ['ליד', 'מאחור', 'מלפני', 'לצד']


"""
ADJECTIVES
"""
adjectives = {}

Words = {
	'determinants': determinants.copy(), 
	'nouns': nouns.copy(), 
	'location_nouns': location_nouns.copy(), 
	'verbs': verbs.copy(), 
	'copula': copula.copy(), 
	'matrix_verbs': matrix_verbs.copy(), 
	'loc_preps': loc_preps.copy(), 
	'adjectives': adjectives.copy()
}
