%% Assignment 2: ECG filtering
%% BY: Mikael Tunturi 657482
%% 
% We start by loading a the ecg|.mat| file, consisting of two vectors:
%% 
% * ecg - a single lead (noisy) ecg signal of shape |1x900|
% * |fs| -  the sampling rate of the signal (300 Hz)

% loading the ecg data
load ecg.mat
%% 
% Plotting the *noisy* ecg signal in the time domain. For a reference on how 
% a *clean* signal should look like you can compare it to the <https://en.wikipedia.org/wiki/Electrocardiography 
% wikipedia article on electrocardiography>.

figure()
plot(t, ecg)
xlabel("Time [s]")
ylabel("Normalized amplitude")
title("Noisy ecg")
grid on
xlim([0,3])
%% Task 1 
% *a)* Define coefficients |b| and |a| for the filter.
% 
% *b)* Visualize the amplitude response $|H_{hum}(e^{j\omega})|$using *basic 
% functions* (e.g., |sin|, |exp|, etc.) 
% 
% *c)* Use the output vectors |[h, f]| from |freqz| to plot the amplitude response 
% $|H_{hum}(e^{j\omega})|$ and verify that it produces the same result as in *b)*.
% 
% *d)* Use the output vectors |[h, t]| from |impz| to plot the impulse response 
% for the first *15* values.
% 
% *Hint:* you can access the documentation using the |doc| function on the command 
% line (e.g. |doc freqz|)

b_coefficient = [0.985, -0.985, 0.986];
a_coefficient = [1, -0.985, 0.971];

H = @(z) (b_coefficient(1) + b_coefficient(2)*z.^-1 + b_coefficient(3)*z.^-2) ./ ...
         (a_coefficient(1) + a_coefficient(2)*z.^-1 + a_coefficient(3)*z.^-2);
     
figure;
subplot(211);
omega = linspace(0, pi, 301);
plot(omega/(2*pi)*fs, 10*log10(abs(H(exp(1j*omega)))))

hold on
[h, f1] = freqz(b_coefficient, a_coefficient, [], fs);
plot(f1, 10*log10(abs(h)))
hold off
ylim([-10, 2]);
xlabel("Frequency (Hz)")
ylabel("Response |H(e\^[j\omega])| (dB)")
title("Amplitude response")

[h, t1] = impz(b_coefficient, a_coefficient, 15, fs);
subplot(212)
stem(t1*1000, h)
grid on
ylim([-0.2, 1.2])
xlim([-0.5, 45])
xlabel("Time (ms)")
ylabel("Response h(x)")
title("Impulse response")
%% Task 2
% *e)* Use a |for-|loop to filter the ECG signal using the given filter
% 
% *f)* Use the |filter| function to verify that you get the same results as 
% in *e)*
% 
% *g)* Plot the original and filtered signal side by side (using |subplot|). 
% Is the interference noise removed?
% 
% *ANSWER:* Yes it is.

x = [ecg zeros(1, length(b_coefficient) - 1)];
y = zeros(size(ecg));
y(1) = b_coefficient(1) * x(1);
y(2) = b_coefficient(1) * x(2) + b_coefficient(2) * x(1) - a_coefficient(2) * y(1);

for n = 3:length(y)
    y(n) = sum(b_coefficient .* x([n n-1 n-2])) - sum(a_coefficient(2:3) .* y([n-1 n-2]));
end

filtered_ecg = filter(b_coefficient, a_coefficient, ecg);

figure()
subplot(211)
plot(t, ecg)
xlabel("Time (s)")
ylabel("Normalized amplitude")
title("Noisy ECG")
grid on

xlim([0, 3])
subplot(212)
plot(t, [filtered_ecg; y].')
xlabel("Time (s)")
ylabel("Normalized amplitude")
title("Filtered ECG")
grid on
xlim([0, 3])
figure;
N_fft = 512;
[Power_noisy, f] = periodogram(ecg, [], N_fft, fs);
[Power_filtered, f] = periodogram(filtered_ecg, [], N_fft, fs);
plot(f, Power_noisy, f, Power_filtered)
title("Power Spectra of ECG signal")
xlabel("Frequency (Hz)")
ylabel("Normalized Power")
legend("Noisy", "Filtered")