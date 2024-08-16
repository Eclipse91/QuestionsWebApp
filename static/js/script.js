function showCorrectAnswer() {
    var myChoiceValue = document.getElementById("myChoice").value.toUpperCase();
    var correctAnswer = document.getElementById("correctAnswer").innerHTML.toUpperCase();

    if (correctAnswer !== myChoiceValue)
        alert("The correct answer is " + correctAnswer + '\nPush enter to get another question');
}

function simulateFormSubmit() {
    document.getElementById('questionForm').submit();
}
