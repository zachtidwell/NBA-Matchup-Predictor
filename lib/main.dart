import 'package:flutter/material.dart';
import './homepage.dart'; //import a homepager

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NBA Predictor',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomePage(), //add the homepage to the main application
    );
  }
}
