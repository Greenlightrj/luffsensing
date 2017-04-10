%A whole bunch of tests of determining tack and luffing from the flex
%sensors.

function res = algorithmplotter()
    
filename = 'luffrecord20170331_2003.csv'; %replace this with the one you want to load

A = csvread(filename, 0, 1); %cut off the timestamp because the colons won't load right
a = A(:,1);
b = A(:,2);
ratios = A(:,3);
t = 0.25*(1:length(a));

clf
hold on
p1 = plot(t, ratios,'k');
xlabel('Time (seconds)')
ylabel('Sensor ratio')
title('Luffing Detection with Two Flex Sensors')

avlength =  15; % how many points are taken into consideration in the running averages

%running_average = runningav(1.15);
%av_dist_from_av = avfromav(1.13, running_average);
runnin_variance = variance(1.15);

    function res = runningav(h)
        %input is y-height on graph to output colors

        average = filter(ones(1, avlength)/avlength, 1, ratios);
        distfromav = ratios - average;
        text(0, h - .01, 'Running Average')
        for i = 1:length(t)
    
            %determine luffing
            if abs(distfromav(i))< 0.01
                plot(t(i), h, 'sb')
            else
                plot(t(i), h, 'sr')
            end
        end
        
        res = distfromav;
    end

    function res = avfromav(h, avs)
        %input is y-height on graph to output colors and output of
        %runningav function
             
        avdistfromav = filter(ones(1, avlength)/avlength, 1, abs(avs));
        text(0, h - .01, 'Average Distance From Average')
        
        for i = 1:length(t)
            if abs(avdistfromav(i))<0.025
                plot(t(i), h, 'sb')
            else
                plot(t(i), h, 'sr')
            end
        
        end
        res = avdistfromav;
    end
    
    function res = variance(h)
        
        %text(0, h - .01, 'Variance')

        for i = 15:length(t)
            vars(i - 14) = var(ratios(i - 14: i));
            
            if vars(i - 14) < 1.5e-4
                plot(t(i), h, 'sb')
            else
                plot(t(i), h, 'sr')
            end
        end
      
        res = vars;
    end
end
