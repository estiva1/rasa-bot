import Widget from 'rasa-webchat'

function App() {
  return (
    <Widget
      //initPayload={null}
      socketUrl={"http://localhost:5005"}
      socketPath={"/socket.io/"}
      customData={{"language": "en"}}
      title={"Rasa Bot by Stanislav Yuzva"}
      embedded={false}
      
    />
  );
}

export default App;
