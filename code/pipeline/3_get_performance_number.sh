#!/bin/bash

#for NATASK in 'nounpp' 'subjrel_that' 'objrel_that';
#for NATASK in 'embedding_mental_SR' 'objrel_that';
#for NATASK in 'nounpp' 'subjrel_that' 'subjrel_that_V1' 'objrel_that' 'objrel_that_V1' 'nounpp_copula_number';  
for NATASK in  'nounpp';  
do
    echo '-------------------------------'
    echo 'Number-agreement task: '$NATASK
    echo '-------------------------------'
    # Calculate accuracies (without ablation)
    # Calc accuracy for each condition (SS/SP/PS/PP)
    for NUMBER in 'singular' 'plural';
    do
        for ATTRACTOR in 'singular' 'plural';
        do
            echo
            eval 'python3 ../analysis/get_agreement_accuracy_for_contrast.py -ablation-results ../../output/Hebrew_'$NATASK'_number_4096.abl -info ../../data/stimuli/Hebrew_'$NATASK'_number_4096.info -condition number_1='$NUMBER' number_2='$ATTRACTOR
        done
    done
done


for NATASK in  'nounpp';  
do
    echo '-------------------------------'
    echo 'Number-agreement task: '$NATASK
    echo '-------------------------------'
    # Calculate accuracies (without ablation)
    # Calc accuracy for each condition (SS/SP/PS/PP)
    for NUMBER in 'masculine' 'feminine';
    do
        for ATTRACTOR in 'masculine' 'feminine';
        do
            echo
            eval 'python3 ../analysis/get_agreement_accuracy_for_contrast.py -ablation-results ../../output/Hebrew_'$NATASK'_gender_4096.abl -info ../../data/stimuli/Hebrew_'$NATASK'_gender_4096.info -condition gender_1='$NUMBER' gender_2='$ATTRACTOR
        done
    done
done

for NATASK in  'objrel_number_V1' 'objrel_number_V2';  
do
    echo '-------------------------------'
    echo 'Number-agreement task: '$NATASK
    echo '-------------------------------'
    # Calculate accuracies (without ablation)
    # Calc accuracy for each condition (SS/SP/PS/PP)
    for NUMBER in 'singular' 'plural';
    do
        for ATTRACTOR in 'singular' 'plural';
        do
            echo 
            eval 'python3 ../analysis/get_agreement_accuracy_for_contrast.py -ablation-results ../../output/Hebrew_'$NATASK'_4096.abl -info ../../data/stimuli/Hebrew_'$NATASK'_4096.info -condition number_1='$NUMBER' number_2='$ATTRACTOR
        done
    done
done


for NATASK in  'objrel_gender_V1' 'objrel_gender_V2';  
do
    echo '-------------------------------'
    echo 'Number-agreement task: '$NATASK
    echo '-------------------------------'
    # Calculate accuracies (without ablation)
    # Calc accuracy for each condition (SS/SP/PS/PP)
    for NUMBER in 'masculine' 'feminine';
    do
        for ATTRACTOR in 'masculine' 'feminine';
        do
            echo
            eval 'python3 ../analysis/get_agreement_accuracy_for_contrast.py -ablation-results ../../output/Hebrew_'$NATASK'_4096.abl -info ../../data/stimuli/Hebrew_'$NATASK'_4096.info -condition gender_1='$NUMBER' gender_2='$ATTRACTOR
        done
    done
done
