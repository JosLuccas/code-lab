import { useState } from "react";

function Home() {
  const [produto1, setProduto1] = useState<number>(0);
  const [produto2, setProduto2] = useState<number>(0);
  const [produto3, setProduto3] = useState<number>(0);
  const [total, setTotal] = useState<number>(0);

  function calcularTotal(e: React.FormEvent<HTMLFormElement>) {
     e.preventDefault();
    setTotal(produto1 + produto2 + produto3);
  }
  return (
    <>
      <form onSubmit={calcularTotal}>
        <h1>Valor totais produto!</h1>
        <label>Valor: Produto 1</label>
        <input type="number"
          onChange={(e) => setProduto1(Number(e.target.value))}
        />
        <label>Valor: Produto 2</label>
        <input type="number"
          onChange={(e) => setProduto2(Number(e.target.value))}
        />
        <label>Valor: Produto 3</label>
        <input type="number"
          onChange={(e) => setProduto3(Number(e.target.value))}
        />
        <button type="submit">Calcular</button>
        <p><br />Total: {total}</p>
      </form>
    </>
  );
}

export default Home;