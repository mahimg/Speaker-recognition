[a1,Fs4] = audioread('vinod (1).wav');
a1=a1(1:2400000,1);
a_speech=(vad('vinod (1).wav'))';
a2=[];

for i=1:size(a_speech,2)
    
   if a_speech(i)==1
       a2=cat(1,a2,a1(80*(i-1)+1:80*i));
   end
    
end    

a=a2(:);
lpc2lsf = dsp.LPCToLSF;
lp_coeff=[];
lp_res=[];
pitch=[];
formants=[];
formants_mag=[];

lp_ceps=[];


LSF=[];
pcc=[];
pcep=[];


for i=1:120:size(a)-159


a_temp=a(i:i+159);
n=160;
w=window(@hamming,n);
a_temp=a_temp.*w;
P=10;


acorr=autocorr(a_temp',159);
acorr=acorr./(abs(max(acorr)));

%figure(1);
%plot(a_temp);
%figure(2);
%plot(acorr);


A=acorr(1:P);
r=acorr(2:(P+1));
A=toeplitz(A);
L=-1*inv(A)*r';

L=L';

lp_coeff=cat(1,lp_coeff,L);

res=conv(a_temp,L);
lp_res=cat(2,lp_res,res);

res_2=res(5:164);
res_3=autocorr(res_2,159);

res_3=acorr./(abs(max(res_3)));

min_pitch=20;
max_pitch=160;

pitch_temp=res_3(min_pitch:max_pitch);

[p_val,p_loc]=max(pitch_temp);

pitch_period=min_pitch+ p_loc;

pitch_freq=(1/pitch_period)*8000;


pitch=cat(1,pitch,pitch_freq);


f=abs(fft(L,8000));
f=f.^(-1);
f=log10(f)*20;
f=f(1:4000);

k=1;

        for   j=2:3999
    
        if f(j)>f(j-1) & f(j)>f(j+1)
           
            formant(k)=j;
            formant_mag(k)=f(j);
            k=k+1;
        end
            
        end
    
  formant=cat(2,formant,zeros(1,3));
  formant_mag=cat(2,formant_mag,zeros(1,3));
  formants=cat(1,formants,formant(1:3));    
  formants_mag=cat(1,formants_mag,formant_mag(1:3));    
      
  
  lp_ceps=cat(1,lp_ceps,lpcc(L,20));
  
   LSF_temp = step(lpc2lsf,L');
   LSF_temp= LSF_temp';
  
  
  LSF=cat(1,LSF,LSF_temp);
  
  [pcc_temp pcep_temp]=lsf2pcc_pcep(LSF_temp,10);
  
  
  pcc=cat(1,pcc,pcc_temp);
  pcep=cat(1,pcep,pcep_temp);
          
end

each_fvector=[];
each_fvector=cat(2,each_fvector,lp_coeff);
each_fvector=cat(2,each_fvector,lp_ceps);
each_fvector=cat(2,each_fvector,LSF);
each_fvector=cat(2,each_fvector,pitch);
each_fvector=cat(2,each_fvector,formants_mag);
each_fvector=cat(2,each_fvector,pcc);
each_fvector=cat(2,each_fvector,pcep);
each_fvector=cat(2,each_fvector,7*ones(size(each_fvector,1),1));