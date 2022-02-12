function R_plaintext = AES_D(ciphertext,key_type,key_str)
IF = [14 11 13 9 ; 9 14 11 13 ; 13 9 14 11 ; 11 13 9 14 ];
IF = uint8(IF);

IIN = zeros(1,128/8);
for i = 1:128/8  
   IIN(i)=hex2dec(ciphertext((i-1)*2+1:i*2));
end

IIN = uint8(IIN);
IIN = reshape(IIN,4,4); % 轉換成4x4矩陣
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
for i = 1 : key_leng/2
    key(i)=hex2dec(key_str((i-1)*2+1:i*2)); % 10進轉16
end
key = uint8(key);

[W,IW] = key_expansion(key,Nr,Nk);
%
% Decryption
%
% 0 th round
%
IS = uint8(zeros(4,4,Nr+1));
IS(:,:,1)=bitxor(IIN,IW(:,:,1));
%
% lst =~ N th round
%
for iround=1:Nr
    %
    % InvSubBytes transformation
    %
    for ir = 1:4
        for ic = 1:4
            IS(ir,ic,iround+1) = Sbox(IS(ir,ic,iround),'I');
            
        end
    end
    %
    % InvShiftRow transformation
    %
    for ir = 2:4
        temp = IS(ir,6-ir:4,iround+1);
        IS(ir,ir:4,iround+1) = IS(ir,1:5-ir,iround+1);
        IS(ir,1:ir-1,iround+1) = temp;
    end
    %
    % InvMisColumns transformation
    %
    if iround~=Nr % !=N
        IS(:,:,iround+1)=matrix_multiplication_AES(IF,IS(:,:,iround+1));           
    end
    %
    % AddRoundKey transformation
    %
    IS(:,:,iround+1)=bitxor(IS(:,:,iround+1),IW(:,:,iround+1));
end
%
%

R_plain = IS(:,:,Nr+1);
R_plain = reshape(R_plain,1,16);
R_plaintext = char();
for i=1:16
    R_plaintext = strcat(R_plaintext,dec2hex(R_plain(i),2));
end
return