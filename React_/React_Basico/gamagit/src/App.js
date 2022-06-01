import React, {useStage} from 'react';

function App(props) {
  const [ usuario, setUsuario ] = useState('');
  return (
    <>
      <input className="usuarioInput" placeholder="Usuário"/>
      <button type="button">Pesquisar</button>
    </>
  );
}

export default App;
