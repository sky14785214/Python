% Block Cipher Modes of Operation for AES
% ECB
clear all ;
clc ;
%
% input data
% plaintext_text = 'do not judge a book by its cover. Do not judge me from my outside.'; 
% text_mode = 'English'
plaintext_text = '說是寂寞的秋的清愁，說是遙遠的海的相思。假如有人問我的憂愁，我不敢說出你的名子。我不敢說出你的名子，假如有人問我的憂愁:說是遙遠的海的相思，說是寂寞的秋的清愁。';
text_mode = 'Chinese';
%
% key_type = 128;
% key_str = '2b7e151628aed2a6abf7158809cf4f3c';
% key_type = 192;
% key_str = '8e73b0f7da0e6452c810f32b8090791562f8ead2522c6b7b';
key_type = 256;
key_str = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4';
%
if strcmp(text_mode,'English') == 1
   plaintext_text_len = length(plaintext_text);
   plaintext = char();
   for i = 1:plaintext_text_len  %for i in 128/8
       plaintext=strcat(plaintext,hex2dec(double(plaintext_text(i)),2));
       fprintf('%s',plaintext)
   end
elseif strcmp(text_mode,'Chinese') == 1
    plaintext_text_len = length(plaintext_text);
    plaintext = char();
    for i = 1:plaintext_text_len
        plaintext = strcat(plaintext,dec2hex(double(plaintext_text(i)),4));
        fprintf('%s\n',plaintext)
    end
end

% Check plaintext

dd = 128/4;
p_leng = length(plaintext);
q = floor(p_leng/dd); % 取商
r = mod(p_leng,dd); % 取餘數
if r ~= 0 
   q = q+1;
   plaintext = strcat(plaintext,'8');
   for i = 1:dd-r-1
       plaintext = strcat(plaintext,'0');
   end
end


% encryption

%fprintf('\nKey  %s\n',key_str);
ciphertext = char();
for iq = 1:q % q=有幾個區塊
    P = plaintext((iq-1)*dd+1:iq*dd);
    c = AES_E(P,key_type,key_str); % p= 1:32, 33:64...
    % key_type = 256;
    % key_str = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4';
    %fprintf('\nBlock #%d\n',iq);
    %fprintf('\nPlaintext %s\n',P);
    %fprintf('\nCiphertext %s\n',c)
    ciphertext = strcat(ciphertext,c);
end


% decryption

%fprintf('\n\n\n');
R_plaintext = char();
for iq = 1:q
    C = ciphertext((iq-1)*dd+1:iq*dd);
    P = AES_D(C,key_type,key_str);
    %fprintf('\nBlock #%d\n',iq);
    %fprintf('\nCiphertext %s\n',C);
    %fprintf('\nPlaintext %s\n',P);
    R_plaintext = strcat(R_plaintext,P);
end
R_plaintext_leng = length(R_plaintext);
if strcmp(text_mode,'English') == 1
   R_plaintext_text = zeros(1,R_plaintext_leng/2);
   for i = 1:R_plaintext_leng/2
       chara = hex2dec(R_plaintext((i-1)*2+1:i*2));
       if chara>=32 && chara<=126
           R_plaintext_text(i) = chara;
       end
   end
elseif strcmp(text_mode,'Chinese') == 1
    R_plaintext_text = zeros(1,R_plaintext_leng/4);
    for i = 1:R_plaintext_leng/4
        chara = hex2dec(R_plaintext((i-1)*4+1:i*4));
        R_plaintext_text(i) = chara;
    end
end
R_plaintext_text = char(R_plaintext_text);

% prinf data

%fprintf('\n')
%fprintf('\nplaintext_text is: %s\n',plaintext_text);
%fprintf('\nplaintext is: %s\n',plaintext);
%fprintf('\nciphertext is: %s\n',ciphertext);
%fprintf('\nR_plaintext is: %s\n',R_plaintext);
%fprintf('\nR_plaintext_text is: %s\n',R_plaintext_text);