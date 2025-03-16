document.getElementById('fetchData').addEventListener('click', async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/notes');
        if (!response.ok) {
            throw new Error('Gagal mengambil data');
        }
        const data = await response.json();
        const dataList = document.getElementById('dataList');
        dataList.innerHTML = '';
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.id}: ${item.course_name}`;
            li.classList.add('p-2', 'border', 'border-gray-300', 'rounded', 'mt-2');
            dataList.appendChild(li);
        });
    } catch (error) {
        console.error('Error:', error);
    }
});
