%% C2: FIR filter design (5p)
%% BY: Mikael Tunturi 657482
%% Task 1
% Generate the truncated ideal low-pass filter with $\omega_c=\pi/4$. Plot the 
% mangitude response for $K=[10, 25,50]$ in the *linear scale*.
% 
% The truncated low-pass filter is defined as:
% 
% $$h_K[n] = \frac{\sin\omega_c n}{\pi n},\quad -K\leq n \leq K$$
% 
% *Hints:* 
%% 
% * You can use |sinc| to define the response $h_\text{K}[n]$. However, verify 
% the definition of |sinc|, since you might need to multiply or divide by $\pi$. 
% * Recall the drawing of spectums from Homework 1.

% cutoff frequency
omega_c = pi/4;

% The ideal lowpass filter would have the following magnitude response
ideal_H = [1,1,0,0];
ideal_f = [0,omega_c,omega_c,pi];

figure();clf;
hold on
plot(ideal_f, abs(ideal_H));

% TODO: generate the truncated lowpass filter and its magnitude response
K_values = [10,25,50];
for a = 1:3
    K = K_values(a);
    h_K = omega_c/pi*sinc(omega_c/pi*(-K:K));
    [H_value,w] = freqz(h_K);
    plot(w, abs(H_value))
end

% TODO: plot your truncated filters response here, the ideal response is
% already drawn
hold off
legend(["Ideal response", "K = 10", "K = 25", "K = 50"])
grid on
ylim([0,1.1])
xlim([0, pi])
% TODO: add axis labels and title!
xlabel('\omega')
ylabel('\midH(e^{j\omega})\mid')
title('Task 1')
%% Task 2
% Plot the magnitude responses of the *Hann*, *Hamming*, and *Blackman* windowed 
% low-pass filters. *Unlike in Task 1 plot them in dB-scale.*
% 
% Let $\omega_c=\pi/4$ and $K=25$. 
% 
% Which window function provides the smallest transition band? Which window 
% function has the largest stopband attenuation? What differences do you see compared 
% to a rectangular window, i.e., the truncated approximation? (Again, think of 
% the Gibbs phenomenon).
% 
% *ANSWER:*
%% 
% * the smallest transition band -> Hann window
% * the largest stopband attenuation -> Blackman window
% * The rectangular window gives a rectangular shape at the edges. The more 
% harmonics are used, the more rectangular the shape is. The impulse response 
% narrows by increasing the cutoff. That does not reduce its integral. Oscillations 
% do ot decrease in magnitude and move towards discontinuity. Those other window 
% functions seem to provide a better solution for filtering.

%TODO:  plot the windowed filter responses in dB


omega_c = pi/4;
K_value = 25;
h_K = omega_c/pi*sinc(omega_c/pi*(-K_value:K_value)); % h_K now with K = 25
N_FFT = length(H_value);
w = linspace(-pi,pi,N_FFT);
H_25 = fftshift(fft(h_K,N_FFT));

% windows
Hann_window = hann(2*K_value + 1);
Hamming_window = hamming(2*K_value + 1);
Blackman_window = blackman(2*K_value + 1);

% magnitude responses
H_by_Hann_window = fftshift(fft(Hann_window,N_FFT));
H_by_Hamming_window = fftshift(fft(Hamming_window,N_FFT));
H_by_Blackman_window = fftshift(fft(Blackman_window,N_FFT));

% plots
figure();
clf;
title('Task 2')
hold on
Hann_calc = 10*log10(abs(H_by_Hann_window.*H_25.'));
plot(w, Hann_calc)
Hamming_calc = 10*log10(abs(H_by_Hamming_window.*H_25.'));
plot(w, Hamming_calc)
Blackman_calc = 10*log10(abs(H_by_Blackman_window.*H_25.'));
plot(w, Blackman_calc)
legend(["Hann window", "Hamming window", "Blackman window"])
xlabel('\omega')
ylabel('\midH(e^{j\omega}\mid  (dB)')
xlim([0,pi])
hold off
%
