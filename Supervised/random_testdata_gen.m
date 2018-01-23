clc
clear
load('fvec.mat');
num_class=20;
[num_data,num_features]=size(fvec);
num_features=num_features-1;
class_size=num_data/num_class;
test_start=9700;
test_size=2999;

test_data1=fvec(test_start:test_start+test_size,1:num_features);
test_data2=fvec(class_size+test_start:class_size+test_start+test_size,1:num_features);
test_data3=fvec(2*class_size+test_start:2*class_size+test_start+test_size,1:num_features);
test_data4=fvec(3*class_size+test_start:3*class_size+test_start+test_size,1:num_features);
test_data5=fvec(4*class_size+test_start:4*class_size+test_start+test_size,1:num_features);

test_data6=fvec(5*class_size+test_start:5*class_size+test_start+test_size,1:num_features);
test_data7=fvec(6*class_size+test_start:6*class_size+test_start+test_size,1:num_features);
test_data8=fvec(7*class_size+test_start:7*class_size+test_start+test_size,1:num_features);
test_data9=fvec(8*class_size+test_start:8*class_size+test_start+test_size,1:num_features);
test_data10=fvec(9*class_size+test_start:9*class_size+test_start+test_size,1:num_features);

test_data11=fvec(10*class_size+test_start:10*class_size+test_start+test_size,1:num_features);
test_data12=fvec(11*class_size+test_start:11*class_size+test_start+test_size,1:num_features);
test_data13=fvec(12*class_size+test_start:12*class_size+test_start+test_size,1:num_features);
test_data14=fvec(13*class_size+test_start:13*class_size+test_start+test_size,1:num_features);
test_data15=fvec(14*class_size+test_start:14*class_size+test_start+test_size,1:num_features);

test_data16=fvec(15*class_size+test_start:15*class_size+test_start+test_size,1:num_features);
test_data17=fvec(16*class_size+test_start:16*class_size+test_start+test_size,1:num_features);
test_data18=fvec(17*class_size+test_start:17*class_size+test_start+test_size,1:num_features);
test_data19=fvec(18*class_size+test_start:18*class_size+test_start+test_size,1:num_features);
test_data20=fvec(19*class_size+test_start:19*class_size+test_start+test_size,1:num_features);

train_size=12000;
tr_data=zeros(num_class*train_size,num_features+1);

for i=1:train_size
   tr_data(20*i,:)=fvec(i,:);
   tr_data(20*i-1,:)=fvec(i+class_size,:);
   tr_data(20*i-2,:)=fvec(i+2*class_size,:);
   tr_data(20*i-3,:)=fvec(i+3*class_size,:);
   tr_data(20*i-4,:)=fvec(i+4*class_size,:);
      tr_data(20*i-5,:)=fvec(i+5*class_size,:);
   tr_data(20*i-6,:)=fvec(i+6*class_size,:);
   tr_data(20*i-7,:)=fvec(i+7*class_size,:);
   tr_data(20*i-8,:)=fvec(i+8*class_size,:);
   tr_data(20*i-9,:)=fvec(i+9*class_size,:);
      tr_data(20*i-10,:)=fvec(i+10*class_size,:);
   tr_data(20*i-11,:)=fvec(i+11*class_size,:);
   tr_data(20*i-12,:)=fvec(i+12*class_size,:);
   tr_data(20*i-13,:)=fvec(i+13*class_size,:);
   tr_data(20*i-14,:)=fvec(i+14*class_size,:);
      tr_data(20*i-15,:)=fvec(i+15*class_size,:);
   tr_data(20*i-16,:)=fvec(i+16*class_size,:);
   tr_data(20*i-17,:)=fvec(i+17*class_size,:);
   tr_data(20*i-18,:)=fvec(i+18*class_size,:);
   tr_data(20*i-19,:)=fvec(i+19*class_size,:);
end
%tr_data=cat(1,lp_both(1:15000,:),lp_both(20000:34999,:));
[model,acc]=trainClassifierkNN20(tr_data)
test_data=[];
test_data=cat(1,test_data5,test_data9(1:2000,:),test_data7(1:1500,:),test_data19(1:2250,:),test_data11(1:2400,:),test_data13(1:1800,:),test_data15(1:2500,:),test_data3(1:1000,:),test_data8(1:500,:),test_data5(1:1200,:),test_data2,test_data13(1:2000,:),test_data16(1:1500,:),test_data12(1:2250,:),test_data10(1:2400,:),test_data12(1:1800,:),test_data15(1:2500,:),test_data18(1:1000,:),test_data11(1:500,:),test_data5(1:1200,:));
X=model.predictFcn(test_data);
%X1=model.predictFcn(test_data1);
%X2=model.predictFcn(test_data2);
%X3=model.predictFcn(test_data3);
%X4=model.predictFcn(test_data4);
%X5=model.predictFcn(test_data5);
%count1=sum(X1==1)
%count2=sum(X2==2)
%count3=sum(X3==3)
%count4=sum(X4==4)
%count5=sum(X5==5)

predicted= [];
for i= 1: (size(X,1))/50;
    predicted(i) = mode(X(50*(i-1)+1:50*(i)));
end

label_size=size(X,1)/50;
window_size=11;
start_ind=1;
end_ind=label_size-window_size;
for i=start_ind:end_ind
    mid=i+(window_size-1)/2;
    left_max=mode(predicted(i:mid-1));
    right_max=mode(predicted(mid+1:i+window_size-1));
    left_count = sum(predicted(i:mid-1) == left_max);
    right_count = sum(predicted(mid+1:i+window_size-1) == right_max);
    if left_count>right_count
        predicted(mid)=left_max;
    else
        predicted(mid)=right_max;
    end
end    

predicted_final=[];
for i=1:size(predicted,2)
    predicted_final=cat(2,predicted_final,predicted(i)*ones(1,50));
end

prob=[];
for i=1:num_class
    count=sum(X(3000*(i-1)+1:3000*i,:)==i);
    prob=cat(2,prob,count/3000);
end    