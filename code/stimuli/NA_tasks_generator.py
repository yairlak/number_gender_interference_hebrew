import sys, argparse
import numpy as np
from lexicon_hebrew import Words

# Output is a tab-delimited list of stimuli with info: sentence \t tense \t subject gender \t subject number

# Parse arguments
parser = argparse.ArgumentParser(description='Stimulus generator for Hebrew')
parser.add_argument('-t', '--natask', default='nounpp', type=str, help = 'Number-agreement (NA) task to generate (nounpp/subjrel_that/objrel)')
parser.add_argument('-n', default=10 , type=int, help = 'number of samples from each condition')
parser.add_argument('-seed', default=1 , type=int, help = 'Random seed for replicability')
args = parser.parse_args()

stimuli = []
np.random.seed(args.seed)

def init_counter(features):
    # Create counter
    import itertools 
    counter = {}
    feature_combinations = list(itertools.product(*features.values())) 
    for comb in feature_combinations:
        counter['_'.join(comb)] = 0
    return counter


def counter_fullfilled(counter, n):
    return False if any(v < n for v in list(counter.values())) else True

# det N1 prep the N2 V1 det N3
if args.natask == 'nounpp_animate_accusative':
    animacies = ['animate', 'inanimate']
    genders = ['masculine', 'feminine']
    numbers = ['singular', 'plural']
    argument_structures = ['accusative', 'unaccusative']
    
    features = {}
    features['N1_animacy'] = ['animate'] # SUBJET IS ALWAYS ANIMATE
    features['N1_gender'] = genders
    features['N1_number'] = numbers
    features['N2_animacy'] = animacies
    features['N2_gender'] = genders
    features['N2_number'] = numbers
    features['V1_argument_struct'] = ['accusative'] # V1 IS ALWAYS ACCUSATIVE
    counter = init_counter(features)
    while not counter_fullfilled(counter, args.n):
        # N1
        N1_gender = genders[np.random.randint(2)]
        N1_number = numbers[np.random.randint(2)]
        N1_animacy = 'animate' # !!! --- SUBJECT IS ANIMATE --- !!!
        N1s = Words['nouns'][N1_animacy][N1_gender][N1_number]#[0:num_nouns]
        IX_N1 = np.random.randint(len(N1s))
        N1 = N1s[IX_N1]
        # PREP
        PREPs = Words['loc_preps']
        IX_PREP = np.random.randint(len(PREPs))
        PREP = PREPs[IX_PREP]
        # N2
        N2_gender = genders[np.random.randint(2)]
        N2_number = numbers[np.random.randint(2)]
        N2_animacy = animacies[np.random.randint(2)]
        N2s = Words['nouns'][N2_animacy][N2_gender][N2_number]#[0:num_nouns]
        IX_N2 = np.random.randint(len(N2s))
        N2 = N2s[IX_N2]
        # N3
        N3_gender = genders[np.random.randint(2)]
        N3_number = numbers[np.random.randint(2)]
        N3_animacy = animacies[np.random.randint(2)]
        N3s = Words['nouns'][N3_animacy][N3_gender][N3_number]#[0:num_nouns]
        IX_N3 = np.random.randint(len(N3s))
        N3 = N3s[IX_N3]
        # V1
        V1_argument_struct = 'accusative' # V1 IS ACCUSATIVE
        V1s = Words['verbs'][N1_animacy][V1_argument_struct][N1_gender][N1_number]#[0:num_nouns]
        IX_V1 = np.random.randint(len(V1s))
        V1 = V1s[IX_V1]
        # sentence
        opposite_number_V1 = 'singular' if N1_number == 'plural' else 'plural'
        opposite_gender_V1 = 'masculine' if N1_gender == 'feminine' else 'feminine'
        sentence = ' '.join(['ה', N1, PREP, 'ה', N2, V1, 'את', 'ה', N3])

        noun_IXs = [IX_N1, IX_N2, IX_N3]
        if len(set(noun_IXs)) == len(noun_IXs): # check noun repetition at the lemma level (i.e., all indexes are different)
            if counter['_'.join([N1_animacy, N1_gender, N1_number, N2_animacy, N2_gender, N2_number, V1_argument_struct])] < args.n:
                stimuli.append([args.natask, sentence,
                       N1_animacy, N1_gender, N1_number,
                       N2_animacy, N2_gender, N2_number,
                       N3_gender, N3_number,
                       V1_argument_struct,
                       Words['verbs'][N1_animacy][V1_argument_struct][N1_gender][opposite_number_V1][IX_V1],
                       Words['verbs'][N1_animacy][V1_argument_struct][opposite_gender_V1][N1_number][IX_V1],
                       Words['verbs'][N1_animacy][V1_argument_struct][opposite_gender_V1][opposite_number_V1][IX_V1]])
                counter['_'.join([N1_animacy, N1_gender, N1_number, N2_animacy, N2_gender, N2_number, V1_argument_struct])]+=1 

    stimuli.sort(key=lambda x: x[1]) # first word
    stimuli.sort(key=lambda x: x[7], reverse=True) # feature 1
    stimuli.sort(key=lambda x: x[5], reverse=True) # feature 2
    stimuli.sort(key=lambda x: x[3], reverse=True) # feature 3
    [print('\t'.join(l)) for l in stimuli]


# det N1 prep the N2 V1 
if args.natask == 'nounpp_animate_unaccusative':
    animacies = ['animate', 'inanimate']
    genders = ['masculine', 'feminine']
    numbers = ['singular', 'plural']
    argument_structures = ['accusative', 'unaccusative']
    
    features = {}
    features['N1_animacy'] = ['animate'] # SUBJET IS ALWAYS ANIMATE
    features['N1_gender'] = genders
    features['N1_number'] = numbers
    features['N2_animacy'] = animacies
    features['N2_gender'] = genders
    features['N2_number'] = numbers
    features['V1_argument_struct'] = ['unaccusative'] # V1 IS ALWAYS ACCUSATIVE
    counter = init_counter(features)
    while not counter_fullfilled(counter, args.n):
        # N1
        N1_gender = genders[np.random.randint(2)]
        N1_number = numbers[np.random.randint(2)]
        N1_animacy = 'animate' # !!! --- SUBJECT IS ANIMATE --- !!!
        N1s = Words['nouns'][N1_animacy][N1_gender][N1_number]#[0:num_nouns]
        IX_N1 = np.random.randint(len(N1s))
        N1 = N1s[IX_N1]
        # PREP
        PREPs = Words['loc_preps']
        IX_PREP = np.random.randint(len(PREPs))
        PREP = PREPs[IX_PREP]
        # N2
        N2_gender = genders[np.random.randint(2)]
        N2_number = numbers[np.random.randint(2)]
        N2_animacy = animacies[np.random.randint(2)]
        N2s = Words['nouns'][N2_animacy][N2_gender][N2_number]#[0:num_nouns]
        IX_N2 = np.random.randint(len(N2s))
        N2 = N2s[IX_N2]
        # N3
        N3_gender = genders[np.random.randint(2)]
        N3_number = numbers[np.random.randint(2)]
        N3_animacy = animacies[np.random.randint(2)]
        N3s = Words['nouns'][N3_animacy][N3_gender][N3_number]#[0:num_nouns]
        IX_N3 = np.random.randint(len(N3s))
        N3 = N3s[IX_N3]
        # V1
        V1_argument_struct = 'unaccusative' # V1 IS UNACCUSATIVE
        V1s = Words['verbs'][N1_animacy][V1_argument_struct][N1_gender][N1_number]#[0:num_nouns]
        IX_V1 = np.random.randint(len(V1s))
        V1 = V1s[IX_V1]
        # sentence
        opposite_number_V1 = 'singular' if N1_number == 'plural' else 'plural'
        opposite_gender_V1 = 'masculine' if N1_gender == 'feminine' else 'feminine'
        sentence = ' '.join(['ה', N1, PREP, 'ה', N2, V1])

        noun_IXs = [IX_N1, IX_N2, IX_N3]
        if len(set(noun_IXs)) == len(noun_IXs): # check noun repetition at the lemma level (i.e., all indexes are different)
            if counter['_'.join([N1_animacy, N1_gender, N1_number, N2_animacy, N2_gender, N2_number, V1_argument_struct])] < args.n:
                stimuli.append([args.natask, sentence,
                       N1_animacy, N1_gender, N1_number,
                       N2_animacy, N2_gender, N2_number,
                       N3_gender, N3_number,
                       V1_argument_struct,
                       Words['verbs'][N1_animacy][V1_argument_struct][N1_gender][opposite_number_V1][IX_V1],
                       Words['verbs'][N1_animacy][V1_argument_struct][opposite_gender_V1][N1_number][IX_V1],
                       Words['verbs'][N1_animacy][V1_argument_struct][opposite_gender_V1][opposite_number_V1][IX_V1]])
                counter['_'.join([N1_animacy, N1_gender, N1_number, N2_animacy, N2_gender, N2_number, V1_argument_struct])]+=1 

    stimuli.sort(key=lambda x: x[1]) # first word
    stimuli.sort(key=lambda x: x[7], reverse=True) # feature 1
    stimuli.sort(key=lambda x: x[5], reverse=True) # feature 2
    stimuli.sort(key=lambda x: x[3], reverse=True) # feature 3
    [print('\t'.join(l)) for l in stimuli]


# det N1 prep the N2 V1 
if args.natask == 'nounpp_inanimate_unaccusative':
    animacies = ['animate', 'inanimate']
    genders = ['masculine', 'feminine']
    numbers = ['singular', 'plural']
    argument_structures = ['accusative', 'unaccusative']
    
    features = {}
    features['N1_animacy'] = ['inanimate'] # SUBJET IS ALWAYS ANIMATE
    features['N1_gender'] = genders
    features['N1_number'] = numbers
    features['N2_animacy'] = animacies
    features['N2_gender'] = genders
    features['N2_number'] = numbers
    features['V1_argument_struct'] = ['unaccusative'] # V1 IS ALWAYS ACCUSATIVE
    counter = init_counter(features)
    while not counter_fullfilled(counter, args.n):
        # N1
        N1_gender = genders[np.random.randint(2)]
        N1_number = numbers[np.random.randint(2)]
        N1_animacy = 'inanimate' # !!! --- SUBJECT IS ANIMATE --- !!!
        N1s = Words['nouns'][N1_animacy][N1_gender][N1_number]#[0:num_nouns]
        IX_N1 = np.random.randint(len(N1s))
        N1 = N1s[IX_N1]
        # PREP
        PREPs = Words['loc_preps']
        IX_PREP = np.random.randint(len(PREPs))
        PREP = PREPs[IX_PREP]
        # N2
        N2_gender = genders[np.random.randint(2)]
        N2_number = numbers[np.random.randint(2)]
        N2_animacy = animacies[np.random.randint(2)]
        N2s = Words['nouns'][N2_animacy][N2_gender][N2_number]#[0:num_nouns]
        IX_N2 = np.random.randint(len(N2s))
        N2 = N2s[IX_N2]
        # N3
        N3_gender = genders[np.random.randint(2)]
        N3_number = numbers[np.random.randint(2)]
        N3_animacy = animacies[np.random.randint(2)]
        N3s = Words['nouns'][N3_animacy][N3_gender][N3_number]#[0:num_nouns]
        IX_N3 = np.random.randint(len(N3s))
        N3 = N3s[IX_N3]
        # V1
        V1_argument_struct = 'unaccusative' # V1 IS UNACCUSATIVE
        V1s = Words['verbs'][N1_animacy][V1_argument_struct][N1_gender][N1_number]#[0:num_nouns]
        IX_V1 = np.random.randint(len(V1s))
        V1 = V1s[IX_V1]
        # sentence
        opposite_number_V1 = 'singular' if N1_number == 'plural' else 'plural'
        opposite_gender_V1 = 'masculine' if N1_gender == 'feminine' else 'feminine'
        sentence = ' '.join(['ה', N1, PREP, 'ה', N2, V1])

        noun_IXs = [IX_N1, IX_N2, IX_N3]
        if len(set(noun_IXs)) == len(noun_IXs): # check noun repetition at the lemma level (i.e., all indexes are different)
            if counter['_'.join([N1_animacy, N1_gender, N1_number, N2_animacy, N2_gender, N2_number, V1_argument_struct])] < args.n:
                stimuli.append([args.natask, sentence,
                       N1_animacy, N1_gender, N1_number,
                       N2_animacy, N2_gender, N2_number,
                       N3_gender, N3_number,
                       V1_argument_struct,
                       Words['verbs'][N1_animacy][V1_argument_struct][N1_gender][opposite_number_V1][IX_V1],
                       Words['verbs'][N1_animacy][V1_argument_struct][opposite_gender_V1][N1_number][IX_V1],
                       Words['verbs'][N1_animacy][V1_argument_struct][opposite_gender_V1][opposite_number_V1][IX_V1]])
                counter['_'.join([N1_animacy, N1_gender, N1_number, N2_animacy, N2_gender, N2_number, V1_argument_struct])]+=1 

    stimuli.sort(key=lambda x: x[1]) # first word
    stimuli.sort(key=lambda x: x[7], reverse=True) # feature 1
    stimuli.sort(key=lambda x: x[5], reverse=True) # feature 2
    stimuli.sort(key=lambda x: x[3], reverse=True) # feature 3
    [print('\t'.join(l)) for l in stimuli]


# det N1 that the N2 V2 V1 det N3
if args.natask == 'objrel':
    genders = ['masculine', 'feminine']
    numbers = ['singular', 'plural']
    
    features = {}
    features['N1_gender'] = genders
    features['N1_number'] = numbers
    features['N2_gender'] = genders
    features['N2_number'] = numbers
    features['V1_argument_struct'] = argument_structures
    features['V2_argument_struct'] = argument_structures
    counter = init_counter(features)

    while not counter_fullfilled(counter, args.n):
        # N1
        N1_gender = genders[np.random.randint(2)]
        N1_number = numbers[np.random.randint(2)]
        N1s = Words['nouns'][N1_gender][N1_number]#[0:num_nouns]
        IX_N1 = np.random.randint(len(N1s))
        N1 = N1s[IX_N1]
        # N2
        N2_gender = genders[np.random.randint(2)]
        N2_number = numbers[np.random.randint(2)]
        N2s = Words['nouns'][N2_gender][N2_number]#[0:num_nouns]
        IX_N2 = np.random.randint(len(N2s))
        N2 = N2s[IX_N2]
        # N3
        N3_gender = genders[np.random.randint(2)]
        N3_number = numbers[np.random.randint(2)]
        N3s = Words['nouns'][N3_gender][N3_number]#[0:num_nouns]
        IX_N3 = np.random.randint(len(N3s))
        N3 = N3s[IX_N3]
        # V1
        V1s = Words['verbs'][N1_gender][N1_number]#[0:num_nouns]
        IX_V1 = np.random.randint(len(V1s))
        V1 = V1s[IX_V1]
        # V2
        V2s = Words['verbs'][N2_gender][N2_number]
        IX_V2 = np.random.randint(len(V2s))
        V2 = V2s[IX_V2]
        # sentence
        opposite_number_V1 = 'singular' if N1_number == 'plural' else 'plural'
        opposite_gender_V1 = 'masculine' if N1_gender == 'feminine' else 'feminine'
        opposite_number_V2 = 'singular' if N2_number == 'plural' else 'plural'
        opposite_gender_V2 = 'masculine' if N2_gender == 'feminine' else 'feminine'
        sentence = ' '.join(['ה', N1, 'ש', 'ה', N2, V2, V1, 'את', 'ה', N3])

        noun_IXs = [IX_N1, IX_N2, IX_N3]
        if len(set(noun_IXs)) == len(noun_IXs): # check noun repetition at the lemma level (i.e., all indexes are different)
            if IX_V1 != IX_V2:                  # check verb repetition at the lemma level
                if counter['_'.join([N1_animacy, N1_gender, N1_number, N2_animacy, N2_gender, N2_number, V1_argument_struct, V2_argument_struct])] < args.n:
                    stimuli.append([args.natask, sentence,
                           N1_gender, N1_number,
                           N2_gender, N2_number,
                           N3_gender, N3_number,
                           Words['verbs'][N1_gender][opposite_number_V1][IX_V1], Words['verbs'][opposite_gender_V1][N1_number][IX_V1], Words['verbs'][opposite_gender_V1][opposite_number_V1][IX_V1], Words['verbs'][N2_gender][opposite_number_V2][IX_V2], Words['verbs'][opposite_gender_V2][N2_number][IX_V2], Words['verbs'][opposite_gender_V2][opposite_number_V2][IX_V2]])
                    counter['_'.join([N1_gender, N1_number, N2_gender, N2_number])]+=1 

    stimuli.sort(key=lambda x: x[1]) # first word
    stimuli.sort(key=lambda x: x[7], reverse=True) # feature 1
    stimuli.sort(key=lambda x: x[5], reverse=True) # feature 1
    stimuli.sort(key=lambda x: x[3], reverse=True) # feature 2
    [print('\t'.join(l)) for l in stimuli]
