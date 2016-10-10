% sandbox for figuring out whether the fast fourier transform will help
% with luff sensing
clear all 
filename = 'luffrecord20160629_1706.csv'; %replace this with the one you want to load

A = csvread(filename, 0, 1); %cut off the timestamp because the colons won't load right
a = A(:,1);
b = A(:,2);
ratios = A(:,3);
ratios = ratios(70:end)

Fs = 4;               % Sampling frequency (hz)
T = 1/4;              % Sampling period (sec)
L = length(ratios);      % Length of signal (data points)
t = (0:L-1)*T;        % Time vector

close all
hold on

F = fft(ratios)

plot(t, ratios)
plot(t, ifft(F))

P2 = abs(F/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

f = Fs*(0:(L/2))/L;
figure
plot(f,P1)
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (Hz)')
ylabel('|P1(f)|')

