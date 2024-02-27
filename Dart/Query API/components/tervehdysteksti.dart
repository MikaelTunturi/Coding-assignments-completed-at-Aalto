// Toteuta tänne luokka Tervehdysteksti

import 'package:flutter/material.dart';
import '../storage/kayttajatiedot.dart';
import 'tyylitelty_teksti.dart';

class Tervehdysteksti extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: Kayttajatiedot().tuttuKayttaja(),
      builder: (BuildContext context, AsyncSnapshot snapshot) {
        if (snapshot.hasData) {
          if (snapshot.data) {
            return TyyliteltyTeksti('Heippa taas!');
          } else {
            return TyyliteltyTeksti('Tervetuloa!');
          }
        } else if (snapshot.hasError) {
          return Text('Virhe käyttäjätietojen hakemisessa.');
        } else {
          return Text('Haetaan käyttäjätietoja..');
        }
      }
    );
  }
}