clear;

A = [-1, 1, 0, 0, 0;
      0,-1, 0, 0, 0;
      0, 0,-0.5, 0.5,-0.1;
      0, 0,-0.5,-0.1,1;
      0, 0,0, 0.1,-0.5];
  
K = [0, 0, 0, 0, 0;
     0, 0, 0, 0, 0;
     0, 0, 0, 0, 0;
     0.1, 0, 0, 0, 0;
     0, 0.5, 0, 0, 0];
 
B = [0.1, 0;
     1, 0;
     0, 0.1;
     0, 0.1;
     0, 0.1];

% f = @(x,u) A*x + B*u + d;

% sys = nonlinearSys('uppertriangular', f, 8, 4);
sys = linearSys('interconnected', A+K, B);

params.tFinal = 0.25;
% params.R0 = zonotope(interval([-0.1;-0.1], [0.1;0.1]));
% params.R0 = polyZonotope(zonotope(capsule([0;0], [0;0], 0.0), 3));
params.R0 = zonotope(interval(-[1e-9;1e-9;1e-9;1e-9;1e-9], [1e-9;1e-9;1e-9;1e-9;1e-9]));
params.U = zonotope(interval([-2;-2], [2;2]));

options.alg = 'lin';
options.tensorOrder = 3;
options.errorOrder = 4;
options.intermediateOrder = 100;
options.timeStep = 0.001;
options.zonotopeOrder = 50;
options.taylorTerms = 6;
options.maxError = ones(5,1) * 0.0001;

polyZono.maxDepGenOrder = 100;
polyZono.maxPolyZonoRatio = 0.001;
polyZono.restructureTechnique = 'reducePca';

options.polyZono = polyZono;

R = reach(sys, params, options);

params.U = zonotope(interval(0.95*[-2;-2], 0.95*[2;2]));
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
utriP45 = plot(R,  [4 5], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
% utriP78 = plot(R,  [7 8], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)

utriPimp12 = plot(R2,  [1 2], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriPimp34 = plot(R2,  [3 4], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
utriPimp45 = plot(R2,  [4 5], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
% utriPimp78 = plot(R2,  [7 8], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)


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
[1, min(V(1,:)), max(V(1,:))]
[2, min(V(2,:)), max(V(2,:))]
[3, min(V(3,:)), max(V(3,:))]
[4, min(V(4,:)), max(V(4,:))]
[5, min(V(5,:)), max(V(5,:))]

disp('Impaired')

Zi = R2.timePoint.set{end,1};
% Z.norm
V = Zi.vertices;
[1, min(V(1,:)), max(V(1,:))]
[2, min(V(2,:)), max(V(2,:))]
[3, min(V(3,:)), max(V(3,:))]
[4, min(V(4,:)), max(V(4,:))]
[5, min(V(5,:)), max(V(5,:))]
% plot(Z)

writematrix(utriP12.Vertices,'iconn12_t250.txt','Delimiter','\t');
writematrix(utriP34.Vertices,'iconn34_t250.txt','Delimiter','\t');
writematrix(utriP45.Vertices,'iconn45_t250.txt','Delimiter','\t');
% writematrix(utriP78.Vertices,'utri78_t250.txt','Delimiter','\t');

writematrix(utriPimp12.Vertices,'iconnimp12_t250.txt','Delimiter','\t');
writematrix(utriPimp34.Vertices,'iconnimp34_t250.txt','Delimiter','\t');
writematrix(utriPimp45.Vertices,'iconnimp45_t250.txt','Delimiter','\t');
% writematrix(utriPimp78.Vertices,'utriimp78_t250.txt','Delimiter','\t');
% writematrix(norrbinP2.Vertices,'norrbin2_t1000.txt','Delimiter','\t');
% writematrix(norrbinP3.Vertices,'norrbin3_t1000.txt','Delimiter','\t');
% writematrix(norrbinP4.Vertices,'norrbin4_t1000.txt','Delimiter','\t');
