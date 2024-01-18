import { readable } from "svelte/store";
import { Preferences } from "@capacitor/preferences";

export const api_url = "https://fauxbank.vercel.app"
// Everything in this file is temporary
const default_values = {
    name: "NOTHING",
    balance: 0.0,
    agency: 1,
    number: 0
}

async function get_account_data() {
    let resp = await fetch(
        api_url + "/api/account/me",
        {
            headers: {
                cors: "no-cors",
                "Authorization": await Preferences.get({key: "jwt"}).then( (token) => token.value)
            }
        }
    ).then(resp => resp.json())
    .then(
        resp => {
            if (resp.detail === "Expired token") {
                window.location.href = "/expired"
            }
        }
    ).catch(err => console.log(err))
    console.log(resp)
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
