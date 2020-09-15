%
% AES
%
clear all;
clc;
%
% establish 4x4 matrices for MixColumns and InvMixColumns transdormations
%
F = [2 3 1 1 ; 1 2 3 1 ; 1 1 2 3 ; 3 1 1 2];
IF = [14 11 13 9 ; 9 14 11 13 ; 13 9 14 11 ; 11 13 9 14 ];
F= uint8(F);
IF = uint8(IF);

%
% input plaintext ,key type and key string
%
plaintext = '00112233445566778899aabbccddeeff';
key_type = 256;
% key_str = '2b7e151628aed2a6abf7158809cf4f3c';
% key_str='8e73b0f7da0e6452c810f32b8090791562f8ead2522c6b7b';
key_str='603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4';

%
IN = zeros(1,128/8);
for i = 1:128/8  %for i in 128/8
   IN(i)=hex2dec(plaintext((i-1)*2+1:i*2));
end
IN = uint8(IN);
IN = reshape(IN,4,4); % 轉換成4x4矩陣
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
    key(i)=hex2dec(key_str((i-1)*2+1:i*2)); % 10進轉16
end
key = uint8(key);
%
% key expansion
%
[W, IW] = key_expansion(key,Nr,Nk); % def 概念
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
%%% 0826

%
% Decryption
%
% 0 th round
%
IS = uint8(zeros(4,4,Nr+1));
Cipher = reshape(Cipher,4,4);
IS(:,:,1)=bitxor(Cipher,IW(:,:,1));
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
    % InvAddRoundKey transformation
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
%

%
% prinr data
%
fprintf('\nplaintext is: %s\n',plaintext);
fprintf('\nciphertext is: %s\n ',ciphertext);
fprintf('\nR_plintext is: %s\n ',R_plaintext);
       