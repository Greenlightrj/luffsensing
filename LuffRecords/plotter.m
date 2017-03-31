%A basic plotter for the luff sensor data
%makes a png of the same name
  
filename = 'luffrecord20161209_1435.csv'; %replace this with the one you want to load

A = csvread(filename, 0, 1); %cut off the timestamp because the colons won't load right
a = A(:,1);
b = A(:,2);
ratios = A(:,3);

t = []
for i = 0:length(a)-1
    t(i+1) = 1/4*i
end

clf % clear figure
hold on
title([filename(15:16), ' ', filename(17:18), ' ', filename(11:14), ' ', filename(20:21), ':', filename(22:23)])
 
p0 = plot(t, ones([1, length(a)]),'--k');
p1 = plot(t, a);
p2 = plot(t, b);
p3 = plot(t, ratios);

l = legend([p1, p2, p3],'a', 'b', 'a/b ratio');
l.Location = 'northeastoutside';
xlabel('time(seconds)')

print(filename(1:23), '-dpng')