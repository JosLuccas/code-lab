import './App.css'
import './index.css'
import { useState } from 'react'

function App() {

  const [nome, setNome] = useState('')
  const [senha, setSenha] = useState('')

  function verificacao() {
    if (nome == 'Admin' && senha == '12345678') {
      alert('Bem-Vindo! ' + nome)
    }
    else {
      alert('Usuário e senha incorreto!')
    }
  }

  function entrar() {
    verificacao()

  }
  return (
    <>

      <form onSubmit={entrar}>
        <h1>Entrar</h1>
        <p>Faça acesso a sua conta</p>
        <label htmlFor="Usuário">Usuário</label>
        <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} />
        <label htmlFor="Senha">Senha</label>
        <input type="password" value={senha} onChange={(e) => setSenha(e.target.value)} />
        <button type='submit'>Entrar</button>
      </form>
    </>
  )
}

export default App
