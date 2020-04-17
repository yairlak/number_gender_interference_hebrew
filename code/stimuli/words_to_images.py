import numpy as np
import os
import matplotlib.pyplot as plt

path2stimuli = '../../data/stimuli/'
path2output = '../../data/stimuli/imgs'
fn = 'trial_file_exp1 - trial_file.csv'
with open(os.path.join(path2stimuli, fn), 'r') as f:
    lines = f.readlines()


def txt2img(s):
    fig, ax = plt.subplots(figsize=(16,10))
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.text(0, 0, s[::-1], fontsize=30, color=(0.8, 0.8, 0.8), ha='center')
    plt.axis('off')
    fig.patch.set_facecolor('black')
    return fig

cnt_practice, cnt_test = (0, 0)
for i, l in enumerate(lines):
    fields = l.split(',')
    stimuli = fields[17:23]
    block_type = fields[0].strip()
    if block_type in ['test', 'practice']:
        if block_type == 'test':
            cnt_test += 1
            cnt = cnt_test
        else:
            cnt_practice += 1
            cnt = cnt_practice

        print(stimuli)
        for j, stim in enumerate(stimuli):
            fig = txt2img(stim)
            fn = os.path.join(path2output, '%s_%i_%i.png'%(block_type, cnt, j))
            plt.savefig(fn,facecolor=fig.get_facecolor())
            plt.close('all')
