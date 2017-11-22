function [PCC, PCEP] = lsf2pcc_pcep(lsf,n)
PCC = [];
PCEP = [];
P = size(lsf,2);

for i = 1 : n 
    PCC(i) = (0.5/n)*(1+((-1)^n));
    for j = 1 : P
        PCC(i) = PCC(i) + ((cos(n*lsf(j))/n);
    end
end

for i = 1 : n 
    PCEP(i) = 0;
    for j = 1 : P
        PCEP(i) = PCEP(i) + ((cos(n*lsf(j))/n);
    end
end

