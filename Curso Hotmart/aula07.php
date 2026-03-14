<?

    # Tipos de Dados:

    # String = Palavras
    # Integer = Número Inteiro
    # Float = Números reais
    # Boolean = True / False
    # Array = Lista -> Um array é uma estrutura que permite guardar vários valores dentro de uma única variável.
    # Object = Objeto
    # Null = Nulo

    # String ex:
    $texto = "Olá, Mundo!";

    # Integer ex:
    $inteiro = 1;

    # Float ex:
    $numero_real = 5.5;

    # Boolean ex:
    $verdadeiro = True;

    # Array ex:
    $lista = array("José", "Wilhan");
    $lista_moderna = ["José", "Wilhan"];

    #Object ex:
    class carro {
        public $cor;
        public $modelo;
        public function __construct($cor,$modelo)
        {
            $this -> cor = $cor;
            $this -> modelo = $modelo;
        }
        public function mensagem()
         {
            return "O carro é $this->cor e o modelo é $this->modelo";   
        }
    }

    $carro = new carro("Azul","Fusca");

    echo $carro -> mensagem();

    # Null
    $nada = null

?>