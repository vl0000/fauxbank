
import { store } from "./store"

export async function makeTransaction(transaction: Object) {
    let response = await fetch(store.api + "/api/payments",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: store.jwt
            },
            // expected format { payee: int, amount: float }
            body: JSON.stringify(transaction)
        }
        )
        .then(res => res.json())
        .catch(err => console.error(err))

        return response
        
}