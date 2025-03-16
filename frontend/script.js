document.getElementById("fetchData").addEventListener("click", function() {
    fetch("http://localhost:8501/materials")  // Pastikan Flask berjalan
    .then(response => response.json())
    .then(data => {
        let output = "<ul>";
        data.forEach(note => {
            output += `<li>${note.title} - Rp${note.price}</li>`;
        });
        output += "</ul>";
        document.getElementById("output").innerHTML = output;
    })
    .catch(error => console.error("Error:", error));
});
