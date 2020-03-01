% -------------------------------------
% Doubly nested long-range dependencies
% -------------------------------------
clear; close all; clc    
debug_mode = 0;
 
if debug_mode
    dbstop if error  
    training = 1;
else
    training = questdlg('Do yo u want to include a training block?','Training block','Yes','No','Yes');
    if training(1) == 'Y', training = 1; else training = 0; end
end

%% TEXTs
text_instruct = 'Buongiorno e grazie per aver deciso di prendere parte a questo studio. \n Nel corso dell''esperimento ti saranno presentate delle frasi \n che possono contenere delle violazioni da un punto di vista grammaticale o del significato.\n Le frasi ti saranno presentate utilizzando una modalità di presentazione visiva seriale rapida, \n ovvero utilizzando una serie di schermate di durata molto breve, ognuna contenente solo una parte della frase. \n Rispondi nel modo più accurato e veloce possibile non appena ti accorgi della violazione premendo il tasto M. \n La frase non si interromperà dopo che avrai premuto il tasto, non ti preoccupare, la tua risposta sarà comunque registrata. \n Alla fine di ogni frase ti verrà presentata una schermata contenente le parole corretto o scorretto “?”, \n ti chiediamo di premere il tasto “M” nel caso in cui ci sia stata una violazione \n o il tasto “Z” nel caso in cui la frase sia accettabile. \n Ti chiediamo di rispondere anche se hai già premuto il tasto M durante la presentazione della frase. \n Durante tutto l''esperimento riceverai un feedback sulle tue risposte. \n Ti chiediamo di essere il più accurato e veloce possibile. \n Premi la barra spaziatrice per continuare';
text_training = 'Si svolgerà adesso una breve prova dell''esperimento. \n Premi la barra spaziatrice quando sei pronto per cominciare.';
text_before_block{1} = 'La fase di prova è finita. \n Inizierà ora l''esperimento vero e proprio. \n A metà dell''esperimento ci sarà una pausa di qualche minuto. \n Premi la barra spaziatrice quando sei pronto per cominciare.' ;
text_before_block{2} = 'Come nella prima parte dell''esperimento ti saranno presentate delle frasi che possono contenere delle violazioni da un punto di vista grammaticale o del significato. \n Rispondi nel modo più accurato e veloce possibile non appena ti accorgi della violazione premendo il tasto M. \n Alla fine di ogni frase ti verrà presentata una schermata contenente le parole corretto o scorretto “?”, \n ti chiediamo di premere il tasto “M” nel caso in cui ci sia stata una violazione o il tasto “Z” nel caso in cui la frase sia accettabile. Ti chiediamo di rispondere anche se hai già premuto il tasto M durante la presentazione della frase.\n Durante tutto l''esperimento riceverai un feedback sulle tue risposte.\n Ti chiediamo di essere il più accurato e veloce possibile.\n Premi la barra spaziatrice per iniziare.';
text_after_block{1} = 'La prima parte dell''esperimento è finita, \n ci sarà ora una pausa di qualche minuto. \n Ti chiediamo di aspettare un attimo prima di alzarti, \n in modo che anche il tuo collega possa completare la prima parte';
text_after_block{2} = 'L''esperimento è finito, ti ringraziamo per la partecipazione. \n Ti chiediamo di restare seduto in modo che anche il tuo collega possa concludere l''esperimento.\n Lo sperimentatore vi darà tutte le informazioni riguardanti lo studio e risponderà alle vostre domande.';

%% INITIALIZATION
addpath('functions')
KbName('UnifyKeyNames')
params = getParamsLocalGlobalParadigm(debug_mode);
fid_log = createLogFile(params, false); % OPEN LOG 
handles = Initialize_PTB_devices(params, debug_mode); % Open screens 

%% LOAD STIMULI 
[sentences_per_block, training_sentences] = load_stimuli(params);     

%% START EXPERIMENT
 try  
    %%%%%%% INSTRUCTIONS (WAIT FOR STROKE KEY PRESS)
%     present_intro_slide(params, handles);
    DrawFormattedText(handles.win, text_instruct, 'center', 'center', handles.white);
    Screen('Flip',handles.win);
    KbStrokeWait;
    
    %%%%%%% GRAND START
    KbQueueStart;
    log_str = createLogString('GrandStart', 0, 0, 0, 0, ' ', GetSecs);
    fprintf(fid_log,log_str); % WRITE-TO-LOG 
     
    %%%%%% TRAINING   alj
    if training 
         %%%%%%% LOOP OVER TRAINING STIMULI
         DrawFormattedText(handles.win, text_training, 'center', 'center', handles.white);
         Screen('Flip',handles.win);
         wait_for_key_press()
         fid_log_train = createLogFile(params, true); % OPEN LOG 
         run_visual_block(handles, 0, training_sentences, fid_log_train, 0, params); 
    end
    cumTrial=0;
    
    
    %%%%%%%% START EXPERIMENT
    for block = 1 :params.n_blocks
        %%%%%% TEXT BEFORE BLOCK STARTS
        DrawFormattedText(handles.win, text_before_block{block}, 'center', 'center', handles.white);
        Screen('Flip',handles.win);
        wait_for_key_press()
        %%%%%%% PRESENT A LONG FIXATION ONLY AT THE BEGINING
        DrawFormattedText(handles.win, '+', 'center', 'center', handles.white);
        Screen('Flip', handles.win);
        WaitSecs(1.5); %Wait before experiment start
        %%%%%%% START EXPERIMENT
        run_visual_block(handles, block, sentences_per_block{block}, fid_log, cumTrial, params);   
        %%%%%%% TEXT AFTER BLOCK ENDS
        DrawFormattedText(handles.win, text_after_block{block}, 'center', 'center', handles.white);
        Screen('Flip',handles.win);
        wait_for_key_press()
    end 
    
catch
    sca
    psychrethrow(psychlasterror);
    KbQueueRelease;
    fprintf('Error occured\n')
end

%% %%%%%%% CLOSE ALL - END EXPERIMENT
fprintf('Done\n')
KbQueueRelease;
sca