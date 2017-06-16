%the final algorithm used to detect luffing

function res = algorithmplotter()
    
filename = 'luffrecord20170331_2014.csv'; %replace this with the one you want to load

A = csvread(filename, 0, 1); %cut off the timestamp because the colons won't load right
a = A(:,1); %(1:184)
b = A(:,2);
ratios = A(:,3);
t = 0.25*(1:length(a));

clf
hold on
%p1 = plot(t, ratios,'k');
xlabel('Time (seconds)')
ylabel('Sensor ratio')
title('Luffing Detection with Two Flex Sensors')
title('Luff Sensor Data Recording')
p0 = plot(t, ones([1, length(a)]),'--k');
p1 = plot(t, a);
p2 = plot(t, b);
p3 = plot(t, ratios, 'k');
l = legend([p1, p2, p3],'stbd sensor', 'port sensor', 'ratio');

avlength =  15; % how many points are taken into consideration in the running averages

% detect is automatically filled in with 1's for luffing and 0's for none
detect = [];

runnin_variance = variance(1.18); % plot the luff detection

res = detect; % return vector of luffing detection for each reading

    function res = variance(h)
        % h is the height on y-axis where the luffing detection readout is plotted
        %text(0, h - .01, 'Variance')
        
        for i = 15:length(t)
            vars(i - 14) = var(ratios(i - 14: i)); % finding the variance of the latest 15 points
            
            if vars(i - 14) < 1.5e-4 % arbitrary parameter determined by trial and error
                plot(t(i), h, 'sb', 'MarkerFaceColor', 'blue')
                detect(i) = 0;
            else  % luffing detected
                plot(t(i), h, 'sr', 'MarkerFaceColor', 'red')
                detect(i) = 1;
            end
        end
      
        res = vars;
    end
end
