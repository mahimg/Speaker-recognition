function rm_silence=vad(filename)
audioSource = dsp.AudioFileReader('SamplesPerFrame',80,...
                               'Filename',filename,...
                               'OutputDataType', 'single');
% Note: You can use a microphone as a source instead by using an audio
% device reader (NOTE: audioDeviceReader requires an Audio System Toolbox
% (TM) license)
% audioSource = audioDeviceReader('OutputDataType', 'single', ...
%                              'NumChannels', 1, ...
%                              'SamplesPerFrame', 80, ...
%                              'SampleRate', 8000);
% Create a time scope to visualize the VAD decision (channel 1) and the
% speech data (channel 2)
scope = dsp.TimeScope(2, 'SampleRate', [8000/80 8000], ...
                      'BufferLength', 80000, ...
                      'YLimits', [-0.3 1.1], ...
                      'ShowGrid', true, ...
                      'Title','Decision speech and speech data', ...
                      'TimeSpanOverrunAction','Scroll');
                  
                  
 VAD_cst_param = vadInitCstParams;
clear vadG729
% Run for 10 seconds
numTSteps = 30000;                              %%%%change rate
temp=[];
aud=[];
while(numTSteps)
  % Retrieve 10 ms of speech data from the audio recorder
  speech = step(audioSource);
  speech=speech(:,1);
  % Call the VAD algorithm
  decision = vadG729(speech, VAD_cst_param);
  temp=cat(1,temp,decision);
  % Plot speech frame and decision: 1 for speech, 0 for silence
 %scope(decision, step(speech,10));
 
 %t=cat(2,speech,decision+zeros(80,1));
 %aud=cat(1,aud,t);
  numTSteps = numTSteps - 1;
end
%release(scope); 
rm_silence=temp;
end