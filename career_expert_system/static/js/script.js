// Function to save a career to LocalStorage
function saveCareer(careerName) {
    let savedCareers = JSON.parse(localStorage.getItem("savedCareers")) || [];
    if (!savedCareers.includes(careerName)) {
        savedCareers.push(careerName);
        localStorage.setItem("savedCareers", JSON.stringify(savedCareers));
        alert(`${careerName} has been saved!`);
    } else {
        alert(`${careerName} is already saved.`);
    }
}

// Function to load saved careers on the saved.html page
function loadSavedCareers() {
    let savedCareers = JSON.parse(localStorage.getItem("savedCareers")) || [];
    let container = document.getElementById("saved-careers");

    if (savedCareers.length === 0) {
        container.innerHTML = "<p>No saved careers yet.</p>";
        return;
    }

    savedCareers.forEach(career => {
        let careerElement = document.createElement("li");
        careerElement.innerHTML = `<a href="/career/${career}">${career}</a>`;
        container.appendChild(careerElement);
    });
}

// Function to clear saved careers
function clearSavedCareers() {
    localStorage.removeItem("savedCareers");
    alert("All saved careers have been removed!");
    location.reload();
}
