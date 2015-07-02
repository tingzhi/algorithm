n = [0  25	30	35	40	45	50];
t = [0  0	0.01	0.17	1.97	21.92	242.360001];
figure(1);
plot(n,t);
xlabel('n (recursive algorithm)');
ylabel('Running time (s)');

x = [0  1	10	100	1000	2000	5000	10000	20000	50000].*1e6;
y = [0  0	0.03	0.28	2.78	5.56	13.89	27.809999	55.630001	139.009995];
figure(2);
plot(x,y);
xlabel('n (iterative algorithm)');
ylabel('Running time (s)');