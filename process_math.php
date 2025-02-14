<?php
$num1 = $_POST['input1'];
$num2 = $_POST['input2'];
$operation = $_POST['operation'];

$command = "python3 math_operations.py input1=$num1 input2=$num2 operation=$operation";
$output = shell_exec($command);

echo $output;
?>
