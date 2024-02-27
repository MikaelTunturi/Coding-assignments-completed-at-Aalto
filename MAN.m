%% Assignment 1: Moving average filtering (pt 2)
%% BY: Mikael Tunturi 657482
% 
% 
% *NOTE:* Implement the function |myMAn(x,n)| at the bottom at this file for 
% subsection *a)*
%% b) Plot the amplitude response
% Plot $|H_N(e^{j\omega})|$ for $N\in\{2,4,6\}$ in the *same* *figure* (use 
% the |hold| function). Use a linear scale. Note that you do not need to use the 
% function defined in *a)*, for this step.

N = 2;
H_func = @(omega, n) (1/n)*(1-exp(-1i*omega*n))./(1-exp(-1i*omega));
omega_vec = 0:0.01:pi;
figure()
hold on
plot(omega_vec, abs(H_func(omega_vec, 2)))
plot(omega_vec, abs(H_func(omega_vec, 4)))
plot(omega_vec, abs(H_func(omega_vec, 6)))
title("Amplitude response")
xlabel("\omega")
ylabel("|H(e\^[j\omega])|")
grid on
%% c) Filtering a signal
% Filter the ECG signal from the previous task (e.g., |ecg.mat|). Plot *both* 
% its spectrum and time domain signal before and after filtering. *Optionally* 
% you can again filter an audio file such as |kiisseli.wav| and listen to its 
% effect for different values of $N$.
% 
% Answer the following questions:
%% 
% * What effect does the value of $N$ have on the amplitude response?
% * What value of $N$is suitable for filtering the ECG signal. Justify your 
% answer.
%% 
% *ANSWER:* The MA-N filter works as a low pass, with higher orders of N creating 
% a smaller passband (as can be seen in the response above). The MA-N has a very 
% loose transition band, and heavy stopband ripple. The ECG signal is best filtered 
% with a value between 5-7.

N = 6;
load ecg.mat

ecg_filtered = myMAn(ecg, N);
figure()
subplot(211)
plot(t, ecg)
title("ECG signal")
subplot(212)
plot(t, ecg_filtered)
title("Filtered ECG signal")
%% a) The MA-N function
% Implement the MA-n filter using either |for| loops, |filter| or |conv.|

function [y] =  myMAn(x, n)
    a = 1;
    b = 1/n*ones([n, 1]);
    y = filter(b, a, x);
end