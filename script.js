function generateEquityAnalysis() {
    const companyName = document.getElementById('companyName').value;
    document.getElementById('companyDisplay').innerText = companyName;

    fetch('/get_stock_price', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symbol: companyName })
    })
    .then(response => response.json())
    .then(data => {
        const price = data.price;
        if (price) {
            document.getElementById('stockPrice').innerText = `Current Stock Price: $${price}`;
            document.getElementById('result').style.display = 'block';
        } else {
            document.getElementById('stockPrice').innerText = 'Could not retrieve stock price.';
            document.getElementById('result').style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}
