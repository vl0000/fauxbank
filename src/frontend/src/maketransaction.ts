
import { store } from "./store"

export async function makeTransaction(transaction: Object) {
    let response = await fetch(store.api + "/api/payments",
        {
            method: "POST",
            headers: { Authorization: store.jwt },
            // expected format { payee: int, amount: float }
            body: transaction
        }
        )
        .then(res => res.json())
        .catch(err => console.error(err))

        if (response.status != 200) {
            console.error("The transaction could not go through\n Status: ", response.status)
        } else {
            return response
        }
        
}