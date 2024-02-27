// Toteuta tänne luokka TyyliteltyTeksti

import 'package:flutter/material.dart';

class TyyliteltyTeksti extends StatelessWidget {
  final String teksti;
  TyyliteltyTeksti(this.teksti);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(16.0),
      child: Text(teksti,
        style: TextStyle(
          fontSize: 32,
        )
      )
    );
  }
}