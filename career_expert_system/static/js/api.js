async function fetchONETData(careerName) {
    const apiKey = "YOUR_ONET_API_KEY";  // Register on ONET Online to get an API Key
    const endpoint = `https://services.onetcenter.org/ws/online/occupations/${careerName}`;
    
    try {
        let response = await fetch(endpoint, {
            headers: {
                "Authorization": `Basic ${btoa(apiKey + ":")}`
            }
        });
        let data = await response.json();
        
        document.getElementById("onet-overview").innerText = data.description;
        document.getElementById("onet-tasks").innerText = data.tasks.join(", ");
        document.getElementById("onet-skills").innerText = data.skills.join(", ");
        document.getElementById("onet-wages").innerText = data.wages.median_wage;
    } catch (error) {
        console.error("Error fetching ONET data:", error);
    }
}
