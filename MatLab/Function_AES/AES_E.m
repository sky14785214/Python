function ciphertext=AES_E(P,key_type,key_str)
F = [2 3 1 1 ; 1 2 3 1 ; 1 1 2 3 ; 3 1 1 2];
IF = [14 11 13 9 ; 9 14 11 13 ; 13 9 14 11 ; 11 13 9 14 ];
F = uint8(F);
IF = uint8(IF);
IN = zeros(1,128/8);

for i = 1:128/8  %for i in 16
   IN(i)=hex2dec(P((i-1)*2+1:i*2));
end

IN = uint8(IN);

IN = reshape(IN,4,4); % �ഫ��4x4�x�}
%

if key_type==128
    Nk = 4;
    Nr = 10;
elseif key_type==192
    Nk = 6;
    Nr = 12;
elseif key_type==256
    Nk = 8;
    Nr = 14;
end
%
key_leng = length(key_str) ;  % len(list)
key = zeros(1,key_leng/2) ; 

for i=1 : key_leng/2
    key(i)=hex2dec(key_str((i-1)*2+1:i*2)); % 10�i��16
end

key = uint8(key);
%
% key expansion
%
[W, IW] = key_expansion(key,Nr,Nk); % def ����
%
% Encryption
%
% 0 th round
%
S = uint8(zeros(4,4,Nr+1));
S(:,:,1)=bitxor(IN,W(:,:,1));
%
% lst =~ N th round
%
for iround=1:Nr
    %
    % SubBytes transformation
    %
    for ir = 1:4
        for ic = 1:4
            S(ir,ic,iround+1) = Sbox(S(ir,ic,iround),'F');
            
        end
    end
    %
    % ShiftRow transformation
    %
    for ir = 2:4
        temp = S(ir,1:ir-1,iround+1);
        S(ir,1:5-ir,iround+1)=S(ir,ir:4,iround+1);
        S(ir,6-ir:4,iround+1)=temp;
    end
    %
    % MisColumns transformation
    %
    if iround~=Nr % !=N
        S(:,:,iround+1)=matrix_multiplication_AES(F,S(:,:,iround+1));           
    end
    %
    % AddRoundKey transformation
    %
    S(:,:,iround+1)=bitxor(S(:,:,iround+1),W(:,:,iround+1));
end
%
%
Cipher = S(:,:,Nr+1);
Cipher = reshape(Cipher,1,16);
ciphertext = char();
for i=1:16
    ciphertext = strcat(ciphertext,dec2hex(Cipher(i),2));
end
%out = ciphertext;
return 