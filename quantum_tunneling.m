% Constants
hbar = 1.0545718e-34;  % Planck's constant (J·s)
m = 9.10938356e-31;    % Mass of an electron (kg)

% Barrier parameters
V0 = 1e-18;   % Barrier height (in Joules, adjust as needed)
a = 1e-9;     % Barrier width (in meters)

% Energy range
E = linspace(0, V0, 1000); % Energies from 0 to V0 (Joules)
% Calculate transmission probability
T = zeros(size(E)); % Initialize array for transmission probabilities

for i = 1:length(E)
    if E(i) < V0
        kappa = sqrt(2 * m * (V0 - E(i))) / hbar;
        T(i) = 1 / (1 + (V0^2 / (4 * E(i) * (V0 - E(i)))) * sinh(kappa * a)^2);
    else
        T(i) = 1; % For E > V0, transmission is effectively 1 (classical case)
    end
end
% Plot transmission probability
figure;
plot(E / 1.6e-19, T, 'LineWidth', 2); % Convert energy to eV for better readability
xlabel('Energy (eV)');
ylabel('Transmission Probability T(E)');
title('Quantum Tunneling Through a Potential Barrier');
grid on;
