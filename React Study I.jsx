
{/*      DISPLAYING Things in the Browser Using  React  */}

import React from 'react';

class App extends React.Component {
  render() {
    return (
      <h1>Hello React</h1>
    );
  }
}

export default App;


{/*       JSX      */}

import React from 'react';

class App extends React.Component {
  render() {
    return (
      <div>
        {/* Use the <h1> tag to display "Hello World" */}
        <h1>Hello World</h1>
        
        {/* Use the <p> tag to display "Let's study React together!" */}
        <p>Let's study React together!</p>
        
      </div>
    );
  }
}
export default App;

{/*             The     IMG    tag      */}

import React from 'react';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello World</h1>
        <p>Let's study React together!</p>
        {/* Use the <img> tag to display the image */}
        <img src="https://s3-ap-northeast-1.amazonaws.com/progate/shared/images/lesson/react/kentheninja.png"/>
      </div>
    );
  }
}

export default App;


{/*     The App.js File        */}

// Import React
import React from "react";
class App extends React.Component {
  render() {
    return (
      <h1>Hello React</h1>
    );
  }
}
export default App;


{/*     JSX  And  JavaScript        */}

import React from 'react';

class App extends React.Component {
  render() {
    // Define the name constant
    const name = "Ken the Ninja";
    
    // Define the imgUrl constant
    const imgUrl = "https://s3-ap-northeast-1.amazonaws.com/progate/shared/images/lesson/react/kentheninja.png";
    
    return (
      <div>
        {/* Use the name constant name to display "Ken the Ninja" */}
        <h1>{name}</h1>
        
        {/* Use the imgUrl constant to display the image */}
        <img src={imgUrl}/>
        
      </div>
    );
  }
}

export default App;
