function out = multiplication_AES(a,b) 
f = a ;
sum = uint8(0);
for i =1:8
    if bitget(b,i)==1
        sum = bitxor(sum,f);
    end
    if bitget(f,8)==0
        f = bitshift(f,1);
    else
        f = bitxor(bitshift(f,1),uint8(27));
    end
end
out = sum ; 
return