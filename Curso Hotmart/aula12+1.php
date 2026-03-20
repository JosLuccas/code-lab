<?php
echo "===== IF, ELSE, ELSEIF =====\n";

/*
IF, ELSE e ELSEIF são usados para tomar decisões no código.
*/

// ==============================
// 1. IF (SE)
// ==============================

echo "\n--- IF ---\n";

$idade = 20;

if ($idade >= 18) {
    echo "Maior de idade\n";
}


// ==============================
// 2. IF + ELSE (SE NÃO)
// ==============================

echo "\n--- IF + ELSE ---\n";

$idade = 16;

if ($idade >= 18) {
    echo "Maior de idade\n";
} else {
    echo "Menor de idade\n";
}


// ==============================
// 3. IF + ELSEIF + ELSE
// ==============================

echo "\n--- IF + ELSEIF + ELSE ---\n";

$nota = 7;

if ($nota >= 9) {
    echo "Excelente\n";
} elseif ($nota >= 6) {
    echo "Aprovado\n";
} else {
    echo "Reprovado\n";
}


// ==============================
// 4. MÚLTIPLAS CONDIÇÕES
// ==============================

echo "\n--- Múltiplas condições ---\n";

$idade = 20;
$temCarteira = true;

if ($idade >= 18 && $temCarteira) {
    echo "Pode dirigir\n";
} else {
    echo "Não pode dirigir\n";
}


// ==============================
// 5. IF SIMPLES (SEM CHAVES)
// ==============================

echo "\n--- IF simples ---\n";

$numero = 10;

if ($numero > 0)
    echo "Número positivo\n";

?>