import { reactive } from "vue";

const api_address = "";

export const store = reactive(
    {
        jwt: null,
        account: {
            name: "loggedout",
            number: 123456,
            balance: 0.0
        }
    }
)