import { reactive } from "vue";

const api_address = "";

export const store = reactive(
    {
        api: "http://127.0.0.1:8000",
        jwt: null,
        account: {
            name: "loggedout",
            number: 123456,
            balance: 0.0
        }
    }
)