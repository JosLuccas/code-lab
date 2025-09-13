import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const [nome, setNome] = useState("");
  const [senha, setSenha] = useState("");
  const navigate = useNavigate();

  function verificacao(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault(); // evita reload da página
    if (nome === "Admin" && senha === "12345678") {
      navigate("/home");
    } else {
      alert("Usuário ou senha incorretos!");
    }
  }

  return (
    <form onSubmit={verificacao}>
      <h1>Entrar</h1>
      <p>Faça acesso à sua conta</p>
      <label>Usuário</label>
      <input
        type="text"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />
      <label>Senha</label>
      <input
        type="password"
        value={senha}
        onChange={(e) => setSenha(e.target.value)}
      />
      <button type="submit">Entrar</button>
    </form>
  );
}

export default Login;