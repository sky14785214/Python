function out = matrix_multiplication_AES(A,B)
 c  = uint8(zeros(4,4));
 for row = 1:4
    for cln = 1:4
         i = uint8(0);
         for  im = 1:4
             s = multiplication_AES(A(row,im),B(im,cln));
             i = bitxor(i,s);
         end
    c(row,cln) = i;
    end
 end
 out = c ;
return