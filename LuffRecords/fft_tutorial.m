
Fs = 1000;            % Sampling frequency (hz)
T = 1/Fs;             % Sampling period (sec)
L = 1000;             % Length of signal (data points)
t = (0:L-1)*T;        % Time vector

S = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t); %Form a signal containing a 50 Hz sinusoid of amplitude 0.7 and a 120 Hz sinusoid of amplitude 1.

X = S + 2*randn(size(t)); %Corrupt the signal with zero-mean white noise with a variance of 4.

clf
hold on
plot(1000*t(1:100),X(1:100))
plot(1000*t(1:100),S(1:100))
title('Signal Corrupted with Zero-Mean Random Noise')
xlabel('t (milliseconds)')
ylabel('X(t)')

Y = fft(X);
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

f = Fs*(0:(L/2))/L;
figure
plot(f,P1)
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (Hz)')
ylabel('|P1(f)|')

