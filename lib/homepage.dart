import 'package:flutter/material.dart';
import './matchup.dart'; //importing the MatchupPage
import './playoff.dart'; //importing the PlayoffPage

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        //adding an Appbar
        leading: Padding(
          padding: const EdgeInsets.all(2.0),
          child: Image.asset("assets/our_logo.png"),
        ),
        title: Text('NBA Predictor'), //the name of the application
        actions: [
          // the actions widget allows us to add several navigation items

          Center(
            //adding the first navigation item and positioning it at the center
            child: OutlinedButton(
              child: Text('Home', style: TextStyle(color: Colors.white)),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => HomePage()),
                );
                Navigator.pop(context);
              },
            ),
          ),

          SizedBox(width: 60), //putting some space between the nav items

          Center(
            //adding the second navigation item and positioning it at the center
            child: OutlinedButton(
              child: Text('Matchup Predictor',
                  style: TextStyle(color: Colors.white)),
              onPressed: () {
                //determining what should happen when the navigation item is clicked.
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => MatchupPage()),
                );
              },
            ),
          ),
          SizedBox(width: 60), //putting some space between the nav items

          Center(
            //adding the second navigation item and positioning it at the center
            child: OutlinedButton(
              child: Text('Playoff Predictor',
                  style: TextStyle(color: Colors.white)),
              onPressed: () => Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const MatchupPage()),
              ),
            ),
          ),
          SizedBox(width: 80)
        ],
      ),
      body: Center(
        //adding a text message and positioning it at the center of the web page.
        child: Text(
          'Home page info will go here',
          style: TextStyle(
              fontSize: 50,
              color: Colors
                  .red), //the text message is red and has a font size of 50.
        ),
      ),
    );
  }
}
