// Toteuta tänne luokka Kayttajatiedot

import 'package:shared_preferences/shared_preferences.dart';

class Kayttajatiedot {
  tuttuKayttaja() async {
    SharedPreferences asetukset = await SharedPreferences.getInstance();
    bool tuttuKayttaja = asetukset.containsKey('TUTTU_KAYTTAJA');
    asetukset.setString('TUTTU_KAYTTAJA', 'KYLLA');

    return tuttuKayttaja;
  }

  onTunnus() async {
    SharedPreferences asetukset = await SharedPreferences.getInstance();
    return asetukset.containsKey('KAYTTAJATUNNUS');
  }

  asetaTunnus(tunnus) async {
    SharedPreferences asetukset = await SharedPreferences.getInstance();
    asetukset.setString('KAYTTAJATUNNUS', tunnus);
  }

  haeTunnus() async {
    SharedPreferences asetukset = await SharedPreferences.getInstance();
    return asetukset.getString('KAYTTAJATUNNUS');
  }
}