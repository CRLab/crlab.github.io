---
title: "Walking in Their Shoes: Poverty in America"
excerpt: "A game that presents scenarios of impoverishment in America. Written as part of a collaboration with researchers at Yale to encourage subjects to gain an alternative perspective to inequalities in America. "
collection: portfolio
---

# Walking in Their Shoes: Poverty in America

A game that presents scenarios of impoverishment in America. Written as part of a collaboration with researchers at Yale to encourage subjects to gain an alternative perspective to inequalities in America. 

## Installation

### Prerequisite software
To download this game one must have the following software installed:
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/)
- [MongoDB](https://www.mongodb.org/)

Other dependencies that come when you run npm install
- [Bower](http://bower.io/)
- [Gulp](http://gulpjs.com/)

### Compilation
- Run the command "Git clone https://github.com/DavidWatkins/Walking-in-Their-Shoes.git" in a directory you want to download the project to
- Run "cd Walking-in-Their-Shoes"
- Run "npm install"
- Run "bower install"
- Run "gulp build"
- The entire project will now be contained in the "Walking-in-Their-Shoes/dist" folder
- Make sure you have mongo set up in your computer (see MongoDB link above)

## Usage

To run the application:
- run "node server.js"
- Connect to:
	- 127.0.0.1/#NAS for no agency/with stats
	- 127.0.0.1/#NANS for no agency/no stats
	- 127.0.0.1/#AGS for agency/with stats
	- 127.0.0.1/#AGNS for agency with no stats
- Connect to 127.0.0.1/getData to receive all records in the mongoDB

## Contributing

In order to make changes to the scenarios shown in the game, modify the file located at 'src/assets/data/gameData.json'<br>
The format is as follows:<br>
```
{
  "Intro": [
	{
	  "agencyText": "",
    "noAgencyText": "",
	  "footnotes": [ "List these out to get a list of sources" ]
	},
	{
	  "agencyText": "this is shown when there is agency",
	  "noAgencyText": "this is shown at no agency",
	  "continueText": ""
	},
	{
	  "text": "This is shown regardless of agency",
	  "continueText": "This is optional"
	}
  ],
  "Final": {
	   "text": "This will be shown at the end"
  },
  "scenarios": [
	{
	  "id": 1,
	  "agency": {
		"Intro": "",
		"Choices": {
		  "msg": "You have two options:",
		  "opt1": "Option 1",
		  "opt2": "",
		  "final": ""
		},
		"Outcome1": {
		  "msg": "",
		  "health": -1,
		  "mentalHealth": 1,
		  "childHealth": -1
		},
		"Outcome2": {
		  "msg": "",
		  "health": -1,
		  "mentalHealth": -1,
		  "childHealth": -1
		},
		"Stats": {
		  "text": "",
		  "footnotes": ""
		}
	  },
	  "no-agency": {
		"Intro": "",
		"Choices": "",
		"Outcome1": {
		  "msg": "",
		  "health": -1,
		  "mentalHealth": -1,
		  "childHealth": -1
		},
		"Outcome2": {
		  "msg": "",
		  "health": -1,
		  "mentalHealth": -1,
		  "childHealth": -1
		},
		"Stats": {
		  "text": "",
		  "footnotes": ""
		}
	  }
	}
  ]
}
```

## History

v1.0 - Initial Release

## Credits

Much thanks to Gina Roussos for providing the description of the game as well as providing the insight on how to make such a game
Sithjester for the character sprite

## License

GPLv3

<div class="github-card" data-github="davidwatkins/Walking-in-Their-Shoes" data-width="400" data-height="150" data-theme="default"></div>
<script src="//cdn.jsdelivr.net/github-cards/latest/widget.js"></script>
