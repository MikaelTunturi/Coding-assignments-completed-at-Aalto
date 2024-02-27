import 'package:flutter/material.dart';
import '../components/tervehdysteksti.dart';
import '../storage/kayttajatiedot.dart';

class Aloitusnakyma extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    final teksti = Tervehdysteksti();
    final nappi = ElevatedButton(
      child: Text('Kysy kysymys'),
      onPressed: () => Navigator.pushNamed(context, '/kysely')
    );

    final sarake = Column(children: [
      teksti,
      nappi
    ]);

    return Scaffold(
      appBar: AppBar(
        title: Text('Kyselysovellus')
      ),
      body: SafeArea(
        child: Center(
          child: Container(
            child: sarake
          )
        )
      )
    );
  }
}