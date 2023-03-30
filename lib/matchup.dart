import 'package:flutter/material.dart';
// ignore: unused_import
import './homepage.dart'; //importing the home widget

class MatchupPage extends StatefulWidget {
  const MatchupPage({Key? key}) : super(key: key);

  @override
  _MatchupPageState createState() => _MatchupPageState();
}

class _MatchupPageState extends State<MatchupPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Matchup'),
        actions: [
          SizedBox(width: 60),
          Center(
            child:
                OutlinedButton(child: Text('Matchup'), onPressed: () => null),
          ),
          SizedBox(width: 80)
        ],
      ),
      body: Container(
        child: Center(
          child: Text(
            'This is the about page. You can outline your vision, mission, and objectives on this page', //Once again, this text message will be displayed in the center of the page.
            style: TextStyle(fontSize: 18),
          ),
        ),
      ),
    );
  }
}
