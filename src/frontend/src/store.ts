import { reactive } from "vue";

const api_address = "";

export const store = reactive(
    {
        api: "https://fauxbank.vercel.app",
        jwt: "",
        account: {
            name: "loggedout",
            number: 123456,
            balance: 0.0
        },
        transactions: [[1, 0, 7811872284, 50000, "2024-01-18T17:49:59.168952Z"]]
    }
,)
