import json from './data/pokemonMoves.json'
import names from './names.js'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useHistory,
  Redirect
} from "react-router-dom";
import { useState } from 'react';
import { render } from '@testing-library/react';


function App() {

  let [imageSelect, setImage] = useState(randImage())
  function randImage() {
    // Get random image
    let num = getRandomInt(0, 511);
    let path = num.toString();
    while (path.length != 4) {
      path = '0' + path;
    }
    let totalPath = `images/${path}.png`;


    return totalPath;
  }

  function setRandImage() {
    setImage(randImage());
  }

  return (
    <Router>
      <Switch>
        <Route path="/step-three">
          <StepThree image={imageSelect} />
        </Route>
        <Route path="/step-two">
          <StepTwo image={imageSelect} setImage={setRandImage} />
        </Route>
        <Route path="/">
          <StepOne />
        </Route>
      </Switch>
    </Router>
  )
}

// Selected pokemon types
let pokeTypes = [];

// List of pokemon moves
let moveList = {
  'normal': [],
  'fire': [],
  'water': [],
  'grass': [],
  'electric': [],
  'ice': [],
  'fighting': [],
  'poison': [],
  'ground': [],
  'ghost': [],
  'flying': [],
  'psychic': [],
  'bug': [],
  'rock': [],
  'dark': [],
  'dragon': [],
  'steel': [],
  'fairy': [],
};
let totalMoves = [];

for (let move in json) {
  // console.log(json[move])
  if (moveList[json[move].type]) {
    moveList[json[move].type].unshift(json[move].name);

  }
  totalMoves.unshift(json[move].name);
}

// Creates a list of pokemon types
function PokeTypes() {
  function addType(type) {
    if (pokeTypes.length < 2) {
      pokeTypes.unshift(type);
    } else {
      let removed = pokeTypes.pop();
      document.getElementById(`btn-${removed}`).classList.toggle('opacity-25');
      pokeTypes.unshift(type);
    }
    document.getElementById(`btn-${type}`).classList.toggle('opacity-25')


  }

  return (
    <div className="grid grid-cols-5 gap-4">
      <button id="btn-Normal" className="bg-normal rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Normal')}>Normal</button>
      <button id="btn-Fire" className="bg-fire rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Fire')}>Fire</button>
      <button id="btn-Water" className="bg-water rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Water')}>Water</button>
      <button id="btn-Grass" className="bg-grass rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Grass')}>Grass</button>
      <button id="btn-Electric" className="bg-electric rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Electric')}>Electric</button>
      <button id="btn-Ice" className="bg-ice rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Ice')}>Ice</button>
      <button id="btn-Fighting" className="bg-fighting rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Fighting')}>Fighting</button>
      <button id="btn-Poison" className="bg-poison rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Poison')}>Poison</button>
      <button id="btn-Ground" className="bg-ground rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Ground')}>Ground</button>
      <button id="btn-Ghost" className="bg-ghost rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Ghost')}>Ghost</button>
      <button id="btn-Flying" className="bg-flying rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Flying')}>Flying</button>
      <button id="btn-Psychic" className="bg-psychic rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Psychic')}>Psychic</button>
      <button id="btn-Bug" className="bg-bug rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Bug')}>Bug</button>
      <button id="btn-Rock" className="bg-rock rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Rock')}>Rock</button>
      <button id="btn-Dark" className="bg-dark rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Dark')}>Dark</button>
      <button id="btn-Dragon" className="bg-dragon rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-start-2 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Dragon')}>Dragon</button>
      <button id="btn-Steel" className="bg-steel rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Steel')}>Steel</button>
      <button id="btn-Fairy" className="bg-fairy rounded-lg text-white font-medium py-2 px-4 h-auto w-7.5 col-span-1 shadow text-center hover:opacity-90 focus:outline-none" onClick={() => addType('Fairy')}>Fairy</button>
    </div>
  );
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

//  Page one
function StepOne() {
  let history = useHistory();

  function RouteTo() {
    history.push("/step-two");
  }
  return (
    <div>
      <header className="flex flex-row ml-5 mt-10">
        <img src={'images/Image 5@2x.png'} className="w-48 h-16" alt="logo" />

      </header>
      <div className="flex flex-col items-center">
        <div className="font-futura text-font-gray mx-auto text-center"><div className="text-6xl">Welcome to PokeGen!</div><br></br><div className="text-base opacity-75  w-3/4 mx-auto">Begin the journey of creating your very own custom Pokemon by following the simple steps below!</div>
        </div>
        <div className="flex flex-row my-20">
          <div className="flex flex-col">
            <div className="flex flex-row items-center">
              <div className="bg-btn-blue rounded-full text-white w-8 h-8 flex items-center justify-center">1</div>
              <div className="text-lg text-font-gray font-semibold ml-3">Pokemon Type</div>
            </div>
            <div className="text-font-gray font-semibold mb-3 mt-8">Instructions:</div>
            <ol className="text-font-gray opacity-75 w-3/4">
              <li className="mb-3">
                1. Select up to <span className="font-semibold">TWO</span> Pokemon types that you want your new Pokemon to be.
              </li>
              <li>
                2. Select ‘Generate’ to generate your new Pokemon!
              </li>
            </ol>
          </div>
          <PokeTypes />
        </div>
        <button className="bg-btn-blue hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg w-min" onClick={RouteTo}>Generate</button>
      </div>
    </div >
  );
}



// Page Two
function StepTwo(props) {
  let history = useHistory();

  function RouteToNext() {
    history.push("/step-three");
  }

  function RouteBack() {
    history.push("/step-one");
  }



  return (
    <div>
      <header className="flex flex-row ml-5 mt-10">
        <img src={'images/Image 5@2x.png'} className="w-48 h-16" alt="logo" />

      </header>
      <div className="flex flex-col items-center">
        <div className="font-futura text-font-gray mx-auto text-center"><div className="text-6xl">Welcome to PokeGen!</div><br></br><div className="text-base opacity-75  w-3/4 mx-auto">Begin the journey of creating your very own custom Pokemon by following the simple steps below!</div>
        </div>
        <div className="flex flex-row my-20 items-center ml-32">
          <div className="flex flex-col w-1/2">
            <div className="flex flex-row items-center">
              <div className="bg-btn-blue rounded-full text-white w-8 h-8 flex items-center justify-center">2</div>
              <div className="text-lg text-font-gray font-semibold ml-3">Pokemon Appearence</div>
            </div>
            <div className="text-font-gray font-semibold mb-3 mt-8">Instructions:</div>
            <ol className="text-font-gray opacity-75 w-3/4">
              <li className="mb-3">
                1. Verify that you are satisfied with your generated Pokemon. If you are go ahead and hit ‘Continue’ where you will be presented with their name and moves.
                          </li>
              <li>
                2. If you are unsatisfied you can hit ‘Back’ and begin the generation process from the beginning. Or if you would just like to generate a new Pokemon with your previous selections just hit ‘Regenerate’.
                          </li>
            </ol>
          </div>
          <img src={props.image} style={{ borderRadius: '4rem' }} height="128px" width="128px"></img>
        </div>
        <div className="flex flex-row mb-10">
          <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg w-min mr-8" onClick={RouteBack}>Back</button>
          <button className="bg-btn-blue hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg w-min" onClick={() => props.setImage()}>Regenerate</button>
          <button className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg w-min ml-8" onClick={RouteToNext}>Continue</button>
        </div>

      </div>
    </div >
  );
}

// Page Three
function StepThree(props) {
  let history = useHistory();
  function RouteBack() {
    history.push("/step-two");
  }

  // Create the the name and moves element
  let [nameSelect, setName] = useState(randName());
  function randName() {
    // Get random moves
    let num = getRandomInt(0, names.length);
    let tempName = names[num];
    return tempName;
  }

  // Get moves of specified type
  let availMoves = []
  if (pokeTypes.length > 0 && availMoves.length == 0) {
    pokeTypes.forEach(moveType => {
      if (moveList[moveType.toLowerCase()]) {
        moveList[moveType.toLowerCase()].forEach(move => {
          availMoves.unshift(move);

        })
      }
    })
  }
  // Always add normal moves
  if (pokeTypes[0] != 'Normal' && pokeTypes[1] != 'Normal' && availMoves.length < 20) {
    moveList['normal'].forEach(move => {
      availMoves.unshift(move);
    })
  }



  // let moves = [];
  let [moves, setMoves] = useState(randMoves())
  function randMoves() {
    // Get random moves
    let tempMoves = availMoves.sort(function () {
      return 0.5 - Math.random();
    });
    tempMoves = tempMoves.slice(availMoves, 6);
    // console.log(tempMoves)
    return tempMoves;
  }
  function NameAndMoves() {
    return (
      <div className="bg-btn-blue bg-opacity-50 p-5 flex flex-col rounded-xl font-futura ml-24 text-2xl text-font-gray">
        <div className="flex flex-row mb-3">
          <div className="text-medium text-3xl">Name:</div>
          {/* Use props.name instead of "Hitmantis" */}
          <div className="bg-white bg-opacity-75 py-1 px-2 rounded-lg ml-3 font-bold">{nameSelect}</div>
          <button className="text-red-600 text-base ml-3 focus:outline-none" onClick={() => setName(randName())}> Regenerate</button>
        </div>
        <div className="text-medium text-3xl mb-3">Moveset:</div>
        <div className="grid grid-col-1 gap-3">
          {/* Iterate through props.moves and create card for each */}
          {moves.map(move => (
            <div className="bg-white bg-opacity-75 py-2 px-3 text-center rounded-lg col-span-1 col-start-1 shadow">{move}</div>
          ))}
        </div>
        <button className="text-red-600 text-base mt-3 focus:outline-none" onClick={() => setMoves(randMoves())}> Regenerate</button>
      </div>
    );
  }

  return (
    <div>
      <header className="flex flex-row ml-5 mt-10">
        <img src={'images/Image 5@2x.png'} className="w-48 h-16" alt="logo" />

      </header>
      <div className="flex flex-col items-center">
        <div className="font-futura text-font-gray mx-auto text-center"><div className="text-6xl">Welcome to PokeGen!</div><br></br><div className="text-base opacity-75  w-3/4 mx-auto">Begin the journey of creating your very own custom Pokemon by following the simple steps below!</div>
        </div>
        <div className="flex flex-row my-20 items-center ml-32 justify-center">
          <div className="flex flex-col w-1/3">
            <div className="flex flex-row items-center">
              <div className="bg-btn-blue rounded-full text-white w-8 h-8 flex items-center justify-center">3</div>
              <div className="text-lg text-font-gray font-semibold ml-3">Name and Moveset</div>
            </div>
            <div className="text-font-gray font-semibold mb-3 mt-8">Instructions:</div>
            <ol className="text-font-gray opacity-75 w-3/4">
              <li className="mb-3">
                1. Verify that you are satisfied with your generated Pokemon name and moveset. If you are go ahead and hit ‘Add To Team’ to download your Pokemon!
                          </li>
              <li>
                2. If you are unsatisfied you can hit ‘Regenerate’ next to either the name or moveset to generate a new set.
                          </li>
            </ol>
          </div>
          <img src={props.image} style={{ borderRadius: '4rem' }} height="128px" width="128px"></img>
          <NameAndMoves />
        </div>
        <div className="flex flex-row mb-10">
          <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg w-min mr-8" onClick={RouteBack}>Back</button>
          <a href={props.image} download={nameSelect}>
            <button className="bg-btn-blue hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg">Add to Team</button>
          </a>
        </div>
      </div>
    </div >
  );
}



export default App;
