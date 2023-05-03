%% Lamberts Equation Solver
% Author: Sorren Chandra
% Date: 03/14/2022
% Contact: sorrenchandra@gmail.com

%%
function [a,alpha,beta,s,c] = LambertsEqn(r1,r2,t,theta,Mu,Tolerance,option)
%
% Solves lamberts equation for semimajor axis given two position
% measurments, change in true anomaly, and change in time
% 
% INPUTS: 
% r1         = position at initial time, vector or magnitude 
% r2         = position at final time, vector or magnitude
% theta      = change in angle between the two position measurments in radians
% Mu         = orbital parameter
% Tolerance  = stopping condition for the bisection method
% option     = used to denote if r1 and r2 are given in vectors or magnitudes,
%             1 if r1 and r2 are vectors, 2 if they are magnitudes
%
% OUTPUTS:
% a          = semi-major axis 
% alpha      =
% beta       =
% s          = semi-perimeter
% c          = chord length between the two positions

% Find chord and semi perimeter 
% Check if r1 and r2 are given in magnitudes or vectors

if option == 1 % given in vectors
    c = abs(r2 - r1); % vector subtraction
elseif option == 2 % given in magnitudes
    c = sqrt( r1^2 + r2^2 - 2*r1*r2*cos(theta)); % law of cosines
end

s = (c + norm(r1) + norm(r2))/2; % semi perimeter in km

% Need initial guesses for a and g
a_min = s/2; % initial guess for a_min
a_max = 2*s; % initial guess for a_max
a = (a_min + a_max)/2; % initial guess for a

alpha = asin(sqrt((s)/(2*a))) * 2; % use initial guess for a to find alpha
beta  = asin(sqrt((s-c)/(2*a))) * 2; % use initial guess for a to find beta
g = sqrt((a^3)/(Mu)) * (alpha - beta - (sin(alpha) - sin(beta))); % use initial guess for a to find t

i = 1; % create iteration counter 

% Solve Lambert's Equation using a Bisection Method

while(abs(t-g) > Tolerance)
       
    alpha = asin(sqrt((s)/(2*a))) * 2;
    beta  = asin(sqrt((s-c)/(2*a))) * 2;
    g = sqrt((a^3)/(Mu)) * (alpha - beta - (sin(alpha) - sin(beta)));
    
    if g > t
        a_min = a;
    elseif g < t
        a_max = a;
    else
        break
    end
    
    a = (a_min + a_max)/2;
    
    if i>10000
        break
    end
    
    i = i + 1; % update iteration counter
    %fprintf("%.3f\n",g)
end

fprintf("Semi-major axis found to be %.3f km\n",a)
fprintf('alpha =  %.3f deg\n',alpha*(180/pi))
fprintf('beta  = %.3f deg\n',beta*(180/pi))
fprintf("Found in %d iterations\n",i)

end