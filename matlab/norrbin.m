clear;

v = 5;
l = 45;
umin = -deg2rad(25);
umax = deg2rad(25);

phi0 = 0;
phidot0 = deg2rad(5);


f = @(x,u) [x(2);
            -(v/(2*l))*(x(2) + x(2)*x(2)*x(2)) + (v*v/(2*l*l)) * u(1)];

sys = nonlinearSys('norrbin', f, 2, 1);

params.tFinal = 1;
% params.R0 = zonotope(interval([-0.1;-0.1], [0.1;0.1]));
% params.R0 = polyZonotope(zonotope(capsule([0;0], [0;0], 0.0), 3));
params.R0 = zonotope(interval([phi0;phidot0], [phi0;phidot0]));
params.U = zonotope(interval(umin, umax));

options.alg = 'lin';
options.tensorOrder = 3;
options.errorOrder = 4;
options.intermediateOrder = 50;
options.timeStep = 0.001;
options.zonotopeOrder = 50;
options.taylorTerms = 6;
options.maxError = [1;1] * 0.001;

polyZono.maxDepGenOrder = 100;
polyZono.maxPolyZonoRatio = 0.001;
polyZono.restructureTechnique = 'reducePca';

options.polyZono = polyZono;

R = reach(sys, params, options);

params.U = zonotope(interval(0.8*umin, 0.8*umax));
R2 = reach(sys, params, options);

veff = 4.75;
f2 = @(x,u) [x(2);
            -(veff/(2*l))*(x(2) + x(2)*x(2)*x(2)) + (veff*veff/(2*l*l)) * u(1)];

sys2 = nonlinearSys('norrbinSlow', f2, 2, 1);
params.U = zonotope(interval(0.8*umin, 0.8*umax));
R3 = reach(sys2, params, options);

veff = 7;
f3 = @(x,u) [x(2);
            -(veff/(2*l))*(x(2) + x(2)*x(2)*x(2)) + (veff*veff/(2*l*l)) * u(1)];

sys3 = nonlinearSys('norrbinFast', f3, 2, 1);
params.U = zonotope(interval(0.8*umin, 0.8*umax));
R4 = reach(sys3, params, options);

grid on;
pbaspect([1 1 1]);
norrbinP = plot(R,  [1 2], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
hold on
norrbinP2 = plot(R2, [1 2], 'EdgeColor', [1,0,0], 'FaceColor', [1,0,0], 'FaceAlpha', 0.1)
hold on
norrbinP3 = plot(R3, [1 2], 'EdgeColor', [0,1,0], 'FaceColor', [0,1,0], 'FaceAlpha', 0.1)
hold on
norrbinP4 = plot(R4, [1 2], 'EdgeColor', [0,1,1], 'FaceColor', [0,1,1], 'FaceAlpha', 0.1)
hold off;

Z = R.timePoint.set{end,1};
% Z.norm
V = Z.vertices;
min(abs(V(2,:)))
max(abs(V(2,:)))
% plot(Z)

writematrix(norrbinP.Vertices,'norrbin_t1000.txt','Delimiter','\t');
writematrix(norrbinP2.Vertices,'norrbin2_t1000.txt','Delimiter','\t');
writematrix(norrbinP3.Vertices,'norrbin3_t1000.txt','Delimiter','\t');
writematrix(norrbinP4.Vertices,'norrbin4_t1000.txt','Delimiter','\t');
