#!/bin/bash 

# PATHS
PATH2STIMULI='../../data/stimuli/'

# NUMBER OF SAMPLES TO GENERATE
NUM_SAMPLES=4096
NUM_STIMULUS_TYPES=16 # How many lines "NA_task_generator.py -n 1" would generate
N=$(($NUM_SAMPLES / $NUM_STIMULUS_TYPES))

for NATASK in 'objrel';
do
    
    # ---------------------
    # GENERATE STIMULI
    # ---------------------
    
    # 1. Generate all possible stimuli from lexicon
    echo 'Generating data...'
    eval 'python3 ../stimuli/NA_tasks_generator.py --natask '$NATASK' -n '$N' > '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt'
    echo 'Stimuli were saved to: '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt'
    # 2. Sanity check: verify and print to screen feature distriution
    echo
    echo 'Test:'
    eval 'python3 ../stimuli/verify_stimuli_file_is_balanced.py -f '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt'
    
    # 3. Prepare in Linzen's format and generate an info pkl file
    echo
    echo 'Transform to Linzen format'
    
    echo 'Number task V1 (outer)'
    TEST_WORD_POSITION=7
    WRONG_WORD_LABEL='verb_1_wrong_number'
    eval 'python3 ../stimuli/convert_to_Linzen_format.py -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt -o '$PATH2STIMULI'Hebrew_'$NATASK'_number_V1_'$NUM_SAMPLES' -p gender_1 2 -p number_1 3 -p gender_2 4 -p number_2 5 -p gender_3 6 -p number_3 7 -p verb_1_wrong_number 8 -p verb_1_wrong_gender 9 -p verb_1_wrong_number_gender 10 -p verb_2_wrong_number 11 -p verb_2_wrong_gender 12 -p verb_1_wrong_number_gender 13 --correct-word-position '$TEST_WORD_POSITION' --wrong-word-label '$WRONG_WORD_LABEL
    
    echo 'Gender task V1 (outer)'
    WRONG_WORD_LABEL='verb_1_wrong_gender'
    eval 'python3 ../stimuli/convert_to_Linzen_format.py -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt -o '$PATH2STIMULI'Hebrew_'$NATASK'_gender_V1_'$NUM_SAMPLES' -p gender_1 2 -p number_1 3 -p gender_2 4 -p number_2 5 -p gender_3 6 -p number_3 7 -p verb_1_wrong_number 8 -p verb_1_wrong_gender 9 -p verb_1_wrong_number_gender 10 -p verb_2_wrong_number 11 -p verb_2_wrong_gender 12 -p verb_1_wrong_number_gender 13 --correct-word-position '$TEST_WORD_POSITION' --wrong-word-label '$WRONG_WORD_LABEL
    
    echo 'Number and Gender task V1 (outer)'
    WRONG_WORD_LABEL='verb_1_wrong_number_gender'
    eval 'python3 ../stimuli/convert_to_Linzen_format.py -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt -o '$PATH2STIMULI'Hebrew_'$NATASK'_number_gender_V1_'$NUM_SAMPLES' -p gender_1 2 -p number_1 3 -p gender_2 4 -p number_2 5 -p gender_3 6 -p number_3 7 -p verb_1_wrong_number 8 -p verb_1_wrong_gender 9 -p verb_1_wrong_number_gender 10 -p verb_2_wrong_number 11 -p verb_2_wrong_gender 12 -p verb_1_wrong_number_gender 13 --correct-word-position '$TEST_WORD_POSITION' --wrong-word-label '$WRONG_WORD_LABEL
    
    echo 'Number task V2 (inner)'
    TEST_WORD_POSITION=6
    WRONG_WORD_LABEL='verb_2_wrong_number'
    eval 'python3 ../stimuli/convert_to_Linzen_format.py -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt -o '$PATH2STIMULI'Hebrew_'$NATASK'_number_V2_'$NUM_SAMPLES' -p gender_1 2 -p number_1 3 -p gender_2 4 -p number_2 5 -p gender_3 6 -p number_3 7 -p verb_1_wrong_number 8 -p verb_1_wrong_gender 9 -p verb_1_wrong_number_gender 10 -p verb_2_wrong_number 11 -p verb_2_wrong_gender 12 -p verb_2_wrong_number_gender 13 --correct-word-position '$TEST_WORD_POSITION' --wrong-word-label '$WRONG_WORD_LABEL
    
    echo 'Gender task V2 (inner)'
    WRONG_WORD_LABEL='verb_2_wrong_gender'
    eval 'python3 ../stimuli/convert_to_Linzen_format.py -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt -o '$PATH2STIMULI'Hebrew_'$NATASK'_gender_V2_'$NUM_SAMPLES' -p gender_1 2 -p number_1 3 -p gender_2 4 -p number_2 5 -p gender_3 6 -p number_3 7 -p verb_1_wrong_number 8 -p verb_1_wrong_gender 9 -p verb_1_wrong_number_gender 10 -p verb_2_wrong_number 11 -p verb_2_wrong_gender 12 -p verb_2_wrong_number_gender 13 --correct-word-position '$TEST_WORD_POSITION' --wrong-word-label '$WRONG_WORD_LABEL
    
    echo 'Number and Gender task V2 (inner)'
    WRONG_WORD_LABEL='verb_2_wrong_number_gender'
    eval 'python3 ../stimuli/convert_to_Linzen_format.py -i '$PATH2STIMULI'Hebrew_'$NATASK'_'$NUM_SAMPLES'.txt -o '$PATH2STIMULI'Hebrew_'$NATASK'_number_gender_V2_'$NUM_SAMPLES' -p gender_1 2 -p number_1 3 -p gender_2 4 -p number_2 5 -p gender_3 6 -p number_3 7 -p verb_1_wrong_number 8 -p verb_1_wrong_gender 9 -p verb_1_wrong_number_gender 10 -p verb_2_wrong_number 11 -p verb_2_wrong_gender 12 -p verb_2_wrong_number_gender 13 --correct-word-position '$TEST_WORD_POSITION' --wrong-word-label '$WRONG_WORD_LABEL


done


