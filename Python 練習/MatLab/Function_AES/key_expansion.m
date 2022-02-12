%
% Key expansions for encryption (W) and decryption (IW)
%
function [W,IW]=key_expansion(key,Nr,Nk)
%
% establish 4X4 matrice for InvMixColumns transformation
%
IF=[14 11 13 9; 9 14 11 13; 13 9 14 11; 11 13 9 14];
IF=uint8(IF);
%
%
key=reshape(key,4,Nk);

%
% key expansion
%
Rcon=uint8([1;0;0;0]);

for ikey=Nk:4*(Nr+1)-1 %  ikey = 8:59
    temp=key(:,ikey);
    if mod(ikey,Nk)==0  
        temp_1=temp(1);
        temp(1:3)=temp(2:4);
        temp(4)=temp_1;
        for is=1:4
            temp(is)=Sbox(temp(is),'F');            
        end
        temp=bitxor(temp,Rcon);
        
        if bitget(Rcon(1),8)==0
            Rcon(1)=bitshift(Rcon(1),1);
        else
            Rcon(1)=bitxor(bitshift(Rcon(1),1),uint8(27));
        end
    end
    key(:,ikey+1)=bitxor(temp,key(:,ikey-Nk+1));    
end

%
%
W=uint8(zeros(4,4,Nr+1));
for i=0:Nr
    W(:,:,i+1)=key(:,4*i+1:4*(i+1));   
end
%
% inverse key
%
IW=uint8(zeros(4,4,Nr+1));
IW(:,:,1)=W(:,:,Nr+1);
IW(:,:,Nr+1)=W(:,:,1);
for ikey=2:Nr
    IW(:,:,ikey) = matrix_multiplication_AES(IF,W(:,:,Nr+2-ikey));

end
return
    
    