const express = require('express');
const app = express();

app.use(express.json());

const USD_RATE = 83.0;

app.get('/convert', (req, res) => {

    const to = req.query.to?.toLowerCase();
    const amount = parseFloat(req.query.amount);

    console.log(req.query);

    let output;
    let from;

    if (to === "inr") {
        from = "usd";
        output = amount * USD_RATE;

    } else if (to === "usd") {
        from = "inr";
        output = amount / USD_RATE;

    } else {
        return res.status(400).json({
            message: "Invalid currency. Use 'usd' or 'inr'"
        });
    }

    return res.json({
        from_currency: from,
        input_amount: amount,
        to_currency: to,
        converted_amount: output
    });

});

app.listen(3000, () => {
    console.log("Currency service running on http://localhost:3000");
});
