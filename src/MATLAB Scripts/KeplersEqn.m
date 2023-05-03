%% AEE 462 Homework 2
% Sorren Chandra 
% 02/12/2022

%% Function to solve Keplers Equation
function E = KeplersEqn(M,e,Tolerance)
% Solve Keplers Equation numerically using a Newton-Raphson Method
% Use for circular and eclipic orbits (i.e 0 < e < 1) 

% e = eccentricity
% E = eccentric anomoly
% M = Mean anomoly 

% M = E+e*sin(E) (keplers equation)
% f(E) = M-E+e*sin(E)
% f'(E) = -1+e*cos(E)
  
    E_k = M; % Set E1 = M
    E_update = E_k - ((M - E_k + e*sin(E_k))/(e*cos(E_k) -1));
    i = 0; % iteration counter
    while(abs(E_update - E_k) > Tolerance)
        i = i+1;
        E_k = E_update;
        E_update = E_k - ((M - E_k + e*sin(E_k))/(e*cos(E_k) -1));
        %fprintf("Iteration %d %d\n",i,E_update)
    end
  
    E = E_k; % Final answer
    
end
    
    
