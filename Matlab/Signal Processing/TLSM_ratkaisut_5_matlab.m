%
% ELEC-C7230 Tietoliikenteen siirtomenetelmät
%
% TLSM laskuharjoitus 5 Matlab - ratkaisut
%

clc; clear all; close all;

%
% Tehtävä 1 - QAM-modulaatio
%

% Generoidaan binääridataa:
bittien_lkm = 10000;
bin_data = round(rand(1,bittien_lkm));

% Modulointi erillisellä funktiolla:
mod_symb = QAM16(bin_data,1);

% Piirretään symbolit:
scatterplot(mod_symb);
disp('Mitattu signaalien teho');
disp(mean(abs(mod_symb).^2));

% Merkitään esimerkkikuvaan symboleita vastaavat binäärisanat:
const_symb = QAM16(reshape(de2bi(0:15,4,'left-msb')', [1 64]), 1);
X = real(const_symb)*0.8-.1;
Y = imag(const_symb)*.8;
text(X,Y,dec2bin(0:15));

%
% Tehtävä 2 - kohinan vaikutus 16-QAM-signaaleihin
%

% Signaali-kohinasuhteet desibeleinä ja lineaarisina
SNR_dB = [10 20];
SNR_lin = 10.^(SNR_dB/10);

% Kohinan keskiteho on 1.
P_N = 1;
h = [];
plottaustyyli = 'k+r.bx';

% Loopataan eri signaaliarvot ja lisätään kuvaan
for k = 1:length(SNR_lin)
    % Signaalin keskiteho
    P_S = P_N*SNR_lin(k);
    % 16-QAM-signaali halutulla keskiteholla
    mod_symb = QAM16(bin_data,P_S);
    % Generoidaan kohinan reaalikomponentti
    N_Re = randn(size(mod_symb))/sqrt(2);
    % Generoidaan kohinan kompleksikomponentti
    N_Im = randn(size(mod_symb))/sqrt(2);
    % Summataan kohinan komponentit ja saadaan kompleksinen kohina, jonka
    % keskiteho on 1.
    N = N_Re + i*N_Im;
    % Lisätään kohina symboleihin
    kohinaiset_symb = mod_symb + N;
    % Piirretään kuva
    h = scatterplot(kohinaiset_symb,1,0,plottaustyyli(2*k-1:2*k),h);
    hold on;
end
legend('SNR 10 dB','SNR 20 dB');

disp('Mitattu kohinan teho')
disp(mean(abs(N).^2));
