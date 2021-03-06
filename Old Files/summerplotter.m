%A whole bunch of tests of determining tack and luffing from the flex
%sensors.

%the top 4 bars are 
    %tack determined from ratio between sensors
    %tack determined from running average of ratio
    
    %luffing determined by difference of ratio from running average
    %luffing determined by average of diff between ratio and avg ratio
    
filename = 'luffrecord20161025_2222.csv' %replace this with the one you want to load
%pythfile = 'verif.csv' %this is the test of whether 

A = csvread(filename, 0, 1) %cut off the timestamp because the colons won't load right
a = A(:,1);
b = A(:,2);
ratios = A(:,3);

%load python data to compare it to matlab conclusions
% pyth = csvread(pythfile);
% ptack = pyth(:,1);
% pluff = pyth(:,2);

%determine luffing by seeing how far the points are from a running average

avlength =  15; % how many points are taken into consideration in the running average
average = filter(ones(1, avlength)/avlength, 1, ratios);
distfromav = ratios - average;
avdistfromav = filter(ones(1, avlength)/avlength, 1, abs(distfromav));

hold on

for i = 1:length(a)
    
    %create seconds timescale for plotting
    t(i) = 0.25*i;
    
    %determine tack based on ratio
    if ratios(i)<1
        %plot(t(i), 1.5, 'sg')
    else
        %plot(t(i), 1.5, 'sr')
    end
    
    %determine tack based on running average
    if average(i)<1
        %plot(t(i), 1.4, 'sg')
    else
        %plot(t(i), 1.4, 'sr')
    end
    
    %determine luffing
    if abs(distfromav(i))< 0.01
        plot(t(i), 1.15, 'sb')
    else
        plot(t(i), 1.15, 'sr')
    end
    
    if abs(avdistfromav(i))<0.025
        %plot(t(i), 1.15, 'sb')
    else
        %plot(t(i), 1.15, 'sr')
    end
end

%p1 = plot(t, a);
%p2 = plot(t, b);
p3 = plot(t, ratios,'k');
%p4 = plot(t, average);
%p5 = plot(t(1:length(distfromav)), distfromav);
%p6 = plot(t(1:length(avdistfromav)), avdistfromav);
%p7 = plot(t, zeros(1, length(t)));

%checking python script agreement
%plot(t, ptack, 'r')
%plot(t, pluff, 'k')

%l = legend([p1, p2, p3, p4, p5, p6],'a', 'b', 'a/b ratio', 'running average of ratio', 'distance from running average', 'average distance from running average');
%l.Location = 'northeastoutside';
xlabel('time(seconds)')
ylabel('sensor ratio')
title('Luffing Detection with Two Flex Sensors')
