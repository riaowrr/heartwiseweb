function updateProgress() {

    const boxes = document.querySelectorAll(".habit-checkbox");

    let completed = 0;

    boxes.forEach(function(box) {
        if (box.checked) {
            completed++;
        }
    });

    const total = boxes.length;

    document.getElementById("progress").textContent =
    completed + " of " + total + " habits completed";
}