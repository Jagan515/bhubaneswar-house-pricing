 // Update slider values in real-time
        document.querySelectorAll('input[type="range"]').forEach(slider => {
            const valueDisplay = document.getElementById(slider.id + '_value');
            valueDisplay.textContent = slider.value;
            
            slider.addEventListener('input', function() {
                valueDisplay.textContent = this.value;
            });
        });

        // Update descriptions for categorical fields
        document.getElementById('LOCALITY_RANK').addEventListener('change', function() {
            const rank = parseInt(this.value);
            const descriptions = {
                1: "Premium areas like Nayapalli, Saheed Nagar",
                2: "High-end areas like Bapuji Nagar, Ashok Nagar", 
                3: "Medium areas like Patia, Chandrasekharpur",
                4: "Standard residential areas",
                5: "Basic residential areas"
            };
            document.getElementById('LOCALITY_RANK_desc').textContent = descriptions[rank];
        });

        document.getElementById('RIVER_PROXIMITY').addEventListener('change', function() {
            const descriptions = {
                0: "Property is not near Kuakhai River",
                1: "Property is near Kuakhai River (Premium Location)"
            };
            document.getElementById('RIVER_PROXIMITY_desc').textContent = descriptions[this.value];
        });

        // Prediction function
        async function predictPrice() {
            const form = document.getElementById('predictionForm');
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            // Show loading state
            const resultDiv = document.getElementById('predictionResult');
            resultDiv.innerHTML = '<i class="fas fa-spinner fa-spin fa-3x mb-3"></i><div>Calculating...</div>';

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (result.success) {
                    resultDiv.innerHTML = `
                        <i class="fas fa-home fa-3x mb-3"></i>
                        <div>Estimated Price</div>
                        <div class="display-4">₹${result.predicted_price}</div>
                        <div class="mt-2">lakhs</div>
                        <small class="mt-2 d-block">Based on current market trends</small>
                    `;
                } else {
                    resultDiv.innerHTML = `
                        <i class="fas fa-exclamation-triangle fa-3x mb-3"></i>
                        <div>Error</div>
                        <div class="mt-2">${result.message}</div>
                    `;
                }
            } catch (error) {
                resultDiv.innerHTML = `
                    <i class="fas fa-exclamation-triangle fa-3x mb-3"></i>
                    <div>Network Error</div>
                    <div class="mt-2">Please try again</div>
                `;
            }
        }

        // Initialize tooltips
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        });