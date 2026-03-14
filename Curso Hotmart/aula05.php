<?php
    # Variavéis

    /*
    $cor = "Azul";
    echo $cor;
    */
    
    # Uso de variavél global:

    $x = 10;

    function teste (){
        global $x;
        echo "O valor de x dentro da função: $x";
    }
    teste();
    echo "<br>O valor de x fora: $x";

?>