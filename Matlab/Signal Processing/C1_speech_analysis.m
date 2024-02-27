%% Assignment 1: Speech Analysis
%% BY: Mikael Tunturi 657482
% 
% 
% Loading the audio file and its associated sampling rate and defining the time 
% vector $t$

[x, fs] = audioread("C:\Users\mikaeltunturi\Downloads\kiisseli.wav");
t = (1:length(x))/fs;
%% 
% Plotting both the whole sequence and a zoomed in one. Feel free to shift the 
% zoomed sequence to some other range to find an appropriate _quazi-periodic_ 
% sequence

figure(1)
subplot(211)
plot(t, x)
xlim([0, t(end)])
xlabel("time [s]")
ylabel("amplitude")
title("kiisseli.wav")
subplot(212)
plot(t, x)
xlim([0.2, 0.8])
xlabel("time [s]")
ylabel("amplitude")
title("Close up of [0.2, 0.8] s")
%% Task 1
% Find a _quazi-periodic_ sequence from the figure above. Create a *new* vector 
% called |x_sample| of length 0.2 seconds and *plot* it.
% 
% *To Do:*
%% 
% * Start by converting the starting time from seconds to samples |i_start| 
% (i.e., to the corresponding vector index) 
% * Convert the duration (0.2 seconds) to number of samples |i_len|
% * Solve the ending time |i_stop = i_start + i_len|
% * Create the new vector |x_sample| by indexing the original signal (e.g., 
% |x[i_start:i_stop])| 

% WRITE CODE HERE:
i_start = find(t == 0.4); %let's choose t=0.4s as a starting point
i_len = find(t == 0.2); %number of samples
i_stop = i_start + i_len; %the ending time
%Let's create the vector.
x_sample = x(i_start:i_stop);
t_sample = t(i_start:i_stop);
plot(t_sample, x_sample)
xlim([0.4, 0.6])
xlabel("time [s]")
ylabel("amplitude")
title("Close up of [0.4, 0.6] s")
%% Task 2
% Plot the spectrum (in dB) of the _quazi-periodic_ sequence you found. *Limit* 
% the frequency range to |[0, 3000]| Hz (i.e., use |xlim|). Use the step-by-step 
% guide provided in the assignment. 
% 
% What is the first formant $F_1$ of your _quazi-periodic_ sequence?
% 
% *Answer:* The highest peak in the spectrum and the first formant F_1 is 215 
% (Hz).

% WRITE CODE HERE:
N_fft = 2^11; %number of fft bins: 2^11 = 2048, "if possible, use powers of two"
delta_f = fs/(N_fft); %frequency resolution
f_vec = -fs/2:delta_f:fs/2 - delta_f; %frequency vector

x_fft = fftshift(fft(x_sample, N_fft));
%The helper function fftshift reorders sequence from [pos freq, neg freq]
%into the much more logical [negative frequencies, positive frequencies].

plot(f_vec, 10*log10(abs(x_fft)))
%Fourier transform returns a complex vector.
%We took the absolute value to calculate the magnitude of the transformed
%sequence.
%The 10*log10(y) changes the scale into decibels.
xlim([0, 3000])
xlabel("frequency [Hz]")
ylabel("dB")