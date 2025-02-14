<!DOCTYPE html>
<html>
<head>
    <title>Math Operations</title>
</head>
<body>
    <h2>Math Operations</h2>
    <form action="process_math.php" method="POST">
        <label for="input1">Enter Number 1:</label>
        <input type="number" name="input1" required><br><br>

        <label for="input2">Enter Number 2:</label>
        <input type="number" name="input2" required><br><br>

        <label for="operation">Select Operation:</label>
        <select name="operation">
            <option value="add">Addition</option>
            <option value="sub">Subtraction</option>
            <option value="mul">Multiplication</option>
            <option value="div">Division</option>
        </select><br><br>

        <input type="submit" value="Calculate">
    </form>
</body>
</html>
