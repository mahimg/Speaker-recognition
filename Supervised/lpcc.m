function C=lpcc(lpc,n)
C= [];
P=size(lpc,2);
C(1) = log(P);
C(2) = lpc(1,1);
for k = 2 : n
    if (2 <= k) & (k <= P)
        C(k+1) = lpc(1,k);
        for l = 1 : k-1
            C(k+1) = C(k+1) +((l/k)*C(l+1)*lpc(1,k-l));
        end
    end
    if (P < k) & (k < n)
        C(k+1) = 0;
        for l = (k-P) : (k-1)
            C(k+1) = C(k+1) + ((l/k)*C(l+1)*lpc(1,k-l));
        end
    end
end
end

