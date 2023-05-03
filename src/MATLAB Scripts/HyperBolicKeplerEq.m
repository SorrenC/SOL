%% AEE 462 Homework 2
% Sorren Chandra 
% 02/12/2022

%% Hyperbolic Kepler Equation 
% Use for hyperbolic orbits, (i.e e > 0)
function H = HyperbolicKeplerEqn(M,e,Tolerance)
    E_k = M; % Set E1 = M
    E_update = E_k - ((M - E_k + e*sinh(E_k))/(e*cosh(E_k) -1));
    i = 0; % iteration counter
    while(abs(E_update - E_k) > Tolerance)
        i = i+1;
        E_k = E_update;
        E_update = E_k - ((M - E_k + e*sinh(E_k))/(e*cosh(E_k) -1));
        fprintf("Iteration %d %d\n",i,E_update)
    end
  
    E = E_k; % Final answer
    H = E; % return value
end