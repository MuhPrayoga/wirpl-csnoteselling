
document.getElementById("fetchData").addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:8501/get_data");
    const data = await response.json();
    document.getElementById("dataContainer").innerText = JSON.stringify(data, null, 2);
});
