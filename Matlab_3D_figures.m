% KIERROS 5: 3D - KUVAAJANPIIRTO
% ROUND 5: 3D Figures

fig = figure(1);
hold all

x = linspace(-2,2);
y = linspace(-2,2);
z = @(x,y) -(x.^2+2.*y.^2).*exp(1-x.^2-y.^2);
[X,Y] = meshgrid(-2:0.16:2);
Z = -(X.^2+2.*Y.^2).*exp(1-X.^2-Y.^2);

subplot(3,2,1);
figure(fig);
mesh(X,Y,Z);
title('Mesh');
xlabel('X');
ylabel('Y');
zlabel('Z');
xticks(-2:1:2);
yticks(-2:2:2);
zticks(-2:0.5:0);

subplot(3,2,2);
figure(fig);
surf(X,Y,Z);
title('Surf');
xlabel('X');
ylabel('Y');
zlabel('Z');
xticks(-2:1:2);
yticks(-2:2:2);
zticks(-2:0.5:0);

subplot(3,2,3);
figure(fig);
plot3(X,Y,Z,'.');
title('Plot3');
xlabel('X');
ylabel('Y');
zlabel('Z');
xticks(-2:1:2);
yticks(-2:2:2);
zticks(-2:0.5:0);

subplot(3,2,4);
figure(fig);
contour(X,Y,Z,20);
title('Contour');
xlabel('X');
ylabel('Y');
xticks(-2:1:2);
yticks(-2:0.5:2);
a = colorbar('Xtick', [-1.8:0.2:-0.2]);

subplot(3,2,5);
figure(fig);
kuva_surfl = surfl(X,Y,Z);
kuva_surfl.EdgeColor = 'none';
title('Surfl');
xlabel('X');
ylabel('Y');
zlabel('Z');
xticks(-2:2:2);
yticks(-2:2:2);
zticks(-2:0.5:0);
colorbar('Xtick', [0:0.2:1]);

subplot(3,2,6);
figure(fig);
pcolor(X,Y,Z);
title('Pcolor');
xlabel('X');
ylabel('Y');
xticks(-2:1:2);
yticks(-2:0.5:2);
colorbar('Xtick', [-2:0.5:0]);