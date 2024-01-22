import { store } from "./store"

async function getTransactions() {
    let list = await fetch(store.api + "/api/payments",
    {
    headers: {
        Authorization: store.jwt
    }
    })
    .then( response => response.json() )

    return list
}
export async function getInfo() {

    let account = await fetch(store.api + "/api/account/me",
    {
    headers: {
        Authorization: store.jwt
    }
    })
    .then( response => response.json() )

    store.transactions = await getTransactions()
    store.account = account
}
