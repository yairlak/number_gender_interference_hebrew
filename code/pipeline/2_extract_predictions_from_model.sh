#!/bin/bash
CUDA='' # ' --cuda' or '' (empty)
#CUDA=' --cuda'

PATH2MODEL='../../data/trained_models/LSTM/hebrew/hidden650_batch64_dropout0.1_lr20.0.pt'
PATH2VOCAB='../../data/trained_models/LSTM/hebrew/vocab.txt'
PATH2STIMULI='../../data/stimuli/'
PATH2OUTPUT='../../output/'
#for NATASK in 'nounpp_number' 'nounpp_gender' 'nounpp_number_gender';
for NATASK in 'objrel_number_V1' 'objrel_gender_V1' 'objrel_number_gender_V1' 'objrel_number_V2' 'objrel_gender_V2' 'objrel_number_gender_V2';
do
    NUM_SAMPLES=4096
    echo
    echo 'Number-agreement task: '$NATASK
    # Calculate accuracies (without ablation)
    echo 'python3 ../analysis/extract_predictions.py '$PATH2MODEL' -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES' -v '$PATH2VOCAB' -o '$PATH2OUTPUT'Hebrew_'$NATASK'_'$NUM_SAMPLES' --eos-separator "<eos>" --format pkl --lang he --uppercase-first-word'$CUDA
    eval 'python3 ../analysis/extract_predictions.py '$PATH2MODEL' -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES' -v '$PATH2VOCAB' -o '$PATH2OUTPUT'Hebrew_'$NATASK'_'$NUM_SAMPLES' --eos-separator "<eos>" --format pkl --lang he --uppercase-first-word'$CUDA
done
