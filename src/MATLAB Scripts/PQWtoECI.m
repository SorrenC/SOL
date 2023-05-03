%% Perifocal to ECI Transformation Solver
% Author: Sorren Chandra 

%% Transformation Function
function [rECI] = PQWtoECI(W,w,i,rPQW)
    
% Perifocal to ECI coordinate functon
%
% Inputs: W - right accension of ascending node, w-argument of periapse,
% i-inclination, PWQ - a position or velocity vector in perifocal
% coordinates. ALL VALUES MUST BE IN DEGREES
%
% Returns a 1x3 matrix

    % Create rotation matrix
    r = [cosd(W)*cosd(w)-sind(W)*sind(w)*cosd(i) -cosd(W)*sind(w)-sind(W)*cosd(w)*cosd(i) sind(W)*sind(i)
         sind(W)*cosd(w)+cosd(W)*sind(w)*cosd(i) -sind(W)*sind(w)+cosd(W)*cosd(w)*cosd(i) -cosd(W)*sind(i)
         sind(w)*sind(i) cosd(w)*sind(i) cosd(i)];
    
    rECI = r*rPQW'; % Need to add " ' " because we want to multiply by the column vector of PWQ
   
end
    
    