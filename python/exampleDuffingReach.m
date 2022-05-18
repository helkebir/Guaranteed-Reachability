% NOTE: Requires CORA Toolbox R2020 to be installed (including dependences)
% See https://tumcps.github.io/CORA/ for further instructions.

% Parameters (stay fixed throughout).
m = 5;
c = 0.2;
k = 0.5;
a = 0.1;

% Equation defining the dynamics.
f = @(x,u) [x(2);
            -(1/m) * (c * x(2) + k * x(1) + a * x(1)^3 - u)];

sys = nonlinearSys('duffing', f);

% Final time.
params.tFinal = 0.1;
% R0 := B(0; 0.1).
params.R0 = zonotope(capsule([0;0], [0;0], 0.1));
% U := [-0.5, 0.5]
params.U = zonotope(interval(-0.5,0.5));

% Reachable set solver options.
options.alg = 'lin';
options.tensorOrder = 3;
options.errorOrder = 3;
options.intermediateOrder = 10;
options.timeStep = 0.05;
options.zonotopeOrder = 10;
options.taylorTerms = 5;

% Nominal reachable set computation
R = reach(sys, params, options);

% Ub = [-0.25, 0.25]
params.U = zonotope(interval(-0.25,0.25));
% Off-nominal reachable set computation
R2 = reach(sys, params, options);

grid on;
pbaspect([1 1 1]);
duffP = plot(R,  [1 2], 'EdgeColor', [0,0,1], 'FaceColor', [0,0,1], 'FaceAlpha', 0.1)
hold on
duffP2 = plot(R2, [1 2], 'EdgeColor', [1,0,0], 'FaceColor', [1,0,0], 'FaceAlpha', 0.1)
hold off;

% Extract final zonotope.
Z = R.timePoint.set{end,1};
% Print norm; useeful for use in the Bihari inequality.
Z.norm
% plot(Z)

% Write polygons shown in both plots to files.
writematrix(duffP.Vertices,'example.txt','Delimiter','\t');
writematrix(duffP2.Vertices,'example_impaired.txt','Delimiter','\t');
