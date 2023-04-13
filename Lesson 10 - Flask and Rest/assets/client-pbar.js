const URL = '/stats/virtual_memory';

function updateMemoryUsage() {
  fetch(URL)
    .then(response => response.json())
    .then(memory_data => {
      console.log(`Memory usage: ${memory_data}`);

      var span = document.getElementById('client-span');
      span.innerHTML = `${(memory_data['used'] / (1024 ** 2)).toFixed(2)} / ${(memory_data['total'] / (1024 ** 2)).toFixed(2)} MiB`;

      var gauge_div = document.getElementById('gauge');
      gauge_div.innerHTML = `
        <div class="bar" style="background-color: rgb(72, 239, 82);
                                transform: translate(${memory_data['percent']}%);">
          <div class="data" style="display: flex;
                                    justify-content: center;
                                    position: absolute;
                                    right: 0;
                                    width: ${memory_data['percent']}%;">
            ${memory_data['percent']}%
          </div>
        </div>
      `;
    });
}

setInterval(updateMemoryUsage, 2000);

updateMemoryUsage();