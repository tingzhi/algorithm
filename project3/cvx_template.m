clear all
format long
a = 1/3;
b = 1/6;
cvx_begin
    variables x1 x2 x3
    maximize(a*log(2*x1+1.3*x2+x3)+b*log(2*x1+0.5*x2+x3)+a*log(0.5*x1+1.3*x2+x3)+b*log(0.5*x1+0.5*x2+x3))
    subject to
    x1 + x2 + x3 == 1;
cvx_end