% Author: Sorren Chandra 
% Date: 03/01/2022
% contact: sorrenchandra@gmail.com

function [h,n,a,e,i,W,w,f] = OrbitalElements(r,v,Mu)
% 
% ORBITALELEMENTS Calculates the six Keplerian orbital elements given a 3-dimensional vector 
% of position and velocity at some instantaneous time t
% Inputs: r=position vector v=velocity vector Mu=gravitation parameter 
% NOTE: The returned vectors have not been normalized, use the function
% norm() to do so. Futhurmore all applicable value are returned in degrees
%
% h = Momentum vector
% n = Line of nodes vector
% e = Eccentricity vector
% i = Oribtal inclination
% W = Right Accesion of Ascending Node
% w = Argument of periapse 
% f = True anamoly

h = cross(r,v); % Find momentum vector
n = cross([0,0,1],h); % Find line of nodes vector
e = (1/Mu)*cross(v,h) - (r/norm(r)); % Find eccentricity vector 
i = (acos( dot ( (h/norm(h) ),[0,0,1] ) ) ) * (180/pi); % Find orbital inclination (and covert to degrees)

% Calculate 2D elements
E = ((norm(v)^2)/2) - (Mu/norm(r));
a = -(Mu/(2*E));

W = (acos(dot([1,0,0],(n/norm(n))))) * (180/pi); % Find Right Accession of Ascending Node (and convert to degrees)

% Need to check for quadrant ambiguity
if dot([0,1,0],n)<0
    W = 360 - W;
else 
    % do nothing, in the right quadrant
end

w = acos((dot(n,e)) / (norm(n) * norm(e))) * (180/pi); % Find Argument of Perigee (and convert to degrees)

% Need to check for quadrant ambiguity
if dot([0,0,1],e)<0
    w = 360 - w;
else 
    % do nothing, in the right quadrant 
end

f = acos((dot(r,e))/(norm(r) * norm(e))) * (180/pi); % Find True anamoly (and convert to degrees)

% Need to check for quadrant ambiguity
if dot(r,v)<0
    f = 360 - f;
else 
    % do nothing, in the right quadrant 
end

end

