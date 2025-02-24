const express = require("express");
const ejs = require("ejs");
const app = express();
const dotenv = require("dotenv");

dotenv.config();

const URL = process.env.URL || "http://localhost:5000/api";
const fetch = (...args)=>import("node-fetch").then(({default: fetch}) => fetch(...args));

app.set("view engine", "ejs");

app.get("/", async(req, res) => {
    const options = {
        method: "GET",
        headers:     {
            "Content-Type": "application/json"
        }
    }
    fetch(URL, options)
    .then(res => res.json())
    .then(json => {console.log(json);})
    .catch(err => {console.log(err);});
    try{
        const response = await fetch(URL, options);
        const data = await response.json();
        res.render("index", {data: data.data});
    }catch(err){
        console.log(err);
        res.status(500).send("Error fetching data");
    }
});

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
