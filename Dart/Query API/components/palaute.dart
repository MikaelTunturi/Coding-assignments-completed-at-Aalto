// Toteuta tänne luokka Palaute

import 'package:flutter/material.dart';
import 'tyylitelty_teksti.dart';

class Palaute extends StatelessWidget {
  final bool oikein;
  final Function haeKysymysFunktio;
  Palaute(this.oikein, this.haeKysymysFunktio);

  @override
  Widget build(BuildContext context) {
    String teksti = 'Oikein meni!';
    if (!oikein) {
      teksti = 'Väärin meni, hups!';
    }

    return Column(children: [
      TyyliteltyTeksti(teksti),
      ElevatedButton(
        child: Text('Seuraava!'),
        onPressed: haeKysymysFunktio,
      )
    ]);
  }
}