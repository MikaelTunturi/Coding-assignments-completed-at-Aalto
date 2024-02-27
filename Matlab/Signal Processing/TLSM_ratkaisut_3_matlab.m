%
%  ELEC-C7230 Tietoliikenteen siirtomenetelmät
%
%  TLSM_laskuharjoitus_3_matlab - ratkaisut
%

clear all; close all;

%
%  Tehtävä 1 - kohinainen tiedonsiirto:
%

% a) Lähetettävän datan generointi:
bittien_lkm = 50;
data = randi([0,1],1,bittien_lkm);

% Modulaatio BPSK-signaaleiksi:
sig_amplitudi = 1;
Tx_data = -sig_amplitudi*(-1).^data;

% Piirretään kuva:
figure(1);
stem(Tx_data,'s');

% b) Kohinainen siirtokanava; oletetaan, että tiedonsiirrossa signaaleihin
% summautuu kohinaa, joka noudattaa standardoitua normaalijakaumaa:
kohina = randn(size(Tx_data));
Rx_data = Tx_data + kohina;

% Lisätään edelliseen kuvaan:
figure(1); hold all;
stem(Rx_data);

% c) Vastaanotto; kvantisoidaan vastaanotetut kohinaiset näytteet sen
% mukaan, onko niiden arvo pienempi vai suurempi kuin 0:

% Alustetaan vektori ykkösiksi
Rx_mod = ones(size(Rx_data));

% Kun Rx_data on pienempi kuin nolla, tallennetaan arvo -1:
Rx_mod(Rx_data < 0) = -1;

% Lisätään kuvaan:
stem(Rx_mod,'^');
legend('Lähetetyt symbolit','Kohinaiset symbolit','Kvantisoidut symbolit')

%
%  Tehtävä 2 - virhetodennäköisyyden arviointi:
%

% a) Toistetaan edellinen tiedonsiirto eri signaali-kohinasuhteilla (SNR):
% SNR on desibeleissä.
SNR_dB = 0:1:14;
SNR_lin = 10.^(SNR_dB/10);

% Oletetaan, että kohinan teho on vakio; tällöin lähetettyjen signaalien
% amplitudi on valittava vastaamaan haluttua signaalin ja kohinan tehojen
% suhdetta: (SNR = P_S/P_N <-> P_S = SNR*P_N).
% Kohinan teho (varianssi) = 1.
sig_amplitudi = sqrt(SNR_lin*1);

% Alustetaan vektori, johon tallennetaan jokaista SNR-arvoa vastaava
% arvioitu bittivirhetodennäköisyys (BER):
BER = zeros(size(SNR_lin));

% Simuloitaessa virhetodennäköisyyksiä tarvitaan yleensä suuri määrä 
% dataa, esim. 1e7 .. 1e9:
bittien_lkm = 1e8;

% Simuloidaan virheet jokaiselle SNR-arvolle:
for i = 1:length(SNR_lin)
    data = randi([0,1],1,bittien_lkm);
    Tx_data = -sig_amplitudi(i)*(-1).^data;
    kohina = randn(size(Tx_data));
    Rx_data = Tx_data + kohina;
    Rx_demod = ones(size(Rx_data));
    % Muunnetaan symbolit suoraan biteiksi:
    Rx_demod(Rx_data < 0) = 0;
    % Lasketaan virheellisten bittien lukumäärä ja bittivirhesuhde:
    BER(i) = sum(abs(Rx_demod-data))/bittien_lkm;
end

% b) Piirretään kuva:
figure(2);
semilogy(SNR_dB,BER,'-o')
grid on;
xlabel('P_S/P_N (dB)');
ylabel('BER');
