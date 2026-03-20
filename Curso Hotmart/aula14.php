<?php
echo "===== LOOPS EM PHP =====\n";

/*
Loops são usados para repetir um bloco de código várias vezes.
*/

// ==============================
// 1. WHILE (ENQUANTO)
// ==============================

echo "\n--- WHILE ---\n";

$contador = 1;

while ($contador <= 5) {
    echo "Número: $contador\n";
    $contador++; // IMPORTANTE: evita loop infinito
}


// ==============================
// 2. DO WHILE
// ==============================

echo "\n--- DO WHILE ---\n";

$contador = 1;

do {
    echo "Número: $contador\n";
    $contador++;
} while ($contador <= 5);


// ==============================
// 3. FOR
// ==============================

echo "\n--- FOR ---\n";

for ($i = 1; $i <= 5; $i++) {
    echo "Número: $i\n";
}


// ==============================
// 4. FOREACH (ARRAYS)
// ==============================

echo "\n--- FOREACH ---\n";

$nomes = ["José", "Maria", "João"];

foreach ($nomes as $nome) {
    echo "Nome: $nome\n";
}


// ==============================
// 5. CUIDADO COM LOOP INFINITO
// ==============================

echo "\n--- LOOP INFINITO (exemplo ruim) ---\n";

/*
$nome = "José";

while ($nome == "José") {
    echo $nome; // NUNCA MUDA → loop infinito
}
*/

echo "Evite loops infinitos!\n";

?>