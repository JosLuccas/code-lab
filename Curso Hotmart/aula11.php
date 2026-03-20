<?
    # Constantes

    # define() → cria uma constante
    # Não usa $
    # Valor não pode ser alterado

    define("exemplo", "isso é um exemplo");
    echo exemplo; //Resultado: Isso é um exemplo

    echo "===== CONSTANTES =====\n";

    // Definindo constantes
    define("NOME", "José");
    define("PI", 3.14159);
    define("IDADE", 20);

    // Exibindo constantes
    echo "Nome: " . NOME . "\n";
    echo "PI: " . PI . "\n";
    echo "Idade: " . IDADE . "\n";

    // Usando constante em cálculo
    $raio = 5;
    $area = PI * pow($raio, 2);
    echo "Área do círculo: " . $area . "\n";

    // Constante mágica (exemplo)
    echo "Arquivo atual: " . __FILE__ . "\n";
?>