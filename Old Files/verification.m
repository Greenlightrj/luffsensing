% comparing qualitative luff data to the sensor readout
% Remember:
% change algorithmplotter to take filename as input.
% first 3.5 seconds not evaluated

%% Video 16
a16 = algorithmplotter('luffrecord20170331_2047.csv');
b16 = [ones((13 - 3.5)*4,1);
    zeros((45 - 13)*4, 1);
    ones((46 - 45)*4, 1);
    zeros((14)*4, 1);
    ];

diff1 = sum(abs(a16.' - b16(1:length(a16)))) %number of differing points
len1 = length(a16)
frac1 = 1- diff1/len1 % percentage agreement

%% Video 9

a9 = algorithmplotter('luffrecord20170331_2003.csv');
b9 = [zeros((22 - 3.5)*4, 1);
    ones((60 - 22)*4,1);
    zeros((77 - 60)*4, 1);
    ones((46 - 77)*4, 1);
    zeros((14)*4, 1);
    ];

diff1 = sum(abs(a9.' - b9(1:length(a9)))) %number of differing points
len1 = length(a9)
frac1 = 1- diff1/len1 % percentage agreement
%% Video 10

a9 = algorithmplotter('luffrecord20170331_2047.csv');
b9 = [ones((13 - 3.5)*4,1);
    zeros((45 - 13)*4, 1);
    ones((46 - 45)*4, 1);
    zeros((14)*4, 1);
    ];

diff1 = sum(abs(a9.' - b9(1:length(a9)))) %number of differing points
len1 = length(a9)
frac1 = 1- diff1/len1 % percentage agreement
%% Video 11

a9 = algorithmplotter('luffrecord20170331_2047.csv');
b9 = [ones((13 - 3.5)*4,1);
    zeros((45 - 13)*4, 1);
    ones((46 - 45)*4, 1);
    zeros((14)*4, 1);
    ];

diff1 = sum(abs(a9.' - b9(1:length(a9)))) %number of differing points
len1 = length(a9)
frac1 = 1- diff1/len1 % percentage agreement
