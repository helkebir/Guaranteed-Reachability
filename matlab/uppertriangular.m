clear;

v = 5;
l = 45;
umin = -deg2rad(25);
umax = deg2rad(25);

phi0 = 0;
phidot0 = deg2rad(5);

% A = [1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 8/8;
%      1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 7/7,   0;
%      1/6, 2/6, 3/6, 4/6, 5/6, 6/6,   0,   0;
%      1/5, 2/5, 3/5, 4/5, 5/5,   0,   0,   0;
%      1/4, 2/4, 3/4, 4/4,   0,   0,   0,   0;
%      1/3, 2/3, 3/3,   0,   0,   0,   0,   0;
%      1/2, 2/2,   0,   0,   0,   0,   0,   0;
%      1/1,   0,   0,   0,   0,   0,   0,   0];

A = [1/1,   0,   0,   0,   0,   0,   0,   0;
     1/2, 2/2,   0,   0,   0,   0,   0,   0;
     1/3, 2/3, 3/3,   0,   0,   0,   0,   0;
     1/4, 2/4, 3/4, 4/4,   0,   0,   0,   0;
     1/5, 2/5, 3/5, 4/5, 5/5,   0,   0,   0;
     1/6, 2/6, 3/6, 4/6, 5/6, 6/6,   0,   0;
     1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 7/7,   0;
     1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 8/8];

B = [1/8, 2/8, 3/8, 4/8;
     1/7, 2/7, 3/7, 4/7;
     1/6, 2/6, 3/6, 4/6;
     1/5, 2/5, 3/5, 4/5;
     1/4, 2/4, 3/4, 4/4;
     1/3, 2/3, 3/3, 4/3;
     1/2, 2/2, 3/2, 4/2;
     1/1, 2/1, 3/1, 4/1];
 
d = 0.1*ones(8,1);

% f = @(x,u) A*x + B*u + d;

f = @(x,u) A*x + B*u + d;

sys = nonlinearSys('uppertriangular', f, 8, 4);

params.tFinal = 0.25;
% params.R0 = zonotope(interval([-0.1;-0.1], [0.1;0.1]));
% params.R0 = polyZonotope(zonotope(capsule([0;0], [0;0], 0.0), 3));
params.R0 = zonotope(interval([0;0;0;0;0;0;0;0], [0;0;0;0;0;0;0;0]));
params.U = zonotope(interval([-1;-1;-1;-1], [1;1;1;1]));

options.alg = 'lin';
options.tensorOrder = 3;
options.errorOrder = 4;
options.intermediateOrder = 100;
options.timeStep = 0.001;
options.zonotopeOrder = 50;
options.taylorTerms = 6;
options.maxError = ones(8,1) * 0.0001;

polyZono.maxDepGenOrder = 100;
polyZono.maxPolyZonoRatio = 0.001;
polyZono.restructureTechnique = 'reducePca';

options.polyZono = polyZono;

R = reach(sys, params, options);

params.U = zonotope(interval(0.9*[-1;-1;-1;-1], 0.9*[1;1;1;1]));
R2 = reach(sys, params, options);
% 
% veff = 4.75;
% f2 = @(x,u) [x(2);
%             -(veff/(2*l))*(x(2) + x(2)*x(2)*x(2)) + (veff*veff/(2*l*l)) * u(1)];
% 
% sys2 = nonlinearSys('norrbinSlow', f2, 2, 1);
% params.U = zonotope(interval(0.8*umin, 0.8*umax));
% R3 = reach(sys2, params, options);
% 
% veff = 7;
% f3 = @(x,u) [x(2);
%             -(veff/(2*l))*(x(2) + x(2)*x(2)*x(2)) + (veff*veff/(2*l*l)) * u(1)];
% 
% sys3 = nonlinearSys('norrbinFast', f3, 2, 1);
% params.U = zonotope(interval(0.8*umin, 0.8*umax));
% R4 = reach(sys3, params, options);

grid on;
pbaspect([1 1 1]);
utriP12 = plot(R,  [1 2], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriP34 = plot(R,  [3 4], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriP56 = plot(R,  [5 6], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriP78 = plot(R,  [7 8], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)

utriPimp12 = plot(R2,  [1 2], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriPimp34 = plot(R2,  [3 4], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriPimp56 = plot(R2,  [5 6], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriPimp78 = plot(R2,  [7 8], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)


% hold on
% norrbinP2 = plot(R2, [1 2], 'EdgeColor', [1,0,0], 'FaceColor', [1,0,0], 'FaceAlpha', 0.1)
% hold on
% norrbinP3 = plot(R3, [1 2], 'EdgeColor', [0,1,0], 'FaceColor', [0,1,0], 'FaceAlpha', 0.1)
% hold on
% norrbinP4 = plot(R4, [1 2], 'EdgeColor', [0,1,1], 'FaceColor', [0,1,1], 'FaceAlpha', 0.1)
% hold off;

Z = R.timePoint.set{end,1};
% Z.norm
V = Z.vertices;
[1, min(abs(V(1,:))), max(abs(V(1,:)))]
[2, min(abs(V(2,:))), max(abs(V(2,:)))]
[3, min(abs(V(3,:))), max(abs(V(3,:)))]
[4, min(abs(V(4,:))), max(abs(V(1,:)))]
[5, min(abs(V(5,:))), max(abs(V(2,:)))]
[6, min(abs(V(6,:))), max(abs(V(3,:)))]
[7, min(abs(V(7,:))), max(abs(V(7,:)))]
[8, min(abs(V(8,:))), max(abs(V(8,:)))]

disp('Impaired')

Zi = R2.timePoint.set{end,1};
% Z.norm
V = Zi.vertices;
[1, min(abs(V(1,:))), max(abs(V(1,:)))]
[2, min(abs(V(2,:))), max(abs(V(2,:)))]
[3, min(abs(V(3,:))), max(abs(V(3,:)))]
[4, min(abs(V(4,:))), max(abs(V(1,:)))]
[5, min(abs(V(5,:))), max(abs(V(2,:)))]
[6, min(abs(V(6,:))), max(abs(V(3,:)))]
[7, min(abs(V(7,:))), max(abs(V(7,:)))]
[8, min(abs(V(8,:))), max(abs(V(8,:)))]
% plot(Z)

writematrix(utriP12.Vertices,'utri12_t250.txt','Delimiter','\t');
writematrix(utriP34.Vertices,'utri34_t250.txt','Delimiter','\t');
writematrix(utriP56.Vertices,'utri56_t250.txt','Delimiter','\t');
writematrix(utriP78.Vertices,'utri78_t250.txt','Delimiter','\t');

writematrix(utriPimp12.Vertices,'utriimp12_t250.txt','Delimiter','\t');
writematrix(utriPimp34.Vertices,'utriimp34_t250.txt','Delimiter','\t');
writematrix(utriPimp56.Vertices,'utriimp56_t250.txt','Delimiter','\t');
writematrix(utriPimp78.Vertices,'utriimp78_t250.txt','Delimiter','\t');
% writematrix(norrbinP2.Vertices,'norrbin2_t1000.txt','Delimiter','\t');
% writematrix(norrbinP3.Vertices,'norrbin3_t1000.txt','Delimiter','\t');
% writematrix(norrbinP4.Vertices,'norrbin4_t1000.txt','Delimiter','\t');
