document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("predictionForm");

    form.addEventListener("submit", function(event) {
        let inputs = form.querySelectorAll("input");
        let allValid = true;

        inputs.forEach(input => {
            if (input.value.trim() === "") {
                input.style.border = "2px solid red";
                allValid = false;
            } else {
                input.style.border = "1px solid #ddd";
            }
        });

        if (!allValid) {
            event.preventDefault();
            alert("⚠ Please fill in all fields before predicting!");
        }
    });
});
