<?
    # Manipulação de Strings.

    # strlen()
    # Conta quantos caracteres tem uma string.

    $texto = "Olá mundo";
    echo strlen($texto); // Resultado: 9

    # str_word_count()
    # Conta quantas palavras existem em uma string.

    $frase = "Aprendendo PHP é legal";
    echo str_word_count($frase); // Resultado: 4
    
    # strrev()
    # Inverte uma string.

    $texto = "PHP";
    echo strrev($texto); // Resultado: PHP (invertido fica PHP mesmo 😅)

    # strpos()
    # Mostra a posição da primeira vez que um texto aparece dentro de outro.

    $frase = "Eu gosto de programar";
    echo strpos($frase, "gosto"); // Resultado: 3

    # str_replace()
    # Substitui uma parte da string por outra.

    $frase = "Eu gosto de Java";
    echo str_replace("Java", "PHP", $frase);

?>