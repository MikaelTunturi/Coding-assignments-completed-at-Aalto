// Toteuta tänne luokka Kysymys

import 'package:flutter/material.dart';
import 'vastausvaihtoehto.dart';
import 'tyylitelty_teksti.dart';

class Kysymys extends StatelessWidget {
  final Map kysymys;
  final Function vastaaFunktio;
  Kysymys(this.kysymys, this.vastaaFunktio);

  @override
  Widget build(BuildContext context) {
    List<Widget> vastausvaihtoehdot = new List();
    for (var vaihtoehto in kysymys['answerOptions']) {
      var vastausvaihtoehto = Vastausvaihtoehto(vaihtoehto['answerText'], () {
        vastaaFunktio(kysymys['questionId'], vaihtoehto['answerOptionId']);
      });

      vastausvaihtoehdot.add(vastausvaihtoehto);
    }

    return Column(children: [
      TyyliteltyTeksti(kysymys['questionText']),
      Expanded(child: ListView(children: vastausvaihtoehdot))
    ]);
  }
}