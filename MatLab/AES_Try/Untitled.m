clc
F = [2 3 1 1 ; 1 2 3 1 ; 1 1 2 3 ; 3 1 1 2];
IF = [14 11 13 9 ; 9 14 11 13 ; 13 9 14 11 ; 11 13 9 14 ];
F = uint8(F);
IF = uint8(IF);

plaintext = '00112233445566778899aabbccddeeff';
key_type = 128;
key_str = '2b7e151628aed2a6abf7158809cf4f3c';

IN = zeros(1,128/8);
for i = 1:128/8 
   IN(i)=hex2dec(plaintext((i-1)*2+1:i*2));
end

IN = uint8(IN);

IN = reshape(IN,4,4); 

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

key_leng = length(key_str) ;  
key = zeros(1,key_leng/2) ; 

for i=1 : key_leng/2
    key(i)=hex2dec(key_str((i-1)*2+1:i*2)); 
end

key = uint8(key);

[W, IW] = key_expansion(key,Nr,Nk); 
S = uint8(zeros(4,4,Nr+1));
S(:,:,1)=bitxor(IN,W(:,:,1));

for iround=1:Nr
    for row = 1:4
        for cln = 1:4
            S(row,cln,iround+1) = Sbox(S(row,cln,iround),'F');
        end
    end

    for row = 2:4
        i = S(row,1:row-1,iround+1);
        S(row,1:5-row,iround+1)=S(row,row:4,iround+1);
        S(row,6-row:4,iround+1)=i;
    end
   
    if iround~=Nr 
        S(:,:,iround+1)=matrix_multiplication_AES(F,S(:,:,iround+1));           
    end
    S(:,:,iround+1)=bitxor(S(:,:,iround+1),W(:,:,iround+1));
end

Cipher = S(:,:,Nr+1);
Cipher = reshape(Cipher,1,16);
ciphertext = char();
for i=1:16
    ciphertext = strcat(ciphertext,dec2hex(Cipher(i),2));
end

% ��
IS = uint8(zeros(4,4,Nr+1));
Cipher = reshape(Cipher,4,4);
IS(:,:,1) = bitxor(Cipher,IW(:,:,1));

for iround = 1:Nr
    for row = 1:4
        for cln = 1:4
            IS(row,cln,iround+1) = Sbox(IS(row,cln,iround),'I');
        end
    end
    
    for row = 2:4
        i = IS(row,6-row,iround+1);
        IS(row,row:4,iround+1) = IS(row,1:5-row,iround+1);
        IS(row,1:row-1,iround+1) = i;
    end     
   
    if iround ~= Nr
        IS(:,:,iround+1) = matrix_multiplication_AES(IF,IS(:,:,iround+1));
    end
    IS(:,:,iround+1) = bitxor(IS(:,:,iround+1),IW(:,:,iround+1))
end

r_plain = IS(:,:,Nr+1);
r_plain = reshape(r_plain,1,16);
r_plaintext = char();
for i=1:16
    r_plaintext = strcat(r_plaintext,dec2hex(r_plain(i),2));
end

fprintf('\nplaintext is: %s\n',plaintext);
fprintf('\nciphertext is: %s\n ',ciphertext);
fprintf('\nR_plintext is: %s\n ',r_plaintext);