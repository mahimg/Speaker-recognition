[a1,Fs4] = audioread('vinod (1).wav');

[b1,Fs4] = audioread('bandi (2).wav');

[c1,Fs4] = audioread('A_Brief_Overview_of_the_Course-W_Qk4RCG-cU.wav');


[d1,Fs4] = audioread('Film_Appreciation_2015_-_Lecture_1_-_Introduction-.wav');

[e1,Fs4]= audioread('INTRODUCTION-1MkWjVjNFhY.wav');


a1=a1(:,1);
b1=b1(:,1);
c1=c1(:,1);
d1=d1(:,1);
e1=e1(:,1);

a_speech=(vad('vinod (1).wav'))';
b_speech=(vad('bandi (2).wav'))';
c_speech=(vad('A_Brief_Overview_of_the_Course-W_Qk4RCG-cU.wav'))';
d_speech=(vad('Film_Appreciation_2015_-_Lecture_1_-_Introduction-.wav'))';
e_speech=(vad('INTRODUCTION-1MkWjVjNFhY.wav'))';


a2=[];
b2=[];
c2=[];
d2=[];
e2=[];


for i=1:size(a_speech,2)
    
   if a_speech(i)==1
       a2=cat(1,a2,a1(80*(i-1)+1:80*i));
   end
    
end    



for i=1:size(b_speech,2)
    
   if b_speech(i)==1
       b2=cat(1,b2,b1(80*(i-1)+1:80*i));
   end
end



for i=1:size(c_speech,2)
    
   if c_speech(i)==1
       c2=cat(1,c2,c1(80*(i-1)+1:80*i));
   end
end    



for i=1:size(d_speech,2)
    
   if d_speech(i)==1
       d2=cat(1,d2,d1(80*(i-1)+1:80*i));
   end
end    


for i=1:size(e_speech,2)
    
   if e_speech(i)==1
       e2=cat(1,e2,e1(80*(i-1)+1:80*i));
   end
end   


[f1,Fs4] = audioread('Lec_1_The_body_of_music-deoGlrnj8os.wav');

[g1,Fs4] = audioread('Lecture_01-_nW17thCk_8.wav');

[h1,Fs4] = audioread('Mod-_1_Lec-1_Introduction_to_Hydraulics-z9wsUWaN-o.wav');


[i1,Fs4] = audioread('Mod-01_Lec-01_Basic_definitions-nfMO7_hwYuE.wav');

[j1,Fs4]= audioread('Mod-01_Lec-01_Course_Overview-iFqs-qrJgeo.wav');


f1=f1(:,1);
g1=g1(:,1);
h1=h1(:,1);
i1=i1(:,1);
j1=j1(:,1);

f_speech=(vad('Lec_1_The_body_of_music-deoGlrnj8os.wav'))';
g_speech=(vad('Lecture_01-_nW17thCk_8.wav'))';
h_speech=(vad('Mod-_1_Lec-1_Introduction_to_Hydraulics-z9wsUWaN-o.wav'))';
i_speech=(vad('Mod-01_Lec-01_Basic_definitions-nfMO7_hwYuE.wav'))';
j_speech=(vad('Mod-01_Lec-01_Course_Overview-iFqs-qrJgeo.wav'))';


f2=[];
g2=[];
h2=[];
i2=[];
j2=[];


for i=1:size(f_speech,2)
    
   if f_speech(i)==1
       f2=cat(1,f2,f1(80*(i-1)+1:80*i));
   end
    
end    



for i=1:size(g_speech,2)
    
   if g_speech(i)==1
       g2=cat(1,g2,g1(80*(i-1)+1:80*i));
   end
end



for i=1:size(h_speech,2)
    
   if h_speech(i)==1
       h2=cat(1,h2,h1(80*(i-1)+1:80*i));
   end
end    



for i=1:size(i_speech,2)
    
   if i_speech(i)==1
       i2=cat(1,i2,i1(80*(i-1)+1:80*i));
   end
end    


for i=1:size(j_speech,2)
    
   if j_speech(i)==1
       j2=cat(1,j2,j1(80*(i-1)+1:80*i));
   end
end   

[k1,Fs4] = audioread('Mod-01_Lec-01_Intro_sound_wave_versus_vibration_di.wav');

[l1,Fs4] = audioread('Mod-01_Lec-01_Introduction_to_Digital_VLSI_Design_.wav');

[m1,Fs4] = audioread('Mod-01_Lec-01_Introduction_to_Nanomaterials-qUEbxT.wav');


[n1,Fs4] = audioread('Mod-01_Lec-01_Lecture-01-Introduction_to_Gas_Dynam.wav');

[o1,Fs4]= audioread('Mod-01_Lec-01_Properties_of_the_Image_of_an_Analyt.wav');


k1=k1(:,1);
l1=l1(:,1);
m1=m1(:,1);
n1=n1(:,1);
o1=o1(:,1);

k_speech=(vad('Mod-01_Lec-01_Intro_sound_wave_versus_vibration_di.wav'))';
l_speech=(vad('Mod-01_Lec-01_Introduction_to_Digital_VLSI_Design_.wav'))';
m_speech=(vad('Mod-01_Lec-01_Introduction_to_Nanomaterials-qUEbxT.wav'))';
n_speech=(vad('Mod-01_Lec-01_Lecture-01-Introduction_to_Gas_Dynam.wav'))';
o_speech=(vad('Mod-01_Lec-01_Properties_of_the_Image_of_an_Analyt.wav'))';


k2=[];
l2=[];
m2=[];
n2=[];
o2=[];


for i=1:size(k_speech,2)
    
   if k_speech(i)==1
       k2=cat(1,k2,k1(80*(i-1)+1:80*i));
   end
    
end    



for i=1:size(l_speech,2)
    
   if l_speech(i)==1
       l2=cat(1,l2,b1(80*(i-1)+1:80*i));
   end
end



for i=1:size(m_speech,2)
    
   if m_speech(i)==1
       m2=cat(1,m2,m1(80*(i-1)+1:80*i));
   end
end    



for i=1:size(n_speech,2)
    
   if n_speech(i)==1
       n2=cat(1,n2,n1(80*(i-1)+1:80*i));
   end
end    


for i=1:size(o_speech,2)
    
   if o_speech(i)==1
       o2=cat(1,o2,o1(80*(i-1)+1:80*i));
   end
end   

[p1,Fs4] = audioread('Mod-01_Lec-01_Review_of_Basic_Structural_Analysis_.wav');

[q1,Fs4] = audioread('Mod-01_Lec-01_Understanding_Cultural_Studies_Part_.wav');

[r1,Fs4] = audioread('Mod-1_Lec-1_Overview_of_the_Course_Practical_and_R.wav');


[s1,Fs4] = audioread('Module_-_1_Lecture_-_1_Semiconductor_materials-xhn.wav');

[t1,Fs4]= audioread('Module_One_-_Lecture_01_-_What_is_Reading_Comprehe.wav');


p1=p1(:,1);
q1=q1(:,1);
r1=r1(:,1);
s1=s1(:,1);
t1=t1(:,1);

p_speech=(vad('Mod-01_Lec-01_Review_of_Basic_Structural_Analysis_.wav'))';
q_speech=(vad('Mod-01_Lec-01_Understanding_Cultural_Studies_Part_.wav'))';
r_speech=(vad('Mod-1_Lec-1_Overview_of_the_Course_Practical_and_R.wav'))';
s_speech=(vad('Module_-_1_Lecture_-_1_Semiconductor_materials-xhn.wav'))';
t_speech=(vad('Module_One_-_Lecture_01_-_What_is_Reading_Comprehe.wav'))';


p2=[];
q2=[];
r2=[];
s2=[];
t2=[];


for i=1:size(p_speech,2)
    
   if p_speech(i)==1
       p2=cat(1,p2,p1(80*(i-1)+1:80*i));
   end
    
end    



for i=1:size(q_speech,2)
    
   if q_speech(i)==1
       q2=cat(1,q2,q1(80*(i-1)+1:80*i));
   end
end



for i=1:size(r_speech,2)
    
   if r_speech(i)==1
       r2=cat(1,r2,r1(80*(i-1)+1:80*i));
   end
end    



for i=1:size(s_speech,2)
    
   if s_speech(i)==1
       s2=cat(1,s2,s1(80*(i-1)+1:80*i));
   end
end    


for i=1:size(t_speech,2)
    
   if t_speech(i)==1
       t2=cat(1,t2,t1(80*(i-1)+1:80*i));
   end
end   

%%Taking min value of a % b
min_t= min([size(a2,1),size(b2,1),size(c2,1),size(d2,1),size(e2,1),size(f2,1),size(g2,1),size(h2,1),size(i2,1),size(j2,1),size(k2,1),size(l2,1),size(m2,1),size(n2,1),size(o2,1),size(p2,1),size(q2,1),size(r2,1),size(s2,1),size(t2,1)]);
A=a2(1:min_t);
B=b2(1:min_t);
C=c2(1:min_t);
D=d2(1:min_t);
E=e2(1:min_t);

F=f2(1:min_t);
G=g2(1:min_t);
H=h2(1:min_t);
I=i2(1:min_t);
J=j2(1:min_t);

K=k2(1:min_t);
L=l2(1:min_t);
M=m2(1:min_t);
N=n2(1:min_t);
O=o2(1:min_t);

P=p2(1:min_t);
Q=q2(1:min_t);
R=r2(1:min_t);
S=s2(1:min_t);
T=t2(1:min_t);

final1_20=[E',I(1:2*min_t/3)',G(1:min_t/2)',S(1:3*min_t/4)',K(1:4*min_t/5)',M(1:3*min_t/5)',O(1:5*min_t/6)',C(1:min_t/3)',H(1:min_t/6)',E(1:2*min_t/5)',B',M(1:2*min_t/3)',P(1:min_t/2)',L(1:3*min_t/4)',J(1:4*min_t/5)',M(1:3*min_t/5)',O(1:5*min_t/6)',R(1:min_t/3)',K(1:min_t/6)',E(1:2*min_t/5)'];