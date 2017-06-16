function result = LowPass(X, frequency)
%Filters a given signal with a 16th order butterworth low pass filter.
%Returns the filtered signal in the form of a vector
%   frequency is the desired cutoff frequency in Hz
%   X is a vector representing the input signal.
    samplingRate = 4; %Hz
    Wn = frequency/samplingRate/2; %normalized cutoff frequency in pi*rad/sample
    %find transfer function coefficients
    [b,a] = butter(8,Wn,'low'); %returns transfer funcion coeffiecients
    %filter the signal
    dataOut = filter(b,a,X);
    result = dataOut;
end
