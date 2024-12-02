let deviceMacs = [];
let deviceIps = [];
let deviceNames = [];
let deviceManufacturer = [];
let deviceStatus = [];

// Função para buscar dispositivos e adicionar ao HTML
async function fetchDevices() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/devices");
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        const devices = await response.json();

        // Seleciona o container da lista e a cover
        const scanContainer = document.querySelector('.scanContainer');
        const coverElement = document.querySelector('.cover');
        coverElement.classList.add('invisible'); // Esconde a cover após carregar os dispositivos

        // Adiciona cada dispositivo recebido ao HTML
        devices.forEach(device => {
            const deviceElement = document.createElement('li');
            deviceElement.classList.add('device');

            deviceElement.innerHTML = `
                <h3>${device.host || "Unknown Device"}</h3>
                <p><strong>MAC:</strong> ${device.mac || "N/A"}</p>
                <p><strong>IP:</strong> ${device.ip || "N/A"}</p>
                <p><strong>Manufacturer:</strong> ${device.manufacturer || "N/A"}</p>
                <p><strong>Status:</strong> ${device.status || "Unknown"}</p>
            `;

            scanContainer.appendChild(deviceElement);

            // Armazenar os dados nos arrays
            deviceMacs.push(device.mac);
            deviceIps.push(device.ip);
            deviceNames.push(device.host);
            deviceManufacturer.push(device.manufacturer);
            deviceStatus.push(device.status);
        });

        console.log("MACs:", deviceMacs);
        console.log("IPs:", deviceIps);
        console.log("Names:", deviceNames);
        console.log("Manufacturers:", deviceManufacturer);
        console.log("Statuses:", deviceStatus);

    } catch (error) {
        console.error("Failed to fetch devices:", error);
    }
}

// Adiciona o evento de clique ao botão "Scan"
document.querySelector('.button').addEventListener('click', fetchDevices);
