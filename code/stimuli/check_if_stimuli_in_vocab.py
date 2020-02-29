from lexicon_hebrew import Words
import numpy as np

path2vocab = '../../data/trained_models/LSTM/hebrew/vocab.txt'
with open(path2vocab, 'r') as f:
    vocab = f.readlines()
vocab = [w.strip() for w in vocab]
#print(vocab)

# -----
# NOUNS
# -----
mss = []; mps = []; fss = []; fps = []
num_nouns = len(Words['nouns']['masculine']['singular'])
print('Outside of vocab:')
for i in range(num_nouns):
    ms = Words['nouns']['masculine']['singular'][i]
    mp = Words['nouns']['masculine']['plural'][i]
    fs = Words['nouns']['feminine']['singular'][i]
    fp = Words['nouns']['feminine']['plural'][i]
    in_vocab = [ms not in vocab, mp not in vocab, fs not in vocab, fp not in vocab]
    if any(in_vocab):
        print(i)
        print(np.asarray([ms, mp, fs, fp])[in_vocab])
    else:
        mss.append(ms)
        mps.append(mp)
        fss.append(fs)
        fps.append(fp)
print('Exist in vocab:')
print(mss)
print(mps)
print(fss)
print(fps)

# -----
# VERBS
# -----
mss = []; mps = []; fss = []; fps = []
num_nouns = len(Words['verbs']['masculine']['singular'])
print('Outside of vocab:')
for i in range(num_nouns):
    ms = Words['verbs']['masculine']['singular'][i]
    mp = Words['verbs']['masculine']['plural'][i]
    fs = Words['verbs']['feminine']['singular'][i]
    fp = Words['verbs']['feminine']['plural'][i]
    in_vocab = [ms not in vocab, mp not in vocab, fs not in vocab, fp not in vocab]
    if any(in_vocab):
        print(i)
        print(np.asarray([ms, mp, fs, fp])[in_vocab])
    else:
        mss.append(ms)
        mps.append(mp)
        fss.append(fs)
        fps.append(fp)
print('Exist in vocab:')
print(mss)
print(mps)
print(fss)
print(fps)
