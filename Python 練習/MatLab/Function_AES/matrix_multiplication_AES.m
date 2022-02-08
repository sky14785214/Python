%
% matris multiplication for AES
%
function out = matrix_multiplication_AES(A,B)
C = uint8(zeros(4,4));
for ir = 1:4
    for ic = 1:4
        temp_sum = uint8(0);
        for im = 1:4
            temp = multiplication_AES(A(ir,im),B(im,ic));
            temp_sum = bitxor(temp_sum,temp);
            
        end 
    C(ir,ic) = temp_sum;
    end
end

out = C;
return