import { readable } from "svelte/store";

// Everything in this file is temporary
const default_values = {
    full_name: "NOTHING",
    balance: 0.0,
    agency: 1,
    account_number: 0
}
async function get_account_data() {
    let resp = await fetch(
        "http://localhost:8000/api/account/1?query=full_name",
        {
            headers: {
                method: "GET",
                cors: "no-cors"
            }
        }
    ).then(resp => resp.json())
    console.log(resp.full_name)
    return resp
}
// refactor this so that only balance and transaction stores are polled repeatedly
export let account = readable(default_values, function start(set) {
    const interval = setInterval(async() => {
        let newval = await get_account_data()
        set(newval)
    }, 5000)

    return function stop() {
        clearInterval(interval)
    }
})
