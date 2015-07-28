clear all
format long
a = 1/3;
b = 1/6;
cvx_begin
    variables x1 x2
    maximize(a*log(x1+0.3*x2+1)+b*log(x1-0.5*x2+1)+a*log(-0.5*x1+0.3*x2+1)+b*log(-0.5*x1-0.5*x2+1))
cvx_end
x3 = 1 - x1 - x2;