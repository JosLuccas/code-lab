<?php
echo "===== OPERADORES EM PHP =====\n";

/*
Operadores são símbolos usados para:
- Fazer cálculos
- Atribuir valores
- Comparar valores
- Criar condições lógicas
*/

// ==============================
// 1. OPERADORES ARITMÉTICOS
// ==============================

echo "\n--- Aritméticos ---\n";

$a = 10;
$b = 5;

echo "Soma: " . ($a + $b) . "\n";        // +
echo "Subtração: " . ($a - $b) . "\n";   // -
echo "Multiplicação: " . ($a * $b) . "\n"; // *
echo "Divisão: " . ($a / $b) . "\n";     // /
echo "Resto: " . ($a % $b) . "\n";       // %


// ==============================
// 2. OPERADORES DE ATRIBUIÇÃO
// ==============================

echo "\n--- Atribuição ---\n";

$x = 10;

$x += 5; // x = x + 5
echo "x += 5: $x\n";

$x -= 3;
echo "x -= 3: $x\n";

$x *= 2;
echo "x *= 2: $x\n";

$x /= 4;
echo "x /= 4: $x\n";


// ==============================
// 3. CONCATENAÇÃO (STRING)
// ==============================

echo "\n--- Concatenação ---\n";

$nome = "José";
$sobrenome = "Lucas";

echo $nome . " " . $sobrenome . "\n"; // .


// ==============================
// 4. OPERADORES DE COMPARAÇÃO
// ==============================

echo "\n--- Comparação ---\n";

$a = 10;
$b = "10";

var_dump($a == $b);  // true (valor igual)
var_dump($a === $b); // false (tipo diferente)
var_dump($a != $b);  // false
var_dump($a > 5);    // true
var_dump($a < 5);    // false


// ==============================
// 5. OPERADOR TERNÁRIO
// ==============================

echo "\n--- Ternário ---\n";

$idade = 18;

$resultado = ($idade >= 18) ? "Maior de idade" : "Menor de idade";
echo $resultado . "\n";


// ==============================
// 6. OPERADORES LÓGICOS
// ==============================

echo "\n--- Lógicos ---\n";

$idade = 20;
$temCarteira = true;

var_dump($idade >= 18 && $temCarteira); // AND (true)
var_dump($idade < 18 || $temCarteira);  // OR (true)
var_dump(!$temCarteira);               // NOT (false)

?>