const prices = {
    1: 180000,
    2: 300000,
    3: 350000,
    4: 60000,
    5: 100000,
    6: 280000,
    7: 400000,
    8: 200000,
    9: 50000,
    10: 350000
};

for (let i = 1; i <= 10; i++) {
    let addBtn = document.getElementById('a' + i);
    let subBtn = document.getElementById('s' + i);
    let amountEl = document.getElementById('am' + i);
    let totalEl = document.getElementById('t' + i);

    let count = 0;
    let price = prices[i];

    addBtn.addEventListener('click', () => {
        count++;
        update();
    });

    subBtn.addEventListener('click', () => {
        if (count > 0) {
            count--;
            update();
        }
    });

    function update() {
        amountEl.innerText = count;
        totalEl.innerText = count * price;
    }
}