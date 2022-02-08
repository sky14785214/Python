%
% 8-bit multiplication for AES
%
function out=multiplication_AES(a,b)
base=a;
sum=uint8(0);
for i=1:8
    if bitget(b,i)==1
        sum=bitxor(sum,base);
    end
    if bitget(base,8)==0
        base=bitshift(base,1);
    else
        base=bitxor(bitshift(base,1),uint8(27));
    end    
end
out=sum;
return

